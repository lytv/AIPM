# Hướng Dẫn Chuyển Sách INSPIRED Sang Audio

## Tổng Quan

Có 2 phương pháp để chuyển text sang audio tiếng Việt:

| Phương pháp | Model | Yêu cầu | Chất lượng | Độ khó |
|--------------|-------|---------|------------|--------|
| **Edge TTS** | Microsoft Edge | Internet, không cần GPU | ⭐⭐⭐⭐ | Dễ |
| **VieNeu-TTS** | Hugging Face | GPU (tốt nhất) | ⭐⭐⭐⭐⭐ | Trung bình |

---

## Cách 1: Sử Dụng Edge TTS (Khuyến nghị - Dễ nhất)

### Bước 1: Cài đặt

```bash
cd /Users/mac/tools/AIPM/ebooks
pip install edge-tts asyncio aiofiles tqdm soundfile numpy
```

### Bước 2: Chạy script

```bash
# Với giọng nữ (mặc định)
python tts_edge_simple.py

# Với giọng nam
python tts_edge_simple.py -v "vi-VN-NamMinhNeural"

# Tùy chỉnh input/output
python tts_edge_simple.py -i input.md -o output.wav -c 5000
```

### Ưu điểm:
- ✅ Không cần GPU
- ✅ Cài đặt đơn giản
- ✅ Chất lượng tốt
- ✅ Miễn phí

### Nhược điểm:
- ⚠️ Cần kết nối internet
- ⚠️ Giới hạn số ký tự mỗi chunk (5000 chars)

---

## Cách 2: Sử Dụng VieNeu-TTS (Chất lượng cao nhất)

### Bước 1: Cài đặt

```bash
cd /Users/mac/tools/AIPM/ebooks
pip install -r requirements.txt
```

**Yêu cầu:**
- GPU NVIDIA (4GB VRAM trở lên)
- CUDA Toolkit
- 8GB RAM trở lên

### Bước 2: Chạy script

```bash
python text_to_audio.py
```

### Ưu điểm:
- ✅ Chất lượng cao nhất
- ✅ Không cần internet khi đã tải model
- ✅ Có thể tùy chỉnh nhiều

### Nhược điểm:
- ⚠️ Cần GPU mạnh
- ⚠️ Cài đặt phức tạp hơn
- ⚠️ Tốn VRAM

---

## Các Model Tốt Nhất Cho Tiếng Việt (Hugging Face)

### Top 1: VieNeu-TTS
- **Link:** https://huggingface.co/pnnbao-ump/VieNeu-TTS
- **Parameters:** 0.3B - 0.6B
- **Downloads:** 5,460
- **Likes:** 57

### Top 2: F5-TTS Vietnamese
- **Link:** https://huggingface.co/hynt/F5-TTS-Vietnamese-ViVoice
- **Downloads:** 1,720
- **Likes:** 37

### Top 3: viXTTS
- **Link:** https://huggingface.co/capleaf/viXTTS
- **Downloads:** 476
- **Likes:** 97 (cao nhất!)

---

## Xử Lý Sự Cố

### Lỗi: "No module named 'edge_tts'"
```bash
pip install edge-tts
```

### Lỗi: "CUDA out of memory"
- Giảm chunk size
- Sử dụng Edge TTS thay vì VieNeu-TTS
- Đóng các ứng dụng khác đang dùng GPU

### Lỗi: "Could not connect to the server"
- Kiểm tra kết nối internet
- Kiểm tra firewall

---

## Kết Quả

File audio sẽ được lưu tại:
- `INSPIRED-Full-Book-EdgeTTS.wav` (Edge TTS)
- `INSPIRED-Full-Book.wav` (VieNeu-TTS)

**Thời gian ước tính:**
- Edge TTS: ~30-60 phút (tùy độ dài text)
- VieNeu-TTS: ~15-30 phút (với GPU tốt)

---

## Tham Khảo

- [Hugging Face Vietnamese TTS Models](https://huggingface.co/models?pipeline_tag=text-to-speech&language=vi)
- [Edge TTS GitHub](https://github.com/rany2/edge-tts)
- [VieNeu-TTS Model Card](https://huggingface.co/pnnbao-ump/VieNeu-TTS)
