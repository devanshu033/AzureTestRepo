from flask import Flask
import cx_Oracle
import pytesseract
import cv2

app = Flask(__name__)

@app.route('/test')
def hello_world():
  return "Hello, World!6844"

if __name__ == '__main__':
  app.run(debug=True)
