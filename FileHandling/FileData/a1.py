n = int(input("Preview:"))
print(open("class-notes.txt")).read(n)

lines = open("class-notes.txt").readlines()
print(len(lines))
for i, l in enumerate(lines, 1):
    print(i, "->", l.strip())

w = input("Skip: ")
for l in lines:
   print(("skip" if l.startswith(w) else "keep"), "->", l.strip())

open("odd-lines.text", "w").writelines(lines[::2])
print("Done")
