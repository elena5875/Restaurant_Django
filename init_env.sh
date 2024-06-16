# init_env.sh
#!/bin/bash
if [ -f .env ]; then
    export $(cat .env | xargs)
fi
