# with open("file.txt","r+") as f:
#     # for line in f:
#         # f.write("hii")
#         print(f.readline())
#         print(f.tell()) # tell the cursor position

with open("file.txt", "r+") as f:
    content = f.read()
    print(f.seek(0)) # Move the cursor to position 0
    f.write(content + "\nhii")
