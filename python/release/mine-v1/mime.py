def main():
    """
    Determines the MIME type based on a file extension.
    Example: 'image.jpg' → 'image/jpeg'
    """
    filename = input("File name: ").strip().lower()

    mime_types = {
        ".gif": "image/gif",
        ".jpeg": "image/jpeg",
        ".jpg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    for extension, mime in mime_types.items():
        if filename.endswith(extension):
            print(mime)
            break
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()
