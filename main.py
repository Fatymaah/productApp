from flask import (Flask,
                   render_template,
                   request,
                   make_response,
                   redirect
                   )              
from models import product
app = Flask('app')
product.initialize()

@app.route('/')
def index():
 
  goods_number = product.Product.select()
  objects = []
  for good in goods_number:
    good_item ={

      'heading': good.heading,
      'subtitle': good.subtitle,
      'thumbnail_link': good.thumbnail_link,
      'fullimage_link' :good.fullimage_link
    }
    objects.append(good_item)
    
  return render_template("index.html",images=objects)


app.run(host='0.0.0.0', port=8080)