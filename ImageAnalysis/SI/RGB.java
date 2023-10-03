import java.awt.Color;

public class RGB {
    public static void main(String[] args) {
        // Crear un objeto Color con componentes RGB (34, 1, 220)
        // Color color = new Color(34, 1, 220);
        // Color color = new Color(255, 255, 255);
        Color color = new Color(0, 0, 0);
        
        // Obtener componentes individuales (R, G, B)
        int red = color.getRed();
        int green = color.getGreen();
        int blue = color.getBlue();
        
        // Obtener el valor RGB como un entero
        int rgbValue = color.getRGB();
        
        // Imprimir los componentes y el valor RGB
        System.out.println("Componente Rojo (R): " + red);
        System.out.println("Componente Verde (G): " + green);
        System.out.println("Componente Azul (B): " + blue);
        System.out.println("Valor RGB: " + rgbValue);
    }
}
