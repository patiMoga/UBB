package entity;

public class Tort extends Entity {
    private String tip;

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
    public void modify(String string) {
        this.tip=string;
    }

    @Override
    public String toString() {
        return "Tort{" +
                "id=" + id +
                ", tip='" + tip + '\'' +
                '}';
    }
}
