import unknown_converter
from flask import *
from imgurpython import ImgurClient

CLIENT_ID = "11c33d95d3e8ffe"
CLIENT_SERCRET = "3f81c51cc9611fb18a74b653d26a7126e688e90d"
imgurClient = ImgurClient(CLIENT_ID, CLIENT_SERCRET)


app = Flask(__name__)

@app.route('/unknown/converter')
def index():
	return render_template("index.html")
@app.route('/')
def hello():
	return "ちゃんと動いてるよ！"

@app.route('/unknown/result/',methods=['POST'])
def result():
	text = request.form["TEXT"]

	#記号・数字などがkeyerrorの例外となるので例外処理。
	try:
		if text == "":
			raise ValueError("error!")
		unknown_image = unknown_converter.convert(text)
	except:
		return render_template("result.html", original_text=text, path="https://imgur.com/wAaOKOv.png", status="https://imgur.com/PTaIr4h.png")

	save_path = "./result/converted.png"
	unknown_image.save(save_path)
	imgur_path = imgurClient.upload_from_path(save_path,config=None,anon=None)['link']
	return render_template("result.html", original_text=text, path=imgur_path, status="https://imgur.com/lxvUwyS.png")

if __name__=="__main__":
	app.run()
# imagelink = Client.upload_from_path(imagepath, config=None, anon=True)["link"]
