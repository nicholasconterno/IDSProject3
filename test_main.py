
from main import load_data, get_mean, get_median,get_stdev,get_summary_statistics
import unittest
class TestDataMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv'
        cls.df = load_data(cls.url)

    def test_get_mean(self):
        mean_rating = get_mean(self.df, 'Rotten Tomatoes %')
        self.assertTrue(isinstance(mean_rating, float))

    def test_get_median(self):
        median_rating = get_median(self.df, 'Rotten Tomatoes %')
        self.assertTrue(isinstance(median_rating, float))

    def test_get_stdev(self):
        stdev_rating = get_stdev(self.df, 'Rotten Tomatoes %')
        self.assertTrue(isinstance(stdev_rating, float))

if __name__ == '__main__':
    unittest.main()
