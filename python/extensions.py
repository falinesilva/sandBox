filename = input ("File name: ")

filesname = filename.lower().strip()

if ".gif" in filesname:
    print("image/gif")
elif ".jpeg" in filesname:
    print("image/jpeg")
elif ".jpg" in filesname:
    print("image/jpeg")
elif ".png" in filesname:
    print("image/png")
elif ".pdf" in filesname:
    print("application/pdf")
elif ".txt" in filesname:
    print("text/plain")
elif ".zip" in filesname:
    print("application/zip")
else:
    print("application/octet-stream")
