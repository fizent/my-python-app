

import tkinter as tk
import pyttsx3
while True:
    name = input("welcom to my app(fazel)" + "\n"+ "enter name :")
    counts = {}

    def say():
        text = entry.get()
        console_text.insert(tk.END, f"hello {name}\n")
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


        
        
        if text in counts:
            counts[text] += 1
            if counts[text] == 3:
                engine.say("stop")
                engine.runAndWait()
                counts[text] = 0
                root.destroy()
                print("just you can use three print (Because it was repetitive)")
        else:
            counts[text] = 1

        
        return text

    def save_text():
        text_to_save = say()
        with open("saved_text.txt", "a") as file:
            file.write(text_to_save + "\n")
        print("Text saved successfully!")

    def clear_text():
        console_text.delete('1.0', tk.END)
        counts.clear()

    def show_text():
        label.config(text="thank you for good opinion you :)")
        root.after(2000, reset_text)  


    def reset_text():
        label.config(text="why did you say ?")

    root = tk.Tk()
    label = tk.Label(root, text="Enter your text:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="If you want to listen, click me", command=say)
    button.pack()

    clear_button = tk.Button(root, text="Clear all texts", command=clear_text)
    clear_button.pack()

    console_text = tk.Text(root)
    console_text.pack()

    button = tk.Button(root, text="good app", command=show_text)
    button.pack()
    button = tk.Button(root, text="bad app", command=show_text)
    button.pack()
    label = tk.Label(root, text="why did you say ?")
    label.pack()
    save_button = tk.Button(root, text="Save text", command=save_text)
    save_button.pack()
    root.mainloop()
    agine = input("do you want run agine ?")
    if agine == "yes" or agine == "ok":
        print("ok")
    else :
        print("okay", name, "bye")
        break


