import cv2

# Open the video capture
cap = cv2.VideoCapture('./output.mp4')  # Replace 'your_video_file.mp4' with your video file path

# Check if the video is opened successfully
if not cap.isOpened():
    print("Error: Could not open video")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Get the current position in milliseconds
    timestamp_msec = cap.get(cv2.CAP_PROP_POS_MSEC)

    # Convert milliseconds to a readable time format
    current_time = int(timestamp_msec / 1000)  # Convert to seconds
    minutes = current_time // 60
    seconds = current_time % 60
    hours = minutes // 60
    minutes = minutes % 60

    # Print the current time
    print(f"Current Time: {hours:02d}:{minutes:02d}:{seconds:02d}")

    # Show the frame (optional)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
