# Обрезка ссылок с помощью Битли

### Описание

Этот проект взаимодействует с сайтом [bit.ly](bit.ly) для обрезания ссылок. Ваша ссылка отправляется на вход, а на
выходе получается сокращенная ссылка типа bit.ly/******.

Вы также можете отправить на вход уже сокращенную ссылку, тогда на выходе будет количество кликов по этой ссылке.

### Как установить

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для
установки зависимостей:

```
pip install -r requirement.txt
```

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

Также необходимо добавить переменную окружения ```BITLINK_TOKEN```

### Пример использования

Укоротить ссылку:

```console
$ python3 main.py https://google.com
Битлинк https://bit.ly/3Gmq4Px
```

Узнать количество переходов по короткой ссылке:

```console
python3 main.py https://bit.ly/3Gmq4Px
По вашей ссылке прошли 1 раз(а)
```

### Цель проекта

Код написан в образовательных целях на онлайн курсе для веб-разработчиков
[dvmn.org](https://dvmn.org/).