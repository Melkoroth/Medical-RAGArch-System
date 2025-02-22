
import pytest
import importlib

# Listado de módulos a probar
modules_to_test = [
    'app',
    'main',
    'scripts.update_prompts',
    'scripts.rollback',
    'modules.analytics_comparison',
    'modules.dynamodb_optimization',
    'modules.ragarch_sources_config',
    'modules.redis_cloud',
    'modules.drug_interaction_api',
    'modules.ocr_aes256_jwt',
    'frontend.interface'
]

# Test para verificar que todos los módulos se importan correctamente
@pytest.mark.parametrize("module_name", modules_to_test)
def test_import_modules(module_name):
    try:
        importlib.import_module(module_name)
    except ModuleNotFoundError:
        pytest.fail(f"Module {module_name} not found.")
    except Exception as e:
        pytest.fail(f"Error importing {module_name}: {str(e)}")

# Test para verificar que los mocks funcionan correctamente
def test_mocks():
    from tests.mock_external_services_optimized import patch
    assert patch is not None, "Mock no se ha aplicado correctamente"
