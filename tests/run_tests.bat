@echo off
pytest tests/test_all.py -v > test_report.txt
echo Tests finished. Report saved to test_report.txt
type test_report.txt
pause
