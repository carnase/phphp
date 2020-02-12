import random
import time
import vk
import vk_api

mess = ["ムムム","ム"]
y=1

while y<1000:
    vk_session = vk_api.VkApi(token='26e9ce009e3f85b9b54a027ad7ec56d04168c2abd59105d20e70ccfcecfa839dd9311ef3ff6029768618e')

    vk = vk_session.get_api()
    print(vk.wall.createComment(owner_id=551893700,post_id=83,message=random.choice(mess)))
    y=y+1
    time.sleep(0.2)
