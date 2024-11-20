package fundamentos;
import java.util.Scanner;
public class exe5 {

	public static void main(String[] args) {
		 Scanner scanner = new Scanner(System.in);
	        
	        int respostasSim = 0; // Variável para contar as respostas "sim"

	        System.out.println("Responda as perguntas com 1 para sim e 2 para não:");
	        System.out.print("Telefonou para a vítima? ");
	        respostasSim += scanner.nextInt() == 1 ? 1 : 0;

	        System.out.print("Esteve no local do crime? ");
	        respostasSim += scanner.nextInt() == 1 ? 1 : 0;

	        System.out.print("Mora perto da vítima? ");
	        respostasSim += scanner.nextInt() == 1 ? 1 : 0;

	        System.out.print("Devia para a vítima? ");
	        respostasSim += scanner.nextInt() == 1 ? 1 : 0;

	        System.out.print("Já trabalhou para a vítima? ");
	        respostasSim += scanner.nextInt() == 1 ? 1 : 0;

	        // Classificação
	        if (respostasSim == 5) {
	            System.out.println("Assassino");
	        } else if (respostasSim >= 3) {
	            System.out.println("Cúmplice");
	        } else if (respostasSim == 2) {
	            System.out.println("Suspeito");
	        } else {
	            System.out.println("Inocente");
	        }

	        scanner.close();
	    }

}
