from app import create_app
import os

# Disable HTTPS for market testing
os.environ['FLASK_DEBUG'] = 'True'

app = create_app()

if __name__ == '__main__':
    # Market testing ke liye simple server
    app.run(debug=True, host='127.0.0.1', port=5001)