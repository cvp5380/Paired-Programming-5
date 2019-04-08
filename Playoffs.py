from selenium import webdriver

browser = webdriver.Firefox()

# Chris & Ciera have heard about a cool new online playoff app. She goes
# to check out its homepage
browser.get('http://localhost:8000')

# They notice the page title and header mention playoff teams assert 'Playoff Teams' in browser.title

# They were invited to enter a basketball matchup straight away

# They type "Milwaukee Bucks vs Detriot Pistons" into a text box 
# When they hit enter, the page updates, and now the page lists
# "1: "Milwaukee Bucks vs Detriot Pistons" as an item in a list

# There is still a text box inviting them to add another item. They
# enter "Boston Celtics vs Indiana Pacers "

# The page updates again, and now shows both items on their list

# They wonder whether the site will remember their list. Then they see
# that the site has generated a unique URL for them -- there is some
# explanatory text to that effect.

# They visits that URL - their playoff list is still there.

# Satisfied, they go back to sleep

browser.quit()