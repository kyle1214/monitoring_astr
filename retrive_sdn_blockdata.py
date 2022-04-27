import common
from substrateinterface import SubstrateInterface

def get_extrinsic_data(block_hash):
    result = substrate.get_block(block_hash=block_hash)
    for extrinsic in result['extrinsics']:
        
        
        if 'address' in extrinsic:
            signed_by_address = extrinsic['address'].value
        else:
            signed_by_address = None
            
        print('Pallet: {}, Call: {}, Signed by: {}'.format(
            extrinsic["call"]["call_module"].name,
            extrinsic["call"]["call_function"].name,
            signed_by_address
        ))
        if extrinsic["call"]["call_function"].name == 'set_keys':
            print(f'{extrinsic["call"]["call_function"].name}:{extrinsic["call"]["call_args"][0]["value"]["aura"].value}')
            print(('Sender: {}'.format(
                signed_by_address
            )))
         

def subscription_handler(obj, update_nr, subscription_id):
    
    #print(f"New block #{obj['header']['number']} produced by {obj['author']}")
    print(f"## New block #{obj['header']['number'], obj['header']['parentHash']}")
    get_extrinsic_data(obj['header']['parentHash'])
    
    if update_nr > 10:
        return {'message': 'Subscription will cancel when a value is returned', 'updates_processed': update_nr}


substrate = SubstrateInterface(
    url=common.WS_URL
)
result = substrate.subscribe_block_headers(subscription_handler, include_author=False)
