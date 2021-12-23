import speech_recognition as sr 
from sign import alphabet

def main():
    # Initialize the recognizer
    r = sr.Recognizer()
    # Creates source as microphone
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        # Adjusts for ambient noise
        print("Please Say something. . .")

        # Listens through microphone for audio

        # Uses recognizer to convert audio to, catches if there is no audio

        try:
            audio = r.listen(source)
            audio2 = r.recognize_google(audio)
        except Exception:
            print("Please Speak Clearly")



        # If there is something wrong with the output, there is a try catch for this

        try:
            print("You have said: \n" + audio2)

        except Exception as e:
                
            print("Error: " + str(e))

        # If the word sign language is said then the function will run

        if audio2.lower() == "sign language":
            sign_language()



def sign_language():
    # Initialize the recognizer
    r = sr.Recognizer()
    # Creates source as microphone
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        # Adjusts for ambient noise
        print("Please say a phrase to be translated for sign language")
        # Listens through microphone for audio

        # Uses recognizer to convert audio to, catches if there is no audio
        try:
            audio3 = r.listen(source)
            audio4 = r.recognize_google(audio3)
        except Exception:
            print("Please Speak Clearly")


        try:
            print("You have said: \n" + audio4)

        except Exception as e:
                
            print("Error: " + str(e))


        
        # Calls the alphabet function in the other file to display hand figures

        alphabet(audio4)


if __name__ == "__main__":
    main()

x = 1