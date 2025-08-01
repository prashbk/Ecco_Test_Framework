import pytest
import re
from pages.feed_page import FeedPage

def test_login_and_open_feed(login):
    page = login
    feed_page = FeedPage(page)
    assert "/feed" in page.url
    assert "ecco" in page.title().lower()
    assert feed_page.is_discover_visible()

def test_logout_flow(login):
    page = login

    # Click the first button that opens a menu with "Logout"
    profile_buttons = page.get_by_role("button")

    for i in range(profile_buttons.count()):
        profile_buttons.nth(i).click()
        try:
            if page.get_by_role("menuitem", name="Logout").is_visible():
                break
        except:
            continue

    # Now click logout
    page.get_by_role("menuitem", name="Logout").click()

    # Validate logout success
    page.wait_for_url("**/login", timeout=5000)
    assert "login" in page.url

def test_invalid_login(page):
    page.goto("https://ecco.app/login")
    page.fill('input[type="email"]', "invalid@example.com")
    page.fill('input[type="password"]', "wrongpassword")
    page.click('button:has-text("Sign In")')
    page.wait_for_timeout(3000)  # wait briefly for push notification

    # Validate error message
    assert page.locator("text=Unable to sign in.").is_visible() or \
           page.locator("text=Login failed. Please try again.").is_visible()