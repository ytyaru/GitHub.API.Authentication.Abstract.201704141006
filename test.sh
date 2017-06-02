#!/bin/bash
path_dir_pj=$(cd $(dirname $0) && pwd)
#path_dir_pj=`dirname ${path_dir_pj}`
#export PYTHONPATH=path_dir_pj
#path_dir_pj=${path_dir_pj}/test
#echo ${path_dir_pj}
python3 -m unittest test_NonAuthentication.py
python3 -m unittest test_BasicAuthentication.py
python3 -m unittest test_TwoFactorAuthentication.py
python3 -m unittest test_OAuthAuthentication.py
python3 -m unittest test_OAuthTokenFromDatabaseAuthentication.py
python3 -m unittest test_OAuthTokenFromDatabaseAndCreateApiAuthentication.py
#python3 -m unittest ${path_dir_pj}/test_NonAuthentication.py
#python3 -m unittest /tmp/GitHub.API.Authentication.Abstract.201704141006/test_NonAuthentication.py
#python3 -m unittest discover -s ${path_dir_pj} ./test/test_NonAuthentication.py
#python3 -m unittest discover -s ${path_dir_pj} test_BasicAuthentication.py
