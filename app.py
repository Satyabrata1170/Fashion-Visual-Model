from flask import Flask, render_template, request, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(__name__)  

# Load your datasets
dress_data = pd.read_csv("dresses_bd_processed_data.csv")
jeans_data = pd.read_csv("jeans_bd_processed_data.csv")

dress_data['category'] = 'dress'
jeans_data['category'] = 'jeans'
full_data = pd.concat([dress_data, jeans_data], ignore_index=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.json.get('keyword', '').lower()
    results = full_data[full_data['category'].str.contains(keyword)]

    output = []
    for _, row in results.iterrows():
        product_id = str(row['product_id'])
        image_path = f"/images/{product_id}.jpg"
        if os.path.exists(os.path.join('images', f"{product_id}.jpg")):
            output.append({'image': image_path, 'title': f"{row['category'].capitalize()} - {product_id}"})
    return jsonify(output)

@app.route('/images/<path:filename>')
def custom_images(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(debug=True)
