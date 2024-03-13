package factory;

import entity.Comanda;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ComandaFactoryTest {

    @Test
    void createEntity() {
        ComandaFactory comandaFactory = new ComandaFactory();
        String inputLine = "1;Chocolate,Vanilla;2023-12-31";

        Comanda comanda = comandaFactory.createEntity(inputLine);

        assertEquals(1, comanda.getID());
        assertEquals(Arrays.asList("Chocolate", "Vanilla"), comanda.getTorturi());
        assertEquals("2023-12-31", comanda.getData());
    }

    @Test
    void toStringFactory() {
        // Arrange
        ComandaFactory comandaFactory = new ComandaFactory();
        Comanda comanda = new Comanda(1, Arrays.asList("Chocolate", "Vanilla"), "2023-12-31");

        // Act
        String resultString = comandaFactory.toStringFactory(comanda);

        // Assert
        assertEquals("1;Chocolate,Vanilla;2023-12-31", resultString);
    }
}
