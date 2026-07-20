import os


def move_file(command: str) -> None:
    parts_of_command = command.split()
    if len(parts_of_command) == 3:
        existing_file_name = parts_of_command[1]
        new_file_path = parts_of_command[2]

        if os.path.exists(existing_file_name):
            if "/" in new_file_path:
                parts_of_directory = new_file_path.split("/")[:-1]

                for i in range(len(parts_of_directory)):
                    dir_path = "/".join(parts_of_directory[:i + 1])
                    if not os.path.exists(dir_path):
                        os.mkdir(dir_path)

            with (open(new_file_path, "w") as file_copy,
                  open(existing_file_name, "r") as existing_file):
                file_copy.write(existing_file.read())

            os.remove(existing_file_name)
