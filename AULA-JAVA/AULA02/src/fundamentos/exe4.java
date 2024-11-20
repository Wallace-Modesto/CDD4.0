package fundamentos;
import java.util.Scanner;
public class exe4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner (System.in);

		        System.out.print("Digite F para feminino ou M para masculino: ");
		        String sexo = entrada.next();

		        if (sexo.equalsIgnoreCase("F")) {
		            System.out.println("Feminino");
		        } else if (sexo.equalsIgnoreCase("M")) {
		            System.out.println("Masculino");
		        } else {
		            System.out.println("Letra inválida. Digite F ou M.");
		        }

		        entrada.close();
		    
		
		
	}

}
