import base64
import time
print('++++++++++++++++++++++++++++++++++++++++++')
print('++              L3xtech code            ++ \n++   Encode and Decode base64 by Cipher ++\n++++++++++++++++++++++++++++++++++++++++++')
string= input(str('\nType your string: '))
string_bytes = string.encode("ascii")
  
base64_bytes = base64.b64encode(string_bytes)
base64_string = base64_bytes.decode("ascii")
time.sleep(1)
print ('.\nencoding...\n.')
time.sleep(3)
print(f"Your string is successfully encoded: {base64_string}")
