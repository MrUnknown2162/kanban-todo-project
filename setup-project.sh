#!/bin/bash

echo "🚀 Tạo cấu trúc dự án Kanban TODO App trong thư mục kanban-todo-project..."

# Tạo thư mục root
mkdir -p kanban-todo-project
cd kanban-todo-project || exit 1

# Backend folders và files
mkdir -p kanban-todo-api/app/core
touch kanban-todo-api/app/core/__init__.py
touch kanban-todo-api/app/core/config.py
touch kanban-todo-api/app/core/security.py
touch kanban-todo-api/app/core/deps.py

mkdir -p kanban-todo-api/app/database
touch kanban-todo-api/app/database/__init__.py
touch kanban-todo-api/app/database/connection.py
touch kanban-todo-api/app/database/models.py
touch kanban-todo-api/app/database/repository.py

mkdir -p kanban-todo-api/app/routers
touch kanban-todo-api/app/routers/__init__.py
touch kanban-todo-api/app/routers/auth.py
touch kanban-todo-api/app/routers/users.py
touch kanban-todo-api/app/routers/boards.py
touch kanban-todo-api/app/routers/tasks.py

mkdir -p kanban-todo-api/app/schemas
touch kanban-todo-api/app/schemas/__init__.py
touch kanban-todo-api/app/schemas/user.py
touch kanban-todo-api/app/schemas/board.py
touch kanban-todo-api/app/schemas/task.py

mkdir -p kanban-todo-api/scripts
touch kanban-todo-api/scripts/seed_data.py
touch kanban-todo-api/scripts/reset_database.py
touch kanban-todo-api/scripts/backup_database.py

mkdir -p kanban-todo-api/tests
touch kanban-todo-api/tests/__init__.py
touch kanban-todo-api/tests/test_auth.py
touch kanban-todo-api/tests/test_users.py
touch kanban-todo-api/tests/test_boards.py
touch kanban-todo-api/tests/test_tasks.py
touch kanban-todo-api/tests/conftest.py

touch kanban-todo-api/.env.example
touch kanban-todo-api/.env
touch kanban-todo-api/.gitignore
touch kanban-todo-api/requirements.txt
touch kanban-todo-api/alembic.ini
touch kanban-todo-api/README.md

# Frontend folders và files
mkdir -p kanban-frontend/assets/css
mkdir -p kanban-frontend/assets/js
mkdir -p kanban-frontend/assets/lib
mkdir -p kanban-frontend/assets/images
mkdir -p kanban-frontend/assets/fonts
mkdir -p kanban-frontend/tests
mkdir -p kanban-frontend/docs

touch kanban-frontend/index.html
touch kanban-frontend/login.html
touch kanban-frontend/register.html

touch kanban-frontend/assets/css/style.css
touch kanban-frontend/assets/css/login.css
touch kanban-frontend/assets/css/responsive.css
touch kanban-frontend/assets/css/themes.css

touch kanban-frontend/assets/js/api.js
touch kanban-frontend/assets/js/auth.js
touch kanban-frontend/assets/js/app.js
touch kanban-frontend/assets/js/kanban.js
touch kanban-frontend/assets/js/utils.js
touch kanban-frontend/assets/js/config.js

touch kanban-frontend/assets/lib/sortable.min.js
touch kanban-frontend/assets/lib/axios.min.js

touch kanban-frontend/assets/images/.gitkeep
touch kanban-frontend/assets/fonts/.gitkeep

touch kanban-frontend/tests/auth.test.js
touch kanban-frontend/tests/api.test.js
touch kanban-frontend/tests/kanban.test.js

touch kanban-frontend/.gitignore
touch kanban-frontend/README.md
touch kanban-frontend/package.json

# Documentation
mkdir -p docs/api
for i in 1 2 3 4 5 6 7 8; do
  mkdir -p docs/buoi-$i
  touch docs/buoi-$i/README.md
done
touch docs/README.md
touch docs/PROJECT_OVERVIEW.md
touch docs/ARCHITECTURE.md
touch docs/DEPLOYMENT_GUIDE.md
touch docs/api/ENDPOINTS.md
touch docs/api/AUTHENTICATION.md
touch docs/api/SCHEMAS.md


touch .gitignore
touch README.md
touch LICENSE
touch CHANGELOG.md
touch CONTRIBUTING.md

echo "✅ Tất cả cấu trúc dự án đã nằm trong thư mục kanban-todo-project."
