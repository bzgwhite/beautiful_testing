from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def mb(tar, tar_name, mb=False):
    options = Options()
    options.headless = True
    filename = 'screenshot_' + str(tar_name) + '.png'
    tar_dir = 'result/'

    if mb:
        options.add_argument('--window-size=412,732')
        options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 Mobile/14C92 Safari/602.1')
        filename = filename.replace('.png','_sp.png')

    print(filename)
    if os.path.exists(tar_dir + filename):
        filename = filename.replace('.png','_after.png')

    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=options.to_capabilities(),
        options=options
    )
    driver.get(tar)
    w = driver.execute_script('return document.body.scrollWidth')
    h = driver.execute_script('return document.body.scrollHeight')
    print(w,h)
    driver.set_window_size(w, h)

    driver.save_screenshot(tar_dir + filename)
    driver.close()