import pandas as pd
import numpy as np
import pickle
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity

def get_latent_topics(df):

    mat = df.values
    categories = df.columns
    names = df.index

    # Let's try using NMF instead....
    k =  9 # number of topics

    topics = ['latent_topic_{}'.format(i) for i in range(k)]

    nmf = NMF(n_components = k)
    nmf.fit(mat)

    W = nmf.transform(mat)
    H = nmf.components_

    W = pd.DataFrame(W, index = names, columns = topics)
    H = pd.DataFrame(H, index = topics, columns = categories)

    W,H = (np.around(x,3) for x in (W, H))
    return W, H

def get_cosine_sim(W):
    cos_sim = pd.DataFrame(cosine_similarity(W, W, dense_output=True))
    cos_sim['names'] = W.index
    cos_sim.set_index('names', inplace=True)
    cos_sim.columns = [col.lower().replace(' ', '_') for col in cos_sim.index]
    return cos_sim

def get_recs(venue, cos_sim):   
    rest = venue.lower().replace(' ', '_')
    return cos_sim[rest].sort_values(ascending=False).iloc[1:10]

