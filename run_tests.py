import logging
import pytest

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('qa_execution.log'),
        logging.StreamHandler()
    ]
)

def main():
    logging.info("Iniciando pruebas...")
    try:
        exit_code = pytest.main(["-v", "web_tests/tests/"])
        
        if exit_code == 0:
            logging.info("Todas las pruebas pasaron exitosamente")
        else:
            logging.warning(f"Algunas pruebas fallaron (Código: {exit_code})")
            
    except Exception as e:
        logging.error(f"Error inesperado: {str(e)}")
        raise  

if __name__ == "__main__":
    main()
