import java.awt.Image;

import javax.swing.JPanel;

public class Main {

    public static void main(String[] args) {
        // Abrir una imagen desde un archivo
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                Image imagen = HerramientasImagen.abrirImagen();
                JFrameImage frame = new JFrameImage(imagen);
                frame.setVisible(true);
            }
        });
    }
}