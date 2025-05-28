import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    excluded = '0O1l'
    chars = ''.join(c for c in string.ascii_letters + string.digits + string.punctuation if c not in excluded)
    password = ''.join(random.choice(chars) for _ in range(length))
    
    strength = password_strength(password)
    result_label.config(text=f"Password: {password}\nStrength: {strength}")

def password_strength(pw):
    score = 0
    if len(pw) >= 12: score += 1
    if any(c.islower() for c in pw) and any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c in string.punctuation for c in pw): score += 1
    return ["Weak", "Medium", "Strong", "Strong"][score-1] if score > 0 else "Very Weak"

# Tkinter GUI
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter password length:").pack()
entry_length = tk.Entry(root)
entry_length.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
