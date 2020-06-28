  
#!/bin/bash

entrypoint(){
    #run migration
    # cd /app/maju/maju
    # echo "applying migrations..."
    # alembic upgrade head

    cd /app/maju
    # run webserver
    echo "starting webserver ...."
    uwsgi --ini /app/maju/run.ini

}

entrypoint