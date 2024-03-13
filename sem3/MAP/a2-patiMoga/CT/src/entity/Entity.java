package entity;

import java.io.Serializable;
import java.util.Objects;

public abstract class Entity implements Serializable {
    protected int id;

    public Entity(int id) {
        this.id = id;
    }

    public int getID() {
        return id;
    }

    public void modify(String string) {}
}

