#!/usr/bin/env python3
"""
Simple Vietnamese Text-to-Speech using Edge TTS
Không cần GPU, dễ cài đặt, chất lượng tốt

Cài đặt:
    pip install edge-tts asyncio aiofiles

Chạy:
    python tts_edge_simple.py
"""

import asyncio
import aiofiles
import os
import re
import argparse
from pathlib import Path
import edge_tts
from tqdm import tqdm

# Cấu hình
VOICE = "vi-VN-HoaiMyNeural"  # Giọng nữ tiếng Việt
# VOICE = "vi-VN-NamMinhNeural"  # Giọng nam tiếng Việt
OUTPUT_SAMPLE_RATE = 48000

# Các giọng tiếng Việt có sẵn:
# - vi-VN-HoaiMyNeural (Nữ)
# - vi-VN-NamMinhNeural (Nam)

async def text_to_speech_edge(text, output_file, voice=VOICE):
    """Chuyển text thành audio sử dụng Edge TTS"""
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)

def clean_text_for_tts(text):
    """Làm sạch text, loại bỏ markdown và ký tự đặc biệt"""
    # Loại bỏ header markdown
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    # Loại bỏ bold/italic
    text = re.sub(r'\*\*|\*|_', '', text)
    # Loại bỏ links
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Loại bỏ code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    # Loại bỏ inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Loại bỏ blockquotes
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    # Loại bỏ horizontal rules
    text = re.sub(r'^[-*_]{3,}$', '', text, flags=re.MULTILINE)
    # Loại bỏ bảng
    text = re.sub(r'\|[|\-\s]+\|', '', text)
    # Chuẩn hóa
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[^\w\s.,!?;:()\'"-]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

async def process_book(input_file, output_file, chunk_size=5000, voice=VOICE):
    """Xử lý toàn bộ sách và tạo audio"""
    # Đọc file
    print(f"📖 Đang đọc: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # Làm sạch
    print("🧹 Đang làm sạch text...")
    clean_text = clean_text_for_tts(raw_text)

    # Chia thành chunks
    print(f"✂️ Đang chia text (chunk size: {chunk_size} chars)...")
    chunks = []
    for i in range(0, len(clean_text), chunk_size):
        chunks.append(clean_text[i:i + chunk_size])

    print(f"   Tổng số chunks: {len(chunks)}")
    print(f"   Giọng đọc: {voice}")

    # Tạo thư mục tạm
    temp_dir = Path(input_file).parent / "temp_audio_tts"
    temp_dir.mkdir(exist_ok=True)

    # Tạo audio cho từng chunk
    print("🎙️ Đang tạo audio (sử dụng Edge TTS)...")
    audio_files = []

    for i, chunk in enumerate(chunks):
        if not chunk.strip():
            continue

        chunk_file = temp_dir / f"chunk_{i:04d}.wav"
        audio_files.append(chunk_file)

        print(f"   Đang xử lý chunk {i+1}/{len(chunks)}...")
        try:
            await text_to_speech_edge(chunk.strip(), str(chunk_file), voice)
            print(f"      ✅ Đã tạo: {chunk_file.name}")
        except Exception as e:
            print(f"      ❌ Lỗi: {e}")
            audio_files.remove(chunk_file)

    # Kết hợp audio (sử dụng simplest method - copy)
    print("\n🎵 Đang kết hợp audio...")

    if audio_files:
        # Đọc và nối audio
        import wave
        import numpy as np
        import soundfile as sf

        combined_audio = None

        for audio_file in tqdm(audio_files):
            audio, sr = sf.read(str(audio_file))
            if combined_audio is None:
                combined_audio = audio
            else:
                combined_audio = np.concatenate([combined_audio, audio])

        # Lưu file kết quả
        sf.write(output_file, combined_audio, sr)
        print(f"\n✅ Đã lưu: {output_file}")
        print(f"   Thời lượng: {len(combined_audio) / sr / 60:.2f} phút")
        print(f"   Sample rate: {sr} Hz")

    # Cleanup
    print("\n🗑️ Đang dọn dẹp...")
    for f in audio_files:
        f.unlink()
    temp_dir.rmdir()

    print("\n✨ Hoàn thành!")

def main():
    parser = argparse.ArgumentParser(
        description="Chuyển sách tiếng Việt thành audio sử dụng Edge TTS"
    )
    parser.add_argument(
        "--input", "-i",
        default="/Users/mac/tools/AIPM/ebooks/00-Full-Book/INSPIRED-Full-Book.md",
        help="Đường dẫn file markdown"
    )
    parser.add_argument(
        "--output", "-o",
        default="/Users/mac/tools/AIPM/ebooks/00-Full-Book/INSPIRED-Full-Book-EdgeTTS.wav",
        help="Đường dẫn file audio đầu ra"
    )
    parser.add_argument(
        "--voice", "-v",
        default="vi-VN-HoaiMyNeural",
        help="Giọng nói (vi-VN-HoaiMyNeural hoặc vi-VN-NamMinhNeural)"
    )
    parser.add_argument(
        "--chunk-size", "-c",
        type=int,
        default=5000,
        help="Số ký tự tối đa cho mỗi chunk"
    )

    args = parser.parse_args()

    # Sử dụng voice từ args
    voice = args.voice

    # Chạy
    asyncio.run(process_book(args.input, args.output, args.chunk_size, voice))

if __name__ == "__main__":
    main()
