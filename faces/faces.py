def convert(face):
    face = face.replace(":)", "🙂").replace(":(", "🙁")
    return face

def main():
    user_input = input("Write something: ")

    user_input = convert(user_input)

    print (user_input)
