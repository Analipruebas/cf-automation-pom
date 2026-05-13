from time import sleep
import pytest
from utils.driver_factory import create_driver


def pytest_addoption(parser):
   # parser.addoption(
    #    "--headless",
    #    action="store_true",
     #   help="Ejecutar pruebas en modo headless (sin interfaz de usuario)"
    #)
   try:
       parser.addoption(
           "--headless",
           action="store_true",
           default=False,
           help="Ejecutar las pruebas en modo headless"
       )
   except ValueError:
       # Si ya existe (por un plugin), Pytest simplemente continuará
       pass

@pytest.fixture
def driver(request):
    headless = request.config.getoption("--headless")
    driver = create_driver(headless=headless)
    yield driver
    sleep(3)
    driver.quit()