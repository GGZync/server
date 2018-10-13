# Plan

## Basic directories

```yaml
./
  Pipfile
  init.py
  serve.py
  main.py
```

## Scripts

### **serve**

```bash
ggz serve [--host=0.0.0.0] [--port=7447]
```

### **install**

```bash
ggz install <github-user@github.com/github-repo>
```

### **run**

```bash
ggz run <app-name | github-user@github.com/github-repo>
```

## Extended directories

### After **"pipenv run init.py"**

```yaml
./
  apps/
  bin/
    ggz.sh | ggz.bat
  Pipfile
  serve.py
  main.py
```

### After **pipenv install GGZync@github.com/Circular-Menu**

```yaml
./
  apps/
    Circular-Menu-34EF63D/
      ...
      (Application files)
      main.py
  
  
```