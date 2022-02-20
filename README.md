<h2>Selenium WebDriver Framework with Pytest on functional Approach </strong>

<h3>Structure of the project:</h3>
<ul>1.core - configs(config, db_config, test_rail) > infrastructure > models(base_model, test_result) > repositories(base_repository, test_result_repository)> cookie > local_storage > page_object_singleton > singleton > result</ul>
<ul>2.pages - homepage(homepage, homepage_locators) > newspage(newspage, news_page_locators) > basepage</ul>
<ul>3.tests > test_motorsport > conftest</ul>
<hr><h3>Setup of the project</h3>
<ul>1.Install postgresql database and create db with name same as in config /core/config/db_config.py
</ul><ul>2.Create table 'test_result' same as provided model in core/infrastructure/models/test_result.py
</ul><ul>3.Install dependencies:</ul>
<ul>pip install -r requirements.txt</ul>
<ul>4.Run tests with command:</ul>
<ul>pytest .</ul>