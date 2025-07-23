from deepface import DeepFace


# Provide the correct path to your image file in Google Drive
image_path = '/Users/ashwinikumar/Desktop/surprise.jpg'

# Analyze facial expression without enforcing detection
result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)


# Print the result
emotion_result = result[0]['emotion']
ordered_emotions = sorted(emotion_result.items(), key=lambda x: x[1], reverse=True)

print("Facial Expression Result:")
for emotion, score in ordered_emotions:
    print(f"{emotion.capitalize()}: {score}")
    