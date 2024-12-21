import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Define the possible weather conditions (e.g., Sunny, Rainy, Cloudy)
weather_conditions = ['Sunny', 'Rainy', 'Cloudy', 'Foggy', 'Windy', 'Snowy']

# Load a pre-trained model such as ResNet50 (already trained on ImageNet)
def load_weather_model():
    try:
        # Load the pre-trained ResNet50 model from Keras (without top layers)
        model = tf.keras.applications.ResNet50(weights='imagenet', include_top=True)
        print("Weather model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Function to predict the weather from the uploaded image
def predict_weather_from_image(image_path):
    model = load_weather_model()
    if model is None:
        return "Model could not be loaded"
    
    # Load and preprocess the uploaded image (resize to 224x224 for ResNet50)
    img = image.load_img(image_path, target_size=(224, 224))  # Image size for ResNet50
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize image data for ResNet50
    
    # Predict the weather condition using the model
    predictions = model.predict(img_array)
    
    # Decode predictions using ImageNet class labels (can be mapped to weather categories manually)
    decoded_predictions = tf.keras.applications.resnet50.decode_predictions(predictions, top=3)[0]
    
    # Since ResNet50 is not specifically trained on weather, manually map predictions to weather categories
    # Example: match predictions based on general object categories like 'cloud', 'sun', etc.
    predicted_class = decoded_predictions[0][1]  # Get the predicted class label
    
    return f"Predicted weather condition: {predicted_class}"

# Example usage
image_path = "D:\django projects\weather images\rainy.jpeg"
weather_prediction = predict_weather_from_image(image_path)
print(weather_prediction)


 affiliate_links = []
        if 'rain' in description.lower():
            affiliate_links = [
                {'title': 'Buy an Umbrella', 'url': 'https://www.amazon.in/Rylan-Automatic-Umbrellas-Windproof-Umberalla/dp/B0D17WJLLH?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/41ka57bJK4L.jpg'},
                {'title': 'Get a Raincoat', 'url': 'https://www.amazon.in/HACER-Waterproof-Universal-Resistant-Portable/dp/B0C6QWCXJ1?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/41iXZ-+4wHL._SY300_SX300_.jpg'}
            ]
        elif 'clear' in description.lower() or 'sunny' in description.lower():
            affiliate_links = [
                {'title': 'Buy Sunscreen', 'url': 'https://www.amazon.in/Derma-Co-Hyaluronic-Sunscreen-Protection/dp/B095CRM8NF?tag=sarath04c-21', 'image':'https://m.media-amazon.com/images/I/41NQN8irrVL._SX300_SY300_QL70_FMwebp_.jpg'}
            ]
        elif 'cold' in description.lower() or temp < 15:
            affiliate_links = [
                {'title': 'Get a Moisturizer', 'url': 'https://www.amazon.in/Moisturizer-Hyaluronic-Hydration-Non-Sticky-Instantly/dp/B09Z6TJP7Y?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/41cwfqxLL4L._SX300_SY300_QL70_FMwebp_.jpg'}
            ]
        elif 'cloud' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Hoodie', 'url': 'https://amzn.to/4aFLfto?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/51-1Kq42BEL._SY879_.jpg'}
            ]
        elif 'snow' in description.lower():
            affiliate_links = [
                {'title': 'Buy Snow Boots', 'url': 'https://amzn.to/4dPvPpk?tag=sarath04c-21', 'image':'https://m.media-amazon.com/images/I/61LL-8KcciL._SY675_.jpg'}
            ]
        elif 'wind' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Windbreaker', 'url': 'https://amzn.to/3R3e5Nx?tag=sarath04c-21', 'image':'https://m.media-amazon.com/images/I/71683ZH6YIL._SX679_.jpg'}
            ]
        elif 'haze' in description.lower():
            affiliate_links = [
                {'title': 'Get an Air Purifier', 'url': 'https://amzn.to/3X10YQG?tag=sarath04c-21', 'image':'https://m.media-amazon.com/images/I/71kd66J0MlL._SY879_.jpg'},
                {'title': 'Wear Anti-Pollution Mask', 'url': 'https://www.amazon.in/OxiClear-OxiMask-Pollution-Mask/dp/B01N952VHF/ref=sr_1_1_sspa?crid=3ITM2GS5M28X8&dib=eyJ2IjoiMSJ9.g648tYGoWCOGbwZnwuxY3sY5Ix7ukc6eWtmLSNRUt_Hu78JMCvnNgmBJM2_vbB58kIetenXPI2CMk3K4LCgc50orskcxtG4USkH9BGVMooAcYZatgteWeb8goOnZ6Z7sB3w-wOA6NUPvK_jv-FBBkMPMcpuofvHyeZf8bag2PtV7Oyrr5QcqnPqKT2bHLBqcciPbZqU4M69o9RPH28w7kKklQZ_diENmVEonprv0O2wYW5leI_e2vxP6z_3lVlUD_6vbi7HtdQ2hAJ-UCuwU0lrRci9V62YlzIs4Y8EiUU4.7_KyMyDmouDGpifEhybz2DYk5cZX5YWJrFwVqi5kci8&dib_tag=se&keywords=anti-pollution+mask&qid=1716883730&sprefix=anti-pollution+mask%2Caps%2C961&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/41j6GUixh4L._SY445_SX342_QL70_FMwebp_.jpg'}
            ]
        elif 'mist' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Warm Jacket', 'url': 'https://www.amazon.in/dp/B07VVZ7NP9?tag=sarath04c-21', 'image': get_random_image('warm jacket')}
            ]
        elif 'drizzle' in description.lower():
            affiliate_links = [
                {'title': 'Get a Waterproof Backpack', 'url': 'https://www.amazon.in/dp/B08B7YXHYY?tag=sarath04c-21', 'image': get_random_image('waterproof backpack')}
            ]
        elif 'thunderstorm' in description.lower():
            affiliate_links = [
                {'title': 'Buy Surge Protector', 'url': 'https://www.amazon.in/dp/B08GQK4V2S?tag=sarath04c-21', 'image': get_random_image('surge protector')}
            ]
        elif 'fog' in description.lower():
            affiliate_links = [
                {'title': 'Buy a High Visibility Vest', 'url': 'https://www.amazon.in/dp/B07V2M1K9K?tag=sarath04c-21', 'image': get_random_image('high visibility vest')}
            ]
        elif 'humid' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Dehumidifier', 'url': 'https://www.amazon.in/dp/B07P6PRLVT?tag=sarath04c-21', 'image': get_random_image('dehumidifier')}
            ]
        elif 'dust' in description.lower():
            affiliate_links = [
                {'title': 'Buy Safety Goggles', 'url': 'https://www.amazon.in/dp/B085HRG1X3?tag=sarath04c-21', 'image': get_random_image('safety goggles')}
            ]
        elif 'smoke' in description.lower():
            affiliate_links = [
                {'title': 'Buy an Air Quality Monitor', 'url': 'https://www.amazon.in/dp/B07N9MPG43?tag=sarath04c-21', 'image': get_random_image('air quality monitor')}
            ]
        elif 'sleet' in description.lower():
            affiliate_links = [
                {'title': 'Buy Insulated Gloves', 'url': 'https://www.amazon.in/dp/B07V2Y5CZY?tag=sarath04c-21', 'image': get_random_image('insulated gloves')}
            ]
        elif 'blizzard' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Snow Shovel', 'url': 'https://www.amazon.in/dp/B0897Q2MZY?tag=sarath04c-21', 'image': get_random_image('snow shovel')}
            ]
        elif 'sandstorm' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Dust Mask', 'url': 'https://www.amazon.in/dp/B07HRKGLTC?tag=sarath04c-21', 'image': get_random_image('dust mask')}
            ]
        elif 'tornado' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Safety Helmet', 'url': 'https://www.amazon.in/dp/B097HZJDC7?tag=sarath04c-21', 'image': get_random_image('safety helmet')}
            ]
        elif 'thunder' in description.lower():
            affiliate_links = [
                {'title': 'Buy Ear Protection', 'url': 'https://amzn.to/3KlxoxG?tag=sarath04c-21', 'image':' https://m.media-amazon.com/images/I/51OGBLwDUfL._SX679_.jpg'}
            ]
        elif 'rainbow' in description.lower():
            affiliate_links = [
                {'title': 'Buy Rainbow Wall Decals', 'url': 'https://amzn.to/4dWCY7g?tag=sarath04c-21', 'image': get_random_image('rainbow wall decals')}
            ]
        elif 'northern lights' in description.lower():
            affiliate_links = [
                {'title': 'Get Northern Lights Projector', 'url': 'https://amzn.to/4bBmRdP?tag=sarath04c-21', 'image': get_random_image('northern lights projector')}
            ]
        elif 'frost' in description.lower():
            affiliate_links = [
                {'title': 'Buy Frost Guard Windshield Cover', 'url': 'https://amzn.to/44ZKPgo?tag=sarath04c-21', 'image': get_random_image('frost guard')}
            ]
        elif 'ice' in description.lower():
            affiliate_links = [
                {'title': 'Get Ice Scraper Mitt', 'url': 'https://amzn.to/4bViwlr?tag=sarath04c-21', 'image': get_random_image('ice scraper')}
            ]
        elif 'sunrise' in description.lower():
            affiliate_links = [
                {'title': 'Buy Sunrise Alarm Clock', 'url': 'https://amzn.to/3R4hV9f?tag=sarath04c-21', 'image': get_random_image('sunrise alarm clock')}
            ]
        elif 'sunset' in description.lower():
            affiliate_links = [
                {'title': 'Grab this wonderful sunset lamp ,Have an awesome Evening!', 'url': 'https://amzn.to/3KhMg08?tag=sarath04c-21', 'image': get_random_image('sunset lamp')}
            ]
        elif 'moon' in description.lower():
            affiliate_links = [
                {'title': 'Make some moonlight dinner with your Love!! ,Grab an interestind Moon lamp', 'url': 'https://www.amazon.in/REFULGIX-3D-Moon-Rechargeable-Lamp/dp/B09NRBHC8C?crid=I3LLS1C75DEO&dib=eyJ2IjoiMSJ9.XhmGN61bn8BMYR9H0V7VOfBMlvZbIa4G4T64jbXlGF6LgZzLur3E9LzRnEzmMopk1dm6YeTPD602UrLP6Ux4Sf_T45Tx0JMG4jBRC8whu1Qjd1jkQOVRNf5J2yTo4I8eGxh7VrcFpiXh7PuAXnuZqQomfvOLYysHq1Xf5Te5HCoqPCNc5hsYRGYOTkTGanMe-ZrW6YNEkk_yLIg9lFS2R08QQcwKm_1PDn9q_0R3qM_tcFYGvHZdQcHo8A9JMcNjIiCqzZhctFZz_iOmtHp8LCNNkf2rFSMCKBJxQu8SfQg.Sq8DbaU1FwEXS1rUdcyoNNeevuRkvlvzmWV5g42sk_o&dib_tag=se&keywords=moon+lamp&qid=1716880330&sprefix=moon+lamp%2Caps%2C382&sr=8-6&linkCode=ll1&tag=sarath04c-21&linkId=a18a389e72c668d2d035d7beef80fa04&language=en_IN&ref_=as_li_ss_tl', 'image': get_random_image('moon lamp')}
            ]
