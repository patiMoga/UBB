package service;

import entity.Comanda;
import entity.Tort;
import org.junit.jupiter.api.Test;
import repository.DuplicateException;
import repository.IRepository;
import repository.Repo;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class ServiceTest {

    @Test
    void addt() throws DuplicateException {
        IRepository<Tort> mockTortRepository = new Repo<>();
        IRepository<Comanda> mockComandaRepository = new Repo<>();
        Service service = new Service(mockTortRepository, mockComandaRepository);
        service.addt(1, "Chocolate Cake");
        assertEquals(1, mockTortRepository.getAll().size());
        assertEquals(1, mockTortRepository.getById(1).getID());
        assertEquals("Chocolate Cake", mockTortRepository.getById(1).getTip());
    }

    @Test
    void getAllt() {
        IRepository<Tort> mockTortRepository = new Repo<>();
        IRepository<Comanda> mockComandaRepository = new Repo<>();
        Service service = new Service(mockTortRepository, mockComandaRepository);

        Collection<Tort> result = service.getAllt();

        assertNotNull(result);
        assertEquals(0, result.size());
    }

    @Test
    void deletet() throws DuplicateException {
        IRepository<Tort> mockTortRepository = new Repo<>();
        IRepository<Comanda> mockComandaRepository = new Repo<>();
        Service service = new Service(mockTortRepository, mockComandaRepository);
        service.addt(1, "Chocolate Cake");

        service.deletet(1);

        assertEquals(0, mockTortRepository.getAll().size());
    }

    @Test
    void updatet() throws DuplicateException {
        IRepository<Tort> mockTortRepository = new Repo<>();
        IRepository<Comanda> mockComandaRepository = new Repo<>();
        Service service = new Service(mockTortRepository, mockComandaRepository);
        service.addt(1, "Chocolate Cake");

        service.updatet(1, "New Flavor");

        assertEquals("New Flavor", mockTortRepository.getById(1).getTip());
    }

    @Test
    void getByIdt() throws DuplicateException {
        IRepository<Tort> mockTortRepository = new Repo<>();
        IRepository<Comanda> mockComandaRepository = new Repo<>();
        Service service = new Service(mockTortRepository, mockComandaRepository);
        service.addt(1, "Chocolate Cake");

        Tort result = service.getByIdt(1);

        assertNotNull(result);
        assertEquals(1, result.getID());
        assertEquals("Chocolate Cake", result.getTip());
    }

    @Test
    void addc() throws DuplicateException {
        // Arrange
        IRepository<Tort> mockTortRepository = new Repo<>();
        IRepository<Comanda> mockComandaRepository = new Repo<>();
        Service service = new Service(mockTortRepository, mockComandaRepository);
        List<String> torturi = Arrays.asList("Chocolate Cake", "Strawberry Cake");

        // Act
        service.addc(1, torturi, "2023-01-01");

        // Assert
        assertEquals(1, mockComandaRepository.getAll().size());
        assertEquals(1, mockComandaRepository.getById(1).getID());
        assertEquals(torturi, mockComandaRepository.getById(1).getTorturi());
        assertEquals("2023-01-01", mockComandaRepository.getById(1).getData());
    }

    @Test
    void getAllc() {
        // Arrange
        IRepository<Tort> mockTortRepository = new Repo<>();
        IRepository<Comanda> mockComandaRepository = new Repo<>();
        Service service = new Service(mockTortRepository, mockComandaRepository);

        // Act
        Collection<Comanda> result = service.getAllc();

        // Assert
        assertNotNull(result);
        assertEquals(0, result.size());
    }

    @Test
    void deletec() throws DuplicateException {
        // Arrange
        IRepository<Tort> mockTortRepository = new Repo<>();
        IRepository<Comanda> mockComandaRepository = new Repo<>();
        Service service = new Service(mockTortRepository, mockComandaRepository);
        service.addc(1, Arrays.asList("Chocolate Cake"), "2023-01-01");

        // Act
        service.deletec(1);

        // Assert
        assertEquals(0, mockComandaRepository.getAll().size());
    }

    @Test
    void updatec() throws DuplicateException {
        // Arrange
        IRepository<Tort> mockTortRepository = new Repo<>();
        IRepository<Comanda> mockComandaRepository = new Repo<>();
        Service service = new Service(mockTortRepository, mockComandaRepository);
        service.addc(1, Arrays.asList("Chocolate Cake"), "2023-01-01");

        // Act
        service.updatec(1, "New Data");

        // Assert
        assertEquals("New Data", mockComandaRepository.getById(1).getData());
    }

    @Test
    void getByIdc() throws DuplicateException {
        // Arrange
        IRepository<Tort> mockTortRepository = new Repo<>();
        IRepository<Comanda> mockComandaRepository = new Repo<>();
        Service service = new Service(mockTortRepository, mockComandaRepository);
        service.addc(1, Arrays.asList("Chocolate Cake"), "2023-01-01");

        // Act
        Comanda result = service.getByIdc(1);

        // Assert
        assertNotNull(result);
        assertEquals(1, result.getID());
        assertEquals(Arrays.asList("Chocolate Cake"), result.getTorturi());
        assertEquals("2023-01-01", result.getData());
    }


}
