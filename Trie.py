# Class trie
# when you are adding a vertex
# you are assigning it an integer value, which is a number_of_vertices + 1
# for instance, suppose you are adding 'a' and number_of_vertices = 4
# then this vertex will have a number 5 assigned to it
# I am storing edges in a dictionary since if the alphabet is large(which can be a case)
# dict(unordered map) will give me a lookup for O(1) in average
#     so for adding a word, I will spend only O(length of the word)
# same for checking if it is in
# Terminal list is used for answering if this vertex is the end of some string
class Trie:
    number_of_vertices = 0
    edges = [dict()]
    terminal = [0]

    def __add_helper(self, cur, vertex, cur_string, size_of_the_string):  # recursive function
        if cur == size_of_the_string:  # we are in the end of the string
            self.terminal[vertex] = True  # this vertex is the end of the string
        else:
            to = cur_string[cur]  # our next character
            if to not in self.edges[vertex]:  # if there is no edge from current to next vertex, we have to add it
                self.number_of_vertices += 1
                self.terminal.append(False)
                self.edges.append(dict())
                self.edges[vertex][to] = self.number_of_vertices
            self.__add_helper(cur + 1, self.edges[vertex][to], cur_string, size_of_the_string)  # go to the next vertex

    def add(self, user_string):
        self.__add_helper(0, 0, user_string, len(user_string))

    def __check_helper(self, cur, vertex, cur_string, size_of_the_string):  # recursive function
        if cur == size_of_the_string:  # we are in the end of the string
            return self.terminal[vertex]
        else:
            to = cur_string[cur]  # our next character
            if to not in self.edges[vertex]:  # if there is no edge from current vertex to the next
                return False  # There is no word in this trie
            return self.__check_helper(cur + 1, self.edges[vertex][to], cur_string, size_of_the_string)

    def check(self, user_string):
        return self.__check_helper(0, 0, user_string, len(user_string))


if __name__ == "__main__":
    a = Trie()
    a.add("a")
    a.add("ab")
    a.add("abcd")
    print(a.check("abc"))
    a.add("abc")
    print(a.check("a"))
    print(a.check("ab"))
    print(a.check("abc"))
    print(a.check("abcd"))
