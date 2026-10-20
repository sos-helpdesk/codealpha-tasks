from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><head><title>My Store</title>
    <style>body{font-family:Arial;background:#f4f4f4;margin:0;text-align:center} header{background:#ff6a00;color:white;padding:20px} .container{display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin:30px} .card{background:white;padding:20px;border-radius:12px;width:200px;box-shadow:0 4px 8px rgba(0,0,0,0.1)} .img-box{background:#eee;padding:20px;border-radius:8px;font-weight:bold} button{background:#222;color:white;border:none;padding:10px;border-radius:6px;width:100%} </style>
    </head><body>
    <header><h1>My E-Commerce Store</h1><p>Task 1 - Complete</p></header>
    <div class="container">
    <div class="card"><div class="img-box">HEADPHONE</div><h3>Wireless Headphone</h3><p>Rs.1999</p><button>Add to Cart</button></div>
    <div class="card"><div class="img-box">WATCH</div><h3>Smart Watch</h3><p>Rs.2999</p><button>Add to Cart</button></div>
    <div class="card"><div class="img-box">BAG</div><h3>Laptop Bag</h3><p>Rs.999</p><button>Add to Cart</button></div>
    <div class="card"><div class="img-box">STAND</div><h3>Mobile Stand</h3><p>Rs.499</p><button>Add to Cart</button></div>
    </div></body></html>
    """
if __name__ == '__main__':
    app.run(debug=True)
