import speech_recognition as sr
import pyttsx3

# Khởi tạo đối tượng phát âm
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Chọn giọng nói thứ 2 trong danh sách giọng nói có sẵn

# Hàm phát âm
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Khởi tạo bộ nhận dạng giọng nói
r = sr.Recognizer()

# Hàm ghi âm và nhận dạng giọng nói
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        # Nhận dạng giọng nói
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Error: {0}".format(e))
        return None

# Vòng lặp chính
while True:
    # Ghi âm và nhận dạng giọng nói
    text = listen()

    # Nếu không thể nhận dạng giọng nói, yêu cầu người dùng nhập văn bản bằng bàn phím
    if text is None:
        text = input("Sorry, I could not understand you. Please type your request: ")

    # Xử lý câu lệnh
    if text == "hello":
        speak("Hello, how can I help you?")
    elif text == "goodbye":
        speak("Goodbye!")
        break
    else:
        speak("I'm sorry, I didn't understand that.")
