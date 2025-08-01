import pytest
import yaml
from pathlib import Path
from playwright.sync_api import sync_playwright

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "env.yaml"

def load_credentials():
    with open(CONFIG_PATH) as f:
        config = yaml.safe_load(f)
    return config["credentials"]["username"], config["credentials"]["password"]

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def login(page):
    username, password = load_credentials()
    page.goto("https://ecco.app/login")
    page.fill('input[type="email"]', username)
    page.fill('input[type="password"]', password)
    page.click('button:has-text("Sign In")')
    page.wait_for_url("**/feed", timeout=10000)
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page_fixture = item.funcargs.get("login") or item.funcargs.get("page")
        if page_fixture:
            screenshot_path = f"reports/{item.name}_failure.png"
            page_fixture.screenshot(path=screenshot_path, full_page=True)
