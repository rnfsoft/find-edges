
$ docker build -t find-edges .
$ docker run -v "$(pwd)":/app find-edges
$ docker ps -q -a | xargs docker rm


Reference:
    https://pixabay.com/photos/lake-sailboat-senior-sailing-it-4466290/
    https://towardsdatascience.com/find-face-edges-in-20-lines-of-code-from-scratch-8058e128c013
    