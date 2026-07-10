import tkinter as tk

# --- Cipher setup: only letters ---
ciphercode = " zxcvbnmlkjhgfdsaqwertyuiop "
backwards = ciphercode[::-1]
code = {ciphercode[i]: backwards[i] for i in range(len(ciphercode))}
print(code)
def atbash(text):
    text = text.lower()
    output = ''
    for letter in text:
        if letter.isalpha():
            output += code.get(letter, letter)
        else:
            output += letter  # numbers/punctuation pass through unchanged
    return output

def on_encode():
    result = atbash(entry.get())
    output_var.set(result)

def on_copy():
    root.clipboard_clear()
    root.clipboard_append(output_var.get())
    root.update()

root = tk.Tk()
root.title("Cipher Encoder")
root.geometry("350x220")

tk.Label(root, text="Text to encode:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Encode", command=on_encode).pack(pady=5)

tk.Label(root, text="Result:").pack()
output_var = tk.StringVar()
output_entry = tk.Entry(root, textvariable=output_var, width=40, state="readonly")
output_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=on_copy).pack(pady=5)

root.mainloop()
