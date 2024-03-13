import entity.Comanda;
import factory.ComandaFactory;
import entity.Tort;
import factory.TortFactory;
import repository.*;
import service.Service;
import userinter.UserI;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class Main {
    public static void main(String[] args) throws DuplicateException, IOException, ClassNotFoundException {

        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("settings.properties")) {
            properties.load(input);
        }
        String repositoryType = properties.getProperty("Repository");
        String tortsFile = properties.getProperty("Tort");
        String commandsFile = properties.getProperty("Comanda");

        IRepository<Tort> repoTort;
        IRepository<Comanda> repoCom;

            switch (repositoryType) {
                case "text": {
                    repoTort = new FileRepo<>(tortsFile, new TortFactory());
                    repoCom = new FileRepo<>(commandsFile, new ComandaFactory());
                    Service serv = new Service(repoTort, repoCom);
                    UserI ui = new UserI(serv);
                    ui.run();
                    break;
                }
                case "memory": {
                    repoTort = new Repo<>();
                    repoCom = new Repo<>();

                    Service serv = new Service(repoTort, repoCom);

                    UserI ui = new UserI(serv);
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
                    Service serv = new Service(repoTort, repoCom);
                    UserI ui = new UserI(serv);
                    ui.run();
                    break;
                }
                default:
                    throw new IllegalArgumentException("Invalid repository type: " + repositoryType);            }
        }
//        TorturiDbRepository repo=new TorturiDbRepository();
//        repo.connectToDb();}


}


