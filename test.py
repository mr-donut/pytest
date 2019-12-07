from selenium import webdriver
import time
import math
try:
    link = [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"]
    for i in link:
        browser = webdriver.Chrome()
        browser.get(i)
        browser.implicitly_wait(10)
        a = math.log(int(time.time()))
        field = browser.find_element_by_css_selector(".textarea")
        field.send_keys(str(a))
        time.sleep(1)
        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()
        time.sleep(5)
        x_element = browser.find_element_by_css_selector("pre.smart-hints__hint").text
        assert "Correct!" in x_element, 'не совпадает ответ!'
        # if AssertionError == (True):
        if x_element != "Correct!":
            print(x_element)

finally:
    time.sleep(5)
    browser.quit()

# Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
# Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений.
# Ваша задача - реализовать автотест со следующим сценарием действий:

    # открыть страницу
    # ввести правильный ответ
    # нажать кнопку "Отправить"
    # дождаться фидбека о том, что ответ правильный
    # проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
#
# Опциональный фидбек — это текст в черном поле, как показано на скриншоте:
# Правильным ответом на задачу в заданных шагах является число

# import time
# import math
# answer = math.log(int(time.time()))
#
# Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:
#
# https://stepik.org/lesson/236895/step/1
# https://stepik.org/lesson/236896/step/1
# https://stepik.org/lesson/236897/step/1
# https://stepik.org/lesson/236898/step/1
# https://stepik.org/lesson/236899/step/1
# https://stepik.org/lesson/236903/step/1
# https://stepik.org/lesson/236904/step/1
# https://stepik.org/lesson/236905/step/1
#
# Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты работали стабильно.
#
# В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!"
# Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.
# Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное локальное время (https://time.is/ru/).
# Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают.