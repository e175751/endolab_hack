import respond_to
import listen_to

@respond_to('test')
def test1(message):
    message.reply('test1 pass!')

@listen_to('test2')
def test2(message):
    message.reply('test2 pass!')