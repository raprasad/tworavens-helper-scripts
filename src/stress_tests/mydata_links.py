
# [ (description, link), (description, link), etc]
my_data_links = [
    #("gary king, all dvobjects", '/api/mydata/retrieve?selected_page=1&dvobject_types=Dataverse&dvobject_types=Dataset&dvobject_types=DataFile&published_states=Published&published_states=Unpublished&published_states=Draft&published_states=In+Review&published_states=Deaccessioned&role_ids=1&role_ids=2&role_ids=3&role_ids=4&role_ids=5&role_ids=6&role_ids=7&role_ids=8&mydata_search_term=&userIdentifier=garyking'),
    #("gary king, DVs, DSs, no files", '/api/mydata/retrieve?selected_page=1&dvobject_types=Dataverse&dvobject_types=Dataset&published_states=Published&published_states=Unpublished&published_states=Draft&published_states=In+Review&published_states=Deaccessioned&role_ids=1&role_ids=2&role_ids=3&role_ids=4&role_ids=5&role_ids=6&role_ids=7&role_ids=8&mydata_search_term=&userIdentifier=garyking'),
    ("raman, DVs, DSs, no files", '/api/mydata/retrieve?selected_page=1&dvobject_types=Dataverse&dvobject_types=Dataset&published_states=Published&published_states=Unpublished&published_states=Draft&published_states=In+Review&published_states=Deaccessioned&role_ids=1&role_ids=2&role_ids=3&role_ids=4&role_ids=5&role_ids=6&role_ids=7&role_ids=8&mydata_search_term=&userIdentifier=dataverseAdmin'),
    
]

import random
def get_random_mydata_url():
    return random.choice(my_data_links)
