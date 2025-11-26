import cv2
import os
import argparse

def center_crop(img, target_w, target_h):
    h, w = img.shape[:2]

    # 若不足目标尺寸，先 pad 黑边
    if h < target_h or w < target_w:
        pad_top = max((target_h - h) // 2, 0)
        pad_bottom = max(target_h - h - pad_top, 0)
        pad_left = max((target_w - w) // 2, 0)
        pad_right = max(target_w - w - pad_left, 0)
        img = cv2.copyMakeBorder(
            img, pad_top, pad_bottom, pad_left, pad_right,
            borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0)
        )
        h, w = img.shape[:2]

    y1 = (h - target_h) // 2
    x1 = (w - target_w) // 2
    return img[y1:y1 + target_h, x1:x1 + target_w]

def extract_frames(video_path, output_folder, crop_w=None, crop_h=None):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Total frames: {total_frames}, FPS: {fps}")

    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if crop_w is not None and crop_h is not None:
            frame = center_crop(frame, crop_w, crop_h)

        frame_filename = os.path.join(output_folder, f"frame_{frame_idx:04d}.png")
        cv2.imwrite(frame_filename, frame)
        if frame_idx % 50 == 0:
            print(f"Saved frame {frame_idx} -> {frame_filename}")
        frame_idx += 1

    cap.release()
    print(f"Frame extraction complete. Saved {frame_idx} frames to {output_folder}.")

def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract frames from a video; optional center-crop to W×H."
    )
    parser.add_argument("video_path", type=str, help="Path to the video file.")
    parser.add_argument("output_folder", type=str, help="Folder to save extracted frames.")
    parser.add_argument("--crop", nargs=2, type=int, metavar=("W", "H"),
                        help="Center-crop each frame to size (W, H).")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.crop is not None:
        crop_w, crop_h = args.crop
    else:
        crop_w = crop_h = None
    extract_frames(args.video_path, args.output_folder, crop_w=crop_w, crop_h=crop_h)