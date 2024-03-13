import javax.sound.midi.Soundbank;
import java.lang.Character;
import java.lang.String;
import java.net.SocketTimeoutException;
import java.sql.SQLOutput;

public class Main {
    public static void main(String[] args){
        System.out.println("Hello!");
        System.out.println("ARGS: " + String.join(" ", args));
        System.out.println("PRIMUL EXERCITIU(toate numerele prime):");
        ex1(args);
        System.out.println("ARGS: " + String.join(" ", args));
        System.out.println("AL DOILEA EXERCITIU(cel mai mare numar):");
        ex2(args);
        System.out.println("ARGS: " + String.join(" ", args));
        System.out.println("AL TREILEA EXERCITIU(cel mai mic numar):");
        ex3(args);
        System.out.println("ARGS: " + String.join(" ", args));
        System.out.println("AL PATRULEA EXERCITIU(cel mai mare divizor comun):");
        ex4(args);
        System.out.println("ARGS: " + String.join(" ", args));
        System.out.println("AL CINCELEA EXERCITIU(cel mai mic multiplu comun):");
        ex5(args);
    }

    public static void ex1(String[] args){
        if(args.length==0)
        {  System.out.println("Adaugati string in args!!!!");
            System.exit(0);}
        else
            System.out.println("Ii bun args!");
        int e=0;
        for(int i=0;i<args.length;i++)
        {

            if(isNumeric(args[i])==true)
            {
                int x = Integer.parseInt(args[i]);
                if(isPrime(x)==true) {
                    e=1;
                    System.out.println(x);
                }
            }
            if(e==0)
                System.out.println("Nu exista nr prime!");


        }

    }
    public static void ex2(String[] args) {
        if (args.length == 0) {
            System.out.println("Adaugati string in args!!!!");
            System.exit(0);
        } else
            System.out.println("Ii bun args!");
        int mx=Integer.MIN_VALUE;
        for (int i = 0; i < args.length; i++) {

            if (isNumeric(args[i]) == true ) {
                int x = Integer.parseInt(args[i]);
                if(mx<x)
                    mx=x;
            }
        }
        System.out.println(mx);
    }
    public static void ex3(String[] args) {
        if (args.length == 0) {
            System.out.println("Adaugati string in args!!!!");
            System.exit(0);
        } else
            System.out.println("Ii bun args!");
        int mx=Integer.MAX_VALUE;
        for (int i = 0; i < args.length; i++) {

            if (isNumeric(args[i]) == true ) {
                int x = Integer.parseInt(args[i]);
                    if(mx>x)
                        mx=x;
                }
            }
        System.out.println(mx);
    }
    public static void ex4(String[] args)
    {
        if (args.length == 0) {
            System.out.println("Adaugati string in args!!!!");
            System.exit(0);
        } else
            System.out.println("Ii bun args!");
        int c=0;
        for(int i=0;i<args.length;i++)
        {
            if(isNumeric(args[i])==true && Integer.parseInt(args[i])>0)
            {
                int b=Integer.parseInt(args[i]);
                c=cmmdc(c,b);


            }
        }
        if(c==0)
            System.out.println("Nu exista numere pozitive");
        else
             System.out.println(c);
    }
    public static void ex5(String[] args)
    {
        if (args.length == 0) {
            System.out.println("Adaugati string in args!!!!");
            System.exit(0);
        } else
            System.out.println("Ii bun args!");
        int c=1;
        for(int i=0;i<args.length;i++)
        {
            if(isNumeric(args[i])==true && Integer.parseInt(args[i])>0 )
            {
                int b=Integer.parseInt(args[i]);
                int prod=b*c;
                c=prod/cmmdc(c,b);


            }
        }
        System.out.println(c);
    }
    public static boolean isPrime(int x)
    {
        if(x<=1)
            return false;
        else
            for(int i=2;i<=x/2;i++)
                if(x%i==0)
                    return false;

        return true;
    }
    public static boolean isNumeric(String str) {
        try {
            Integer.parseInt(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }


    }
    public static int cmmdc(int a,int b)
    {
        int r=a%b;
        while(r!=0)
        {
            a=b;
            b=r;
            r=a%b;
        }
        return b;
    }
}

