import paytable
import paylines
import time
import slot_helper

def main():
    start_time = time.time()
    pay_table = paytable.little_wild_panda_paytable
    pay_lines = paylines.little_wild_panda_paylines
    reels = {'reel1':'hzbefzhhgbdzhczeddfgccgzhsdacadsgcffgbzhcshfhfgdbdeeebhcgeedcbczaghadshzdgcacahgcdecdhgghszgehdegshbdbsgczfdafazgceghgffzdhcf',
             'reel2':'cfezgcwzbfzdhhwgzcbcwhaacfgzwghfzbhczgczdddhdcazhawdcwfdezefwdsgeazfehgbgdbzehbzaewzcgwgccfzfhhwghzwcaezbhddzgdezfdsghsdgghzggchghzedscbzdfseach',
             'reel3':'zffgfbeeazdacesdfbfefzfhgbgzefedccbshhddzdeeeczefbafebehfafhfzdfcegeheczcdfezghzcgabzddhzafsafcezcdzfcbgdzdfazcehzgzfazhbzcffzegefgdzdcseezfeeaccdb',
             'reel4':'bffwchfgeezgfbzbegzgeezhwdzgbdzehgbzdfgzwhzbazafhghefefcwegcwgczhehadzadsffwczfehhafzgefzcehsggegdegzefzghfwzebzhgzbdzhfzgezhcegwhsfzahgzgfzhfzhczwczdwffaazcgeshdgfheddhhewc',
             'reel5':'ezdezebezhezeaceefzgsezecahggzgehdhhdcfgfedgdchzhfzcbazagazbgbhdghehfhaeefdfzfghzdegfeagzcbshfzffbfszfbgcegzbcghfzedgsgfzhsfgfsbahhzhfhzdczegeeafzhgzfghchghzgbasf'
             }
    reels_free = {'reel1':'hbefhhgbdhcedsdfgccghsdacadsgcffgbhcshfhfgdbdeeebhcgeedcbcaghadshdgcacahgcdecdhgghsgehdegshbdbsgcfdafagceghgffdhcf',
             'reel2':'cfegcwbfdhhwgcbcwhasacfgwghfbhcgcdddhdcahawdcwfdeefwdsgeafehgbgdbehbaewcgwgccffhhwghwcaebhddgdefdsghsdgghggchghedscbdfseacshw',
             'reel3':'ffgfbeeadacesdfbfeffhgbgefedccbshhdddeeecefbafebehfafhfdfcegeheccdfeghcgabddhafsafcecdfcbgddfacehsgfahbcffegefgddcseefeeaccdb',
             'reel4':'bffwchfgeegfbbeggsewehwdgbdehgbdfgwhbaafhghefefcwegcwgchehadadsffwcfehhafgefcehsggegdegefghfwebhgbdhfgehcegwhsfahggfhfhcwcdwffaacgeshdgfheddhheswc',
             'reel5':'edeebeheeaceefgseecahgggehdhhdcfgfedgdchhfcbaagabgbhdghehfhaeefdffghdegfeagcbshfffbfsfbgcegbcghfedgsgfhsfgfbahhshfhdcegeeafhgfghchghgbasf'
             }
    
    rows = 3
    cols = 5
    line_waybar = True
    
    symbols = ['w','a','b','c','d','e','f','g','h','s','z']
    s = slot_helper.Slot(pay_table,reels,rows,cols,pay_lines,symbols,reels_free)
    s.run_simulation(100000000)
    print('Time taken in seconds :',time.time() - start_time)

main()
