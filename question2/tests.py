import unittest
from dateparse import Date, InvalidDateError, sort_dates


class DateparseTest(unittest.TestCase):
    def setUp(self):
        self.good_dates = ['Jan 31, 1999', 'Feb 28, 2012', 'Mar 1, 2000',
                           'Apr 2, 2001', 'May 10, 2002', 'Jun 5, 2003',
                           'Jul 14, 2006', 'Aug 26, 2011', 'Sep 8, 1492',
                           'Oct 20, 2008', 'Nov 30, 2010', 'Dec 6, 2014']
        
    def testGoodGetDay(self):
        get_day = lambda date: Date(date).get_date().day
        self.assertEqual(map(get_day, self.good_dates),
                         [31, 28, 1, 2, 10, 5, 14, 26, 8, 20, 30, 6])
    
    def testGoodGetMonth(self):
        get_month = lambda date: Date(date).get_date().month
        self.assertEqual(map(get_month, self.good_dates),
                         range(1, 13))
    
    def testGoodGetYear(self):
        get_year = lambda date: Date(date).get_date().year
        self.assertEqual(map(get_year, self.good_dates),
                         [1999, 2012, 2000, 2001, 2002, 2003, 2006, 2011,
                          1492, 2008, 2010, 2014])
    
    def testGetDateStrings(self):
        get_date_string = lambda date: str(Date(date))
        self.assertEqual([get_date_string(date) for date in self.good_dates],
                         self.good_dates)
    
    def testSortDatesAscending(self):
        sorted_dates = ['Sep 8, 1492', 'Jan 31, 1999', 'Mar 1, 2000',
                        'Apr 2, 2001', 'May 10, 2002', 'Jun 5, 2003',
                        'Jul 14, 2006', 'Oct 20, 2008', 'Nov 30, 2010',
                        'Aug 26, 2011', 'Feb 28, 2012', 'Dec 6, 2014']
        self.assertEqual(sort_dates(self.good_dates),
                         sorted_dates)
    
    def testSortDatesDescending(self):
        sorted_dates = ['Sep 8, 1492', 'Jan 31, 1999', 'Mar 1, 2000',
                        'Apr 2, 2001', 'May 10, 2002', 'Jun 5, 2003',
                        'Jul 14, 2006', 'Oct 20, 2008', 'Nov 30, 2010',
                        'Aug 26, 2011', 'Feb 28, 2012', 'Dec 6, 2014']
        self.assertEqual(sort_dates(self.good_dates, reverse=True),
                         list(reversed(sorted_dates)))
        
    def testBadDates(self):
        # Test for bad month
        self.assertRaises(InvalidDateError, Date, 'Jon 5, 2012')
        # Test for good format but invalid date
        self.assertRaises(InvalidDateError, Date, 'Feb 29, 2013')
        # Test for bad format
        self.assertRaises(InvalidDateError, Date, '8-6-1999')
        # Test to ensure validation works
        # We don't want day == 20 since it was omitted
        self.assertRaises(InvalidDateError, Date, 'Oct 2008')
        # Test for just plain bad data!
        # Using comma in about the right spot
        self.assertRaises(InvalidDateError, Date, 'Hello, world')


if __name__ == "__main__":
    unittest.main()