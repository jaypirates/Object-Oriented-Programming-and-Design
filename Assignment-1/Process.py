class Process:
    def __init__(self):
        self.name = None
        self.owner = None
        self.PID = None
        self.number_of_threads = None
        self.percent_of_cputime = None
        self.total_of_cputime = None

    def Add(self):
        self.name = input("Name of Process : ")
        self.owner = input("Name of Owner : ")
        self.PID = input("PID : ")
        self.number_of_threads = input("Number of Threads : ")
        self.percent_of_cputime = input("Percent of CPU time : ")
        self.total_of_cputime = input("Total time of CPU : ")

    def display_all_attributes(self):
        print("Name of Process : " + self.name)
        print("Name of Owner : " + self.owner)
        print("PID : " + self.PID)
        print("Number of Threads : " + self.number_of_threads)
        print("Percent of CPU time : " + self.percent_of_cputime)
        print("Total time of CPU : " + self.total_of_cputime)
