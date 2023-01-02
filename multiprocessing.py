from multiprocessing import Process

p1 = Process(name='master update', target=u.updateMaster, args=())
p1.start()
p2 = Process(name='total mapping', target=u.totalMapping, args=())
p2.start()
p1.join()
p2.join()
