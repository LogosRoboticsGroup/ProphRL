import subprocess
from pathlib import Path
import shlex

# 根目录按你的实际路径改
ROOT = Path("interact_demo/demo-2arm-control_rotate")

def merge_two_segments(folder: Path):
    seg0 = folder / "seg_000.mp4"
    seg1 = folder / "seg_001.mp4"
    out  = folder / "merged.mp4"   # 输出文件名，可自己改

    if not seg0.exists() or not seg1.exists():
        print(f"[skip] {folder} 缺 seg_000 或 seg_001")
        return

    if out.exists():
        print(f"[skip] {out} 已存在")
        return

    # 生成 concat 列表文件
    concat_file = folder / "concat_list.txt"
    concat_file.write_text(
        f"file {shlex.quote(str(seg0))}\n"
        f"file {shlex.quote(str(seg1))}\n",
        encoding="utf-8"
    )

    # ffmpeg concat demuxer（无重编码，只拼接）
    cmd = [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_file),
        "-c", "copy",
        str(out),
    ]

    print(f"[run] {' '.join(cmd)}")
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    if result.returncode == 0:
        print(f"[ok] {folder.name} -> {out.name}")
    else:
        print(f"[error] {folder.name}")
        print(result.stdout)

    # 用完可以把临时 concat 文件删掉
    concat_file.unlink(missing_ok=True)

def main():
    folder = Path("/Users/zhangjiahui/Research/CVPR26 VLARL/ProphRL/docs/assets/videos/interact_demo/demo-2arm-control_rotate")
    for sub in folder.iterdir():
        if sub.is_dir():
            merge_two_segments(sub)

if __name__ == "__main__":
    main()
