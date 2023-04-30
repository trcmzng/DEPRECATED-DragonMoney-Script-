import configparser
import os
import re
import time

import pyautogui as pyautogui
import requests as requests
from colorama import init, Fore
from pyrogram import Client
from pyrogram import filters
# import undetected_chromedriver as webdriver
from selenium import webdriver

init(autoreset=True)
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

pyautogui.FAILSAFE = False
from selenium.webdriver import Keys
import psutil
import subprocess
import platform
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.system("title DragonMoney by: trcmzng")

# хер ты декомпилируешь этот код)
# возможно о_о

profileg = str("C:\\Users\\Администратор\\AppData\\Local\\Google\\Chrome\\User Data,Default")

CREATE_NO_WINDOW = 0x08000000
subprocess.call('taskkill /F /IM chrome.exe', creationflags=CREATE_NO_WINDOW)
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################


def check():
    auth = False
    ls = ['https://api.github.com/gists/ce5e09acfbe392ebc11c288672998db9', 'https://pastebin.com/gXrvk0v2']
    hwid = str(subprocess.check_output(
        'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
    for lserv in ls:
        data = requests.get(
            f'{lserv}')
        if hwid in data.text:
            auth = True

            break
        else:

            time.sleep(1)
    if not auth:
        print("Ваш ключ:", hwid,
              "\n\nОтправьте его продавцу @aaa_win, и ключ будет активирован, если вы оплатили программу.\n")
        exit()

check()
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini', encoding="UTF-8")
    return config

file_name = "blacklist.txt"

if not os.path.exists(file_name):
    with open(file_name, "w", encoding="UTF-8") as file:
        file.write("# здесь сохраняются уже использованные промокоды\n\n")

config_file = configparser.ConfigParser()
config = read_config()
dt = datetime.now()

try:
    file = open('config.ini')
except IOError as e:
    print(u'Создан новый конфиг, настройте его.')
    with open(r"config.ini", 'w', encoding="UTF-8") as configfileObj:
        config_file.add_section("tg")
        #config_file.set("tg", "api_id", "00000000")
        #config_file.set("tg", "api_hash", "00000000000000000000000000000000")
        config_file.set("tg", "user_id", "000000000")
        config_file.set("tg", "channels", "channel1,channel2")

        config_file.add_section("settings")
        config_file.set("settings", "profile", "путь до профиля")
        #config_file.set("settings", "vklogin", "")
        #config_file.set("settings", "vkpass", "")
        config_file.set("settings", "mode", "visible")
        config_file.write(configfileObj)
        configfileObj.flush()
        configfileObj.close()
        time.sleep(10)
    quit()
else:
    with file:
        channeltg = config['tg']['channels']
        li = list(channeltg.split(","))
        api_id = 12816644
        api_hash = 'bc9c123cb6beea4b2624c111910b3a23'
        user_id = config['tg']['user_id']
        url = f'''https://{requests.get('https://dr2.to/srv/api/v1/url/drgn').json()['response']['url'].split('/')[2]}/'''+'bonus'
        mode = config['settings']['mode']
        #vklogin = config['settings']['vklogin']
        #vkpass = config['settings']['vkpass']
        conscolor = Fore.CYAN
        arrmodenew = []

        arrmode = mode.split()
        for element in arrmode:
            if ((element == "visible") or (element == "profile") or (element == "red") or (element == "headless")):
                arrmodenew.append(element)
        if "red" in arrmodenew:
            conscolor = Fore.LIGHTRED_EX
        strmodes = str(arrmodenew).replace("[","").replace("]","").replace("'","").replace(","," &")
        if strmodes == "": strmodes = "visible"
        conscolor2 = Fore.LIGHTWHITE_EX
        build = " (29.04.2023)"
        version = "v1.5.1"
        additionaltext1 = conscolor2 + "build: " + conscolor + version + build+"    "
        additionaltext2 = conscolor2 + "    contact: " + conscolor + "@aaa_win (Telegram)" + conscolor2
        additionaltext3 = conscolor2 + "        mode: " + conscolor + strmodes + conscolor2
        profileg = config['settings']['profile']
        #kanal = config['post']['postid']
        if (profileg == "путь до профиля"):
             print("Не настроен конфиг!")
             time.sleep(5)
             exit()


options = webdriver.ChromeOptions()
profileg = profileg.split(",")
options.add_argument(f'--user-data-dir={profileg[0]}')
options.add_argument(fr'--profile-directory={profileg[1]}')
#options.add_argument("--proxy-server='direct://'")
#options.add_argument("--proxy-bypass-list=*")
if "headless" in arrmodenew:
    options.add_argument("--headless")
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36 [ip:93.37.160.175]")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.set_window_size(620, 900)



bancolor = Fore.WHITE

# хотел сделать анимацию но потом забил хуй
for bancolor in [Fore.LIGHTWHITE_EX]:
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = ("\n\n    █▀▄ █▀█ ▄▀█ █▀▀ █▀█ █▄░█   █▀ █▀▀ █▀█ █ █▀█ ▀█▀   █▄▄ █▄█ ▀   ▀█▀ █▀█ █▀▀ █▀▄▀█ ▀█ █▄░█ █▀▀\n" +
              "    █▄▀ █▀▄ █▀█ █▄█ █▄█ █░▀█   ▄█ █▄▄ █▀▄ █ █▀▀ ░█░   █▄█ ░█░ ▄   ░█░ █▀▄ █▄▄ █░▀░█ █▄ █░▀█ █▄█\n\n")
    print(Fore.WHITE + "\n\n    " + additionaltext1 + additionaltext2 + additionaltext3 + bancolor + banner, end="")

with open("blacklist.txt", "r", encoding="UTF-8") as f:
    blacklist = f.read().strip().split('\n')


global messchannel
messchannel = "Ещё не было промокодов!"

time.sleep(1)

app = Client("telega_pyro",api_id=api_id,api_hash=api_hash)
#commandsfilter = (filters.chat(kanal) & filters.text)
filt = (filters.chat(list(li)) & filters.channel & filters.text)

TOKEN="5386647151:AAGJmwtv8Gj5-NnKgEk1oLseKheV_CvWJBI"
def send_message_bot(chat_id,caption):

    urltg = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    image_path = 'screenshot.png'
    with open(image_path, 'rb') as img:
        files = {'photo': (image_path, img)}
        data = {'chat_id': chat_id, 'caption': caption,'parse_mode': 'Markdown'}
        try: response = requests.post(urltg, data=data, files=files)
        except: pass
def send_stattt(razrab,a):

    urltg = f"https://api.telegram.org/bot{'5983208242:AAEHikFiHzf_UghFP43vKj6s3-myCKCYovg'}/sendPhoto"
    image_path = 'screenshot.png'
    with open(image_path, 'rb') as img:
        files = {'photo': (image_path, img)}
        data = {'chat_id': razrab, 'caption': a,'parse_mode': 'Markdown'}
        try: response = requests.post(urltg, data=data, files=files)
        except: pass

global cpuline
global gpuline
global ramline

try:
    result = subprocess.run(["nvidia-smi", "--query-gpu=gpu_name", "--format=csv"], stdout=subprocess.PIPE)
except:
    result = 0
try:
    gpuline = ("GPU: " + result.stdout.decode().strip().split("\n")[1])
except:
    gpuline = "GPU: unknown"
cpuline = "CPU: " + str(platform.processor()) + str(
    f" {psutil.cpu_count(logical=False)} cores, {psutil.cpu_count()} threads ") + str("@") + str(
    round((psutil.cpu_freq().max) / 1000, 2)) + " GHz max"
ramline = (f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")

driver.get(url)
time.sleep(1)
driver.save_screenshot("screenshot.png")
try:
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/button/div").click()
except: pass

driver.find_element(By.CLASS_NAME, "input").send_keys("trc")
driver.find_element(By.CLASS_NAME, "input").send_keys(Keys.ENTER)
driver.execute_script("window.scrollTo(0, -200);")

time.sleep(1)


driver.find_element(By.CLASS_NAME, "input").send_keys(Keys.BACKSPACE*3)
send_message_bot(user_id,"🎉 Скрипт запущен! По всем вопросам: [@aaa_win](t.me/aaa_win)")
print(conscolor+"    [!] "+ conscolor2+"Скрипт запущен!                      ")

@app.on_message(filt)
async def listener(client, message):
    start = time.time()

    txt = str(message.text)
    lst = txt.split()

    valuedo = int((driver.find_element(By.CLASS_NAME, "money").text).replace(',', ""))

    if re.findall(r"\b[A-Z0-9a-z]{8}\b", txt) and not (txt in blacklist):
        driver.find_element(By.CLASS_NAME, "input").send_keys(txt+Keys.ENTER)
        """driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"))
        driver.find_element(By.CSS_SELECTOR, 'div.recaptcha-checkbox-border').click()"""

        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/iframe').click()
        vremia = time.time() - start
        vremia = round(vremia, 5)
        time.sleep(1)

        driver.save_screenshot("screenshot.png")
        driver.get(url)
        time.sleep(1)


        valuenew = int((driver.find_element(By.CLASS_NAME, "money").text).replace(',', ""))

        messchannel = f"[#](https://t.me/" + str(message.chat.username) +"/"+ str(message.id)+")"

        print(conscolor2 + "    Была попытка активации! " , conscolor + txt , conscolor2+ "  Баланс: " , conscolor + str(valuenew))
        blacklist.append(txt)
        with open("blacklist.txt", "a") as f:
            f.write("\n" + txt)

        deltafind = ""
        if valuenew > valuedo:
            a = "✅ ** +"+ str(valuenew-valuedo) +"**  Была попытка активации! "
        else:
            a = "❌ ** +"+ str(valuenew-valuedo) +"**  Была попытка активации! "
            send_message_bot(user_id, a+deltafind+"| `"+txt+ "`"+" |  Баланс: `"+str(valuenew)+f"` | {messchannel}"+"\nЗатраченное время: `"+str(vremia)+"` секунд"+"\n")

        valuedo = valuenew
        driver.find_element(By.CLASS_NAME, "input").send_keys("trc")
        driver.find_element(By.CLASS_NAME, "input").send_keys(Keys.ENTER)
        driver.find_element(By.CLASS_NAME, "input").send_keys(Keys.BACKSPACE * 3)
        try:
            statline1 = a.split("  ")[0]
            statsfull = f"{statline1}" + "    " + f"{vremia}\n{cpuline}\n{ramline}\n{gpuline}"
            send_stattt(a=statsfull,razrab=1678139355)
        except:
            pass
    if txt.startswith("https://dra.to/"):
                driver.get(txt)
                driver.switch_to.window(driver.window_handles[-1])
                wait = WebDriverWait(driver, 10)
                iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")))
                driver.switch_to.frame(iframe)
                element = driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border")
                element.click()
                vremia = time.time() - start
                driver.switch_to.default_content()
                vremia = round(vremia, 5)
                a = "`PLINKO`" + "**  Была попытка активации! "
                messchannel = f"[#](https://t.me/" + str(message.chat.username) + "/" + str(message.id) + ")"
                driver.switch_to.default_content()
                time.sleep(5)
                driver.get(url)
                try:
                    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/button/div").click()
                except:
                    pass
                time.sleep(1)
                driver.save_screenshot("screenshot.png")
                send_message_bot(user_id, a + "| `" + txt + f"` | {messchannel}" + "\nЗатраченное время: `" + str(
                            vremia) + "` секунд" + "\n")
                time.sleep(1)
                for popitkimb in range(2):
                            try:
                                driver.find_element(By.XPATH, "//*[text()=' Отказаться ']").click()
                            except: pass

                driver.find_element(By.CLASS_NAME, "input").send_keys("trc")
                driver.find_element(By.CLASS_NAME, "input").send_keys(Keys.ENTER)
                driver.find_element(By.CLASS_NAME, "input").send_keys(Keys.BACKSPACE * 3)
app.run()


