from main import app
from db import db

@app.before_first_request
def create_table():
    db.create_all()
    
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    
    app.run(port=5000, debug= True)