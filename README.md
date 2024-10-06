
# 🌌 Satellite Insights & Space Exploration Chatbot

Welcome to the **Satellite Insights & Space Exploration Chatbot** project! This application is designed to assist researchers, space enthusiasts, and the general public by providing summarized insights from satellite data and answering questions related to space exploration, NASA missions, planets, stars, and more.

## 🚀 Features

### 🛰️ Satellite Insights Summarizer
- **Function**: Upload satellite data in CSV or JSON format to get a simplified summary of the information.
- **Benefit**: Makes satellite data more accessible by turning complex observations into understandable insights for scientists, researchers, and the public.
- **Implementation**: Utilizes OpenAI's API to summarize satellite data into key trends and insights.

### 💬 Space Exploration Chatbot
- **Function**: A chatbot that answers questions about planets, stars, NASA missions, and space history.
- **Benefit**: Educates the public and increases engagement with NASA’s work by providing quick and accurate responses.
- **Implementation**: Powered by Together AI’s language model, this chatbot is perfect for anyone curious about space.

## 🛠️ Tech Stack
- **Streamlit**: For building the web interface.
- **OpenAI API**: For satellite data summarization.
- **Together AI API**: For generating responses related to space exploration in the chatbot.
- **Python**: The core language used for development.

## 📂 Project Structure
```bash
├── streamlit_app.py          # Main application file
├── secrets.toml              # File for storing API keys (do not share)
├── satellite_data.csv        # Example satellite data file for testing
├── README.md                 # Project documentation (this file)
└── requirements.txt          # List of dependencies
```

## 📊 Example Data
Here's a sample of the satellite data used in this project. You can upload this or similar data files to the application:

```csv
latitude,longitude,temperature,humidity,cloud_coverage,observation_time
34.0522,-118.2437,25.3,60,20,2023-10-05 10:30:00
36.7783,-119.4179,27.6,55,10,2023-10-05 10:45:00
40.7128,-74.0060,22.1,70,30,2023-10-05 11:00:00
51.5074,-0.1278,18.5,80,45,2023-10-05 11:15:00
48.8566,2.3522,20.2,75,25,2023-10-05 11:30:00
35.6895,139.6917,28.4,65,15,2023-10-05 11:45:00
55.7558,37.6173,16.8,85,50,2023-10-05 12:00:00
39.9042,116.4074,30.0,50,5,2023-10-05 12:15:00
28.6139,77.2090,32.3,45,0,2023-10-05 12:30:00
-33.8688,151.2093,24.7,55,15,2023-10-05 12:45:00
```

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/satellite-insights-chatbot.git
cd satellite-insights-chatbot
```

### 2. Install Dependencies
To install the required packages, you can run:
```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys
You’ll need to add your API keys in the `secrets.toml` file:
```toml
aiml_api_key = "your_openai_api_key"
together_ai_key = "your_together_ai_key"
```

### 4. Run the Application
Once everything is set up, run the app using the command:
```bash
streamlit run streamlit_app.py
```

### 5. Upload Satellite Data or Ask Space Questions
- You can upload a CSV or JSON file with satellite data to get an insightful summary.
- You can also ask questions to the chatbot about space missions, planets, and more.

## 💻 API Configuration
- **OpenAI API**: Used to summarize satellite data.
- **Together AI API**: Powers the chatbot for answering space exploration queries.

Make sure to sign up for API keys from [OpenAI](https://openai.com) and [Together AI](https://together.ai) to access their services.

## 📚 How It Works

### Satellite Insights Summarizer
1. **Upload Satellite Data**: Upload a CSV or JSON file.
2. **Processing**: The data is passed to OpenAI’s model, which summarizes the complex information.
3. **Result**: You receive a simplified summary of key observations from the satellite data.

### Space Exploration Chatbot
1. **Ask a Question**: Use the chatbot interface to ask a space-related question.
2. **Processing**: The question is passed to Together AI’s model.
3. **Result**: You receive a detailed response related to the query.

## 🛡️ License
This project is licensed under the **MIT License**.

## 🤝 Contributions
 - Malaika Farooq
Contributions are welcome! Feel free to submit a pull request or open an issue if you find a bug or have a feature request.

## 🛰️ Future Enhancements
- **Real-time satellite data fetching**.
- **Enhanced data visualization**.
- **Advanced predictions using satellite data**.
