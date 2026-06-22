from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from problem_v2_spec import AERO_INPUT_COLS, AERO_OUTPUT_COLS


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--input",
        type=str,
        default="data/aero_labeled_v2_300k_hard40k_khead.csv",
        help="Path to the labeled 300k aero CSV.",
    )
    p.add_argument(
        "--outdir",
        type=str,
        default="data",
        help="Directory where the .npy files and README will be written.",
    )
    p.add_argument(
        "--prefix",
        type=str,
        default="aero_300k_hard40k_khead",
        help="Output filename prefix.",
    )
    return p.parse_args()


def resolve_path(base: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else base / path


def stats_lines(df: pd.DataFrame, cols: list[str]) -> list[str]:
    lines: list[str] = []
    for col in cols:
        s = pd.to_numeric(df[col], errors="coerce")
        lines.append(
            f"- {col}: min={float(s.min()):.6g}, max={float(s.max()):.6g}"
        )
    return lines


def main() -> None:
    args = parse_args()
    in_path = resolve_path(PROJECT_ROOT, args.input)
    outdir = resolve_path(PROJECT_ROOT, args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(in_path)
    if "status" in df.columns:
        df = df[df["status"] == "ok"].copy()

    required = AERO_INPUT_COLS + AERO_OUTPUT_COLS
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise KeyError(f"Missing required columns: {missing}")

    df = df.dropna(subset=required).reset_index(drop=True)

    x = df[AERO_INPUT_COLS].to_numpy(np.float32)
    y = df[AERO_OUTPUT_COLS].to_numpy(np.float32)
    xy = np.concatenate([x, y], axis=1)

    prefix = args.prefix
    x_name = f"{prefix}_input.npy"
    y_name = f"{prefix}_output.npy"
    xy_name = f"{prefix}_input_output.npy"
    x_cols_name = f"{prefix}_input_columns.txt"
    y_cols_name = f"{prefix}_output_columns.txt"
    xy_cols_name = f"{prefix}_input_output_columns.txt"
    readme_name = f"{prefix}_README.txt"

    np.save(outdir / x_name, x)
    np.save(outdir / y_name, y)
    np.save(outdir / xy_name, xy)

    (outdir / x_cols_name).write_text("\n".join(AERO_INPUT_COLS) + "\n", encoding="utf-8")
    (outdir / y_cols_name).write_text("\n".join(AERO_OUTPUT_COLS) + "\n", encoding="utf-8")
    (outdir / xy_cols_name).write_text(
        "\n".join(AERO_INPUT_COLS + AERO_OUTPUT_COLS) + "\n",
        encoding="utf-8",
    )

    lines: list[str] = []
    lines.append("300k Aerodynamic Dataset Export")
    lines.append("")
    lines.append(f"Source CSV: {in_path.name}")
    lines.append(f"Rows exported: {len(df)}")
    lines.append("Status filter: status == ok")
    lines.append("Missing-value filter: rows with NaN in required columns were removed")
    lines.append("Data type in .npy files: float32")
    lines.append("")
    lines.append("Saved files")
    lines.append(f"- {x_name}: input matrix with shape ({x.shape[0]}, {x.shape[1]})")
    lines.append(f"- {y_name}: output matrix with shape ({y.shape[0]}, {y.shape[1]})")
    lines.append(f"- {xy_name}: concatenated [input | output] matrix with shape ({xy.shape[0]}, {xy.shape[1]})")
    lines.append(f"- {x_cols_name}: input column names in saved order")
    lines.append(f"- {y_cols_name}: output column names in saved order")
    lines.append(f"- {xy_cols_name}: combined column names in saved order")
    lines.append("")
    lines.append("Input columns and value ranges")
    lines.extend(stats_lines(df, AERO_INPUT_COLS))
    lines.append("")
    lines.append("Output columns and value ranges")
    lines.extend(stats_lines(df, AERO_OUTPUT_COLS))
    lines.append("")
    lines.append("Input column order")
    lines.extend(f"- {c}" for c in AERO_INPUT_COLS)
    lines.append("")
    lines.append("Output column order")
    lines.extend(f"- {c}" for c in AERO_OUTPUT_COLS)
    lines.append("")
    lines.append("Combined column order")
    lines.extend(f"- {c}" for c in (AERO_INPUT_COLS + AERO_OUTPUT_COLS))

    (outdir / readme_name).write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Exported {len(df)} rows to {outdir}")
    print(f"Saved: {x_name}, {y_name}, {xy_name}, {readme_name}")


if __name__ == "__main__":
    main()
