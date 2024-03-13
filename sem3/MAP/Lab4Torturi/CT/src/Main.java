import database.DBConnection;
import entity.Comanda;
import entity.Tort;
import factory.ComandaFactory;
import factory.TortFactory;
import repository.*;
import service.Service;
import userinter.UserI;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class Main {
    public static void main(String[] args) throws DuplicateException, IOException {
//        String opt;
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("settings.properties")) {
            properties.load(input);
        }
        String repositoryType = properties.getProperty("Repository");
        String tortsFile = properties.getProperty("Tort");
        String commandsFile = properties.getProperty("Comanda");

        IRepository<Tort> repoTort;
        IRepository<Comanda> repoCom;
        Service service;
        UserI ui;
//        while (true) {true
//            System.out.println("1.Memory repository");
//            System.out.println("2.Text File repository");
//            System.out.println("3.Binary File repository");
//            System.out.println("x.Exit");
//            System.out.print("Optiunea aleasa:");
//            Scanner scanner = new Scanner(System.in);
//            opt = scanner.next();

        switch (repositoryType) {

            case "text": {
                repoTort = new FileRepo<>(tortsFile, new TortFactory());
                repoCom = new FileRepo<>(commandsFile, new ComandaFactory());
                service = new Service(repoTort, repoCom);
                ui = new UserI(service);
                ui.run();
                break;
            }
            case "memory": {
                repoTort = new Repo<>();
                repoCom = new Repo<>();

                Service serv = new Service(repoTort, repoCom);

                ui = new UserI(serv);
                serv.addt(1, "Tiramisu");
                serv.addt(2, "CarrotCake");
                serv.addt(3, "RedVelvet");
                serv.addt(4, "Caramel");
                serv.addt(5, "TrioChocola");
                ui.run();
                break;
            }
            case "binary": {
                repoTort = new BinaryRepo<>(tortsFile);
                repoCom = new BinaryRepo<>(commandsFile);
                service = new Service(repoTort, repoCom);
                ui = new UserI(service);
                ui.run();
                break;
            }
            case "database":
                DBConnection.setConnection();
                repoTort = new TortDatabaseRepo();
                repoCom = new ComandaDatabaseRepo();
                service = new Service(repoTort, repoCom);
                ui = new UserI(service);
                ui.run();
                break;
            default:
                throw new IllegalArgumentException("Invalid repository type: " + repositoryType);
        }
    }
}

