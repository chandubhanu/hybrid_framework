REM Run only sanity tests and generate an HTML report
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
