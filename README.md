<h1>Тестовое задание</h1>
<h2>Задание:</h2>
"Хранилище файлов с доступом по http"

Реализовать демон, который предоставит возможность для загрузки (upload) ,
скачивания (download) и удаления файлов.

Upload:
- получив файл от клиента, демон возвращает в отдельном поле http
response хэш загруженного файла
- демон сохраняет файл на диск в следующую структуру каталогов:
     store/ab/abcdef12345...
где "abcdef12345..." - имя файла, совпадающее с его хэшем.
/ab/  - подкаталог, состоящий из первых двух символов хэша файла.
Алгоритм хэширования - на ваш выбор.

Download:
Запрос на скачивание: клиент передаёт параметр - хэш файла. Демон ищет
файл в локальном хранилище и отдаёт его, если находит.

Delete:
Запрос на удаление: клиент передаёт параметр - хэш файла. Демон ищет
файл в локальном хранилище и удаляет его, если находит.

Результат работы должен быть в виде ссылки на git репозиторий с исходным
кодом выполненного ТЗ.
<h2>Решение:</h2>
<p>Файловый сервер, написанный на стандартной библиотеке http. Работает только с POST-запросами
и осуществляет три действия с файлами: прием от клиента, передача клиенту и удаление.
Файл сохраняется под захэшированным названием, хэш возвращается клиенту. Скачивание и удаление файла
происходит при запросе с указанием этого хэша.</p>
<p>Примеры запросов:<br>
  headers={"method": "upload", "filename": "test"} body="байт-код данных из файла"<br>
  headers={"method": "download", "filename": "9gn439mla43nfd8f9"}<br>
  headers={"method": "delete", "filename": "89nfa902nig0sdna18"}<br>
</p>
<p>Для запуска необходимо заполнить config.ini</p>

<h2>Недостатки, можно исправить:</h2>
- разные запросы для разных действий (GET, PUT, DELETE)
- чтение из входящего потока не всех данных сразу, а по несколько байт, для разгрузки оперативной памяти
