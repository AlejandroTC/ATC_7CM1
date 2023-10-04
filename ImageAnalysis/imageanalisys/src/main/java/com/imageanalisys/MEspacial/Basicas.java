package com.imageanalisys.MEspacial;

import java.awt.Color;
import java.awt.Image;
import java.awt.image.BufferedImage;

import com.imageanalisys.HerramientasImagen;

public class Basicas {
    public static Image escalaDeGrises(Image original)
    {
        //To buffer para leer la informacion
        BufferedImage originalBuffered = HerramientasImagen.toBufferedImage(original);
        //Recorrer imagen buffereada
        for(int i=0; i < originalBuffered.getWidth(); i++){
            for (int j=0; j < originalBuffered.getHeight(); j++){
                //Promedio de colores RGB:
                int valorpix = originalBuffered.getRGB(i, j);
                Color whatColors = new Color(valorpix);
                int prom = ((whatColors.getRed() + whatColors.getGreen() + whatColors.getBlue())/3);
                // System.out.println(prom);
                Color bn = new Color(prom, prom, prom);
                int bnC = bn.getRGB();
                originalBuffered.setRGB(i, j, bnC);
            }
        }
        Image ImageBN = HerramientasImagen.toImage(originalBuffered);
        return ImageBN;
    }

     public static Image algo(Image original, int m)
    {
        //To buffer para leer la informacion
        BufferedImage originalBuffered = HerramientasImagen.toBufferedImage(original);
        //Recorrer imagen buffereada
        for(int i=0; i < originalBuffered.getWidth(); i++){
            for (int j=0; j < originalBuffered.getHeight(); j++){
                //Promedio de colores RGB:
                int valorpix = originalBuffered.getRGB(i, j);
                Color whatColors = new Color(valorpix);
                whatColors = new Color(validar(whatColors.getRed()+m), validar(whatColors.getGreen()+m), validar(whatColors.getBlue()+m));
                originalBuffered.setRGB(i, j, whatColors.getRGB());
            }
        }
        Image ImageColored = HerramientasImagen.toImage(originalBuffered);
        return ImageColored;
    }
    private static int validar (int i){
        if(i>255) return 255;
        if(i<0) return 0;
        return i;
    }
}
