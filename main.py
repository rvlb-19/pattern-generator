import itertools
import string

def generate_permutations(charset='', n=1):
    return list(map(lambda x: ''.join(x), itertools.product(charset, repeat=n)))

def generate_str(target, source):
    return target.format(source)

def execute(patterns=[], charset='', permutations_qnt=1):
    permutations = []
    for i in range(permutations_qnt):
        permutations += generate_permutations(charset, n=i+1)

    with open('output.txt', mode='w') as f:
        for t in patterns:
            for s in permutations:
                f.write(generate_str(t, s) + '\n')

if __name__ == '__main__':
    PATTERNS = ['{}something.com']
    CHARSET = string.ascii_lowercase
    PERMUTATIONS_QNT = 3
    execute(patterns=PATTERNS, charset=CHARSET, permutations_qnt=PERMUTATIONS_QNT)