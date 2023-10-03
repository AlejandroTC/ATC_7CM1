from PIL import ImageColor

# Crear un objeto de color con los componentes R, G y B
color = (34, 1, 220)

# Obtener el valor RGB
rgb_value = ImageColor.getcolor(f"rgb{color}", "RGB")
print(f"Valor RGB: {rgb_value}")
print(f"Valor entero de RGB: {int(rgb_value)}")