"""
Phase 1: EBU R128 loudness normalization.

Target: -14 LUFS integrated, -1.0 dBTP true-peak ceiling.
Use pyloudnorm; cross-check against ffmpeg's loudnorm filter.
"""


def normalize_wav(input_path: str, output_path: str,
                   target_lufs: float = -14.0, tp_ceiling: float = -1.0) -> None:
    raise NotImplementedError("TODO: implement pyloudnorm normalization")
