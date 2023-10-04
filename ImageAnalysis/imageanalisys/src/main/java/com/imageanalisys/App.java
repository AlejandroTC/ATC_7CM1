package com.imageanalisys;

import java.awt.Image;
import javax.swing.JPanel;

import com.imageanalisys.MEspacial.Basicas;

public class App 
{
    public static void main(String[] args) {
        // Abrir una imagen desde un archivo
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                Image imagen = HerramientasImagen.abrirImagen();
                // //Imagen Original
                // JFrameImage original = new JFrameImage(imagen);
                // original.setVisible(true);
                // //Histograma
                // HerramientasImagen.calcularHistograma(imagen, "Original");
                // //Escala Grises
                // JFrameImage frame = new JFrameImage(Basicas.escalaDeGrises(imagen));
                // frame.setVisible(true);
                // //Histograma Gristes
                // HerramientasImagen.calcularHistograma(Basicas.escalaDeGrises(imagen), "Grises");
                JFrameImage Colorear = new JFrameImage(imagen);
                Colorear.setVisible(true);
                HerramientasImagen.calcularHistograma(imagen, "Original");
                JFrameImage Coloreareada = new JFrameImage(Basicas.aumentarIluminacion(imagen, 20));
                Coloreareada.setVisible(true);
                HerramientasImagen.calcularHistograma(Basicas.aumentarIluminacion(imagen, 20), "Coloreada");
                
            }
        });
    }
}
