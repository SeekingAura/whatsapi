import pywhatkit
from pywhatkit.whats import sendwhatmsg_instantly
from pywhatkit.misc import web_screenshot

# pywhatkit.start_server(port=8001)

# x = pywhatkit.open_web()

web_screenshot("https://web.whatsapp.com")
x = sendwhatmsg_instantly(
    phone_no="+351923032090",
    message="yolandro",
    wait_time=15,
    tab_close=True,
    close_time=4,
)
print(x)
