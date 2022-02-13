class HomePageLocatorCollection:
    def __init__(self):
        self.news_button = "//ul[@class='ms-content-menu visible']" \
                           "//a[@href='/all/news/']"
        self.subscribe_button = "//div[@class='ms-footer_top-start']" \
                                "//a[contains(text(), 'Subscribe to our newsletter')]"
        self.onetrust_button = "//div[@class='banner-actions-container']//button"
