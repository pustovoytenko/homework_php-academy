from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time
import csv
# import os
# foxdriver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "geckodriver")
# print(foxdriver)
# os.environ["webdriver.gecko.driver"] = foxdriver


# function which find questions on page and parsing:
# title, time, subscribes and answered or no (http://toster.ru).
# def questions_toster():
#     questions = driver.find_elements_by_class_name("question_short")
#     for question in questions:
#         title = question.find_element_by_class_name("question__title-link").text
#         subscribers = question.find_element_by_class_name("question__views-count").text.split()[0]
#         published = question.find_element_by_tag_name("time").get_attribute("datetime")
#
#         try:
#             question.find_element_by_class_name("icon_check")
#             is_answered = True
#         except NoSuchElementException:
#             is_answered = False
#
#         print("{}|{}|{}{}|{}{}".format(title, published, "subs:", subscribers, "is answered:", is_answered))
#     return
#
driver = webdriver.Firefox()
# # driver.implicitly_wait(1)
#
driver.get("http://toster.ru")
#
# # input words in search string
# search_input = driver.find_element_by_name("q")
# search_input.send_keys("selenium python" + Keys.RETURN)
# time.sleep(1)
#
# # find number of pages
# pages = driver.find_elements_by_class_name("paginator__item-link")
# num_of_pages = len(pages)
#
# for page in range(1, num_of_pages):
#
#     questions_toster()
#
#     try:
#         driver.find_element_by_class_name("next").click()
#     except NoSuchElementException:
#         print("Last page")
#     time.sleep(1)
#
#
# # mobile version
driver.set_window_size(414, 736)

driver.find_element_by_xpath("//button[@role='btn_suggest']").click()
search_mob_input = driver.find_element_by_name("q")
search_mob_input.send_keys("python webdriver" + Keys.RETURN)
time.sleep(1)

# save base url for parsing
base_url = driver.current_url
# print(base_url)

# # first page
# questions_mob = driver.find_elements_by_class_name("question__title-link")
# list_questions_mob = []
#
# # get links from first page
# for question_mob in questions_mob:
#     link = question_mob.get_attribute("href")
#     list_questions_mob.append(link)
#
# # parsing questions by links
# for link_page in list_questions_mob:
#     driver.get(link_page)
#     # time.sleep(1)
#
#     views = driver.find_element_by_class_name("question__views-count").text.split()[0]
#     tags = driver.find_element_by_class_name("tags-list").text
#     body = driver.find_element_by_class_name("question__text").text
#
#     # print(views, "\n", tags.split(), "\n", body)
#     break
#     time.sleep(1)

# next pages
# move to 1st page with search result
driver.get(base_url)

# find number of pages
pages_mob = driver.find_elements_by_class_name("paginator__item-link")
nums = len(pages_mob)

# parsing pages
with open('toster.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["title", "subs", "create date", "is answered"])
    writer.writeheader()
    for num in range(1, nums):
        try:
            driver.find_element_by_class_name("next").click()
            time.sleep(1)

            questions = driver.find_elements_by_class_name("question_short")
            for question in questions:
                title = question.find_element_by_class_name("question__title-link").text
                subscribers = question.find_element_by_class_name("question__views-count").text.split()[0]
                published = question.find_element_by_tag_name("time").get_attribute("datetime")
                title_mod = "{}{}{}".format("\'", title, "\'")
                # print(title)
                try:
                    question.find_element_by_class_name("icon_check")
                    is_answered = True
                except NoSuchElementException:
                    is_answered = False
                writer.writerow({"title": title_mod,
                                "subs": subscribers,
                                "create date": published,
                                "is answered": is_answered})
                # break
        except NoSuchElementException:
            print("Last page")

    time.sleep(1)


driver.quit()
