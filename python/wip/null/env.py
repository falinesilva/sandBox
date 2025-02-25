def new_list(s):
        user_list = []
        name = s.strip()
        user_list.append(name)
        return user_list

def main():

    user_input = input("input: ")

    users_new_list = new_list(user_input)

    print(users_new_list)

main()