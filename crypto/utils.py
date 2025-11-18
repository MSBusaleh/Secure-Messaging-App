import base64

def display_message(encMsg):
    output = base64.b64encode(encMsg)
    output_str = output.decode('utf-8')
    return output_str
  
def parse_message(encMsg):
    # output_str = encMsg.encode('utf-8')
    # output = base64.b64encode(output_str)
    return base64.b64decode(encMsg.encode('utf-8'))