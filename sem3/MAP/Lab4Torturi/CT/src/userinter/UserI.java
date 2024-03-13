package userinter;

import entity.Comanda;
import entity.Tort;
import repository.DuplicateException;
import service.Service;

import java.util.*;

public class UserI {
        private Service serv;
        public UserI(Service serv)
        {
            this.serv=serv;

        }
        public void afist()
        {
                Collection<Tort> torturi=serv.getAllt();
                for(Tort t:torturi)
                        System.out.println(t);
        }
        public void afisc(){
                Collection<Comanda> comenzi=serv.getAllc();
                for(Comanda c:comenzi)
                        System.out.println(c);
        }
        public boolean verif_id_t(int id){
                Collection<Tort> torturi=serv.getAllt();
                for(Tort t:torturi){
                        if(id==t.getID())
                                return false;
                }
                return true;
        }
        public boolean verif_id_c(int id){
                Collection<Comanda> comenzi=serv.getAllc();
                for(Comanda c:comenzi){
                        if(id==c.getID())
                                return false;
                }
                return true;
        }
        public void print_menu(){
                System.out.println("1.Adauga Tort.");
                System.out.println("2.Sterge Tort.");
                System.out.println("3.Modifica Tort.");
                System.out.println("4.Adauga Comanda.");
                System.out.println("5.Sterge Comanda.");
                System.out.println("6.Modifica Comanda.");
                System.out.println("pt.Print Torturi.");
                System.out.println("pc.Print Comenzi.");
                System.out.println("x.Exit.");
        }
        public void add_tort(Scanner scanner)
        {

                System.out.print("Id tort: ");
                int id=scanner.nextInt();
                System.out.print("Tip tort: ");
                String tip=scanner.next();
                if(verif_id_c(id)==false){
                        System.out.println("Id deja existent!");
                        return;
                }
                try{
                        serv.addt(id,tip);
                } catch (DuplicateException e) {
                        System.out.println("Element existent!");
                }

        }
        public void del_tort(Scanner scanner){
                System.out.print("Id tort care va fi sters: ");
                int id = scanner.nextInt();
                try {
                serv.deletet(id);
                }
                catch (NoSuchElementException e){
                        System.out.println("Nu exista id!");
                }
        }
        public void modif_tort(Scanner scanner){
                System.out.print("Id tort care va fi modificat: ");
                int id = scanner.nextInt();
                if(verif_id_t(id)==true){
                        System.out.println("Adaugati un id existent!");
                        return;
                }
                System.out.print("Tipul cu care va fi modificat: ");
                String tip=scanner.next();
                Tort t=new Tort(id,tip);
                serv.updatet(t);
        }
        public void add_com(Scanner scanner) throws DuplicateException {
                System.out.print("Id Comanda: ");
                int id=scanner.nextInt();
                if(verif_id_c(id)==false){
                        System.out.println("Id deja existent!");
                        return;
                }
                System.out.println("Lista torturi: ");
                afist();
                System.out.print("Numar torturi din comanda: ");
                int nr=scanner.nextInt();
                List<String> torturi=new ArrayList<>();
                for(int i=0;i<nr;i++)
                {
                        scanner.nextLine();
                        System.out.print("Id tort pt comanda:");
                        int index=scanner.nextInt();
                        torturi.add(serv.getByIdt(index).getTip());
                }
                System.out.println("Data comenzii: ");
                String date=scanner.next();
                try{
                serv.addc(id,torturi,date);}
                catch (DuplicateException e){
                        System.out.println("Element existent!");;
                }
        }
        public void del_com(Scanner scanner){
                System.out.print("Id comanda care va fi stearsa: ");
                int id = scanner.nextInt();
                try{
                        serv.deletec(id);}
                catch (NoSuchElementException e){
                        System.out.println("Nu exista id!");
                }

        }
        public void modif_com(Scanner scanner){
                System.out.print("Id comanda care va fi modificata: ");
                int id=scanner.nextInt();
                if(verif_id_c(id)==true){
                        System.out.println("Adaugati un id existent!");
                        return;
                }
                System.out.print("Data care va fi modificata: ");
                String date=scanner.next();
                Comanda c=new Comanda(id,serv.getByIdc(id).getTorturi(),date);
                serv.updatec(c);
        }
        public void run() throws DuplicateException {
                while(true){
                        print_menu();
                        String opt;
                        System.out.print("Optiunea aleasa:");
                        Scanner scanner=new Scanner(System.in);
                        opt=scanner.next();
                        switch(opt){
                                case "1":{
                                        add_tort(scanner);
                                        break;
                                }
                                case "4":
                                {
                                        add_com(scanner);
                                        break;
                                }
                                case "pt":{
                                        afist();
                                        break;
                                }
                                case "2": {
                                        del_tort(scanner);
                                        break;
                                }
                                case "5":
                                {
                                        del_com(scanner);
                                        break;
                                }
                                case "3":{
                                        modif_tort(scanner);
                                        break;
                                }
                                case "6":
                                {
                                        modif_com(scanner);
                                        break;
                                }
                                case "pc":{
                                        afisc();
                                        break;
                                }
                                case "x":{
                                        return;}

                                default:
                                        System.out.println("Optiune gresita!");
                                        break;

                                }
                        }
                }

        }










