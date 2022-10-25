import shodan

SHODAN_API_Key = "{Enter your Shodan API Key}"

Hit_the_API = shodan.Shodan(SHODAN_API_Key)

My_Output_File = open('List-of-SpringBootServers.txt', 'a')

Search_Query = "http.favicon.hash:116323821"

try:
    Output = Hit_the_API.search(Search_Query)
    print('Results Found: {}'.format(Output['total']))
    for result in Output['matches']:
        print('IP: {}'.format(result['ip_str']+':'+str(result['port'])))
        if result['port']==80:
            State = "http://"
        else:
            State = "https://"
        Out = State+result['ip_str']
    else:
        out = "http://"+result['ip_str']+':'+str(result['port'])
    My_Output_File.write(Out+'\n')
    print('')
except shodan.APIError as e:
        print('Error: {}'.format(e))
