# EmoSense: Emotion Recognition Using Facial Features

A cross-platform mobile application that enables users to upload or capture images and accurately detect and classify emotions based on facial features. This project applies advanced computer vision techniques to provide real-time emotional feedback.

## 👨‍💻 Team Members
- Ashwini Kumar – [ashwinik@mun.ca](mailto:ashwinik@mun.ca)
- Ismat Sifat Yousuf – [isyousuf@mun.ca](mailto:isyousuf@mun.ca)
- Md. Imran Hossain Showrov – [mihshowrov@mun.ca](mailto:mihshowrov@mun.ca)

---

## 📱 What is EmoSense?

EmoSense is a deep learning–powered mobile app built using **Kivy** and **FastAPI**. It performs real-time emotion detection from facial images using two neural networks:
- A **Key Facial Points Detection** model trained on grayscale facial landmark data.
- A **Facial Expression Classification** model trained on 20,000+ labeled and augmented images for 5 emotions: **Angry**, **Disgust**, **Sad**, **Happy**, and **Surprised**.

---

## 🎯 Objectives

- Design and train robust ANN and ResNet models for emotion detection.
- Implement end-to-end emotion classification using facial key points.
- Deploy backend services using FastAPI for real-time predictions.
- Deliver a cross-platform Kivy-based mobile interface.
- Contribute to the field of emotion-aware systems and applications.

---

## 📦 Tech Stack

| Component      | Technology Used            |
|----------------|----------------------------|
| Frontend       | Kivy (Python)              |
| Backend API    | FastAPI                    |
| Deep Learning  | TensorFlow, Keras          |
| Image Handling | OpenCV                     |
| Data Storage   | Numpy, Pandas              |
| DevOps         | Git, GitHub, Cloud Storage |

---

## 🧠 Methodology

1. **Data Preparation**:  
   - Used 20,000+ facial images (2,000 annotated).
   - Applied data augmentation: brightness changes, flipping, zooming, darkening.
   - Training/Testing split: 80/20.

2. **Model Architecture**:
   - CNN-based key facial landmark detection on 96x96 grayscale images.
   - Emotion classifier trained on 5 labels using flattened key-point features.

3. **Backend Deployment**:
   - FastAPI endpoints for prediction and image processing.
   - Pretrained models loaded and served using TensorFlow Serving.

4. **Mobile UI**:
   - Kivy interface for image capture/upload and displaying emotion results.
   - Real-time emotion detection via REST API calls.

---

## 💡 Business Use Cases

- Customer emotion detection in retail and marketing.
- Student engagement monitoring in virtual classrooms.
- Driver alertness detection for automotive safety.
- Mental health analysis using facial expression patterns.
- Emotion-adaptive content recommendations in entertainment.

---

## 🚀 Future Enhancements

- Multimodal Emotion Detection (facial + voice + text)
- Emotion-driven UX for games and apps
- Emotion-based authentication systems
- Integration with social platforms and wearable devices

---

## 📅 Project Timeline

| Milestone              | Status       |
|------------------------|--------------|
| Data Collection        | ✅ Completed |
| Model Training         | ✅ Completed |
| API Development        | ✅ Completed |
| UI/UX Development      | ✅ Completed |
| Deployment & Testing   | ✅ Completed |
| Final Documentation    | ✅ Completed |

---

## 🙏 Acknowledgements

This project was developed as part of the **AI 6002 – Capstone Project** at Memorial University of Newfoundland under the guidance of the faculty and project advisors.


