import speedtest
sp=speedtest.Speedtest()

print(f"Download speed is {'{:.1f}'.format(sp.download()/1024/1024)} Mb/s")
print(f"Upload speed is {'{:.1f}'.format(sp.upload()/1024/1024)} Mb/s")
