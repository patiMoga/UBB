package service;

import entity.Comanda;
import entity.Tort;
import repository.DuplicateException;
import repository.IRepository;

import java.util.Collection;
import java.util.List;

public class Service {
    IRepository<Tort> repot;
    IRepository<Comanda> repoc;

    public Service(IRepository<Tort> repot, IRepository<Comanda> repoc){
        this.repot=repot;
        this.repoc=repoc;
    }
    public void addt(int id,String tip) throws DuplicateException {
        repot.add(new Tort(id,tip));
    }
    public Collection<Tort> getAllt(){
        return repot.getAll();
    }

    public void deletet(int id)
    {
        repot.delete(id);
    }
    public void updatet(Tort t)
    {
        repot.update(t);
    }
    public Tort getByIdt(int id){
         return repot.getById(id);
    }




    public void addc(int id, List<String> torturi, String data) throws DuplicateException {
        Comanda c=new Comanda(id,torturi,data);
          repoc.add(c);
    }
    public Collection<Comanda> getAllc(){
        return repoc.getAll();
    }

    public void deletec(int id)
    {
        repoc.delete(id);
    }
    public void updatec(Comanda c)
    {
        repoc.update(c);
    }
    public Comanda getByIdc(int id){
        return repoc.getById(id);
    }
}
