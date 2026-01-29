import math

def main():
	n = 1000

	x_0 = float(0.0)
	x_1 = float(2.0)

	dx = (x_1 - x_0) / (n - 1)

	print(f"{'x':>10} {'sin(x)':>15}")
	print("-" * 25)

	x = x_0
	for i in range(n):
		print(f"{x:10.6f} {math.sin(x):15.8f}")
		x += dx

main()