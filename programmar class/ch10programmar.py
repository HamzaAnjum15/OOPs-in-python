class programmar:
    company="microsoft"
    def __init__(self,name,job):
       self.name=name
       self.job=job
    def info(self):
       print(f"the name of the programmar is {self.name} and his job is {self.job}")

hamza=programmar("hamza","data science")
ali=programmar("ali","artificial intelligence")
hamza.info()
ali.info()