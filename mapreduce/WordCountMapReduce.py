from functools import reduce
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFreqCount(MRJob):

    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)
        
    def combiner_count_words(self, word, counts):
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        yield None, (sum(counts), word)

    def reducer_sort_count(self, _, word_pairs):
        # Just the top 10 words
        for count, key in sorted(word_pairs, reverse=True)[:10]:
            yield ('%020d' % int(count), key)

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_get_words,
                combiner=self.combiner_count_words,
                reducer=self.reducer_count_words    
                ),
            MRStep(
                reducer=self.reducer_sort_count
            )
        ]


if __name__ == '__main__':
    MRWordFreqCount.run()