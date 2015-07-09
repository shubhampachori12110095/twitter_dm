__author__ = 'kjoseph'

import os, sys, glob, codecs
from casostwitter import TwitterUser
from casostwitter.general_utils import tab_stringify_newline, get_handles

sys.argv = ['',
            '/Users/kjoseph/git/thesis/thesis_python/twitter_login_creds',
            '/Users/kjoseph/Desktop/mikhail/',
           '/Users/kjoseph/Desktop/mikhail/users.txt']

print sys.argv

if len(sys.argv) != 4:
    print 'usage:  [known_user_dir] [output_dir] [tweet_id_file]'
    sys.exit(-1)

handles = get_handles(glob.glob(os.path.join(sys.argv[1],"*.txt")))
print 'n authed users: ', len(handles)

out_dir = sys.argv[2]

user_sns = [line.strip() for line in open(sys.argv[3]).readlines()]

print 'num users: ', len(user_sns)

of = codecs.open("output_fil.tsv","w","utf8")
for i in range(len(user_sns)):
    user = TwitterUser(handles[i], screen_name=user_sns[i])
    user.populate_tweets_from_api(json_output_filename=out_dir+user_sns[i]+".json",
                                  sleep_var=False)
    print('\tgetting friends for: ', user_sns[i])
    rts = 0
    gt = 0
    for t in user.tweets:
        if t.retweeted is not None:
            rts+=1
        if t.geocode_info is not None:
            gt +=1

    of.write(tab_stringify_newline([user.screen_name,
                                 gt,
                                 rts,
                                len(user.tweets),
                                user.earliest_tweet_time,
                                user.latest_tweet_time,
                                user.name,
                                user.n_total_tweets,
                                user.creation_date,
                                user.followers_count,
                                user.following_count]))

of.close()



