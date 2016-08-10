if [ $1 = "wget" ]
then
  wget https://pypi.python.org/packages/16/5e/62ccc6a4a154e0822f02b3918fb4c666130bf54b2fa4e0a7fa43057c3bf2/SpeechRecognition-3.4.6.tar.gz
  wget https://pypi.python.org/packages/d0/dc/ffb9ce5e3f19bd289902915a9f68b7d199216065f8ea17d5b5e8e4ad86ee/PyAudio-0.2.9.tar.gz
elif [ $1 = "curl" ]
then
  curl -OL https://pypi.python.org/packages/16/5e/62ccc6a4a154e0822f02b3918fb4c666130bf54b2fa4e0a7fa43057c3bf2/SpeechRecognition-3.4.6.tar.gz
  curl -OL https://pypi.python.org/packages/d0/dc/ffb9ce5e3f19bd289902915a9f68b7d199216065f8ea17d5b5e8e4ad86ee/PyAudio-0.2.9.tar.gz
fi
tar -zxvf  SpeechRecognition-3.4.6.tar.gz
tar -zxvf PyAudio-0.2.9.tar.gz
cd SpeechRecognition-3.4.6
python setup.py install --user
cd ..
cd PyAudio-0.2.9
python setup.py install --user
cd ..
if [ $2 = "keep" ]
then
  rm SpeechRecognition-3.4.6.tar.gz
  rm pyPortAudio.tar.gz
  exit 0
fi
rm -rf SpeechRecognition-3.4.6
rm -rf PyAudio-0.2.9
rm SpeechRecognition-3.4.6.tar.gz
rm PyAudio-0.2.9.tar.gz
