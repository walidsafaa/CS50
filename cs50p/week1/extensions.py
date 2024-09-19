filename = input("File name: ").strip().lower()

extensions = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip",
}

if filename[-4:] in extensions:
    print(extensions[filename[-4:]])
elif filename[-5:] in extensions:
    print(extensions[filename[-5:]])
else:
    print("application/octet-stream")

'''
file = (input("File name: ")).lower().strip().split(".")

application = ["zip", "pdf"]
image = ["png", "gif"]

if file[-1] == "txt":
    print("text/plain")
elif file[-1] in application:
    print(f"application/{file[-1]}")
elif file[-1] == "jpg" or file[-1] == "jpeg":
    print("image/jpeg")
elif file[-1] in image:
    print(f"image/{file[-1]}")
else:
    print("application/octet-stream")
'''