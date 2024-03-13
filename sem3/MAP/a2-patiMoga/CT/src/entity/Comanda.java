package entity;
import java.util.List;
import java.util.*;

public class Comanda extends Entity {
    private List<String> torturi;
    private String data;
    public Comanda( int ID,List<String> torturi, String data) {
        super(ID);
        this.torturi = torturi;
        this.data = data;
    }
    public List<String> getTorturi() {
        return torturi;
    }

    @Override
    public void modify(String string) {
        this.data=string;
    }

    public String getData() {
        return data;
    }
    @Override
    public String toString() {
        return "Comanda{" +
                "id=" + id +
                ", torturi=" + torturi +
                ", data=" + data + '}';}}
