# Тестирование сниппетов

1. Добавить информацию из файла целиком. Например, git.md.
2. Добавить кусочек текста между заголовками.
3. Добавить отдельный абзац.

## Файл целиком

<include repo_url="https://github.com/fish-train/flnt-test/src/git.md" src="!path .\src\git.md" sethead="3"></include>

## Текст между заголовками

<include repo_url="https://github.com/fish-train/flnt-test/src/start.md" src="!path .\src\start.md" from_heading="Создание проекта Foliant" to_heading="Создание репозитория" sethead="3"></include>

## Абзац

<include repo_url="https://github.com/fish-train/flnt-test/src/docs.md" src="!path .\src\docs.md" from_id="editor_id1" to_id="editor_id2" sethead="3"></include>