from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import pygame


# URL of the webpage you want to monitor
url = "http://aadl3inscription2024.dz/"
sound_file = "./notification-6175.mp3"

# Function to create a WebDriver instance
def create_driver():
    return webdriver.Chrome()  # You can use any webdriver here

# Function to check if the webpage is accessible
def is_page_accessible(driver, url):
    try:
        driver.get(url)
        return True
    except WebDriverException:
        return False
    
def play_mp3(mp3_file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()

# Function to refresh the webpage until it's accessible
def refresh_until_accessible(driver, url):
    while not is_page_accessible(driver, url):
        print("Page is not accessible. Refreshing...")
        time.sleep(10)  # Adjust the refresh interval as needed
    print("Page is now accessible!")
    play_mp3(sound_file)

# Create a WebDriver instance
driver = create_driver()

# Start monitoring
refresh_until_accessible(driver, url)

# Note: Do not close the driver here if you want to keep the browser open.
# driver.quit()  # Commented out to keep the browser open
