import requests

def test_server():
    port = 8085
    host = 'localhost'
    
    try:
        response = requests.get(f"http://{host}:{port}/", timeout=25)
        
        print(f"Response content: {response.text}")
        
        if response.status_code == 200:
            print(f"success: 200")
        else:
            print(f"fail: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    test_server()