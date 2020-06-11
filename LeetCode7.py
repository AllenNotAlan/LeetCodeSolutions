#Given a 32-bit signed integer, reverse digits of an integer.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = x * -1
            s = str(x)
            new_s = int("".join(list(reversed(s)))) * -1
        else:
            s = str(x)
            new_s = int("".join(list(reversed(s))))

        if new_s > (2**31 - 1) or new_s < (-(2**31 - 1)):
            return 0

        return new_s

    print(10 + reverse(1, 120))
