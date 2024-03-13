import database.DBConnection;
import entity.Tort;
import repository.DuplicateException;
import repository.IRepository;
import repository.TortDatabaseRepo;

public class SqliteConnnection {
    public static void main(String[] args) {
        DBConnection.setConnection();
        IRepository<Tort> repoTort = new TortDatabaseRepo();
        System.out.println(repoTort.getAll());
        try {
            for(int i = 1; i <= 100; i++) {
                repoTort.add(new Tort(i, "Tort_" + i));
            }
        } catch (DuplicateException e) {
            throw new RuntimeException(e);
        }
        System.out.println(repoTort.getAll());
//        repoTort.update(new Tort(1, "Cheesecake"));
//        System.out.println(repoTort.getAll());
        repoTort.getAll();
    }
}

