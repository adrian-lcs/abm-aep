"""
Phase 1: Multi-codec FFmpeg encoding engine.

Encodes a normalized WAV reference into all 10 target formats:
WAV + MP3(96k/128k/320k) + Vorbis(q2/q4) + AAC(128k/256k) + Opus(96k/128k).
For Vorbis, measure and report the resulting average bitrate via ffprobe.
"""

FORMATS = [
    "wav",
    "mp3_96k", "mp3_128k", "mp3_320k",
    "vorbis_q2", "vorbis_q4",
    "aac_128k", "aac_256k",
    "opus_96k", "opus_128k",
]


def encode_all_formats(input_wav: str, out_dir: str) -> dict:
    raise NotImplementedError("TODO: implement ffmpeg-python encoding per FORMATS")


def measure_actual_bitrate(path: str) -> float:
    raise NotImplementedError("TODO: shell out to ffprobe, parse actual kbps")
