# Heart_Disease_Prediction_System

1. How to Run the Project (Locally)

2. Clone the repository: git clone cd

Install Dependencies: pip install numpy pandas scikit-learn streamlit pyngrok

Prepare the Model and App: Ensure you have the heart_gtigwd.csv dataset in the project directory. The notebook will generate heart_disease_model.sav and app.py. If running this project directly from a Colab notebook, the model saving and app.py creation steps are handled within the notebook.

3. Run the Streamlit Application: To run the Streamlit app locally, execute the following command in your terminal:

streamlit run app.py This will open the application in your web browser.

4. Using ngrok for Public Access (Optional): If you need to expose your local Streamlit application to the internet, you can use ngrok. Obtain an authentication token from the ngrok dashboard and then run: ngrok authtoken YOUR_NGROK_AUTH_TOKEN nohup streamlit run app.py --server.port 8501 & ngrok http 8501 This will provide you with a public URL to share your application.
