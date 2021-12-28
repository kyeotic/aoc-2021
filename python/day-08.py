import os

file_path = '../inputs/day-08.txt'


def part1():
    entries = get_input()

    def is_match(encoded_digit):
        l = len(encoded_digit)
        return l == 2 or l == 4 or l == 3 or l == 7

    result = 0
    for inputs, outputs in entries:
        result += len([x for x in outputs if is_match(x)])

    return result


def part2():
    entries = get_input()

    return sum([int(get_output(build_digit_map(entry), entry[1])) for entry in entries])


def build_digit_map(entry):
    # S   = signal

    # BASIC
    # A   = S in 7 that is NOT in 4
    # C,F = S in 4 that IS in     1
    # B,D = S in 4 that is NOT in 7
    # E,G = S in 8 that is NOT in 4 && 7

    # ADVANCED
    # 0   = NOT D    ; has all - XOR B,D. Identifies D, ergo B
    # 2   = NOT B,F  ; has all - B and XOR C,F. Identifies F (not in 1), ergo C
    # 3   = NOT B,E  ; has all - B & E; Identifies E
    # 5   = NOT C,E  ; Identifies C
    # 6   = NOT C
    # 9   = NOT E

    # C   = S
    inputs, outputs = entry
    digit_map = {}  # actual digit -> input segments
    segment_map = {}  # actual segment - input segment

    # known based on length
    digit_map['1'] = get_only(n for n in inputs if len(n) == 2)
    digit_map['4'] = get_only(n for n in inputs if len(n) == 4)
    digit_map['7'] = get_only(n for n in inputs if len(n) == 3)
    digit_map['8'] = get_only(n for n in inputs if len(n) == 7)

    all_segments = digit_map['8']

    def all_except(input, missing):
        # check that input has all_segments except for those in missing
        remaining = sub_digits(all_segments, missing)
        return all(s in input for s in remaining)

    # Basic
    segment_map['a'] = get_only(s for s in digit_map['7']
                                if s not in digit_map['4'])

    c_f = ''.join(s for s in digit_map['4'] if s in digit_map['1'])
    b_d = ''.join(s for s in digit_map['4'] if s not in digit_map['7'])
    e_g = ''.join(s for s in digit_map['8']
                  if s not in digit_map['7'] and s not in digit_map['4'])

    # Advanced

    digit_map['0'] = get_only(n for n in inputs if len(n) == 6
                              and all_except(n, b_d))
    segment_map['b'] = get_only(s for s in digit_map['0'] if s in b_d)
    segment_map['d'] = sub_digits(b_d, segment_map['b'])

    # 2
    digit_map['2'] = get_only(n for n in inputs if len(n) == 5
                              and all_except(n, segment_map['b'] + c_f))
    segment_map['f'] = get_only(s for s in digit_map['1']
                                if s not in digit_map['2'])
    segment_map['c'] = sub_digits(c_f, segment_map['f'])

    # 9
    digit_map['9'] = get_only(n for n in inputs if len(n) == 6
                              and all_except(n, e_g))
    segment_map['e'] = sub_digits(e_g, digit_map['9'])
    segment_map['g'] = sub_digits(e_g, segment_map['e'])

    # remaining
    digit_map['3'] = get_only(n for n in inputs if len(n) == 5 and
                              all_except(n, segment_map['b'] + segment_map['e']))

    digit_map['5'] = get_only(n for n in inputs if len(n) == 5 and all_except(
        n, segment_map['c'] + segment_map['e']))

    digit_map['6'] = get_only(
        n for n in inputs if len(n) == 6 and all_except(n, segment_map['c']))

    # invert to get a map of input_segments to actual_digit
    return {sort_string(v): k for k, v in digit_map.items()}


def has_digits(signal, predicate):
    return all(s for s in signal if s in predicate)


def sub_digits(original, list_to_remove):
    sc = set(list_to_remove)
    return ''.join([n for n in original if n not in sc])


def get_output(digit_map, outputs):
    return ''.join(digit_map[''.join(sorted(digit))] for digit in outputs)


def get_only(gen):
    l = list(gen)
    if len(l) != 1:
        raise IndexError(f'generator had other than 1 option {l}')
    return l[0]


def sort_string(val):
    return ''.join(sorted(val))


def get_input():
    input = open(os.path.join(os.path.dirname(__file__),
                              file_path), 'r').read().splitlines()
    results = []
    for entry in input:
        signals, outputs = entry.split('|')
        results.append(
            ([sort_string(signal.strip()) for signal in signals.split()],
             [sort_string(output.strip()) for output in outputs.split()])
        )

    # print(results)
    return results


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))
