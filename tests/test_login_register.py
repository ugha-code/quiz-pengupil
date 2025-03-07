from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL aplikasi yang diuji
BASE_URL = "http://localhost:8000"

# Setup WebDriver (gunakan Chrome)
driver = webdriver.Chrome()

def test_register(username, email, password, expected_message):
    """
    Fungsi untuk menguji form registrasi.
    """
    driver.get(f"{BASE_URL}/register.php")
    time.sleep(2)

    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

    body_text = driver.page_source
    if expected_message in body_text:
        print(f"✅ Test Register ({username}) PASSED")
    else:
        print(f"❌ Test Register ({username}) FAILED")

def test_login(username, password, expected_message):
    """
    Fungsi untuk menguji form login.
    """
    driver.get(f"{BASE_URL}/login.php")
    time.sleep(2)

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

    body_text = driver.page_source
    if expected_message in body_text:
        print(f"✅ Test Login ({username}) PASSED")
    else:
        print(f"❌ Test Login ({username}) FAILED")

# ---------------- TEST CASES ----------------

# Test Case untuk Registrasi
test_register("newuser", "newuser@example.com", "ValidPass@123", "Registrasi berhasil")
test_register("existinguser", "newuser2@example.com", "ValidPass@123", "Username sudah digunakan")
test_register("newuser3", "invalidemail", "ValidPass@123", "Email tidak valid")
test_register("newuser4", "user@example.com", "short", "Password minimal 8 karakter")
test_register("newuser5", "", "ValidPass@123", "Email wajib diisi")
test_register("", "validemail@example.com", "ValidPass@123", "Username wajib diisi")
test_register("", "", "", "Semua field wajib diisi")

# Test Case untuk Login
test_login("newuser", "ValidPass@123", "Login berhasil")
test_login("invaliduser", "ValidPass@123", "Username atau Password salah")
test_login("newuser", "WrongPass@123", "Username atau Password salah")
test_login("", "ValidPass@123", "Username wajib diisi")
test_login("newuser", "", "Password wajib diisi")
test_login("", "", "Username dan password wajib diisi")

# ---------------- SELESAI ----------------
driver.quit()
