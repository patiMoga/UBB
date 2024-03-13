package repository;

import database.DBConnection;
import entity.Tort;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class TortDatabaseRepo extends Repo<Tort> {

    private Connection connection = DBConnection.getConnection();


    public TortDatabaseRepo() {
        loadFromDatabase();
    }

    private void loadFromDatabase() {
        try {
            String query = "SELECT * FROM Tort";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                int id = resultSet.getInt("Id");
                String tip = resultSet.getString("Tip");
                entities.add(new Tort(id, tip));
            }
        }
        catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
    @Override
    public void add(Tort tort) throws DuplicateException {
        super.add(tort);
        int id = tort.getID();
        String tip = tort.getTip();
        String query = "INSERT INTO Tort (Id, Tip) VALUES (?, ?)";
        try{
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setInt(1, id);
            statement.setString(2, tip);
            statement.executeUpdate();
        }

        catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void delete(int id) {
        super.delete(id);
        String query = "DELETE FROM Tort WHERE Id = ?";
        try {
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setInt(1, id);
            statement.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
    @Override
    public void update(Tort tort) {
        super.update(tort);
        String query = "UPDATE Tort SET Tip = ? WHERE Id = ?";
        try {
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, tort.getTip());
            statement.setInt(2, tort.getID());
            statement.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
