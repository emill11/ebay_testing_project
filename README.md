# Проект по тестированию сайта и мобильного приложения eBay.

![Шапка сайта](assets/ebay.jpg)

[eBay](https://www.ebay.com/)

## Проект реализован с использованием:

<div style="display: flex; flex-wrap: wrap;">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="40" height="40" alt="Python" title="Python">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" width="40" height="40" alt="Pytest" title="Pytest">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" width="40" height="40" alt="Pycharm" title="Pycharm">
  <img src="assets/selene.png" width="40" height="40" alt="Selene" title="Selene">
  <img src="assets/selenium.png" width="40" height="40" alt="Selenium" title="Selenium">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/androidstudio/androidstudio-original.svg" width="40" height="40" alt="Android Studio" title="Android Studio">
  <img src="assets/appium.png" width="40" height="40" alt="Appium" title="Appium">
  <img src="assets/selenoid.png" width="40" height="40" alt="Selenoid" title="Selenoid">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" width="40" height="40" alt="Jenkins" title="Jenkins">
  <img src="assets/allure_report.png" width="40" height="40" alt="Allure report" title="Allure report">
  <img src="assets/tg.png" width="40" height="40" alt="Telegram" title="Telegram">
</div>

## Web UI

### Список проверок:

✔️ добавление продукта в корзину  
✔️ поиск продукта через главное поле ввода  
✔️ поиск продукта через расширенный поиск  
✔️ поиск продукта через навигационную панель  
✔️ поиск продукта через категории  
✔️ отображение недавно просмотренного продукта

#### Jenkins используется для запуска автотестов, которые выполняются в Selenoid.

[Проект в Jenkins](https://jenkins.autotests.cloud/job/ebay_project/)

#### Allure report:

<img src="assets/allure_web.jpg" alt="Allure отчет" onclick="openFullscreen(this)" style="width: 100%; height: auto; transform: scale(0.8);">
<img src="assets/selenoid.gif" alt="Allure отчет" onclick="openFullscreen(this)" style="width: 100%; height: auto; transform: scale(0.8);">

#### Оповещение о результатах прохождения тестов в Telegram:

<div style="text-align: center;">
  <img src="assets/report_tg.jpg" alt="Telegram отчет" style="width: 240px; height: 195px;">
</div>

#### Для локального запуска тестов необходимо выполнить команду в терминале:

```
pytest --context=local
```

## Mobile

### Список проверок:

✔️ добавление продукта в корзину  
✔️ добавление продукта в список отслеживаемых  
✔️ отображение недавно просмотренного продукта  
✔️ поиск продукта через категории  

#### Автотесты выполняются в эмуляторе Android либо на реальном устройстве.

#### Allure report  

<img src="assets/allure_app.jpg" alt="Allure отчет" onclick="openFullscreen(this)" style="width: 100%; height: auto; transform: scale(0.8);">
