package repository;

import entity.Entity;

import java.util.ArrayList;

public abstract class AbsRepo<T extends Entity> implements IRepository<T> {
    protected ArrayList<T> entities = new ArrayList<>();
}