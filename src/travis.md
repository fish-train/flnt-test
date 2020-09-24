# Интеграция с Travis CI

Travis CI позволяет развернуть сайт при изменении кода в репозитории.

Чтобы включить интеграцию с Travis CI:

1. Откройте настройки профиля GitHub.
2. Откройте страницу Applications.
3. Добавьте приложение Travis CI по инструкции [Reviewing your authorized integrations](https://docs.github.com/en/github/authenticating-to-github/reviewing-your-authorized-integrations).
4. Залогиньтесь на сайте [](https://travis-ci.org/).
5. Активируйте репозиторий.
6. Добавьте файл  .travis.yml в репозиторий:
  
    ```
    sudo: required
    services:
      - docker
    install: ''
    script:
      - docker-compose run --rm foliant make site --with mkdocs
    deploy:
      provider: pages
      local-dir: flnt-test.mkdocs
      skip-cleanup: true
      github-token: $GITHUB_TOKEN
      keep-history: true
      verbose: true
      on:
        branch: master
    ```

7. Чтобы проверить интеграцию, сделайте коммит и выполните команду `git push`.
