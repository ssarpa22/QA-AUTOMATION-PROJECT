#  QA Automation Project  
**Automatización de pruebas para E-commerce (Web + API)**  

##  Tecnologías  
- **UI Testing**: Selenium WebDriver + Python + pytest  
- **API Testing**: Postman + Newman  
- **CI/CD**: GitHub Actions  

##  Estructura del Proyecto  
```bash
/qa-automation-project  
├── web-tests/       # Tests de interfaz web  
├── api-tests/       # Tests de API  
├── docs/            # Documentación  
└── .github/         # Automatización con GitHub Actions  
```

##  Como Ejecutar  
### Tests UI (Selenium):  
```bash
pip install -r requirements.txt  
pytest web-tests/tests/test_login.py --browser=chrome  
```

### Tests API (Postman):  
```bash
newman run api-tests/collections/ecommerce_api.postman_collection.json  
```

##  Reportes  
- **Allure Reports** para tests UI (ver `/allure-report` después de ejecutar).  
- **HTML Reports** para Postman.  

##  Proximos Pasos  
- [ ] Añadir pruebas móviles con Appium  
- [ ] Integrar con Jenkins  

---

 **Creado por Ignacio Martínez** | [LinkedIn](www.linkedin.com/in/ignacio-martinez-qa) | ✉️ naching13@gmail.com  
