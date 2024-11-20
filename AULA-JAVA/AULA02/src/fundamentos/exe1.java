package fundamentos;

import java.util.Scanner;

public class exe1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número de 1 a 7 (1 - Domingo, 2 - Segunda, etc.): ");
        int numero = scanner.nextInt();

        String diaDaSemana;

        switch (numero) {
            case 1:
                diaDaSemana = "Domingo";
                break;
            case 2:
                diaDaSemana = "Segunda-feira";
                break;
            case 3:
                diaDaSemana = "Terça-feira";
                break;
            case 4:
                diaDaSemana = "Quarta-feira";
                break;
            case 5:
                diaDaSemana = "Quinta-feira";
                break;
            case 6:
                diaDaSemana = "Sexta-feira";
                break;
            case 7:
                diaDaSemana = "Sábado";
                break;
            default:

                diaDaSemana = "Valor inválido";

        }

        System.out.println("O dia da semana é: " + diaDaSemana);
    }
}
