import datetime
from functools import partial

def sort_dates(dates, cmp=None, key=None, reverse=False):
    """Takes an iterable of date strings in the format of 'mmm d, yyyy' and
    returns a list of date strings sorted by date.    
    cmp, key, and reverse follow the same convention as the sorted() function
    """
    return map(str, sorted(map(Date, dates),
                           cmp=cmp, key=key, reverse=reverse))

class Date(object):
    """Date proxy class to handle date comparisons for date strings
    in the format of 'mmm d, yyyy'
    """
    
    MONTHS = { k:v for v, k in
                enumerate(('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'), 1) }
    
    def __init__(self, date_str):
        """Takes a date_str in the format 'mmm d, yyyy'
        """
        self._date_str = date_str
        self._date_val = self._validate()
    
    def get_date(self):
        """Return internal datetime.date value"""
        return self._date_val
    
    def _validate(self):
        """Used to validate self._date_str format and generate self._date_val
        raises InvalidDateError for an invalid self._date_str
        """
        error = partial(InvalidDateError, self._date_str)
        if ',' not in self._date_str[5:7]:
            raise error('Comma not present in expected location.')
        elif len(self._date_str) not in (11, 12):
            raise error('Invalid length - must be 11 or 12 characters.')
        else:
            try:
                return datetime.date(self._get_year(),
                                     self._get_month(),
                                     self._get_day())
            except Exception as e:
                raise error(repr(e))
    
    def _get_day(self):
        """Returns int day value from self._date_str"""
        if self._date_str[5] == ',':
            return int(self._date_str[4])
        else:
            return int(self._date_str[4:6])
    
    def _get_month(self):
        """Returns int month value from self._date_str"""
        return self.MONTHS[self._date_str[:3]]
    
    def _get_year(self):
        """Returns int year value from self._date_str"""
        return int(self._date_str[-4:])
    
    def __str__(self):
        """Returns self._date_str for str representation"""
        return self._date_str
    
    def __repr__(self):
        """Returns repr of self._date_str"""
        return repr(self._date_str)
    
    # Use comparisons from internal _date_val for sorting, etc.
    
    def __eq__(self, other):
        return self._date_val.__eq__(other._date_val)
    
    def __ne__(self, other):
        return self._date_val.__ne__(other._date_val)
    
    def __lt__(self, other):
        return self._date_val.__lt__(other._date_val)
    
    def __le__(self, other):
        return self._date_val.__le__(other._date_val)
    
    def __gt__(self, other):
        return self._date_val.__gt__(other._date_val)
    
    def __ge__(self, other):
        return self._date_val.__ge__(other._date_val)

class InvalidDateError(Exception):
    def __init__(self, date_str, extra_message=None):
        message = ('Invalid date string %s, must be in the format of '
                   '"mmm d, yyyy"' % repr(date_str))
        if extra_message:
            message += ': ' + extra_message
        super(InvalidDateError, self).__init__(message)

    