a = '''PGRpdiBkaXI9Imx0ciI+dnLomZrmi5/kuJbnlYzvvIzloavlhYXkurrlj6PotYTmupDjgII8YnI+CjwvZGl2PjxkaXYgZGlyPSJsdHIiPjxicj4KPC9kaXY+PGRpdiBkaXI9Imx0ciI+PGJyPgo8L2Rpdj48ZGl2IGRpcj0ibHRyIj48YnI+CjwvZGl2PjxkaXYgY2xhc3M9Indwc19zaWduYXR1cmUiPuWPkeiHquaIkeeahOWwj+exs+aJi+acujwvZGl2Pg==
'''

import base64
b = base64.b64decode(a.encode("ascii"))
print(b)
