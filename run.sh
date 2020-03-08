case $1 in
   "dev")
        export FLASK_APP=app
        export FLASK_ENV=development
        flask run -p 5005
        ;;
   "prod")
        export FLASK_APP=app    
        export FLASK_ENV=production
        flask run -p 5005
        ;;
   *) echo "acceptable command line args: dev or prod"
        ;;
esac