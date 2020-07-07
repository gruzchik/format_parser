# How to use

 - Rename or copy `settings_def.py` to `settings.py` and fill out parameters inside
 

# Run Python script with docker

 - clone repository to local folder
 - build docker image from Dockerfile
  
 `docker build -t pp .`
 - add current folder as a volume and run python using command
 
 `docker run --rm -v $(pwd):/app pp python /app/output_teamcity_json.py`

Also we can execute this using running shell file `rundocker.sh`. We have to run this file in the directory where is located Dockerfile


# Python script locally
 
 - For JSON output run `output_teamcity_json.py`
 - For JSON output from file run `file_output_teamcity.py`
 - For XML output run `output_teamcity_xml.py`
 
# Bash script
 
 - Run `output_teamcity.sh -t json` for output in JSON
 
 - Run `output_teamcity.sh -t xml` for output in XML
 
 - Runing script without paramaters `output_teamcity.sh` show output in XML format
 
 
 Both scripts uses the same configuration file
