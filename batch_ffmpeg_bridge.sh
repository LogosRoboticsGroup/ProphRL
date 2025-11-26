#!/usr/bin/env bash

# 进入存放 mp4 的目录（注意路径有空格，一定要加引号）
cd "/Users/zhangjiahui/Research/CVPR26 VLARL/Prophet/docs/assets/videos/perturbed_actions" || exit 1

# 遍历当前目录下所有 mp4
for f in *.mp4; do
  # 如果目录里没有 mp4，避免输出 "*.mp4" 这种假名字
  [ -e "$f" ] || continue

  out="${f%.mp4}_web.mp4"
  echo "Converting: $f -> $out"

  ffmpeg -i "$f" \
    -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p \
    -c:a aac -b:a 128k \
    -movflags +faststart \
    "$out"
done

echo "Done."
