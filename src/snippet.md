# Тестирование сниппетов

1. Добавить информацию из файла целиком. Например, git.md.
2. Добавить кусочек текста между заголовками.
3. Добавить отдельный абзац.

## Файл целиком

<include src="!path .\src\git.md" sethead="3"></include>

## Текст между заголовками

<include src="!path .\src\start.md" from_heading="Создание проекта Foliant" to_heading="Создание репозитория" sethead="3"></include>

## Абзац

<include src="!path .\src\docs.md" from_id="editor_id1" to_id="editor_id2" sethead="3"></include>