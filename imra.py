from seleniumbase import SB

with SB(uc=True, test=True) as imran:
    if True:
    url = "https://kick.com/brutalles"
    imran.uc_open_with_reconnect(url, 5)
    imran.uc_gui_click_captcha()
    imran.sleep(1)
    imran.uc_gui_handle_captcha()
    imran.sleep(1)
    if imran.is_element_present('button:contains("Accept")'):
        imran.uc_click('button:contains("Accept")', reconnect_time=4)
    if imran.is_element_visible('#injected-channel-player'):
        while imran.is_element_visible('#injected-channel-player'):
            imran.sleep(10)
