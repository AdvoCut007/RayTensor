[![RayTests](https://github.com/AdvoCut007/RayTensor/actions/workflows/raytests.yml/badge.svg)](https://github.com/AdvoCut007/RayTensor/actions/workflows/raytests.yml)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![version](https://img.shields.io/badge/version-2.8.9-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=RayTensor+v+2.8.9)](https://git.io/typing-svg)

# Что это?

## RayTensor - веб-приложение для выявления и диагностики респираторных заболеваний любой стадии путём анализа КТ и/или рентгена.

# Как это работает?

## Tensorflow в связке с Keras составляют основу приложения - нейронную сеть, определяющую 3 диагноза у рентген-снимков:
<ul>
<li><h3>1. Пневмония.</h3></li>
<li><h3>2. Covid-19 (SARS-CoV-2)</h3></li>
<li><h3>3. Очаговый туберкулёз лёгких</h3></li>
</ul>

## 2 диагноза для КТ-снимков:
<ul>
<li><h3>1. Пневмония.</h3></li>
<li><h3>2. Covid-19 (SARS-CoV-2)</h3></li>
</ul>

# Использование Tensorflow и keras для создания нейронной сети:

### Импорт библиотек и инициализация проекта:

<p align="center">
<img src="static/images/readme/tensorinit.png">
</p>

### Создание тренировочного и валидационного датасета:

<p align="center">
<img src="static/images/readme/tensordf.png">
</p>

### Точность определения диагноза составляет более 90%!

<p align="center">
<img src="static/images/readme/accuracy.png">
</p>


### Вершину айсберга составляет веб-сервер, написанный на микрофреймворке Flask.

<p align="center">
<img src="static/images/readme/flask.png">
</p>

## Frontend основан на стандартном HTML5 с привязкой к стилям Bootstrap, а также на встроенном в Flask шаблонизаторе Jinja, обеспечивающий высокую читаемость кода за счёт сокращения его количества.

<p align="center">
<img src="static/images/readme/jinja.png">
</p>

# Использование

## Установка:

```shell
git clone https://github.com/AdvoCut007/RayTensor
cd RayTensor
pip install --upgrade pip
pip install -r requirements.txt
```

## Запуск:

```shell
python3 app.py
```

## При развёртывании сервера нас встречает минималистичная главная страница с основными гиперссылками. Кроме того, header может обеспечить Вам быстрое перемещение по сайту.

<p align="center">
<img src="static/images/readme/index.png">
</p>

## В зависимости от выбранного варианта, откроется шаблонизированная форма загрузки образца на сайт:

<p align="center">
<img src="static/images/readme/flaskform.png">
</p>

## После выбора файла форма передаст файл модели для дальнейшей предобработки и анализа:

<p align="center">
<img src="static/images/readme/preprocess.png">
</p>

## Долгожданный результат! На выходе сайт возвращает выгруженное Вами изображение, а также показывает поставленный диагноз и его вероятность.

<p align="center">
<img src="static/images/readme/result.png">
</p>

# Для всех вопросов:
### [Telegram](https://t.me/RightMonarch)
