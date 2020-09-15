# JB2020AudioAnomaiy
Тестовое задание для проекта "Автоматический поиск аномалий на аудиозаписях"

Аудио, над которыми планируется производить манипуляции нужно добавить в папку ```samples```

Для запуска следует собрать docker образ и запустить его в интерактивном режиме (с ключами -t -i)

```
Usage:
    <command> [params]

Commands:
    exit
    reverse [input file] [output file]
    crop [input file] [list of intervals in seconds]
    concat [input files list] [output file]
```
