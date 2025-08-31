# Bank UI Tests — Strong + Allure

Добавлено:
- Allure-отчёт (`allure-pytest`). Результаты складываются в `reports/allure`.
- Автоприложения к отчёту: скриншоты и HTML страницы при падении.
- Параллельный запуск, артефакты CI (скриншоты/HTML/Allure results).

## Локальный запуск с Allure
```bash
python3 -m pip install -r requirements.txt
export BASE_URL=https://mb1.bbr.ru
export UI_USER=e.volkova
export UI_PASS=1qaz!QAZ
export AFTER_LOGIN_ASSERT_CSS='[id$=":mainMenu"]'

# Запуск тестов с генерацией allure-results
python3 -m pytest -m e2e -n 2 --alluredir=reports/allure -q

# Просмотр отчёта локально (если установлен Allure CLI):
# brew install allure
allure serve reports/allure
```

## GitHub Actions
В workflow результаты кладутся в `reports/allure` и загружаются как artifact `allure-results`.
Можно подключить генерацию статичного HTML через сторонний action позже.
