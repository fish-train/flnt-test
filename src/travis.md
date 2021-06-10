# Интеграция с Travis CI

**Travis CI** – распределённый веб-сервис для сборки и тестирования программного обеспечения, использующий GitHub в качестве хостинга исходного кода.

Travis CI позволяет развернуть сайт при изменении кода в репозитории.

Чтобы включить интеграцию с Travis CI:

1. Откройте настройки профиля GitHub.
2. Откройте страницу «Applications».
3. Добавьте приложение Travis CI по инструкции [Reviewing your authorized integrations](https://docs.github.com/en/github/authenticating-to-github/reviewing-your-authorized-integrations).
4. Залогиньтесь на сайте [Travis CI](https://travis-ci.com/).
5. Активируйте репозиторий.
6. Добавьте файл  **.travis.yml** в репозиторий:
  
        language: python
        services:
        - docker
        install: ''
        script:
        - docker-compose run --rm foliant make site --with mkdocs
        
        deploy:
        - provider: pages:git
          edge: true
          token: $GITHUB_TOKEN
          local-dir: flnt-test.mkdocs
          keep-history: true
          verbose: true
          on:
            branch: master

7. Чтобы проверить интеграцию, сделайте коммит и выполните команду:

        git push
