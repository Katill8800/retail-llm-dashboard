
@echo off
REM Activate Anaconda base environment
CALL conda activate base

REM Change to your project folder
cd /d C:\Users\DT412RZ\Downloads\retail_llm_dashboard

REM Run the LLM query script
python llm_query.py

pause
