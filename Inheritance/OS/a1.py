import os

print("=== Science Notes ===")
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("=== Word Count ===")
with open("maths-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.
        strip())
print()

print("=== Merging Notes ===")
if os.path.exists("all-notes.txt"):
    print("all-notes.txt aldready exists - overwriting")
else:
    print("all-notes.txt not found - creating now")

content = ""
with open("science-notes.txt", "r") as f:
    content += "___science-notes.txt ---\n"
    content += f.read() + "\n"
with open("maths-notes.txt", "r") as f:
    content += "___maths-notes.txt ---\n"
    content += f.read() + "\n"
with open("all-notes.txt", "w") as out:
    out.write(content)