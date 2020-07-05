from selenium import webdriver
from selenium.webdriver.support.select import Select
import constants as con #TODO: move const file to config directory
import logging
import logging.config


##################################
#  Logging configuration         #
##################################
logging.config.fileConfig('conf/log.conf')
# create logger using the module name
logger = logging.getLogger(__file__)


##################################
#  Driver configuration          #
##################################
driver = webdriver.Chrome(executable_path=con.CHROME_DRIVER)
driver.get(con.URL)
currentURL = driver.current_url
print(f' current url: {currentURL}  \n')

##################################
#  CSS selectors                 #
##################################
# User identification field selector
userIdSelector = 'input[id="username"]'
# Password field selector
passwordSelector = 'input[id="pwd"]'
# Send button selector
sendButtonSelector = 'button[id="sendClocking"]'
# Final message selector
resultMessageSelector = '#purr-container > div > div.notice-body > h3'
# Detail message selector
detailMessageSelector = '#purr-container > div > div.notice-body > p'
# Recents clockings
recentClockings1 = '#recentClockings > tr:nth-child(1) > td:nth-child(1) > p'
recentClockings2 = '#recentClockings > tr:nth-child(2) > td:nth-child(1) > p'
recentClockings3 = '#recentClockings > tr:nth-child(3) > td:nth-child(1) > p'
recentClockings4 = '#recentClockings > tr:nth-child(4) > td:nth-child(1) > p'



if __name__ == '__main__':


    if currentURL == con.URL:

        try:
            logger.info("... Starting clock-in process")

            # Set the user ID
            driver.find_element_by_css_selector(userIdSelector).send_keys(con.USER_ID)
            
            # Set the user password
            driver.find_element_by_css_selector(passwordSelector).send_keys(con.PASS)

            # Send fulfilled form
            driver.find_element_by_css_selector(sendButtonSelector).click()

            # Get the result message
            # TODO: implement capture success message in order tu validate process is done

            # Get the last recent clockings
            currentClocking = driver.find_element_by_css_selector(recentClockings1).text
            clocking2 = driver.find_element_by_css_selector(recentClockings2).text
            clocking3 = driver.find_element_by_css_selector(recentClockings3).text
            clocking4 = driver.find_element_by_css_selector(recentClockings4).text

        except: #TODO: capture the specific error selenium selector related
            logger.error(" ** ERROR: Something is wrong!  :(   \n")
            raise
        else: 
            logger.info("... Process finished without script errors   :)")
            logger.info(f"Current clocking: {currentClocking}")
            logger.info(f"Previus clocking: {clocking2}")
            logger.info(f"Previus clocking: {clocking3}")
            logger.info(f"Previus clocking: {clocking4}")
        finally:
            driver.close()
            print('Fin')
