class Algorithm: 
    
    def finished(self):
        """Check if the dataset is sorted. 
        
        Return True if the dataset is sorted. 
        Return False if the dataset is not sorted."""

        for i in range(len(self.dataset) - 1): 
            a = self.dataset[i].value
            b = self.dataset[i+1].value
            if not a <= b: 
                return False
        return True
