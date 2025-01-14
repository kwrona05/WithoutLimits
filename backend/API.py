import cv2
import io
from flask import Flask, jsonify, request
@app.route('/api/obstacle', methods=['POST'])

def obstacle_detection():
    file = request.files('image')
    img = cv2.imdecode(np.fromstring(file.read(), np.unit8), cv2.IMREAD_COLOR)

    result = {'message': 'Obstacle detected'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)