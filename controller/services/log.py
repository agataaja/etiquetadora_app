import datetime

class Log:

    def printLog(self, txt):
        self.current_date = datetime.datetime.now()
        self.text_date = '{}_{}_{}'.format(self.current_date.day, self.current_date.month, self.current_date.year)
        print('\n--------------'+ self.current_date.strftime("%d/%m/%Y  %H:%M:%S")+ '  -> ' + txt)       
