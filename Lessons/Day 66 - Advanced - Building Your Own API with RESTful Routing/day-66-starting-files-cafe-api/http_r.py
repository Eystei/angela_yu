from requests import request


def api(a):
    if a == 'all':
        payload = 'loc=Shoreditch'
        url = f"http://127.0.0.1:5000/all?{payload}"
        response = request(method="GET", url=url)
        print(response.text)

    if a == "update":
        response = request(method="PATCH", url='http://127.0.0.1:5000/update-price/1111?new_price=100')
        print(response.status_code)

    if a == 'delete':
        response = request(method="DELETE", url='http://127.0.0.1:5000/report-closed/25?api-key=TopSecretAPIKey')
        print(response.json())


if __name__ == '__main__':
    api('delete')
