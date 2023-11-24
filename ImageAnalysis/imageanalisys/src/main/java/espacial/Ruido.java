package espacial;

import java.awt.Color;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.util.Random;

import com.imageanalisys.HerramientasImagen;

/*
 * ToDo: Agregar ruido sustrativo, mezclado
 * Sustrativo normal
 * Mezclado es agegar primero el aditivo y luego sustrativo
 * Quitar el ruido con el metodo de convolucion
 * Investigar el metodo para guardar una imagen en archivo
 * 
 */

public class Ruido {
    public static Image agergarRuidoAditivo(Image original, double por){
        Random ran = new Random();
        BufferedImage bi = HerramientasImagen.toBufferedImage(original);
        // double aux = por/100;
        int cp = (int) ((por/100)*(bi.getHeight()*bi.getWidth()));
        Color aditivo = new Color(255, 255, 255);
        int x, y;
        for(int j=0; j<cp; j++){
            //posicion aleatoria dentro de la imagen
            x = ran.nextInt(bi.getWidth());
            y = ran.nextInt(bi.getHeight());
            bi.setRGB(x, y, aditivo.getRGB());
        }
        return  null;
    }
}
