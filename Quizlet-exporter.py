from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import os


def make_folder(path):
    try:
        path = path.replace('\\', '/')
        folder_name = str(path) + "/words"
        os.mkdir(folder_name)
    except FileExistsError:
        pass
    except PermissionError:
        print('Permission denied - try running as an administrator')
        input('Press enter to exit...')
        sys.exit()
    except FileNotFoundError:
        print('Error: Make sure your directory is correct and you are specifying the full path.')
        input('Press enter to exit...')
        sys.exit()


def write_the_file(text, file_name, path):
    f = open(f"{path}/words/{file_name}.txt", "w", encoding='utf-8')
    f.write(text)
    f.close()


def login(driver, username, password):
    login_button = driver.find_element_by_xpath('/html/body/div[3]/div[1]/header/div[1]/div[2]/div[3]/button[1]')
    login_button.click()

    time.sleep(2)

    login_name = driver.find_element_by_id(str('username'))
    login_name.send_keys(username)

    login_pass = driver.find_element_by_id(str('password'))
    login_pass.send_keys(password)

    login_pass.send_keys(Keys.ENTER)


def if_exists(driver, path):
    try:
        driver.find_element_by_xpath(path)
        return True
    except NoSuchElementException:
        return False


def get_words(driver):
    # more button
    if if_exists(driver, '/html/body/div[7]/div/div[1]/div/button'):
        close_button = driver.find_element_by_xpath('/html/body/div[7]/div/div[1]/div/button')
        close_button.click()
    try:
        time.sleep(1)
        driver.get_screenshot_as_file('capture123.png')
        more = driver.find_element_by_xpath(
            '//*[@id="setPageSetDetails"]/div[1]/div/div/div/section/div/div[1]/div/div[4]/span/span/button')
        more.click()
    except NoSuchElementException:
        more = driver.find_element_by_xpath(
            '//*[@id="setPageSetDetails"]/div[1]/div/div/div/section/div/div[1]/div/div[3]/span/span/button')
        more.click()

    # export button
    try:
        export = driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div/span[4]/button')
        export.click()
    except NoSuchElementException:
        try:
            time.sleep(1)
            export = driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div/span[4]/button')
            export.click()
        except NoSuchElementException:
            export = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/span[4]/button')
            export.click()

    time.sleep(1)
    separator = driver.find_element_by_xpath('//*[@id="SetPageExportModal-wordDelimComma-radio"]')
    separator.click()

    txt = driver.find_element_by_xpath('//*[@id="SetPageExportModal-textarea"]').get_attribute('value') + '\n---,---\n'
    return txt


def save_to_file(text, file_name, path):
    f = open(f"{path}/words/{file_name}.txt", "a", encoding='utf-8')
    f.write(text)
    f.close()


def inside_list_def(name, unit_name):
    inside_list = [name]
    print(inside_list)
    if name == 'null':
        if name[1] == ' ':
            inside_list.append(int(name[0]))
        else:
            inside_list.append(int(name[0:2]))
    else:
        if name[len(unit_name) + 2] == ' ':
            inside_list.append(int(name[len(unit_name) + 1]))
        else:
            inside_list.append(int(name[len(unit_name) + 1:len(unit_name) + 3]))
    return inside_list


def get_list_of_unit_names(driver, unit_number, file_name, unit_name, path):
    parent_div_text = """//*[@id="DashboardPageTarget"]/div/section[2]/div/div[2]/div/div/div/div/div[2]/div/div"""
    parent_div_text2 = """//*[@id="DashboardPageTarget"]/div/section/div/div[2]/div/div/div/div/div[2]/div/div"""
    try:
        time.sleep(1)
        parent_div = driver.find_element_by_xpath(parent_div_text)
    except NoSuchElementException:
        parent_div = driver.find_element_by_xpath(parent_div_text2)
        parent_div_text = parent_div_text2

    count_of_divs = len(parent_div.find_elements_by_xpath("./div"))

    list_from_unit = []
    for i in range(0, count_of_divs - 1):

        name = driver.find_element_by_xpath(
            f"""{parent_div_text}/div[{i + 1}]/div/div/div[1]/div/div/div[1]/a/h4""").text

        inside_list = inside_list_def(name, unit_name)

        if inside_list[1] == unit_number:
            list_from_unit.append(inside_list[0])

            element_from_unit = driver.find_element_by_xpath(
                f"""{parent_div_text}/div[{i + 1}]/div/div/div[1]/div/div/div[1]/a""")
            element_from_unit.send_keys(Keys.ENTER)

            save_to_file(get_words(driver), file_name, path)

            driver.back()
            time.sleep(2)

    list_from_unit.sort()
    return list_from_unit


def file_to_list(separator, file_name, path):
    file = []
    f = open(f"{path}/words/{file_name}.txt", "r", encoding='utf-8')
    for line in f:
        stripped_line = line.strip()
        split = stripped_line.split(separator)
        word_en = split[0]
        word_pl = split[1]
        otherway = [word_pl, word_en]
        file.append(otherway)
    f.close()
    return file


def list_to_txt_separetor(lst, sep):
    txt = ""
    for x in range(0, len(lst) - 1):
        for y in range(0, len(lst[x])):
            if y == 0:
                txt += str(lst[x][y]) + sep
            elif y == 1:
                txt += str(lst[x][y])
        txt += "\n"
    return txt


def main():
    try:
        path = str(sys.argv[7])
        separetor = str(sys.argv[6])
        make_folder(path)
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

        driver = webdriver.Chrome(options=options)
        unit_number = int(sys.argv[5])  # <-- unit number
        unit_name = str(sys.argv[4])  # <-- the name after which is the number
        file_name = f"{unit_name}_{unit_number}_words"
        write_the_file('', file_name, path)
        driver.get(sys.argv[1])  # <-- Link

        time.sleep(2)

        login(driver, sys.argv[2], sys.argv[3])  # <-- username, password

        time.sleep(2)

        get_list_of_unit_names(driver, unit_number, file_name, unit_name,path)

        write_the_file(list_to_txt_separetor(file_to_list(',', file_name, path), separetor), file_name, path)
        print("lol it accually worked")
    finally:
        driver.quit()


if __name__ == '__main__':
    main()

