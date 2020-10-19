import json
from urllib import parse,request
import webhoseio

def read_webhose_key():
    webhose_api_key = None
    try:
        with open('search.key','r') as f:
            webhose_api_key = f.readline().strip()
    except:
        raise IOError('search.key not found')
    return webhose_api_key 
def run_query(search_term,size=10):
    webhose_api_key = read_webhose_key()
    if not webhose_api_key:
        raise KeyError('webhose key not found')
    root_url = 'http://webhose.io/search'
    
    query_string = parse.quote(search_term)
    
    search_url = ('{root_url}?token={key}&format=json&q={query}'
    '&sort=relevancy&size={size}').format(root_url=root_url,key=webhose_api_key,query=query_string,size=size)

    results = []
    
    try:
        response = request.urlopen(search_url).read().decode('utf-8')
        json_response = json.loads(response)

        for post in json_response['posts']:
            results.append({'titile':post['title'],'link':post['url'],'summary':post['text'][:200]})
    except:
        print('error while querying the API')
    return  results
def undependant():
    query = input('what are you searching for ?')
    threads = input('how many results you want ?')
    with open('tango_django/search.key','r') as f:
        key = f.readline()
    try:
        webhoseio.config(token=key)
        results = webhoseio.query("filterWebContent",{"q":query})
        for i in range(len(threads)):
            print(results['posts'][i]['text'])
        # for post in results['posts'][:10]['text']:
        #     count += 1
        #     print(f'result number {count} \n {post}')
    except KeyError as err:
        print(f'ooopsie :{err}')
    

if __name__ =='__main__':
    print('search api is running undepandantly !')
    undependant()
    

