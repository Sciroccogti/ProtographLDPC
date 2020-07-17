import itertools

from TannerGraph import TannerGraph


class Identity(TannerGraph):

    def __init__(self, args):

        TannerGraph.__init__(self, args)

        # args describes length of identity matrix
        if len(args) == 1:
            for i in range(int(args[0])):
                self.tanner_graph[i] = [i]

        # returns a graph who's matrix contains an entry in the location arg[i] of column i for all columns.
        elif len(args) > 1:
            for i in range(len(args)):
                self.tanner_graph[i] = [args[i]]


    @staticmethod
    def permutation_set(width):

        indices = [i for i in range(width)]
        permutations = list(itertools.permutations(indices))

        permutation_set = []
        for permutation in permutations:
            permutation_set.append(Identity(permutation))

        return permutation_set