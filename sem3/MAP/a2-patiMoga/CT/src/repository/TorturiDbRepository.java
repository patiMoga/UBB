package repository;

import entity.Tort;
import org.sqlite.SQLiteDataSource;

import java.sql.Connection;
import java.sql.SQLException;

public class TorturiDbRepository extends Repo<Tort>{
    private String JDBC_URL="jdbc:sqlite:patiserie.db";
    private Connection connection;
    public void connectToDb(){
        SQLiteDataSource ds=new SQLiteDataSource();
        ds.setUrl(JDBC_URL);
        try {
            if(connection==null|| connection.isClosed()){
                connection=ds.getConnection();
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
