#### Function that takes prime, unbalanced direction, and polynomial and returns a list of tuples
####

def poly_to_rows(p, unbal_dir, coeffs):
	hp = (p + 1) // 2
	denoms = [-unbal_dir, unbal_dir - 1, unbal_dir * (1 - unbal_dir)]
	prod_eval = [pow(denom % p, -1, p) for denom in denoms]

	dirs = [0, 1, unbal_dir]
	const_quad_eval = [sum([x * y for x, y in zip(coeffs[:3], [1, d, d*d])]) for d in dirs]

	line_sums = [[0 for _ in range(3)] for _ in range(hp)]
	line_counts = [[0 for _ in range(p)] for _ in range(3)] 

	point_sums = [[0 for _ in range(p)] for _ in range(hp)]
	point_counts = [[0 for _ in range(p)] for _ in range(p)]

	for k in range(3):
		for l in range(p):
			val = (prod_eval[k] * (const_quad_eval[k] + (coeffs[3] * l * l))) % p

			line_sums[0][k] += val
			line_counts[k][val] += 1

			point_sums[0][l] += val
			point_counts[l][val] += 1

	for i in range(1, hp):
		for j in range(3):
			line_sums[i][j] = line_sums[i - 1][j] + p - p * line_counts[j][p - i]

	for i in range(1, hp):
		for j in range(p):
			point_sums[i][j] = point_sums[i - 1][j] + 3 - p * point_counts[j][p - i]

	return [tuple([x] + coeffs + [unbal_dir] + y + z) for x, y, z in zip(range(1, hp), line_sums[1:], point_sums[1:])]
