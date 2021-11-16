

# Estudos com Selenium e Python


## Pre Requisitos
 - Selenium WebDrivers (GeckoDriver,ChromeDriver)
 - OpenJDK 17
 - Python >= 3.10



## Testes com Selenium WebDriver(Documentação incompleta)

- Webdriver - um tipo de servidor web que permite que o -selenium se conecte com o browser
- GeckoDriver - firefox
- ChromeDriver - chrome

## Testes com Selenium GRID (Em Desenvolvimento)

### Arquitetura do Sistema 
 --Imagem com a arquitetura

### Como Testar
 - Inicialmente , execute o .jar do selenium server com o comando para iniciar o HUB


 ```
    java -jar selenium-server.jar hub
 ```

- Para registrar um Node valido para execucao a automação execute

```
    java -jar selenium-server.jar node
```

- Para registrar um Node a um Hub que esta em outra rede utilize
```
    java -jar .\selenium-server.jar node --config config.json
```
-nota: Caso precise , altere o endereço no arquivo config.json
