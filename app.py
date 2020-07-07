__author__ = 'vikesh'

import os
import wolframalpha
from flask import Flask, request, Response, redirect






app = Flask(__name__)

client = wolframalpha.Client('PWTW9A-VQL5TVEGPY')


@app.route('/thel',methods=['post'])
def thel():
    '''
    :Example:
    /thel current weather in mumbai?
    '''
    text = request.values.get('text')
    try:
        res = client.query(text)
    except UnicodeEncodeError:
        return Response(('Sorry I did\'t get you. Would you please simplify your query?'
                        '%s is not valid input.' % text),
                        content_type='text\plain; charset=utf-8')
    resp_qs = ['Hi Top Answer for "%s"\n' % text]
    resp_qs.extend(next(res.results).text)

    return Response(''.join(resp_qs),
                    content_type='text/plain; chatset=utf-8')

@app.route('/')
def hello():
    return redirect('https://github.com/stpaul2coderdojo/slack-TheL')


if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
