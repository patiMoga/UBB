package repository;

import entity.Entity;
import factory.IEntityFactory;

import java.io.*;
import java.util.Collection;
import java.util.Scanner;

public class FileRepo<T extends Entity> extends Repo<T> {
    private String fileName;
    private IEntityFactory<T> entityF;

    public FileRepo(String fileName,IEntityFactory<T> entityF) throws FileNotFoundException, DuplicateException {
        this.fileName = fileName;
        this.entityF=entityF;

        loadFromFile();
    }
    private void loadFromFile() throws FileNotFoundException, DuplicateException {
        File file=new File(fileName);
        Scanner scanner=new Scanner(file);
        while(scanner.hasNextLine()){
            String line=scanner.nextLine();
            T entity=entityF.createEntity(line);
            add(entity);
        }
    }
    private void clearFile(){
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            writer.write("");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveToFile(){
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            Collection<T> coll=getAll();
            for(T entity:coll){
                writer.write(entityF.toStringFactory(entity));
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    public void add(T entity) throws DuplicateException {
        super.add(entity);
        clearFile();
        saveToFile();


    }
    public void delete(int id){
        super.delete(id);
        clearFile();
        saveToFile();
    }

    @Override
    public void update(T entity) {
        super.update(entity);
        clearFile();
        saveToFile();
    }
}
