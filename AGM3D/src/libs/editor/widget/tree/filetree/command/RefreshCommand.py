

class RefreshCommand():
    
    def __init__(self, tree):
        self.tree = tree
        
    def execute(self):
        print self.tree
        item = self.tree.currentItem()
        self.tree.refresh(item)
        