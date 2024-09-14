# TiVPO-PR1

## Запуск приложения

Для запуска приложению нужно передать путь до фала с описанием символов. В данном
случаем испольуется файл-пример (examples/input_example.txt)

```bash
git clone https://github.com/YAPONE4/TiVPO-PR1
cd TiVPO-PR1
python3 tivpo_pr1/__main__.py examples/input_example.txt
```

## Сборка и запуск приложения как zippapp

```bash
cd TiVPO-PR1
python3 -m zipapp tivpo_pr1
python3 tivpo_pr1.pyz examples/input_example.txt
```