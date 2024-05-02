###################
# I SUCK AT CODING #
#   JAVI C.        #
###################
import socket
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

# Initialize the OLED display
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
disp.begin()
disp.clear()
disp.display()

# Load font
font = ImageFont.load_default()

# Function to get IP address
def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 53))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except:
        return "No IP Address..."

# Get the IP address
ip_address = get_ip_address()

# Create an image
image = Image.new('1', (disp.width, disp.height))
draw = ImageDraw.Draw(image)

# Select the font
font = ImageFont.load_default()

# Draw IP address on the image using the selected font
draw.text((0, 0), "IP address: ", font=font, fill=255)
draw.text((0, 20), ip_address, font=font, fill=255)

# Display image
disp.image(image)
disp.display()


