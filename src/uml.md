# UML-диаграммы в PlantUML

## Установка PlantUML

1. Установите [Java](https://www.java.com/en/download/).
2. Установите [Graphviz](https://plantuml.com/ru/graphviz-dot).
3. Создайте переменную среды `GRAPHVIZ_DOT` и укажите в ее значении путь до файла dot.exe. Например, C:\Program Files (x86)\Graphviz2.38\bin\dot.exe.
4. Скачайте файл [plantuml.jar](http://sourceforge.net/projects/plantuml/files/plantuml.jar/download).
5. Установите препроцессор для Foliant: `pip install foliantcontrib.plantuml`
6. В файле foliant.yml  добавьте `plantuml` в раздел препроцессоров.
7. Добавьте параметр `plantuml_path` и укажите путь к файлу plantuml.jar. Например, D:\plantuml\plantuml.jar.

Подробнее об использовании PlantUML в Foliant см. статью [Plantuml](https://foliant-docs.github.io/docs/preprocessors/plantuml/#usage).

## Примеры диаграмм

### Диаграмма последовательности

<plantuml>
    @startuml
    actor Foo1
    boundary Foo2
    control Foo3
    entity Foo4
    database Foo5
    collections Foo6
    Foo1 -> Foo2 : To boundary
    Foo2 -> Foo3 : To control
    Foo1 -> Foo4 : To entity
    Foo1 -> Foo5 : To database
    Foo5 <- Foo6 : To collections
    @enduml
</plantuml>
