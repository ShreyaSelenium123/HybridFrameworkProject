 pytest -s -v -m "regression and sanity" --html=./Reports/report.html --browser chrome
rem pytest -s -v -m "sanity" --html=./Reports/report.html --browser chrome
rem pytest -s -v -m "regression or sanity" --html=./Reports/report.html --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/report.html --browser chrome
