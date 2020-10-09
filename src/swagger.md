# Интеграция Swagger с документацией

Чтобы интегрировать Swagger со своим проектом:

1. Создайте описание API в [Swagger Editor](https://editor.swagger.io/) и сохраните YAML-файл. Например, под названием **openapi_3.0.2.yaml**.
2. Перейдите в [репозиторий Swagger UI](https://github.com/swagger-api/swagger-ui) и нажмите на кнопку **Clone or download**.
3. Нажмите на кнопку **Download ZIP**.
4. Распакуйте архив и перейдите в папку `dist`.
5. Из папки `dist` скопируйте файл **swagger-ui.css** и вставьте его в папку `css` проекта.
6. Из папки `dist` скопируйте файлы **swagger-ui-bundle.js** и **swagger-ui-standalone-preset.js** и вставьте их в папку `js` проекта.
7. В файл **foliant.yml** добавьте настройки mkdocs:

        extra_css:
          - css/swagger-ui.css
        extra_javascript:
          - js/swagger-ui-bundle.js
          - js/swagger-ui-standalone-preset.js

8. Скопируйте YAML-файл с описанием API в папку проекта.
9. Создайте MD-файл и вставьте в него код:

```html
<link rel="stylesheet" type="text/css" href="css/swagger-ui.css" >
<style>
  html
  {
    box-sizing: border-box;
    overflow: -moz-scrollbars-vertical;
    overflow-y: scroll;
  }
  *,
  *:before,
  *:after
  {
    box-sizing: inherit;
  }
  body {
    margin:0;
    background: #fafafa;
  }
</style>

<div id="swagger-ui"></div>

<script src="js/swagger-ui-bundle.js"> </script>
<script src="js/swagger-ui-standalone-preset.js"> </script>
<script>
window.onload = function() {
  // Build a system
  const ui = SwaggerUIBundle({
    url: "https://petstore.swagger.io/v2/swagger.json",
    //url: "../src/openapi_3.0.2.yaml",
    //url: "/openapi_3.0.2.yaml",
    dom_id: '#swagger-ui',
    defaultModelsExpandDepth: -1,
    docExpansion: "list",
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  })
  window.ui = ui
}
</script>

<style>
.swagger-ui .info .title small pre {
    padding: 1px;
    background-color: #444;
}
.swagger-ui .info .title small {
    font-size: 10px;
    position: relative;
    top: -5px;
    display: inline-block;
    margin: 0 0 0 5px;
    padding: 4px;
    vertical-align: super;
    border-radius: 57px !important;
    background: #89bf04 !important;
}
.swagger-ui .info .title small pre.version {
    background-color: #89bf04;
    border: 0px;
  }
.swagger-ui pre.version {
      padding: 0px;
      max-width: 60px;
      border: 0px;
  }
.swagger-ui .info .title small pre {
      padding:0px;
  }
.swagger-ui .info .title small {
      background-color: rgb(137, 191, 4);
  }
  .swagger-ui table th, .swagger-ui table td {
      padding: 10px !important;
  }
  .swagger-ui table th {
    color: white;
    font-size:16px;
}
.swagger-ui .col_header {
    color: black !important;
}
div#swagger-ui {
    border: 1px solid #dedede;
}
.swagger-ui .info .title small pre {
    padding: 1px;
    background-color: #444;
}
.swagger-ui .info .title small {
    font-size: 10px;
    position: relative;
    top: -5px;
    display: inline-block;
    margin: 0 0 0 5px;
    padding: 4px;
    vertical-align: super;
    border-radius: 57px !important;
    background: #89bf04 !important;
}
.swagger-ui .info .title small pre.version {
    background-color: #89bf04;
  }
.swagger-ui li.tabitem {
    list-style: none !important;
}
.swagger-ui .response-col_description__inner p {
  color: white;
  font-style: normal;
  font-size: 12px;
}
.swagger-ui pre.version {
    padding: 0px;
}
.swagger-ui .info .title small pre {
    padding:0px;
}
.swagger-ui .info .title small {
    background-color: rgb(137, 191, 4);
}
.swagger-ui a.tablinks {
    margin-right: 20px;
}
.swagger-ui td.col.response-col_status {
    padding: 10px !important;
}
.swagger-ui .opblock .opblock-section-header h4 {
  font-size: 18px !important;
  font-weight: bold;
  padding: 0px;
}
.swagger-ui td.col, .swagger-ui td.col.col_header.response-col_description {
    padding: 10px;
}
.swagger-ui h4.opblock-title_normal {
    font-size: 16px;
    font-style: italic;
}
.swagger-ui h4.opblock-title_normal[id] {
    padding-bottom: 15px;
    font-style: italic;
  }
.swagger-ui {
  border: 1px solid #dedede;
}
.swagger-ui select {
    font-weight: normal !important;
    font-family: monospace;
}
.swagger-ui table {
  table-layout: auto !important;
}
.swagger-ui .scheme-container {
  padding: 0px 0px 15px 0px;
}
.swagger-ui .renderedMarkdown p {
    font-size: 14px;
}
.swagger-ui tr.response p {
  font-style: italic;
}
.swagger-ui table.model tbody tr td {
  padding: 1em !important;
}
.response-content-type.controls-accept-header small code {
    font-size: 12px;
  }
.swagger-ui .opblock-summary-path a.nostyle {
    font-family: monospace;
}
.swagger-ui .info {
  /* margin: -25px 0px !important; */
}
.swagger-ui .main span.url {
    display: none;
}
.swagger-ui span.opblock-summary-path a.nostyle {
    font-family: Monospace !important;
    size: 16px;
}
.swagger-ui .opblock-description-wrapper, .swagger-ui .opblock-external-docs-wrapper, .swagger-ui .opblock-title_normal {
    padding: 15px 20px 5px 20px;
}
.swagger-ui h1[id], .swagger-ui h2[id], .swagger-ui h3[id], .swagger-ui h4[id], .swagger-ui h5[id] {
    margin: 0px;
    padding: 0px;
}
.swagger-ui pre {
    font-family: Monaco, Monospace !important;
    font-size: 11px;
  }
h6, h6 code.highlighter-rouge {
    font-size: 16px;
}
.swagger-ui .responses-inner h4, .swagger-ui .responses-inner h5 {
  font-size: 16px;
}
.swagger-ui code {
    font-size: 12px;
}
/* disable the try it out buttons
button.btn.try-out__btn {
    display: none;
}
*/

.topbar {
    display: none;
}
</style>
```

## Пример описания API

<link rel="stylesheet" type="text/css" href="css/swagger-ui.css" >
<style>
  html
  {
    box-sizing: border-box;
    overflow: -moz-scrollbars-vertical;
    overflow-y: scroll;
  }
  *,
  *:before,
  *:after
  {
    box-sizing: inherit;
  }
  body {
    margin:0;
    background: #fafafa;
  }
</style>

<div id="swagger-ui"></div>

<script src="js/swagger-ui-bundle.js"> </script>
<script src="js/swagger-ui-standalone-preset.js"> </script>
<script>
window.onload = function() {
  // Build a system
  const ui = SwaggerUIBundle({
    url: "https://petstore.swagger.io/v2/swagger.json",
    //url: "../src/openapi_3.0.2.yaml",
    //url: "/openapi_3.0.2.yaml",
    dom_id: '#swagger-ui',
    defaultModelsExpandDepth: -1,
    docExpansion: "list",
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  })
  window.ui = ui
}
</script>

<style>
.swagger-ui .info .title small pre {
    padding: 1px;
    background-color: #444;
}
.swagger-ui .info .title small {
    font-size: 10px;
    position: relative;
    top: -5px;
    display: inline-block;
    margin: 0 0 0 5px;
    padding: 4px;
    vertical-align: super;
    border-radius: 57px !important;
    background: #89bf04 !important;
}
.swagger-ui .info .title small pre.version {
    background-color: #89bf04;
    border: 0px;
  }
.swagger-ui pre.version {
      padding: 0px;
      max-width: 60px;
      border: 0px;
  }
.swagger-ui .info .title small pre {
      padding:0px;
  }
.swagger-ui .info .title small {
      background-color: rgb(137, 191, 4);
  }
  .swagger-ui table th, .swagger-ui table td {
      padding: 10px !important;
  }
  .swagger-ui table th {
    color: white;
    font-size:16px;
}
.swagger-ui .col_header {
    color: black !important;
}
div#swagger-ui {
    border: 1px solid #dedede;
}
.swagger-ui .info .title small pre {
    padding: 1px;
    background-color: #444;
}
.swagger-ui .info .title small {
    font-size: 10px;
    position: relative;
    top: -5px;
    display: inline-block;
    margin: 0 0 0 5px;
    padding: 4px;
    vertical-align: super;
    border-radius: 57px !important;
    background: #89bf04 !important;
}
.swagger-ui .info .title small pre.version {
    background-color: #89bf04;
  }
.swagger-ui li.tabitem {
    list-style: none !important;
}
.swagger-ui .response-col_description__inner p {
  color: white;
  font-style: normal;
  font-size: 12px;
}
.swagger-ui pre.version {
    padding: 0px;
}
.swagger-ui .info .title small pre {
    padding:0px;
}
.swagger-ui .info .title small {
    background-color: rgb(137, 191, 4);
}
.swagger-ui a.tablinks {
    margin-right: 20px;
}
.swagger-ui td.col.response-col_status {
    padding: 10px !important;
}
.swagger-ui .opblock .opblock-section-header h4 {
  font-size: 18px !important;
  font-weight: bold;
  padding: 0px;
}
.swagger-ui td.col, .swagger-ui td.col.col_header.response-col_description {
    padding: 10px;
}
.swagger-ui h4.opblock-title_normal {
    font-size: 16px;
    font-style: italic;
}
.swagger-ui h4.opblock-title_normal[id] {
    padding-bottom: 15px;
    font-style: italic;
  }
.swagger-ui {
  border: 1px solid #dedede;
}
.swagger-ui select {
    font-weight: normal !important;
    font-family: monospace;
}
.swagger-ui table {
  table-layout: auto !important;
}
.swagger-ui .scheme-container {
  padding: 0px 0px 15px 0px;
}
.swagger-ui .renderedMarkdown p {
    font-size: 14px;
}
.swagger-ui tr.response p {
  font-style: italic;
}
.swagger-ui table.model tbody tr td {
  padding: 1em !important;
}
.response-content-type.controls-accept-header small code {
    font-size: 12px;
  }
.swagger-ui .opblock-summary-path a.nostyle {
    font-family: monospace;
}
.swagger-ui .info {
  /* margin: -25px 0px !important; */
}
.swagger-ui .main span.url {
    display: none;
}
.swagger-ui span.opblock-summary-path a.nostyle {
    font-family: Monospace !important;
    size: 16px;
}
.swagger-ui .opblock-description-wrapper, .swagger-ui .opblock-external-docs-wrapper, .swagger-ui .opblock-title_normal {
    padding: 15px 20px 5px 20px;
}
.swagger-ui h1[id], .swagger-ui h2[id], .swagger-ui h3[id], .swagger-ui h4[id], .swagger-ui h5[id] {
    margin: 0px;
    padding: 0px;
}
.swagger-ui pre {
    font-family: Monaco, Monospace !important;
    font-size: 11px;
  }
h6, h6 code.highlighter-rouge {
    font-size: 16px;
}
.swagger-ui .responses-inner h4, .swagger-ui .responses-inner h5 {
  font-size: 16px;
}
.swagger-ui code {
    font-size: 12px;
}
/* disable the try it out buttons
button.btn.try-out__btn {
    display: none;
}
*/

.topbar {
    display: none;
}
</style>
