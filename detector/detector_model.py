from tensorflow.python.keras.preprocessing import image
from profession_detector import settings
import numpy as np


def detection(img_obj):

	def preprocess_input(x):
		x *= (1. / 255)
		return x

	def decode_predictions(preds, top, CLASS_INDEX):
		results = []
		for pred in preds:
			top_indices = pred.argsort()[-top:][::-1]
			for i in top_indices:
				each_result = {}
				each_result['prof'] = CLASS_INDEX[str(i)].title()
				each_result['accu'] = int(pred[i] * 100)
				results.append(each_result)
		return results

	def run_inference(model,picture):
		Output_Dict = {
			"9" : "waiter",
			"6" : "mechanic",
			"2" : "engineer",
			"4" : "firefighter",
			"0" : "chef",
			"5" : "judge",
			"7" : "pilot",
			"8" : "police",
			"3" : "farmer",
			"1" : "doctor"
		}

		image_to_predict = image.load_img(picture, target_size=(224, 224))
		image_to_predict = image.img_to_array(image_to_predict, data_format="channels_last")
		image_to_predict = np.expand_dims(image_to_predict, axis=0)

		image_to_predict = preprocess_input(image_to_predict)

		prediction = model.predict(x=image_to_predict, steps=1)

		predictiondata = decode_predictions(prediction, top=int(3), CLASS_INDEX=Output_Dict)
		
		return predictiondata

	picture = f'{img_obj.image.url[1:]}'
	results = run_inference(settings.model,picture)
	
	return results