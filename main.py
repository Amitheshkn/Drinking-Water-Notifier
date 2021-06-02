import time
from plyer import notification 

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "A general rule of thumb for healthy people is to drink two to three cups of water per hour",
            app_icon = r"C:\drinkingwater.ico",  #add the path where the drining water icon is located
            timeout = 5   #time in seconds for the notifier to be seen
        )
        time.sleep(60*60) #time in seconds for the notifier to repeat(1 hour)
