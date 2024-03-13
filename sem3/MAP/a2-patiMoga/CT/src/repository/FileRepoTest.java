package repository;

import entity.Entity;
import factory.IEntityFactory;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.IOException;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class FileRepoTest {

    private static final String TEST_FILE_NAME = "testfile.txt";

    private static class TestEntity extends Entity {
        public TestEntity(int ID) {
            super(ID);
        }
    }

    private static class TestEntityFactory implements IEntityFactory<TestEntity> {
        @Override
        public TestEntity createEntity(String line) {
            int id = Integer.parseInt(line);
            return new TestEntity(id);
        }

        @Override
        public String toStringFactory(TestEntity entity) {
            return String.valueOf(entity.getID());
        }
    }

    private FileRepo<TestEntity> fileRepo;

    @BeforeEach
    void setUp() {
        try {
            File testFile = new File(TEST_FILE_NAME);
            testFile.createNewFile();
            fileRepo = new FileRepo<>(TEST_FILE_NAME, new TestEntityFactory());
        } catch (IOException | DuplicateException e) {
            e.printStackTrace();
        }
    }

    @Test
    void add() {
        TestEntity entity = new TestEntity(1);
        assertDoesNotThrow(() -> fileRepo.add(entity));

        assertTrue(fileRepo.getAll().contains(entity));
    }

    @Test
    void delete() {
        TestEntity entity = new TestEntity(1);
        assertDoesNotThrow(() -> fileRepo.add(entity));
        assertDoesNotThrow(() -> fileRepo.delete(1));
        assertFalse(fileRepo.getAll().contains(entity));
    }

    @Test
    void update() {
        TestEntity entity = new TestEntity(1);
        assertDoesNotThrow(() -> fileRepo.add(entity));

        assertDoesNotThrow(() -> fileRepo.update(1, "newString"));

    }
}
