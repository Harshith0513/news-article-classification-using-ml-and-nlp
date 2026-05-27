import pickle
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

import joblib

from classifier import predict

class NewsClassifierHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/classify':
            # Read the length of the data from headers
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')

            # Parse the form data
            form_data = parse_qs(post_data)
            news_text = form_data.get("news_article", [""])[0]

            # Predict category
            category = str(predict(news_text))
            print('category found')
            print('category' + category)

            # Send response
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(category.encode())

    def do_GET(self):
        if self.path == "/":
            self.path = "/templates/index2.html"
        return super().do_GET()

    def predict_2(self, text):
        loaded_model = joblib.load(open('/Users/mr_iconic_/PycharmProjects/PythonProject1/News Article /Models/final_news_cv_vectorizer.pkl', 'rb'))
        vectorizer = joblib.load(open('/Users/mr_iconic_/PycharmProjects/PythonProject1/News Article /Models/newsclassifier_RFOREST_model.pkl','rb'))
        transformed_text = vectorizer.transform([text]).toarray()
        prediction = loaded_model.predict(transformed_text)
        print(str(prediction))
        return prediction[0]

if __name__ == "__main__":
    PORT = 8000
    server = HTTPServer(("localhost", PORT), NewsClassifierHandler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()
