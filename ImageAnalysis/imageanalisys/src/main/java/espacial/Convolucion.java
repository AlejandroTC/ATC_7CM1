package espacial;

import java.awt.Image;
import java.awt.image.BufferedImage;

/*
 * ToDo: tenemos que ddeterminar el divisior
 * offset: es un valor que se añade al resultante
 */

public class Convolucion{
    //Mascara de deteccion de bordes
    BufferedImage ImagenOriginal;

    public Convolucion(BufferedImage ImagenOriginal){
        this.ImagenOriginal = ImagenOriginal;
    }

    //Convolucion simple
    public Image convolucionar(int[][] mascara, int div){
        
        return null;
    }
}