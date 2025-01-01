import time  
import random
from identity_farmer.identity_farmer import IdentityFarmer

if __name__ == '__main__':
    identity_farmer = IdentityFarmer()
    batch_size = 10
    total_requests = 100 # Ensure 100 avatars are generated
    for i in range(total_requests // batch_size):
        identities = []
        for _ in range(batch_size):
            identity = identity_farmer.get_identity()
            if identity is not None:
                identities.append(identity)
            time.sleep(random.uniform(1, 3)) 
        identity_farmer.append_to_json(identities)
    
    print("All identities saved in fake_data.json")
