import os
import subprocess

while True:
    user_input = input("prompt> ")
    commands = user_input.split(';')

    for command in commands:
        command = command.strip()

        if command == "exit":
            print("終了します。")
            exit()

        if "|" in command: 
            commands_list = command.split('|')
            output = None

            for cmd in commands_list:
                cmd = cmd.strip()
                process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                output, _ = process.communicate(input=output)
            
            print(output)

        else:
            try:
                result = subprocess.check_output(command, shell=True, text=True)
                print(result)
            except subprocess.CalledProcessError as e:
                print("エラー:", e)
