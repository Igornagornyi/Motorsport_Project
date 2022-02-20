<h2>Selenium WebDriver Framework with Pytest on functional Approach </strong>

<h3>Structure of the project:</h3>
<ul>1.core - configs > infrastructure > cookie > singleton > db repositories </ul>
<ul>2.pages - homepage > newspage > basepage > locators</ul>
<ul>3. tests > test > conftest</ul>
<hr><h3>Setup of the project</h3>
<ul>1.Install postgresql database and create db with name same as in config /core/config/db_config.py
</ul><ul>2.Create table 'test_result' same as provided model in core/infrastructure/models/test_result.py
</ul><ul>3.Install dependencies:</ul>
<ul>pip install -r requirements.txt</ul>
<ul>4.Run tests with command:</ul>
<ul>pytest .</ul>