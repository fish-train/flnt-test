# UML-диаграммы в PlantUML

## Установка PlantUML

1. Установите [Java](https://www.java.com/en/download/).
2. Установите [Graphviz](https://plantuml.com/ru/graphviz-dot).
3. Создайте переменную среды `GRAPHVIZ_DOT` и укажите в ее значении путь до файла dot.exe. Например, C:\Program Files (x86)\Graphviz2.38\bin\dot.exe.
4. Скачайте файл [plantuml.jar](http://sourceforge.net/projects/plantuml/files/plantuml.jar/download).
5. В корне проекта создайте файл plantuml.cfg и добавьте настройки отображения диаграмм. Подробнее см. в статье [Skinparam command](https://plantuml.com/ru/skinparam).
6. Установите препроцессор для Foliant: `pip install foliantcontrib.plantuml`
7. В файле foliant.yml  добавьте `plantuml` в раздел препроцессоров.
8. Добавьте параметр `plantuml_path` и укажите путь к файлу plantuml.jar. Например, D:\plantuml\plantuml.jar.
9. Добавьте параметры `params` и `config`.
10. В параметре `config` укажите путь до  файла plantuml.cfg: !path plantuml.cfg.

Подробнее об использовании PlantUML в Foliant см. статью [Plantuml](https://foliant-docs.github.io/docs/preprocessors/plantuml/#usage).

Настройки отображения диаграмм см. в 

## Примеры диаграмм

### Диаграмма последовательности

<plantuml>
    @startuml
    Alice -> Bob : Hi
    Alice -> Bob : This is very long
    @enduml
</plantuml>

### Диграмма активностей

<plantuml>
    @startuml Удаление лог-файлов
    start
    :Получить список файлов в папке;
    repeat
      :Получить полный путь к файлу;
      if (Это действительно файл?) then (Да)
        if (Имя файла заканчивается на 'log') then (Да)
          :Удалить файл;
          if (Путь к файлу сущетсвует?) then (Нет)
            :Показать сообщение <b>"Файл <Имя файла> удален"</b>;
          endif
        endif
      endif
    repeat while (Есть еще файлы в папке?)
    stop
    @enduml
</plantuml>