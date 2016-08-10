if [ $1 = "wget" ]
then
  wget https://pypi.python.org/packages/16/5e/62ccc6a4a154e0822f02b3918fb4c666130bf54b2fa4e0a7fa43057c3bf2/SpeechRecognition-3.4.6.tar.gz
elif [ $1 = "curl" ]
then
  curl -OL https://pypi.python.org/packages/16/5e/62ccc6a4a154e0822f02b3918fb4c666130bf54b2fa4e0a7fa43057c3bf2/SpeechRecognition-3.4.6.tar.gz
fi
tar -zxvf  SpeechRecognition-3.4.6.tar.gz
cd SpeechRecognition-3.4.6
python setup.py install --user
