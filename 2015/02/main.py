def parse_input():
    content = open("input.txt").read()
    content = content.split('\n')
    measures = []
    for row in content:
        rc = row.split('x')
        measures.append(rc)

    return measures


def calc_box_wrapsurface(row):
    surfaces_base = [int(row[0]) * int(row[1]), int(row[1]) * int(row[2]), int(row[0]) * int(row[2])]
    smallest_surface = min(surfaces_base)
    total_surface = sum(double_array_value(surfaces_base)) + smallest_surface
    return total_surface


def double_array_value(val):
    res = []
    for el in val:
        res.append(el * 2)
    return res


if __name__ == '__main__':
    measures = parse_input()
    total_surfaces = []
    for measureRow in measures:
        total_surfaces.append(calc_box_wrapsurface(measureRow))
    print(sum(total_surfaces))
