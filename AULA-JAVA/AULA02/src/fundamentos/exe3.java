package fundamentos;
import java.util.Scanner;
public class exe3 {
	
		    public static void main(String[] args) {
		        Scanner scanner = new Scanner(System.in);

		        System.out.print("Digite a primeira nota: ");
		        double nota1 = scanner.nextDouble();

		        System.out.print("Digite a segunda nota: ");
		        double nota2 = scanner.nextDouble();

		        double media = (nota1 + nota2) / 2;

		        System.out.println("A média do aluno é: " + media);

		        scanner.close();
		    }
		
	}


