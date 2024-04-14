def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 67890\n")
    except PermissionError:
        print("Permission error occurred. Unable to create or write to the file.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("File creation process completed.")


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found. Unable to read the file.")
    except Exception as e:
        print("An unexpected error occurred:", e)


def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("This is line 4 (appended)\n")
            file.write("98765 (appended)\n")
            file.write("Yet another line appended: ABCDE\n")
    except PermissionError:
        print("Permission error occurred. Unable to append to the file.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("File appending process completed.")


if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
