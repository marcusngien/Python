# ===== 1. Changing case =====
message = "Goodbye! Cristiano Ronaldo. In my opinion, you are still a legend even though you don't have a world cup."
print(message)
print(message.title())       # ... Even Though You Don'T Have ...  <- note: "Don'T", title() treats ' as a word boundary
print(message.lower())       # all lowercase
print(message.upper())       # ALL UPPERCASE
print(message.capitalize())  # only the first letter uppercase, the rest lowercase
print(message.swapcase())    # swap upper <-> lower


# ===== 2. f-string =====
name = "Cristiano Ronaldo"
message = "In my opinion, you are still a legend even though you don't have a world cup."
full_message = f"Goodbye! {name}, {message}"
print(full_message)

# use a method inside {}
name = "cristiano ronaldo"
full_message = f"Goodbye! {name.title()}, {message}"
print(full_message)

# title() only the name (not the whole sentence)
greeting = f"Goodbye, {name.title()}!"
print(greeting)


# ===== 3. Tab and newline =====
print("AI:\tClaude")                          # \t = tab
print("AI:\nClaude")                          # \n = new line
print("AI:\n\tClaude\n\tChatGPT\n\tDeepseek")  # new line + tab

# escape characters
print("C:\\Users\\Python")      # \\ prints one backslash
print('He said: "Hello"')       # use '' outside to print ""
print("It\'s fine")             # \' prints a single quote
print(r"C:\new\table")          # r"" raw string: no escape


# ===== 4. Stripping whitespace =====
# Tip: use repr() or [] to make spaces visible
favourite_ai = "  Claude  "
print(f"[{favourite_ai}]")             # [  Claude  ]

# Wrong 1: forgot the brackets -> the method is NOT called
print(favourite_ai.rstrip)             # <built-in method rstrip of str object ...>

# Wrong 2: called, but not assigned -> original is unchanged (strings are immutable)
favourite_ai.rstrip()
print(f"[{favourite_ai}]")             # [  Claude  ]

# Correct: assign the result back
favourite_ai = favourite_ai.rstrip()
print(f"[{favourite_ai}]")             # [  Claude]

# lstrip() / strip()
text = "   Claude   "
print(f"[{text.lstrip()}]")            # [Claude   ]  remove left
print(f"[{text.rstrip()}]")            # [   Claude]  remove right
print(f"[{text.strip()}]")             # [Claude]      remove both sides

# strip with arguments: removes ANY of these characters from the edges
print("xxhelloxx".strip("x"))          # hello
print("abcHELLOcba".strip("abc"))      # HELLO   (a, b, c are treated as a set)


# ===== 5. Removing prefix / suffix =====
# Python 3.9+
link = "https://python.org"
link = link.removeprefix("https://")
print(link)                            # python.org

file_name = "notes.py"
print(file_name.removesuffix(".py"))   # notes

# removeprefix vs lstrip
print("xxhello".removeprefix("x"))     # xhello  (remove the exact string ONCE)
print("xxhello".lstrip("x"))           # hello   (remove ALL matching characters)


# ===== 6. Other useful string methods =====
text = "Python is fun"
print(len(text))                       # 13
print(text.replace("fun", "great"))    # Python is great
print(text.split())                    # ['Python', 'is', 'fun']
print("-".join(["a", "b", "c"]))       # a-b-c
print(text.startswith("Py"))           # True
print(text.endswith("fun"))            # True
print(text.find("is"))                 # 7  (-1 if not found)
print(text.count("n"))                 # 2