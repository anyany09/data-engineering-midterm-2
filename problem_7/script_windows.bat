@echo off
REM Run the Docker container

docker build -t csv_processor . --no-cache
setlocal

REM Set default values (modify as needed)
set INPUT_FILE=input.csv
set OUTPUT_FILE=output.csv
set COLUMN_NAME=category
set FILTER_VALUE=sports

REM Allow user to override default values
if not "%~1"=="" set INPUT_FILE=%1
if not "%~2"=="" set OUTPUT_FILE=%2
if not "%~3"=="" set COLUMN_NAME=%3
if not "%~4"=="" set FILTER_VALUE=%4

REM Run the Docker container
docker run --rm -v "%cd%:/app" csv_processor %INPUT_FILE% %OUTPUT_FILE% %COLUMN_NAME% %FILTER_VALUE%

endlocal