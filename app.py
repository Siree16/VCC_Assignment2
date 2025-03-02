from flask import Flask, request
import time

app = Flask(__name__)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route("/fib")
def fib():
    n = int(request.args.get("n", 30))
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    return f"Fibonacci({n}) = {result}, Time taken: {end_time - start_time:.2f} seconds"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
