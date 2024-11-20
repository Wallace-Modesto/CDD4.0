package fundamentos;

import java.util.Scanner;

public class aula02 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double n1, n2, n3;
		Scanner entrada = new Scanner (System.in);
		System.out.println("Digite o 1 numero:");
		n1 = entrada.nextDouble();
		System.out.println("Digite o ");
		n2 = entrada.nextDouble();
		System.out.println("Digite o ");
		n3 = entrada.nextDouble();
		
		if (n1 > n2) {
			if (n1 > n3) {
				System.out.println("N1 é o maiorr" + n1);
			} else {
				System.out.println("O N3 é o maior " + n3);
			}
		}else {
			if (n2 > n3) {
				System.out.println("N2 é o maiorr" + n2);
			}else {
				System.out.println("N3 é o maiorr" + n3);
			}
		}
		
	}
}


		
