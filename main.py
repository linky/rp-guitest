import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
ADDRESS = 'http://192.168.1.22'
if len(sys.argv) == 3:
    ADDRESS = sys.argv[1]
    if sys.argv[2] == 'firefox':
        browser = webdriver.Firefox()

# loading time limit
browser.implicitly_wait(10)

def loadingTime(_url):
    browser.get(_url)
    # check document.ready state
    page_state = browser.execute_script('return document.readyState;')
    return page_state == 'complete'

def skipDialog():
    # click on background image
    mt = browser.find_element_by_id('main_content')
    mt.click()

def getItems(_groups):
    # traverse all groups all application in the groups
    for group in _groups:
        apps = browser.find_elements_by_class_name('app-item')
        for app in apps:
            text = app.find_element_by_class_name('app-name').text
            # open group
            if text == group:
                app.click()
                # get all apps in the current group
                group_apps = browser.find_elements_by_class_name('app-item')
                for group_app in reversed(group_apps):
                    text = group_app.find_element_by_class_name('app-name').text
                    # return Back
                    if text == 'Back':
                        group_app.click()
                    else:
                        print("\t" + text)
                break
            # print item name
            elif group == None:
                print(text)

def getVersion():
    footer = browser.find_element_by_id('footer')
    version = footer.find_element_by_tag_name('a').text
    print(version)

def runApps(_apps):
    for app in _apps:
        items = browser.find_elements_by_class_name('app-item')
        for item in items:
            text = item.find_element_by_class_name('app-name').text
            # run Application
            if text == app:
                print('running ' + text + '...')
                item.click()
                browser.get(ADDRESS)
                break

lt = loadingTime(ADDRESS)
print(lt)

#skipDialog()

getItems([None, 'System', 'Development'])

getVersion()

runApps(['Oscilloscope & Signal Generator', 'DFT Spectrum Analyser', 'LCR meter', 'Logic analyser', 'Bode Analyser'])

browser.close()