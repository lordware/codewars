class FileMaster:
    def __init__(self, filepath):
        self.filepath = filepath
        self.split = filepath.split("/")

    def extension(self):
        return self.split[-1:][0].split(".")[1]

    def filename(self):
        return self.split[-1:][0].split(".")[0]

    def dirpath(self):
        res = ""
        for x in self.split:
            if x == self.split[-1:][0]:
                return res
            else:
                res += x + "/"
