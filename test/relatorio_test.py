import pytest

if __name__ == "__main__":
    # Executar os testes e gerar o relatório XML
    pytest.main([
        '--maxfail=1',  # Máximo de falhas antes de interromper os testes
        '--disable-warnings',  # Desabilitar os avisos
        '--junitxml=test-reports/results.xml'  # Gerar o relatório XML
    ])
