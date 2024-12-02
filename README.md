# PCOS Predictor

This project is a **PCOS Prediction Tool** that leverages machine learning to predict the likelihood of Polycystic Ovary Syndrome (PCOS) based on user inputs. It provides a user-friendly interface for interacting with the model and displaying predictions.

## Features

- **Interactive UI**: Simple and intuitive design for entering the required data.
- **Machine Learning Model**: Logistic Regression model to predict PCOS.
- **Real-Time Prediction**: Get instant results based on input data.
- **Categorical and Numerical Features**: Handles a mix of categorical and numerical features effectively using preprocessing pipelines.
- **Live Demo**: Try the app online!

## Live Demo

👉 [PCOS Predictor - Live Demo](https://dishamondal2024-pcos-predictor.hf.space/)

## Installation

To run this project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/pcos-predictor.git
   cd pcos-predictor
   ```

2. **Install dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   streamlit run app.py
   

4. **Access the app**:
   Open [http://localhost:8501](http://localhost:8501) in your web browser.

## Usage

1. Enter the required details, such as `Skin Darkening`, `Weight`, and other attributes.
2. Click the **Predict PCOS** button.
3. The app will display whether the individual is likely to have PCOS.

## Dataset

The model is trained using a PCOS dataset that includes features like:
- Follicle count (left and right ovaries)
- Weight (kg)
- AMH levels
- Lifestyle attributes (Fast Food consumption, Pimples, etc.)

## Technologies Used

- **Frontend**: Streamlit for the interactive user interface.
- **Backend**: Python-based preprocessing and Logistic Regression model.
- **Machine Learning**: Scikit-learn for building and training the model.
- **Deployment**: Hugging Face Spaces for hosting the app.

## File Structure

```
.
├── app.py              # Streamlit app for user interaction
├── model.pkl           # Saved machine learning model
├── requirements.txt    # Dependencies for the project
├── README.md           # Project documentation
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
