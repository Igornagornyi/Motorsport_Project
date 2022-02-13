class NewsPageLocatorCollection:
    def __init__(self):
        self.filter_button = "//div[@class='ms-filter_toggler']"
        self.search_field = "//input[@class='ms-filter-search_input']"
        self.search_field_result_first = "//div[@class='ms-filter-option']/span[1]"
        self.search_field_result = "//div[@class='ms-filter-option']/span"

