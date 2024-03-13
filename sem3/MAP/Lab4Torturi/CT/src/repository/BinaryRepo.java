package repository;

import entity.Entity;

import java.io.*;

public class BinaryRepo<T extends Entity> extends Repo<T>{
    private final String fileName;

    public BinaryRepo(String fileName) {
        this.fileName = fileName;
        loadFromFile();
    }
    private void loadFromFile() {
        try (ObjectInputStream input = new ObjectInputStream(new FileInputStream(fileName))) {
            while (true) {
                super.add((T)input.readObject());
            }
        } catch (FileNotFoundException e) {
            try {
                new File(fileName).createNewFile();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
            throw new RuntimeException(e);

        } catch (EOFException e) {

        } catch (IOException e) {

        } catch (DuplicateException e) {
            throw new RuntimeException(e);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }

    }
    private void saveFile(){
        try (ObjectOutputStream output = new ObjectOutputStream(new FileOutputStream(fileName))) {
            for(T entity : entities){
                output.writeObject(entity);
            }
        } catch (FileNotFoundException fileNotFoundException) {
            try {
                new File(fileName).createNewFile();
            }catch (IOException ioException){

            }

        }catch (IOException ioException){

        }
    }
    private void clearFile(){
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            writer.write("");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Override
    public void add(T entity) throws DuplicateException {
        super.add(entity);
        clearFile();
        saveFile();
    }

    @Override
    public void delete(int id) {
        super.delete(id);
        clearFile();
        saveFile();
    }

    @Override
    public void update(T entity) {
        super.update(entity);
        clearFile();
        saveFile();
    }
}

