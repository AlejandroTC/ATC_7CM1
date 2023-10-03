package com.imageanalisys;

import javax.swing.ImageIcon;
import java.awt.Color;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.util.Random;

public class JFrameImage extends javax.swing.JFrame {
//ATC
    private javax.swing.JLabel jLabelImagen;

    public JFrameImage(Image imagen) {
        initComponents();
        // Mandar una imagen al label
        //this.jLabelImagen.setIcon(new ImageIcon(imagen));
        int w = imagen.getWidth(null);
        int h = imagen.getHeight(null);
        Image imagenEscalada = HerramientasImagen.toBufferedImage(imagen).getScaledInstance(w/4, h/4, BufferedImage.TYPE_INT_RGB);
        this.jLabelImagen.setIcon(new ImageIcon(imagenEscalada));
        
        Random random = new Random();
        int x = random.nextInt(imagenEscalada.getWidth(null));
        int y = random.nextInt(imagenEscalada.getHeight(null));
        int rgb = HerramientasImagen.toBufferedImage(imagen).getRGB(x,y);

        // Extrae los componentes RGB (rojo, verde, azul)
        int red = (rgb >> 16) & 0xFF;
        int green = (rgb >> 8) & 0xFF;
        int blue = rgb & 0xFF;
        // Imprime los valores RGB del punto aleatorio
        System.out.println("Coordenadas: (" + x + ", " + y + ")");
        System.out.println("Valor RGB: (" + red + ", " + green + ", " + blue + ")");

        //Contar frecuencia de colores
        Color verdeRan = new Color(88,111,7);
        int ce = verdeRan.getRGB();
        //Bufferear imagen
        BufferedImage imgrec = HerramientasImagen.toBufferedImage(imagenEscalada);
        int contador = 0;
        //Nuevo color para cambio visual
        Color cambio = new Color(0, 111, 255);
        int newColor = cambio.getRGB();
        //Recorrer imagen buffereada
        for(int i=0; i<imgrec.getWidth(); i++){
            for (int j=0; j<imgrec.getHeight(); j++){
                int valorpix = imgrec.getRGB(i, j);
                if(ce == valorpix){
                    contador++;
                    //Cambiar color
                    imgrec.setRGB(i,j, newColor);
                }
            }
        }
        System.out.println(contador);
        Image cambiada = HerramientasImagen.toImage(imgrec);
        HerramientasImagen.calcularHistograma(imagenEscalada);
        this.jLabelImagen.setIcon(new ImageIcon(imagenEscalada));

    }

    private void initComponents() {
        jLabelImagen = new javax.swing.JLabel();
        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().add(jLabelImagen, java.awt.BorderLayout.CENTER);
        pack();
    }
}
