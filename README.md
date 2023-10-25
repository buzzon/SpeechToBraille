# SpeechToBraille
Данная библиотека предоставляет инструменты для: 
* Перевода заранее записанного аудиофайла формата .mp3 в текст на русском языке
* Перевода текста на русском языке в брайль

## Установка
`pip install SpeechToBraille`

## Дополнительные зависимости
`pip install huggingsound`

## Использование
#### speechToText

```python
from SpeechToBraille import speechToText

#Метод преобразует файл формата .mp3 с записью речи на русском языке в текст
#Пример пути: './test.mp3'
speechToText(path) 
>>> "Привет, мир!"
```

#### convertTextToBraille
```python
from SpeechToBraille import convertTextToBraille

#Метод преобразует текст на русском языке в брайль
converTextToBraille(text)
>>> ⠏⠗⠊⠺⠑⠞⠂ ⠍⠊⠗⠖ 
```
