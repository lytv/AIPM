#!/usr/bin/env python3
"""
Text-to-Speech Converter for Vietnamese Book
Using VieNeu-TTS model from Hugging Face

Usage:
    python text_to_audio.py --input <path_to_markdown> --output <output_folder>

Requirements:
    pip install transformers torch accelerate soundfile librosa tqdm
"""

import os
import re
import argparse
import torch
import soundfile as sf
import librosa
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForTextToSpeech
from pathlib import Path

# Cấu hình
MODEL_NAME = "pnnbao-ump/VieNeu-TTS"
OUTPUT_SAMPLE_RATE = 22050
MAX_CHARS_PER_CHUNK = 200  # Giới hạn ký tự cho mỗi chunk để tránh OOM

def clean_text_for_tts(text):
    """Làm sạch text, loại bỏ markdown và ký tự đặc biệt"""
    # Loại bỏ header markdown (#, ##, ###)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    # Loại bỏ bold/italic (*, **, _)
    text = re.sub(r'\*\*|\*|_', '', text)
    # Loại bỏ links [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Loại bỏ code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    # Loại bỏ inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Loại bỏ blockquotes
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    # Loại bỏ horizontal rules
    text = re.sub(r'^[-*_]{3,}$', '', text, flags=re.MULTILINE)
    # Loại bỏ bảng (giữ lại nội dung)
    text = re.sub(r'\|[|\-\s]+\|', '', text)
    # Loại bỏ dòng trống thừa
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Thay thế các ký tự đặc biệt bằng khoảng trắng
    text = re.sub(r'[^\w\s.,!?;:()\'"-]', ' ', text)
    # Chuẩn hóa khoảng trắng
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def split_text_into_chunks(text, max_chars=MAX_CHARS_PER_CHUNK):
    """Chia text thành các chunks nhỏ để xử lý"""
    # Tách theo câu
    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_chars:
            current_chunk += sentence + " "
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence + " "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def load_model(model_name):
    """Load VieNeu-TTS model"""
    print(f"🔄 Đang tải model: {model_name}")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTextToSpeech.from_pretrained(
        model_name,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True
    )

    # Move to GPU if available
    if torch.cuda.is_available():
        model = model.to("cuda")
        print("✅ Sử dụng GPU")
    else:
        print("✅ Sử dụng CPU")

    return tokenizer, model

def text_to_speech(tokenizer, model, text, output_path):
    """Chuyển đổi text thành audio"""
    # Chuẩn bị input
    inputs = tokenizer(text, return_tensors="pt")

    # Move to same device as model
    if torch.cuda.is_available():
        inputs = {k: v.to("cuda") for k, v in inputs.items()}

    # Generate speech
    with torch.no_grad():
        speech = model.generate_speech(
            inputs["input_ids"],
            attention_mask=inputs.get("attention_mask")
        )

    # Convert to numpy and save
    audio = speech.cpu().numpy()

    # Resample to desired sample rate if needed
    if model.config.audio_encoder_sample_rate != OUTPUT_SAMPLE_RATE:
        audio = librosa.resample(
            audio,
            orig_sr=model.config.audio_encoder_sample_rate,
            target_sr=OUTPUT_SAMPLE_RATE
        )

    sf.write(output_path, audio, OUTPUT_SAMPLE_RATE)
    return len(audio) / OUTPUT_SAMPLE_RATE  # Return duration in seconds

def combine_audio_files(audio_files, output_path):
    """Kết hợp nhiều file audio thành một"""
    print("🎵 Đang kết hợp các file audio...")

    combined_audio = None
    for file_path in tqdm(audio_files):
        audio, sr = librosa.load(file_path, sr=OUTPUT_SAMPLE_RATE)
        if combined_audio is None:
            combined_audio = audio
        else:
            combined_audio = np.concatenate([combined_audio, audio])

    sf.write(output_path, combined_audio, OUTPUT_SAMPLE_RATE)
    print(f("✅ Đã lưu file audio tổng hợp: {output_path}")
    print(f("   Thời lượng: {len(combined_audio) / OUTPUT_SAMPLE_RATE:.2f} giây")

import numpy as np

def main():
    parser = argparse.ArgumentParser(
        description="Chuyển đổi sách tiếng Việt thành audio sử dụng VieNeu-TTS"
    )
    parser.add_argument(
        "--input", "-i",
        default="/Users/mac/tools/AIPM/ebooks/00-Full-Book/INSPIRED-Full-Book.md",
        help="Đường dẫn file markdown đầu vào"
    )
    parser.add_argument(
        "--output", "-o",
        default="/Users/mac/tools/AIPM/ebooks/00-Full-Book/INSPIRED-Full-Book.wav",
        help="Đường dẫn file audio đầu ra"
    )
    parser.add_argument(
        "--temp-dir", "-t",
        default="/Users/mac/tools/AIPM/ebooks/00-Full-Book/temp_audio",
        help="Thư mục tạm cho các chunk audio"
    )
    parser.add_argument(
        "--chunk-size", "-c",
        type=int,
        default=MAX_CHARS_PER_CHUNK,
        help="Số ký tự tối đa cho mỗi chunk"
    )

    args = parser.parse_args()

    # Tạo thư mục tạm
    temp_dir = Path(args.temp_dir)
    temp_dir.mkdir(parents=True, exist_ok=True)

    # Đọc file text
    print(f"📖 Đang đọc file: {args.input}")
    with open(args.input, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    print(f"   Tổng số ký tự: {len(raw_text)}")

    # Làm sạch text
    print("🧹 Đang làm sạch text...")
    clean_text = clean_text_for_tts(raw_text)
    print(f"   Ký tự sau khi làm sạch: {len(clean_text)}")

    # Chia thành chunks
    print("✂️ Đang chia text thành chunks...")
    chunks = split_text_into_chunks(clean_text, args.chunk_size)
    print(f"   Tổng số chunks: {len(chunks)}")

    # Load model
    tokenizer, model = load_model(MODEL_NAME)

    # Tạo audio cho mỗi chunk
    audio_files = []
    print("🎙️ Đang tạo audio...")

    for i, chunk in enumerate(tqdm(chunks)):
        if not chunk.strip():
            continue

        output_file = temp_dir / f"chunk_{i:04d}.wav"
        try:
            duration = text_to_speech(
                tokenizer, model,
                chunk.strip(),
                str(output_file)
            )
            audio_files.append(output_file)
            tqdm.write(f"   Chunk {i+1}/{len(chunks)}: {duration:.2f}s")
        except Exception as e:
            tqdm.write(f"❌ Lỗi ở chunk {i}: {e}")

    # Kết hợp audio
    if audio_files:
        combine_audio_files(audio_files, args.output)
    else:
        print("❌ Không có file audio nào được tạo")

    # Cleanup temp files (optional)
    print(f"\n🗑️ Đang dọn dẹp files tạm...")
    for f in audio_files:
        f.unlink()
    temp_dir.rmdir()

    print("\n✨ Hoàn thành!")

if __name__ == "__main__":
    main()
