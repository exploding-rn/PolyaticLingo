import tkinter as tk

# --- Your cipher logic ---
usercodechoice = ' zxcvbnmlkjhgfdsaqwertyuiop '
backwards = usercodechoice[::-1]
code = {usercodechoice[i]: backwards[i] for i in range(len(usercodechoice))}

def atbash(text):
    text = text.lower()
    output = ''
    for letter in text:
        if letter in code:
            output += code[letter]
        else:
            output += letter   # keep characters that aren't in the cipher
    return output

# --- GUI part ---
def on_encode():
    user_text = entry.get()
    result = atbash(user_text)
    output_label.config(text=result)

root = tk.Tk()
root.title("Cipher Encoder")
root.geometry("350x200")

# Input label + entry
tk.Label(root, text="Text to encode/decode:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Encode button
tk.Button(root, text="Encode/Decode", command=on_encode).pack(pady=10)

# Output label
tk.Label(root, text="Result:").pack()
output_label = tk.Label(root, text="", fg="blue", wraplength=300)
output_label.pack(pady=5)

root.mainloop()