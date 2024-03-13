package entity;

import java.util.Objects;

public class Tort extends Entity {
    private String tip;
    private static final String DELIMITER = ";";

    public Tort(int ID, String tip) {
        super(ID);
        this.tip = tip;
    }

    public String getTip() {
        return tip;
    }

    public void setTip(String tip) {
        this.tip = tip;
    }

    @Override
    public String toString() {
        return "Tort{" +
                "id=" + id +
                ", tip='" + tip + '\'' +
                '}';
    }
}
