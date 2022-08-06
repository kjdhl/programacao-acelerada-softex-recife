import java.io.*;
import java.io.Serializable;
public class Aluno implements java.io.Serializable {
	public String nome;
	public String classe;

 }
 public class serializando {

	public static void main(String [] args) {
		Aluno e  = new Aluno();
		e.nome = "aluno1";
		e.classe = "A";
	   
	   
	
		FileOutputStream objeto = new FileOutputStream("C:/alunos.ser");
		ObjectOutputStream out = new ObjectOutputStream(objeto);
		out.writeObject(e);
		out.close();
		objeto.close();
	   
	}
 }

 public class deserealizando{

	public static void main(String [] args) {
		   FileInputStream objeto = new FileInputStream("C:/alunos.ser");
		   ObjectInputStream out = new ObjectInputStream(objeto);
		   e = (Aluno) out.readObject();
		   out.close();

	}

 }
