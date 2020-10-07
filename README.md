<h1>Тестовое задание</h1>
<p>Файловый сервер, написанный на стандартной библиотеке http. Работает только с POST-запросами
и осуществляет три действия с файлами: прием от клиента, передача клиенту и удаление.
Файл сохраняется под захэшированным названием, хэш возвращается клиенту. Скачивание и удаление файла
происходит при запросе с указанием этого хэша</p>
<p>Примеры запросов:<br>
  {"method": "upload", "filename": "test"} body="байт-код данных из файла"<br>
  {"method": "download", "filename": "9gn439mla43nfd8f9"}<br>
  {"method": "delete", "filename": "89nfa902nig0sdna18"}<br>
</p>
<p>Для запуска необходимо заполнить config.ini</p>
