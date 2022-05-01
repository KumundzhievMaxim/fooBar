from typing import Dict
from pytrends.request import TrendReq


def pull_search_interest(keyword: str) -> Dict:
    """ Helper function which return sorted search score within fixed time-frame.
     Notes:
        in requirements it was not specified for what exactly period search score has to be,
        hence used def values.
     """

    connector = TrendReq()
    response_df = connector.get_historical_interest(keywords=[keyword]).sort_values(f'{keyword}', ascending=False)
    response_df['datetime'] = response_df.index

    datetime = response_df.datetime.dt.strftime('%Y-%m-%d-%H:%M:%S').values
    scores = response_df[keyword].tolist()
    zipper = zip(datetime, scores)

    return dict(zipper)
