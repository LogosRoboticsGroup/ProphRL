import subprocess
from pathlib import Path
import shlex

# 根目录按你的实际路径改
ROOT = Path("interact_demo/demo-cm-control")

def merge_segments(folder: Path, num_segments: int = 3):
    # 按 seg_000, seg_001, ..., seg_00{n-1} 命名
    segs = [folder / f"seg_{i:03d}.mp4" for i in range(num_segments)]
    out  = folder / "merged.mp4"

    # 检查是否都有
    missing = [s.name for s in segs if not s.exists()]
    if missing:
        print(f"[skip] {folder} 缺 {', '.join(missing)}")
        return

    if out.exists():
        print(f"[skip] {out} 已存在")
        return

    # 生成 concat 列表文件
    concat_file = folder / "concat_list.txt"
    lines = []
    for s in segs:
        # 用单引号包起来，避免路径里有空格（你现在路径里就是有空格的）
        lines.append(f"file '{s}'\n")
        # 如果你更喜欢用 shlex.quote，也可以：
        # lines.append(f"file {shlex.quote(str(s))}\n")

    concat_file.write_text("".join(lines), encoding="utf-8")

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
    result = subprocess.run(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True)

    if result.returncode == 0:
        print(f"[ok] {folder.name} -> {out.name}")
    else:
        print(f"[error] {folder.name}")
        print(result.stdout)

    # 用完把临时 concat 文件删掉
    concat_file.unlink(missing_ok=True)

def main():
    root = Path("/Users/zhangjiahui/Research/CVPR26 VLARL/ProphRL/docs/assets/videos/interact_demo/demo-cm-control")
    for sub in root.iterdir():
        if sub.is_dir():
            merge_segments(sub, num_segments=3)

if __name__ == "__main__":
    main()
