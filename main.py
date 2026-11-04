from src.sistema import SistemaGestion

def main():
    sys = SistemaGestion()
    
    print("--- Inicializando prueba de sistema base ---")
    id1 = sys.reg_sol("E1", "Juan Perez", "juan@mail.com", "ACADEMICA", "Reclamo de nota", "ALTA")
    id2 = sys.reg_sol("E2", "Maria Gomez", "maria@mail.com", "CERTIFICADO", "Pedido de analitico", "MEDIA")
    
    sys.asig_resp(id1, "R1", "Carlos Ruiz", "Bedelia")
    sys.chg_st(id1, "EN_PROCESO")
    
    print("\n--- Listado filtrado (PENDIENTES) ---")
    pends = sys.buscar(k_estado="PENDIENTE")
    for p in pends:
        print("Pendiente:", p["id"], p["descripcion"])
        
    print("\n--- Reporte ---")
    sys.rep_basico()

if __name__ == "__main__":
    main()