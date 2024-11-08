@echo off
REM Create the main project directory
mkdir "threat-intelligence-project"

REM Create data directories
mkdir "threat-intelligence-project\data\raw"
mkdir "threat-intelligence-project\data\processed"
mkdir "threat-intelligence-project\data\models"

REM Create source code directories
mkdir "threat-intelligence-project\src\data_collection"
mkdir "threat-intelligence-project\src\data_processing"
mkdir "threat-intelligence-project\src\ml_models"
mkdir "threat-intelligence-project\src\api"
mkdir "threat-intelligence-project\src\utils"

REM Create frontend directories
mkdir "threat-intelligence-project\frontend\public"
mkdir "threat-intelligence-project\frontend\src"
mkdir "threat-intelligence-project\frontend\src\components"

REM Create tests directory
mkdir "threat-intelligence-project\tests"

REM Create docs directory
mkdir "threat-intelligence-project\docs"

REM Create initial files in data/raw
echo. > "threat-intelligence-project\data\raw\threat_data_source_1.json"
echo. > "threat-intelligence-project\data\raw\threat_data_source_2.csv"

REM Create initial files in data/processed
echo. > "threat-intelligence-project\data\processed\processed_threat_data.csv"
echo. > "threat-intelligence-project\data\processed\threat_indicators.json"

REM Create initial files in data/models
echo. > "threat-intelligence-project\data\models\trained_model.pkl"

REM Create initial files in src/data_collection
echo. > "threat-intelligence-project\src\data_collection\collect_osint.py"
echo. > "threat-intelligence-project\src\data_collection\scrape_forum_data.py"

REM Create initial files in src/data_processing
echo. > "threat-intelligence-project\src\data_processing\process_data.py"
echo. > "threat-intelligence-project\src\data_processing\feature_extraction.py"

REM Create initial files in src/ml_models
echo. > "threat-intelligence-project\src\ml_models\train_model.py"
echo. > "threat-intelligence-project\src\ml_models\predict_threats.py"

REM Create initial files in src/api
echo. > "threat-intelligence-project\src\api\app.py"
echo. > "threat-intelligence-project\src\api\routes.py"

REM Create initial files in src/utils
echo. > "threat-intelligence-project\src\utils\helpers.py"
echo. > "threat-intelligence-project\src\utils\logger.py"

REM Create initial files in frontend/public
echo. > "threat-intelligence-project/frontend/public/index.html"
echo. > "threat-intelligence-project/frontend/public/styles.css"

REM Create initial files in frontend/src
echo. > "threat-intelligence-project/frontend/src\App.js"
mkdir "threat-intelligence-project/frontend/src/components"
echo. > "threat-intelligence-project/frontend/src/components/ThreatList.js"
echo. > "threat-intelligence-project/frontend/src/components/ThreatDetail.js"
echo. > "threat-intelligence-project/frontend/src/components/Header.js"

REM Create initial test files
echo. > "threat-intelligence-project/tests/test_data_collection.py"
echo. > "threat-intelligence-project/tests/test_data_processing.py" 
echo. > "threat-intelligence-project/tests/test_ml_models.py" 

REM Create documentation files
echo. > "threat-intelligence-project/docs/README.md" 
echo. > "threat-intelligence-project/docs/CONTRIBUTING.md" 
echo. > "threat-intelligence-project/docs/INSTALLATION.md" 
echo. > "threat-intelligence-project/docs/USAGE.md" 

REM Create requirements file
echo. > "threat-intelligence-project/requirements.txt"

@echo Folder structure created successfully!