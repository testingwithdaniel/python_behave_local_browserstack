import json
import os

from selenium import webdriver

# chrome_driver_exe = "/Users/mukeshtiwari/Documents/sel_setup/chromedriver"

CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'config/local.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)


BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['user']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['key']

def before_scenario(context,scenario):

     if CONFIG_FILE == "config/local.json":
          context.browser = webdriver.Chrome(CONFIG['environments'][0]['chrome_driver_exe'])
          context.browser.maximize_window()
     elif CONFIG_FILE == "config/browserstack.json":
          desired_capabilities = CONFIG['environments'][TASK_ID]
          for key in CONFIG["capabilities"]:
               if key not in desired_capabilities:
                    desired_capabilities[key] = CONFIG["capabilities"][key]

          context.browser = webdriver.Remote(
               desired_capabilities=desired_capabilities,
               command_executor="http://%s:%s@hub-use.browserstack.com/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
          )

def after_scenario(context,scenario):
     context.browser.quit()
