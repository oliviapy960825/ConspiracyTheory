### contributors-all nan- no use, discard

### 'display_text_range': no idea what is it, discard

### geo- some are nan some are not, Deprecated, use coordinates instead. Discard

### id-drop id, use id_str instead

### in_reply_to_status_id - drop, use in_reply_to_status_id_str instead

### 'in_reply_to_user_id', drop, use in_reply_to_user_id_str instead

### is_quote_status, discard, since when quoted_status_id_str surfaces, it already means that the tweet is a quote tweet

### 'quoted_status_id', discard, use quoted_status_id_str' instead

### coordinates- some tweets have coordinates, maybe can map the tweets by coordinates and see the relations, keep coordinates, The inner coordinates array is formatted as geoJSON (longitude first, then latitude)

### created_at - all not nan, maybe can map by created time to see what's happening behind it

### entities- all not nan, but no idea what it is. Still, keep it

### entended_entities- some are nan and some are not. but no idea what it is. Still, keep it, When between one and four native photos or one video or one animated GIF are in Tweet, contains an array 'media' metadata.

### favorite_count-not nan, keep it

### favorited- not nan, keep it, Indicates whether this Tweet has been liked by the authenticating user

### full_text - keep it

### id_str- keep it

### in_reply_to_screen_name - keep, maybe apply text analytics or NLP on it to figure out what's in common

### in_reply_to_status_id_str', keep

### 'in_reply_to_user_id_str', keep

### 'lang', keep

### 'metadata', keep

### 'possibly_sensitive', keep, This field only surfaces when a Tweet contains a link. The meaning of the field doesn’t pertain to the Tweet content itself, but instead it is an indicator that the URL contained in the Tweet may contain content or media identified as sensitive content. 

### quoted_status, keep, this attribute contains the Tweet object of the original Tweet that was quoted.

### 'quoted_status_id_str', keep, only surfaces when the Tweet is a quote Tweet. This is the string representation Tweet ID of the quoted Tweet.

### 'retweet_count', keep, which could be used to determine the popularity of a certain tweet

### 'retweeted',Indicates whether this Tweet has been Retweeted by the authenticating user

### 'retweeted_status', This attribute contains a representation of the original Tweet that was retweeted. Keep

### 'source', keep, Utility used to post the Tweet, as an HTML-formatted string. could be used to analyze behavoiral pattern

### 'truncated', Keep, Indicates whether the value of the text parameter was truncated

### 'user', dictionary of the user attributes, keep

### 'withheld_in_countries', keep, a list of uppercase two-letter country codes this content is withheld from.
