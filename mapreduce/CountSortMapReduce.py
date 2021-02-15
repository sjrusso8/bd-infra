from mrjob.job import MRJob
from mrjob.step import MRStep

class JobBalanceBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_jobs,
                    reducer=self.reducer_sum_balance),
            MRStep(reducer=self.reducer_sorted_output)
        ]
    
    def mapper_get_jobs(self, _, line):
        (age, jobs,*_) = line.split(";")
        yield jobs, age
    
    def reducer_sum_balance(self, jobs, age):
        yield sum(int(age)), jobs

    def reducer_sorted_output(self, age, jobs):
        for job in jobs:
            yield job, age

if __name__ == '__main__':
    JobBalanceBreakdown.run()
    
