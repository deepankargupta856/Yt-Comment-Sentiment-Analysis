# YouTube Comment Sentiment Analysis Chrome Extension

![Project Banner](https://img.shields.io/badge/Project-YT_Comment_Analysis-blue.svg)
![Language](https://img.shields.io/badge/Language-Python-brightgreen.svg)
![Framework](https://img.shields.io/badge/Backend-Flask-red.svg)

A Chrome plugin to analyze the sentiment of comments on a YouTube video. This project uses a machine learning model, served via a Flask backend, to process and classify comments as positive, negative, or neutral.

## 🚀 Features

* **Real-time Sentiment Analysis:** Analyzes the comments section of any active YouTube video.
* **Browser Integration:** Runs as a simple-to-use Chrome extension.
* **Data Visualization:** (Assumed) Presents a summary of comment sentiments (e.g., a pie chart or percentage breakdown).

## 🛠️ Tech Stack

* **Machine Learning:** Python, Scikit-learn, Pandas (inferred from `notebooks` and `src`)
* **Backend:** Flask (from `flask_app` directory)
* **Data/Model Versioning:** [DVC (Data Version Control)](https://dvc.org/) (from `dvc.yaml`)
* **Frontend:** Chrome Extension (HTML/CSS/JavaScript)
* **Deployment:** Docker, AWS (inferred from `Dockerfile`, `appspec.yml`)

## 📂 Project Structure

This project follows a standard data science project structure:

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers.
├── data
│   ├── external       <- Data from third-party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- Project documentation.
├── flask_app          <- Flask application for serving the model.
├── models             <- Trained and serialized models.
├── notebooks          <- Jupyter notebooks for data exploration and model training.
├── reports            <- Generated analysis (e.g., figures, HTML reports).
├── requirements.txt   <- The Python dependency file.
├── setup.py           <- Makes the project pip installable.
├── src                <- Source code for use in this project.
│   ├── data           <- Scripts to download or generate data.
│   ├── features       <- Scripts to turn raw data into features.
│   ├── models         <- Scripts to train and predict models.
│   └── visualization  <- Scripts for visualizations.
│
└── tox.ini            <- tox file for testing.
```

## 🏁 Getting Started

Follow these instructions to get a local copy up and running for development and testing.

### Prerequisites

* Python 3.8+
* [DVC](https://dvc.org/doc/install) (Data Version Control)

### 1. Clone the Repository

```bash
git clone [https://github.com/deepankargupta856/Yt-Comment-Sentiment-Analysis.git](https://github.com/deepankargupta856/Yt-Comment-Sentiment-Analysis.git)
cd Yt-Comment-Sentiment-Analysis
```

### 2. Set Up the Environment

It's recommended to use a virtual environment.

```bash
# Create a virtual environment
python -m venv myenv

# Activate it
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate
```

### 3. Install Dependencies

Install all the required Python packages.

```bash
pip install -r requirements.txt
```

### 4. Pull Data and Models

This project uses DVC to manage large files like datasets and models.

```bash
dvc pull
```
*(Note: This requires configuring a DVC remote. If no remote is set up, you may need to run the data processing and training pipelines first.)*

### 5. Run the Backend Server

The Flask server exposes the ML model as an API.

```bash
# (Command to run the Flask app - e.g.,)
python flask_app/app.py
```


## 💡 Usage

1.  Once the backend server is running and the extension is loaded, navigate to any YouTube video page.
2.  Click the "Yt-Comment-Sentiment-Analysis" icon in your Chrome toolbar.
3.  The extension will fetch comments, send them to the backend for analysis, and display the sentiment results.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
