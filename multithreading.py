from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
        f1 = executor.submit(dsp.processMaster,base,dsp_df,refund_dsp)
        f2 = executor.submit(dsp.processDSP,base,dsp_df,refund_dsp,opr_dsp_df,opr_refund_dsp)
        f3 = executor.submit(dsp.processAADHARUCL,base,aadhar_ucl,refund_aadhar_ucl,opr_aadhar_ucl,opr_refund_aadhar_ucl)
        f4 = executor.submit(dsp.processAADHARDSP,base,aadhar_dsp,refund_aadhar_dsp,opr_aadhar_dsp,opr_refund_aadhar_dsp)



  OR


  import threading

  t1 = threading.Thread(target=print_square, args=(10,))
  t2 = threading.Thread(target=print_cube, args=(10,))

  # starting thread 1
  t1.start()
  # starting thread 2
  t2.start()

  # wait until thread 1 is completely executed
  t1.join()
  # wait until thread 2 is completely executed
  t2.join()

  # both threads completely executed
  print("Done!")
