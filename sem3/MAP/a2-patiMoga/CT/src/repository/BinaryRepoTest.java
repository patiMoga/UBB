package repository;

import entity.Entity;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

class BinaryRepoTest {

    private static class TestEntity extends Entity {
        public TestEntity(int ID) {
            super(ID);
        }
    }

    private static class TestBinaryRepo extends BinaryRepo<TestEntity> {
        public TestBinaryRepo(String fileName) {
            super(fileName);
        }
    }

    @Test
    void add() {
        TestBinaryRepo binaryRepo = new TestBinaryRepo("testfile_add.bin");
        TestEntity entity = new TestEntity(1);

        assertDoesNotThrow(() -> binaryRepo.add(entity));
        assertTrue(binaryRepo.getAll().contains(entity));
    }

    @Test
    void delete() {
        TestBinaryRepo binaryRepo = new TestBinaryRepo("testfile_delete.bin");
        TestEntity entity = new TestEntity(1);
        assertDoesNotThrow(() -> binaryRepo.add(entity));

        assertDoesNotThrow(() -> binaryRepo.delete(1));
        assertFalse(binaryRepo.getAll().contains(entity));
    }

    @Test
    void update() {
        TestBinaryRepo binaryRepo = new TestBinaryRepo("testfile_update.bin");
        TestEntity entity = new TestEntity(1);
        assertDoesNotThrow(() -> binaryRepo.add(entity));

        assertDoesNotThrow(() -> binaryRepo.update(1, "newString"));
    }

    @Test
    void loadFromFile_FileNotFound() {
        TestBinaryRepo binaryRepo = new TestBinaryRepo("nonexistentfile.bin");
        assertThrows(RuntimeException.class, binaryRepo::getAll);
    }

    @Test
    void loadFromFile_IOException() {
        // Arrange
        TestBinaryRepo binaryRepo = new TestBinaryRepo("unreadablefile.bin");
        File file = new File("unreadablefile.bin");
        file.setReadable(false);
        assertThrows(RuntimeException.class, binaryRepo::getAll);

    }

    @Test
    void saveFile_FileNotFound() {
        TestBinaryRepo binaryRepo = new TestBinaryRepo("readonlyfile.bin");
        File file = new File("readonlyfile.bin");
        file.setReadOnly();
        assertThrows(IOException.class, binaryRepo::saveFile);

        file.setWritable(true);
    }

    @Test
    void saveFile_IOException() {
        String nonExistentDirectory = "nonexistentdirectory";
        String fileName = nonExistentDirectory + "/unwritablefile.bin";
        TestBinaryRepo binaryRepo = new TestBinaryRepo(fileName);
        assertThrows(IOException.class, binaryRepo::saveFile);
    }

    @Test
    void clearFile_IOException() {
        TestBinaryRepo binaryRepo = new TestBinaryRepo("unwritablefile.bin");
        File file = new File("unwritablefile.bin");
        file.setReadOnly();
        assertThrows(IOException.class, binaryRepo::clearFile);

        file.setWritable(true);
    }
}
