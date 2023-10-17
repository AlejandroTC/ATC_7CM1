package com.imageanalisys;

import java.awt.Image;
import com.imageanalisys.MEspacial.Basicas;
import com.imageanalisys.MEspacial.Binarizacion;

public class App {
    public static void main(String[] args) {
        // Abrir una imagen desde un archivo
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                UmbralAutomatico();
                // negativeGrises();
                // negative();
                // binarizar();
                // binarizar2();
                // egrises();
                // ilium();
                // imagenFria();
                // imagenCalida();

            }
        });
    }

    protected static void UmbralAutomatico() {
        Image imagen = HerramientasImagen.abrirImagen();
        // Imagen Original
        JFrameImage original = new JFrameImage(imagen);
        original.setSize(500, 500);
        original.setVisible(true);
        // Histograma
        HerramientasImagen.calcularHistograma(imagen, "Original", 0, 500);
        //HACE ALGO
        int umbral = HerramientasImagen.obtenerUmbral(Basicas.escalaDeGrises(imagen));
        JFrameImage modificado = new JFrameImage(Binarizacion.binarizarImagen(Basicas.escalaDeGrises(imagen), umbral));
        modificado.setSize(500, 500);
        modificado.setLocation(500, 0);
        modificado.setVisible(true);
        // Histograma
        HerramientasImagen.calcularHistograma(Binarizacion.binarizarImagen(Basicas.escalaDeGrises(imagen), umbral), "Binarizacion", 500, 500);
           
    }

    protected static void negativeGrises() {
        Image imagen = HerramientasImagen.abrirImagen();
        // Imagen Original
        JFrameImage original = new JFrameImage(imagen);
        original.setSize(500, 500);
        original.setVisible(true);
        // Histograma
        HerramientasImagen.calcularHistograma(imagen, "Original", 0, 500);
        //Imagen en negativo
        JFrameImage negG = new JFrameImage(Basicas.negativeGrises(imagen, 255));
        negG.setSize(500, 500);
        negG.setLocation(500, 0);
        negG.setVisible(true);
        // Histograma negativo
        HerramientasImagen.calcularHistograma(Basicas.negativeGrises(imagen, 255), "Negativo Escala de Grises", 500, 500);
    }

    protected static void negative() {
        Image imagen = HerramientasImagen.abrirImagen();
        // Imagen Original
        JFrameImage original = new JFrameImage(imagen);
        original.setSize(500, 500);
        original.setVisible(true);
        // Histograma
        HerramientasImagen.calcularHistograma(imagen, "Original", 0, 500);
        //Imagen en negativo
        JFrameImage neg = new JFrameImage(Basicas.negative(imagen, 255));
        neg.setSize(500, 500);
        neg.setLocation(500, 0);
        neg.setVisible(true);
        // Histograma negativo
        HerramientasImagen.calcularHistograma(Basicas.negative(imagen, 255), "Negativo", 500, 500);
    }

    public static void egrises() {
        Image imagen = HerramientasImagen.abrirImagen();
        // Imagen Original
        JFrameImage original = new JFrameImage(imagen);
        original.setSize(500, 500);
        original.setVisible(true);
        // Histograma
        HerramientasImagen.calcularHistograma(imagen, "Original", 0, 500);
        // Escala Grises
        JFrameImage gris = new JFrameImage(Basicas.escalaDeGrises(imagen));
        gris.setSize(500, 500);
        gris.setLocation(500, 0);
        gris.setVisible(true);
        // Histograma Gristes
        HerramientasImagen.calcularHistograma(Basicas.escalaDeGrises(imagen), " Escala de Grises", 500, 500);
    }

    public static void ilium() {
        // Abrir imagen
        Image imagen = HerramientasImagen.abrirImagen();
        // Mostrar imgaen original
        JFrameImage original = new JFrameImage(imagen);
        original.setSize(500, 500);
        original.setVisible(true);
        // Histograma imagen Original
        HerramientasImagen.calcularHistograma(imagen, "Original", 0, 500);
        // Mostrar imagen iluminada
        JFrameImage ilum = new JFrameImage(Basicas.aumentarIluminacion(imagen, 20));
        ilum.setSize(500, 500);
        ilum.setLocation(500, 0);
        ilum.setVisible(true);
        // Histograma imagen iluminada
        HerramientasImagen.calcularHistograma(Basicas.aumentarIluminacion(imagen, 20), "Iluminada", 500, 500);
    }

    public static void imagenFria() {
        // Abrir imagen
        Image imagen = HerramientasImagen.abrirImagen();
        // Mostrar imgaen original
        JFrameImage original = new JFrameImage(imagen);
        original.setSize(500, 500);
        original.setVisible(true);
        // Histograma imagen Original
        HerramientasImagen.calcularHistograma(imagen, "Original", 0, 500);
        // Mostrar imagen iluminada
        JFrameImage fria = new JFrameImage(Basicas.frio(imagen, 20));
        fria.setSize(500, 500);
        fria.setLocation(500, 0);
        fria.setVisible(true);
        // Histograma imagen iluminada
        HerramientasImagen.calcularHistograma(Basicas.frio(imagen, 20), "Imagen Fría", 500, 500);
    }

    public static void imagenCalida() {
        // Abrir imagen
        Image imagen = HerramientasImagen.abrirImagen();
        // Mostrar imgaen original
        JFrameImage original = new JFrameImage(imagen);
        original.setSize(500, 500);
        original.setVisible(true);
        // Histograma imagen Original
        HerramientasImagen.calcularHistograma(imagen, "Original", 0, 500);
        // Mostrar imagen iluminada
        JFrameImage calida = new JFrameImage(Basicas.calido(imagen, 20));
        calida.setSize(500, 500);
        calida.setLocation(500, 0);
        calida.setVisible(true);
        // Histograma imagen iluminada
        HerramientasImagen.calcularHistograma(Basicas.calido(imagen, 20), "Imagen Cálida", 500, 500);
    }

    public static void binarizar(){
        Image imagen = HerramientasImagen.abrirImagen();
        JFrameImage original = new JFrameImage(imagen);
        original.setSize(500, 500);
        original.setVisible(true);
        // Histograma
        HerramientasImagen.calcularHistograma(imagen, "Original", 0, 500);
        //HACE ALGO
        JFrameImage modificado = new JFrameImage(Binarizacion.binarizarImagen(Basicas.escalaDeGrises(imagen), 230));
        modificado.setSize(500, 500);
        modificado.setLocation(500, 0);
        modificado.setVisible(true);
        // Histograma
        HerramientasImagen.calcularHistograma(Binarizacion.binarizarImagen(Basicas.escalaDeGrises(imagen), 230), "Binarizacion", 500, 500);
                
    }
    public static void binarizar2(){
        Image imagen = HerramientasImagen.abrirImagen();
        JFrameImage original = new JFrameImage(imagen);
        original.setSize(500, 500);
        original.setVisible(true);
        // Histograma
        HerramientasImagen.calcularHistograma(imagen, "Original", 0, 500);
        //HACE ALGO
        JFrameImage modificado = new JFrameImage(Binarizacion.binarizarImagen(Basicas.escalaDeGrises(imagen), 150, 230));
        modificado.setSize(500, 500);
        modificado.setLocation(500, 0);
        modificado.setVisible(true);
        // Histograma
        HerramientasImagen.calcularHistograma(Binarizacion.binarizarImagen(Basicas.escalaDeGrises(imagen), 150, 230), "Binarizacion", 500, 500);
                
    }
}
