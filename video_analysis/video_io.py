import cv2

def read_video(file_path):
    cap = cv2.VideoCapture(file_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Chuyển đổi từ BGR sang RGB
        frames.append(frame)
    cap.release()
    return frames

def save_video(frames, output_path, fps=30):
    if not frames:
        raise ValueError("No frames to save")

    height, width, layers = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Sử dụng codec H.264
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame in frames:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Chuyển đổi từ RGB sang BGR
        out.write(frame)

    out.release()
    print(f"Video saved successfully at {output_path}")
