package database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnection {
    public static Connection connection;

    private DBConnection() {}

    public static void setConnection() {
//        Class.forName("org.sqlite.JDBC");
        String projectRoot = System.getProperty("user.dir");
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:" + projectRoot + "/CT/src/database/cofetarie.db");
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

    }
    public static Connection getConnection() {
        if(connection == null) {
            throw new RuntimeException("No database connection provided!");
        }
        return connection;
    }
}
