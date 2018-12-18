if self.bounds[0] <= refIdx <= self.bounds[1]:
    if (refIdx >= 2):
        # need only use the positive array
        if (refIdx + 2 <= self.bounds[1]):
            p = self.state[1][refIdx - 2: refIdx + 3]
        else:
            # requires padding on the right
            p = self.state[1][refIdx - 2:]
            p += [0] * ( 5 -len(p) )
    elif -2 <= refIdx <= 1:
        # requires information from both positive and negative arrays
        # check if within bounds
        if refIdx - 2 > self.bounds[0] and refIdx + 2 <= self.bounds[1]:
            # within bounds, can just generate
            p = self.state[0][:abs(refIdx - 1)][::-1] # reverse it
            p += self.state[1][:refIdx + 3]
        elif refIdx - 2 > self.bounds[0]:
            # within lower, but not upper bound
            # upper bound must be in the positive array as initialState is positive
            p = self.state[0][:abs(refIdx - 1)][::-1] # reverse it
            p += self.state[1][0:]
            p += [0] * ( 5 -len(p) )
        elif refIdx + 2 <= self.bounds[1]:
            # within upper bound, but not lower bound
            if self.bounds[0] >= 0:
                # we just need to add the negative array
                p = [0] * abs(refIdx - 2)
                p += self.state[1][:refIdx + 3]
            else:
                # the bound is within the negative numbers
                p = [0] * abs(refIdx - 2 - self.bounds[0])
                p += self.state[0][:abs(self.bounds[0]) - 1][::-1]
                p += self.state[1][:refIdx + 3]
        else:
            # not within any bound
            # lower bound must be <= 0
            if self.bounds[0] >= 0:
                # we just need to add the negative array
                p = [0] * abs(refIdx - 2)
                p += self.state[1][:refIdx + 3]
            else:
                # the bound is within the negative numbers
                p = [0] * abs(refIdx - 2 - self.bounds[0])
                p += self.state[0][:abs(self.bounds[0]) - 1][::-1]
                p += self.state[1][:refIdx + 3]
    elif refIdx <= -3:
        # only in the negative array
        pass
else:
    print("Uncaught index {}, bounds = [{}, {}]".format(refIdx, self.bounds[0], self.bounds[1]))
    quit()
