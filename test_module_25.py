import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from settings import valid_email, valid_password, user_name

def test_show_my_pets(browser, go_to_my_pets):
   '''Проверка,  что мы попали на страницу "Мои питомцы"'''

   submit_button = WebDriverWait(pytest.driver, 10).until(
      EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link')))
   submit_button.click()

   assert browser.find_element(By.TAG_NAME, 'h2').text == user_name

def test_all_pets_are_present(browser, go_to_my_pets):
    """Проверка, что присутствуют все питомцы"""
    assert browser.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    submit_button = WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link')))
    submit_button.click()

    assert browser.find_element(By.TAG_NAME, 'h2').text == user_name

    info_pet = browser.find_element(By.CSS_SELECTOR, 'div.left:nth-child(1)').text.split('\n')[1]
    number_of_pets = int("".join(filter(str.isdigit, pet_info)))
    print(number_of_pets)

    assert len(browser.find_elements(By.CSS_SELECTOR, 'tbody tr')) == number_of_pets

def test_no_same_name(go_to_my_pets):
    '''Поверка, что на странице нет питомцев с одинаковыми данными'''
    # Сохраняем данные о питомце
    my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    # Неявные ожидания:
    pytest.driver.implicitly_wait(10)

    list_data_my_pets = []
    for i in range(len(data_my_pets)):
        list_data = data_my_pets[i].text.split("\n")
        list_data_my_pets.append(list_data[0])
    set_data_my_pets = set(list_data_my_pets)
    assert len(list_data_my_pets) == len(set_data_my_pets)

def test_there_is_a_name_age_and_gender(browser, go_to_my_pets):
   '''Поверка, что у всех питомцев есть имя, возраст и порода'''

   submit_button = WebDriverWait(browser, 10).until(
      EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link')))
   submit_button.click()

   # Сохраняем данные о питомцах
   pet_info = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Настраиваем ожидание:
   wait = WebDriverWait(pytest.driver, 5)

   for i in range(len(pet_data)):
       assert wait.until(EC.visibility_of(pet_data[i]))

   # Ищем в теле таблицы все имена питомцев и ожидаем увидеть их на странице:
   name_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
   for i in range(len(name_my_pets)):
      assert wait.until(EC.visibility_of(name_my_pets[i]))

   # Ищем в теле таблицы все породы питомцев и ожидаем увидеть их на странице:
   type_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
   for i in range(len(type_my_pets)):
      assert wait.until(EC.visibility_of(type_my_pets[i]))

   # Ищем в теле таблицы все данные возраста питомцев и ожидаем увидеть их на странице:
   age_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
   for i in range(len(age_my_pets)):
      assert wait.until(EC.visibility_of(age_my_pets[i]))
