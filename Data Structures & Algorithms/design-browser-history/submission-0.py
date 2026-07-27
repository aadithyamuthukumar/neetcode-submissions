class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        

    def visit(self, url: str) -> None:

        urlNode = Node(url)
        urlNode.prev = self.curr
        self.curr.next = urlNode
        self.curr = urlNode

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next        
            steps -= 1
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)