from mrjob.job import MRJob
from mrjob.step import MRStep

class AgeBreakdown(MRJob):
        def steps(self):
            return [
                    MRStep(mapper=self.mapper_get_ages,
                            reducer=self.reducer_count_ages)
            ]

        def mapper_get_ages(self, _, line):
                (age, *_) = line.split(';')
                yield age, 1

        def reducer_count_ages(self, key, values):
                yield key, sum(values)

if __name__ == '__main__':
    AgeBreakdown.run()
