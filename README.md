# Fashion Visual Search & Intelligent Styling Assistant
An end-to-end machine learning system that enables basic image classification for fashion items (Dress or Jeans), with a web-based user interface built using Flask.


## Project Workflow

1. **Data Collection & Image Downloading**  
   - Started with CSV files containing image URLs (`dresses_bd_processed_data.csv`, `jeans_bd_processed_data.csv`).
   - Wrote a script to download and store images locally in the `images/` folder.

2. **Image Preprocessing & EDA**  
   - Performed univariate/bivariate analysis in `Fashion_Visual_Search_EDA.ipynb`.
   - Applied preprocessing like resizing, normalization, and encoding category labels.

3. **Model Development**  
   - Built a CNN using Keras to classify images as either **Dress** or **Jeans**.
   - Implemented early stopping and model checkpointing.
   - Saved the best performing model as `model.weights.best.keras`.

4. **Web Deployment with Flask**  
   - Developed a user-friendly Flask interface in `app.py`.
   - User enters a `Category`, and the app:
     - Displays the corresponding product image
     - Predicts and shows the clothing category (Dress or Jeans)



##  How to Run the Project

**Open With VsCode**

**Run the Flask app**
   - python app.py
**Access the app in your browser**
   - Go to http://127.0.0.1:5000 (By Default)
