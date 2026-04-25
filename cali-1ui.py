import pickle
from flask import Flask, request, render_template

# Load the pre-trained model
with open(r"D:\California_House_Prediction [Resume P]\Linear_Regression_california.pkl", 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def greet():
    return render_template('index.html')

@app.route('/pred', methods=['POST'])
def pred():
    try:
        # Get and validate inputs (IMPORTANT FIX)
        MedInc = request.form.get("MedInc")
        HouseAge = request.form.get("HouseAge")
        Population = request.form.get("Population")
        AveOccup = request.form.get("AveOccup")
        AveBedrms = request.form.get("AveBedrms")
        Latitude = request.form.get("Latitude")

        # Check if any field is empty
        if not all([MedInc, HouseAge, Population, AveOccup, AveBedrms, Latitude]):
            return render_template('index.html', error="Please fill all fields!")

        # Convert to float
        MedInc = float(MedInc)
        HouseAge = float(HouseAge)
        Population = float(Population)
        AveOccup = float(AveOccup)
        AveBedrms = float(AveBedrms)
        Latitude = float(Latitude)

        # Prediction
        ans = model.predict([[MedInc, HouseAge, Population, AveOccup, AveBedrms, Latitude]])

        # 🔥 Convert to actual price
        actual_price = ans[0] * 100000

        # Format nicely
        formatted_price = f"₹ {actual_price:,.0f}"

        # Final output
        return render_template(
            'index.html',
            result=f"Estimated House Price: {formatted_price}"
        )

    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)