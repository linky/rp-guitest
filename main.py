from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.implicitly_wait(10)

def loadingTime(_url):
    browser.get(_url)
    page_state = browser.execute_script('return document.readyState;')
    return page_state == 'complete'

def skipDialog():
    mt = browser.find_element_by_id('main_content')
    mt.click()

def getItems(_groups):
    for group in _groups:
        apps = browser.find_elements_by_class_name('app-item')
        for app in apps:
            text = app.find_element_by_class_name('app-name').text
            if text == group:
                app.click()
                group_apps = browser.find_elements_by_class_name('app-item')
                for group_app in reversed(group_apps):
                    text = group_app.find_element_by_class_name('app-name').text
                    if text == 'Back':
                        group_app.click()
                    else:
                        print("\t" + text)
                break
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
            if text == app:
                print('running ' + text + '...')
                item.click()
                browser.get('http://192.168.1.5')
                break

lt = loadingTime('http://192.168.1.5')
print(lt)

#skipDialog()

getItems([None, 'System', 'Development'])

getVersion()

runApps(['Oscilloscope & Signal Generator', 'DFT Spectrum Analyser', 'LCR meter', 'Logic analyser', 'Bode Analyser'])

browser.close()