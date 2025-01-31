import requests

ENDPOINT = " https://api.thecatapi.com"

# HEADERS = {
#   "x-api-key": live_r9eWrey9H1MTxJ3hvR3NM3ycGccvyX837JdYWGfG0vWEr4sW26WOVtSjPk77tN8C 
# }

def test_get_resp():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    


def test_get_random_cat_image():
    response = requests.get(ENDPOINT + "/v1/images/search")
    assert response.status_code == 200 
    assert "id", "hobby"
    data = response.json()
    print(data)

#def test_get_5_random_cat_images():
 #   response = requests.get(ENDPOINT + "/v1/images/search?limit=5")
 #   assert response.status_code == 200 

  #  data = response.json()
  #  print(data)

#def test_get_11_random_cat_images():
 #   response = requests.get(ENDPOINT + "/v1/images/search?limit=11")
 #   assert response.status_code == 200 

#def test_get_20_random_cat_images():
 #   response = requests.get(ENDPOINT + "/v1/images/search?limit=20")
 #  assert response.status_code == 200 

  #  data = response.json()
  #  print(data)


