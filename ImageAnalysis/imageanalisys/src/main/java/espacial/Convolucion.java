package espacial;

import java.awt.Color;
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
        Color nuevo;
        for (int x=0; x < this.ImagenOriginal.getWidth();x++)
        {
            for(int y=0; y < this.ImagenOriginal.getHeight(); y++){
                int rgb = convolucionar(x, y, mascara, div);
                nuevo = new Color(rgb);
                this.ImagenOriginal.setRGB(x, y, nuevo.getRGB());
            }
        }
        return null;
    }

    private int convolucionar(int x, int y, int[][] mascara, int div) {
        // for (int j=0; j < mascara.length ; j++ ){
        //     for (int m=0; m < mascara.length ; m++){
        //         //verificar si la mascara es diferente a 0
        //         if(mascara[j][m] != 0){
        //             //
        //         }
        //     }
        // }
        Color aux;
        int aR=0, aG=0, aB=0;
        for (int j=0; j<9; j++)
        {
            int rgb = obtenerRGB(x, y, j);
            if(rgb != 0)
            {
                aux = new Color(rgb);
                aR+=aux.getRed()*mascara[j][0];
                aG+=aux.getGreen()*mascara[j][0];
                aB+=aux.getBlue()*mascara[j][0];

            }
        }
        aR /= div;
        aG /= div;
        aB /= div;
        aux = new Color(aR, aG, aB);
        return aux.getRGB();
    }

    private int obtenerRGB(int x, int y, int j){
        int rgb = 0;
        switch (j) {
            case 0:
                if(x-1<0 || y-1<0) return 0;
                if ((x-1>this.ImagenOriginal.getHeight()) || (y-1>this.ImagenOriginal.getWidth())) return 0;
                rgb = this.ImagenOriginal.getRGB(x-1, y-1);
                break;
            case 1:
                if(x-1<0 || y<0) return 0;
                if ((x-1>this.ImagenOriginal.getHeight()) || (y>this.ImagenOriginal.getWidth())) return 0;
                rgb = this.ImagenOriginal.getRGB(x-1, y);
                break;
            case 2:
                if(x-1<0 || y+1<0) return 0;
                if ((x-1>this.ImagenOriginal.getHeight()) || (y+1>this.ImagenOriginal.getWidth())) return 0;
                rgb = this.ImagenOriginal.getRGB(x-1, y+1);
                break;
            case 3:
                if(x<0 || y-1<0) return 0;
                if ((x>this.ImagenOriginal.getHeight()) || (y-1>this.ImagenOriginal.getWidth())) return 0;
                rgb = this.ImagenOriginal.getRGB(x, y-1);
                break;
            case 4:
                if(x<0 || y+1<0) return 0;
                if ((x>this.ImagenOriginal.getHeight()) || (y+1>this.ImagenOriginal.getWidth())) return 0;
                rgb = this.ImagenOriginal.getRGB(x, y+1);
                break;
            case 5:
                if(x+1<0 || y-1<0) return 0;
                if ((x+1>this.ImagenOriginal.getHeight()) || (y-1>this.ImagenOriginal.getWidth())) return 0;
                rgb = this.ImagenOriginal.getRGB(x+1, y-1);
                break;
            case 6:
                if(x+1<0 || y<0) return 0;
                if ((x+1>this.ImagenOriginal.getHeight()) || (y>this.ImagenOriginal.getWidth())) return 0;
                rgb = this.ImagenOriginal.getRGB(x+1, y);
                break;
            case 7:
                if(x+1<0 || y+1<0) return 0;
                if ((x+1>this.ImagenOriginal.getHeight()) || (y+1>this.ImagenOriginal.getWidth())) return 0;
                rgb = this.ImagenOriginal.getRGB(x+1, y+1);
                break;
            default:
                rgb = this.ImagenOriginal.getRGB(x, y);
                break;
        }
        return rgb;
    }
}