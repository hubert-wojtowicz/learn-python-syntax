class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud["pyThOn"] = 10
print(len(cloud))
cloud.add("Python")
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.add("pythons")


for tag in cloud:
    print(tag)

print(cloud.__dict__)  # private member still acessible
print(cloud.__tags)  # this is private