from flask import Flask, render_template
from dotenv import load_dotenv
import os
from database.db import init_db, close_db
from routes.idea_routes import ideas_bp

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_secret_key')

    app.config['DATABASE'] = os.getenv(
        'DATABASE', 
        os.path.join(app.root_path, 'database', 'app.db')  
    )

    os.makedirs(os.path.dirname(app.config['DATABASE']), exist_ok=True)

    app.teardown_appcontext(close_db)
    app.register_blueprint(ideas_bp)

    with app.app_context():
        init_db()

    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
