from pathlib import Path
from faster_whisper import WhisperModel

model = WhisperModel("medium", device="cuda", compute_type="float32")

for audio in Path("/audio").rglob("*"):
    if audio.suffix.lower() not in {".mp3", ".m4a", ".wav", ".ogg", ".flac", ".opus"}:
        continue

    print(f"\nTranscribing: {audio.name}")

    segments, _ = model.transcribe(str(audio))

    text = " ".join(segment.text.strip() for segment in segments)

    output = Path("/output") / f"{audio.stem}.txt"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text + "\n", encoding="utf-8")

    print(text)
    print(f"Saved: {output}")

print("\nDone!")
