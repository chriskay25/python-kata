def rgb_to_hex(r, g, b):
    colors = {'red': r, 'green': g, 'blue': b}
    for c in colors:
        if colors[c] > 255: colors[c] = 255
        if colors[c] < 0: colors[c] = 0
        colors[c] = hex(colors[c])[2:].upper()
        if colors[c] == '0': colors[c] = colors[c] + '0'
        if len(colors[c]) == 1 and colors[c] != '0':
            colors[c] = '0' + colors[c]
    return colors['red'] + colors['green'] + colors['blue']

rgb_to_hex(148, 0, 211)
rgb_to_hex(255,255,300)

# WAY faster methods:

# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))

# OR

# def rgb(r, g, b):
#     clamp = lambda x: max(0, min(x, 255))
#     return "%02X%02X%02X" % (clamp(r), clamp(g), clamp(b))