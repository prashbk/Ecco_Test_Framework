class FeedPage:
    def __init__(self, page):
        self.page = page

    def is_discover_visible(self):
        try:
            self.page.wait_for_selector("text=ecco", timeout=5000)
            return True
        except:
            return False
