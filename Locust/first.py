from locust import User, task

class FirstTest(User):
    @task(1)
    def first(self):
        print("jndcjklsdncs")

    @task(2)
    def second(self):
        print("dvfdbdb fdvbg fdv fvb gfb ")