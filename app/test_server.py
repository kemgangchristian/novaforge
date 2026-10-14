from http.server import HTTPServer
import threading
import unittest
from urllib.request import urlopen

from server import Handler


class AppTests(unittest.TestCase):
    def test_repond_novaforge_app(self):
        # Le port 0 laisse le système choisir un port libre
        server = HTTPServer(("127.0.0.1", 0), Handler)
        port = server.server_address[1]
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with urlopen(f"http://127.0.0.1:{port}/") as response:
                self.assertEqual(response.status, 200)
                self.assertEqual(response.read(), b"NovaForge app\n")
        finally:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    unittest.main()
