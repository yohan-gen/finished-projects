import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;

public class russian_roulette {
    
    public static void main(String[] args) {

        ArrayList<Integer> roulette = new ArrayList<Integer>();

        Random rand = new Random();
        int shot = rand.nextInt(6);

        for (int i=1; i<=6; i++){
            roulette.add(i);
        }
        System.out.println("Welcome to the russian roulette, test your lucky in a dangerous life or death game...");

        boolean ammunition = true;

        while (ammunition) {
            System.out.println("Choose one number from the list below and lets see if you're lucky enough to survive : ");
            System.out.println(roulette);
            System.out.println("Choosen number : ");
            Scanner sc = new Scanner(System.in);
            int escolha = sc.nextInt();

            if (escolha == shot) {
                System.out.println("As expected you little SHIT! you died like the pathetic loser you are");
                ammunition = false;
            }
            else {
                roulette.remove(Integer.valueOf(escolha));
                System.out.println("Well looks like THIS TIME, AND ONLY THIS TIME you survived...");
            }
            if (roulette.size() == 1){
                System.out.println("Congratu fucking lations, you passed the test, welcome to the alive club");
                ammunition = false;
            }
        }
    }   
}