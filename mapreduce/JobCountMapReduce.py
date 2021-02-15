from mrjob.job import MRJob
from mrjob.step import MRStep

class JobBreakdown(MRJob):
        def steps(self):
            return [
                    MRStep(mapper=self.mapper_get_jobs,
                            reducer=self.reducer_count_jobs)
            ]

        def mapper_get_jobs(self, _, line):
                (_,job, *_) = line.split(';')
                yield job, 1

        def reducer_count_jobs(self, key, values):
                yield key, sum(values)

if __name__ == '__main__':
    JobBreakdown.run()
