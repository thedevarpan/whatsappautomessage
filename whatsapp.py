import pyautogui as pg
import time

#select number of message
print("How many message you want to send: ")
number_of_message=int(input())

#enter the message
print("Write down your message: ")
your_text=input()

time.sleep(5)
for i in range(number_of_message):
               pg.write(your_text)
               pg.press("enter")
