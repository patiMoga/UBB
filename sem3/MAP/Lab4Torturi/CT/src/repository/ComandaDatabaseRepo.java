package repository;

import database.DBConnection;
import entity.Comanda;
import entity.Tort;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class ComandaDatabaseRepo extends Repo<Comanda>{
    private Connection connection = DBConnection.getConnection();

    public ComandaDatabaseRepo() {
        loadFromDatabase();
    }

    private void loadFromDatabase() {
        try {
            String query = "SELECT * FROM Comanda";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                int id = resultSet.getInt("Id");
                String data = resultSet.getString("Data");
                List<String> torturi = loadTortsFromComanda(id);
                entities.add(new Comanda(id, torturi, data));
            }
        }
        catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
    private List<String> loadTortsFromComanda(int comandaId) {
        List<String> tortList = new ArrayList<>();

        try {
            String tortComandaQuery = "SELECT tortId FROM Tort_Comanda WHERE comandaId = ?";
            PreparedStatement tortComandaStatement = connection.prepareStatement(tortComandaQuery);
            tortComandaStatement.setInt(1, comandaId);
            ResultSet tortComandaResultSet = tortComandaStatement.executeQuery();

            while (tortComandaResultSet.next()) {
                int tortId = tortComandaResultSet.getInt("tortId");

                String tortQuery = "SELECT * FROM Tort WHERE Id = ?";
                PreparedStatement tortStatement = connection.prepareStatement(tortQuery);
                tortStatement.setInt(1, tortId);
                ResultSet tortResultSet = tortStatement.executeQuery();

                if (tortResultSet.next()) {
                    String tip = tortResultSet.getString("Tip");
                    tortList.add(tip);
                }
            }
        }
        catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return tortList;
    }
}
