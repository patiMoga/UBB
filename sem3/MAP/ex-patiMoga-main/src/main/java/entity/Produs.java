package entity;

import java.io.Serializable;

public class Produs extends Entity implements Serializable {
    private Integer uniqueID;
    private String marca;
    private String nume;
    private double pret;
    private int cantitate;

    public Produs() {
    }

    public Produs(Integer id, String marca, String nume, double pret, int cantitate) {
        this.uniqueID = id;
        this.marca = marca;
        this.nume = nume;
        this.pret = pret;
        this.cantitate = cantitate;
    }


    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public double getPret() {
        return pret;
    }

    public void setPret(double pret) {
        this.pret = pret;
    }

    public int getCantitate() {
        return cantitate;
    }

    public void setCantitate(int cantitate) {
        this.cantitate = cantitate;
    }

    @Override
    public String toString() {
        if(cantitate == 0)
            return "n/a";
        return "id=" + uniqueID +
                ", marca='" + marca + '\'' +
                ", nume='" + nume + '\'' +
                ", pret=" + pret +
                ", cantitate=" + cantitate +
                '}';
    }

    @Override
    public void setUniqueID(Integer uniqueID) {
        this.uniqueID = uniqueID;
    }

    @Override
    public Integer getUniqueID() {
        return uniqueID;
    }

}
