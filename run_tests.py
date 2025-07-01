import logging


def main():
    logging.info("Iniciando pruebas...")
    try:
        pytest.main(["-v", "web_tests/tests/"])
        logging.info("Pruebas completadas")
    except Exception as e:
        logging.error(f"Error: {str(e)}")

        logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='qa_execution.log'
)
