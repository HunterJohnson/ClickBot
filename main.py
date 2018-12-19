# params = {location(s), click_nums, url(s)}

# use Tor to set IP (new node / [custom] bridge ) for each click

import web

import torlib

def main():
  url = input(url)
  exit_url = input(exit_url)
  time = input(time) # time will be randomly adjusted
  click_num = input(clicknum)
  locations = input(locations)
  
  while(click_num > 0)
    loc = shuffle(locations)
    x = torlib.new_tor_connection(loc) # or use bridge/custom nodes
    x.navigate(url)
    x.sleep(time)   # or x.random_click / browse
    x.navigate(exit_url)
    x.sleep(30)
    x.close()
    click_num -= 1
    
    
if __name__ == "__main__":
    main()
