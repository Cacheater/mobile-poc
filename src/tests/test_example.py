from src.pages import ExamplePage

def test_example():
    driver = get_driver()
    page = ExamplePage(driver)
    page.example_method()
    # Agrega tus aserciones aquí
    driver.quit()