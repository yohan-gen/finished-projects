import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;
import java.util.Arrays;

public class forcaEXT{

    public static void main(String[] args){

        String[] forca = {"materializacao","trigonometrico","alquimizar","carbonização","congruencia","hidrocarbonetos","eletrostatica","ionizacao","xenon","boron","ondulatoria","eletromagnetismo","convergente","divergente","polytetrafluoroethylene"};

        Random rand = new Random();
        int rword = rand.nextInt(forca.length);
        String word = forca[rword];
        ArrayList<String> letters = new ArrayList<>(); 

        System.out.println("Jogo da forca nivel EXTREMO, teste seu QI");

        for (int i = 0; i < word.length(); i++) {
            letters.add("_");
        }

        System.out.println(letters +"\n"+ word);

    }
}