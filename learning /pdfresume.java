import java.io.*;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.rendering.PDFRenderer;

public class LatexToPdfImage {

    public static void latexToPdf(String latexCode, String texFilename, String pdfFilename) {
        try {
            // Write LaTeX code to .tex file
            FileWriter writer = new FileWriter(texFilename);
            writer.write(latexCode);
            writer.close();

            // Compile LaTeX to PDF using pdflatex
            ProcessBuilder processBuilder = new ProcessBuilder("pdflatex", texFilename);
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();

            // Read output from the process
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Wait for process to complete
            int exitCode = process.waitFor();
            if (exitCode == 0) {
                System.out.println("PDF saved as " + pdfFilename);
            } else {
                System.out.println("LaTeX compilation failed.");
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void pdfToImage(String pdfFilename, String imageFilename) {
        try {
            // Load PDF
            PDDocument document = PDDocument.load(new File(pdfFilename));
            PDFRenderer renderer = new PDFRenderer(document);

            // Render first page to image
            BufferedImage image = renderer.renderImageWithDPI(0, 300);
            ImageIO.write(image, "PNG", new File(imageFilename));

            document.close();
            System.out.println("Image saved as " + imageFilename);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        String latexCode = """
            \\documentclass[letterpaper,11pt]{article}
            \\usepackage{hyperref}
            \\begin{document}
            \\title{My Resume}
            \\author{Jake Ryan}
            \\maketitle
            \\section{Contact Information}
            Email: \\href{mailto:jake@su.edu}{jake@su.edu} \\\\
            GitHub: \\href{https://github.com/...}{github.com/jake}
            \\end{document}
        """;

        String texFile = "document.tex";
        String pdfFile = "document.pdf";
        String imageFile = "document.png";

        latexToPdf(latexCode, texFile, pdfFile);
        pdfToImage(pdfFile, imageFile);
    }
}
