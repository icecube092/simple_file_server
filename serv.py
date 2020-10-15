import configparser
import hashlib
import http
import os
import random
import sys
from http import server


server_config = configparser.ConfigParser()
server_config.read("config.ini")


class HttpProcessor(server.BaseHTTPRequestHandler):
    """
    обработчик запросов
    """
    def do_POST(self):
        length = int(self.headers.get("Content-Length"))
        content = self.rfile.read(length)
        self.rfile.close()
        method = self.headers.get("method")
        filename = self.headers.get("filename")
        if not method or not filename:
            self.send_response(http.HTTPStatus.BAD_REQUEST, "too few values")
            self.end_headers()
            return
        else:
            if method == "upload":
                self.upload(filename, content)
            elif method == "download":
                self.download(filename)
            elif method == "delete":
                self.delete(filename)
            else:
                self.send_response(http.HTTPStatus.NOT_FOUND, "method not found")
                self.end_headers()

    def upload(self, filename: str, data: bytes):
        """
        загрузка переданных данных в файл на сервере
        :param filename: переданное название файла
        :param data: байт-код с данными файла
        """
        name = hashlib.sha1(str(random.randint(1, 1000000)).encode("utf-8")).hexdigest()
        if not os.path.exists(f"store/{name[:2]}"):
            os.mkdir(f"store/{name[:2]}")
        with open(f"store/{name[:2]}/{name}.txt", "wb") as file:
            file.write(data)
        self.send_response(http.HTTPStatus.OK, name)
        self.end_headers()

    def download(self, filename: str):
        """
        передача данных из файла клиенту
        :param filename: хэш файла
        """
        if os.path.exists(f"store/{filename[:2]}/{filename}.txt"):
            with open(f"store/{filename[:2]}/{filename}.txt", "rb") as file:
                data = file.read()
            self.send_response(http.HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(data)
        else:
            self.send_response(http.HTTPStatus.NOT_FOUND, "file not found")
            self.end_headers()

    def delete(self, filename: str):
        """
        удаление файла с сервера
        :param filename: хэш файла
        """
        path = f"store/{filename[:2]}/{filename}.txt"
        if os.path.exists(path):
            os.remove(path)
            self.send_response(http.HTTPStatus.OK)
        else:
            self.send_response(http.HTTPStatus.NOT_FOUND, "file not found")
        self.end_headers()


if __name__ == '__main__':
    if not os.path.exists("store"):
        os.mkdir("store")
    serv = server.ThreadingHTTPServer(
        (server_config["server"]["host"], int(server_config["server"]["port"])), HttpProcessor
    )
    print("Working...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Exit")
        sys.exit(1)
