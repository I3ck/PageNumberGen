class PageNumberGen:
    def __init__(self, minpage, maxpage, displayedpages, showmin=True, showmax=True):
        self.minpage = minpage
        self.maxpage = maxpage
        self.displayedpages = displayedpages
        self.showmin = showmin
        self.showmax = showmax

    def get_linear(self, currentpage):
        output = []
        pagesleft = self.displayedpages
        if self.showmin:
            output.append(self.minpage)
            pagesleft -= 1

        if self.showmax:
            pagesleft -= 1

        for i in range(pagesleft):
            output.append(currentpage - pagesleft/2 + i)

        if self.showmax:
            output.append(self.maxpage)

        return output

if __name__ == "__main__":
    test = PageNumberGen(0, 100, 10)
    print test.get_linear(13)





