package entity;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class ComandaTest {

    @Test
    void modify() {
        List<String> torturi = Arrays.asList("Chocolate", "Vanilla", "Strawberry");
        Comanda comanda = new Comanda(1, torturi, "2023-12-31");

       comanda.modify("2023-02-04");
       assertEquals(comanda.getData(),"2023-02-04");

    }


    @Test
    void getTorturi() {
        List<String> torturi = Arrays.asList("Chocolate", "Vanilla", "Strawberry");
        Comanda comanda = new Comanda(1, torturi, "2023-12-31");
        assertEquals(torturi, comanda.getTorturi());
        Comanda emptyComanda = new Comanda(2, new ArrayList<>(), "2024-01-01");
        assertEquals(new ArrayList<>(), emptyComanda.getTorturi());
    }

    @Test
    void getData(){
        Comanda comanda = new Comanda(1, Arrays.asList("Chocolate"), "2023-12-31");

        String resultData = comanda.getData();

        assertEquals("2023-12-31", resultData);
    }

    @Test
    void testToString() {
        List<String> torturi = Arrays.asList("Chocolate", "Vanilla", "Strawberry");
        Comanda comanda = new Comanda(1, torturi, "2023-12-31");

        String resultToString = comanda.toString();

        assertEquals("Comanda{id=1, torturi=[Chocolate, Vanilla, Strawberry], data=2023-12-31}", resultToString);
    }
}