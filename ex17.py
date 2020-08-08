in_file = open("in.txt");in_data = in_file.read();print(" the input file is %d bytes long" % len(in_data));

out_file = open("ex15sample.txt", "w"); out_file.write(in_data);out_file.close();in_file.close();

print(len("fgywrd"))
