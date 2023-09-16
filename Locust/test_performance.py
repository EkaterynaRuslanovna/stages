from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(5, 10)  # Інтервал між запитами (в секундах)

    # Запит POST
    @task(1)
    def post_resource(self):
        self.client.post("/pet", json={"id": 300594,
                                       "category": {
                                           "id": 1,
                                           "name": "string"
                                       },
                                       "name": "VASILIY",
                                       "photoUrls": [
                                           "string"
                                       ],
                                       "tags": [
                                           {
                                               "id": 0,
                                               "name": "string"
                                           }
                                       ],
                                       "status": "available"
                                       })

    # Запит GET
    @task(3)
    def get_resource(self):
        self.client.get("/pet/300594")

    # Запит PUT
    @task(2)
    def put_resource(self):
        self.client.put("/pet", json={"id": 300594,
                                      "category": {
                                          "id": 1,
                                          "name": "string"
                                      },
                                      "name": "VASYA",
                                      "photoUrls": [
                                          "string"
                                      ],
                                      "tags": [
                                          {
                                              "id": 0,
                                              "name": "string"
                                          }
                                      ],
                                      "status": "sold"
                                      })

    # Запит DELETE
    @task(4)
    def delete_resource(self):
        self.client.delete("/pet/300594", headers={'api_key': 'special-key'})
