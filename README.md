








Flood Prediction Model: Start with building a basic deep learning model using TensorFlow or PyTorch to predict flood risk. You can use your elevation data and weather data for training.

Data Ingestion: Use GeoPandas and Rasterio to load and process geospatial data (e.g., elevation, weather data).

Flood Risk Calculation: Based on the model predictions, calculate flood zones using thresholds (e.g., predicted rainfall, elevation thresholds, etc



# 1 install & run

#NOTE : the requirements will be a few Gb woth of storage. Unless you're working with a codespace, the installation will take some time depending on your internet speed.
# 1.1 install mini conda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh

# 1.2 Restart Terminal then create a virtual environment with conda 
conda create --name flood_mapping python=3.8
conda init
conda activate flood_mapping

# 1.3 Install all requirements 
pip install -r requirements.txt

Note : if issues arise with gdal install
conda install -c conda-forge gdal
sudo apt-get update
sudo apt-get install -y gdal-bin libgdal-dev
pip install gdal
pip install requirements.txt

# 1.4 install gcloud CLI for importing sentinel 1 data 
Bash : 


curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get update && sudo apt-get install google-cloud-cli
gcloud init


