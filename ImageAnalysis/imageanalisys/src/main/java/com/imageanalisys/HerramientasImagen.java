package com.imageanalisys;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.swing.JFileChooser;
import javax.swing.filechooser.FileNameExtensionFilter;

public class HerramientasImagen {
    
    public static Image abrirImagen (){
    
          try {
            // definir los filtros para lectura
            FileNameExtensionFilter filtro =
                    new FileNameExtensionFilter("Imagenes","jpg","jpeg","png","bmp");
            // crear un selector de archivos
            JFileChooser selector = new JFileChooser();
            // Especifica la carpeta inicial
            File Folder = new File("/Users/atc/Documentos/Repos/ATC_7CM1/ImageAnalysis");
            selector.setCurrentDirectory(Folder);
            // agregar el filtro al selector
            selector.addChoosableFileFilter(filtro);
            // especificar que solo se puedan abrir archivos
            selector.setFileSelectionMode(JFileChooser.FILES_ONLY);
            
            //ejecutar el selector de imagenes
            
            int res = selector.showOpenDialog(null);
            
            if (res == 1 ){
                
                return null;
                
            }
            
            File archivo = selector.getSelectedFile();
            
            BufferedImage bi = ImageIO.read(archivo);
            
            return toImage(bi);
        } catch (IOException ex) {
            Logger.getLogger(HerramientasImagen.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    
    }  
    
    public static Image toImage (BufferedImage bi){
        return bi.getScaledInstance(bi.getWidth(),bi.getHeight(), BufferedImage.TYPE_INT_RGB);
    }
    
    public static BufferedImage toBufferedImage (Image imagen){
         // imagen es un objeto de tipo BufferedImage
//        if (imagen instanceof BufferedImage){
//          return (BufferedImage)imagen;
//        }
        BufferedImage bi = 
                new BufferedImage(imagen.getWidth(null), imagen.getHeight(null), BufferedImage.TYPE_INT_RGB);
        
        Graphics2D nueva = bi.createGraphics();
        nueva.drawImage(imagen, 0, 0,null);
        nueva.dispose();
        
        return bi;
    }
    
    public static Image copiarImagen(Image i){
        BufferedImage bi = toBufferedImage(i);
        return bi.getScaledInstance(bi.getWidth(),bi.getHeight(), BufferedImage.TYPE_INT_RGB);
    }

    public static void calcularHistograma(Image imagen, String titulo, int x, int y){
        //Contadores
        double[] contR = new double[256];
        double[] contG = new double[256];
        double[] contB = new double[256];
        // recorrer los pixeles de la imagen
        BufferedImage bi = toBufferedImage(imagen);
        for(int i=0; i<bi.getWidth(); i++){
            for(int j=0; j<bi.getHeight(); j++){
                Color thisColor = new Color(bi.getRGB(i, j));
                contR[thisColor.getRed()] = contR[thisColor.getRed()]+1;
                contG[thisColor.getGreen()] = contG[thisColor.getGreen()]+1;
                contB[thisColor.getBlue()] = contB[thisColor.getBlue()]+1;
            }
        }
        Graficador graficador = new Graficador("Valor", "Frecuencia", titulo);
        // Agrega los datos al objeto Graficador
        graficador.agregarSerie("Rojo", contR);
        graficador.agregarSerie("Azul", contB);
        graficador.agregarSerie("Verde", contG);
        
        graficador.crearGrafica();
        graficador.muestraGrafica(x, y);
    }
}