from wordcloud import WordCloud, STOPWORDS
from collections import Counter
from stopwords import get_stopwords
import numpy as np
from PIL import Image

def gen_wordcloud(wc, path, source):
    counts_all = Counter()
    with open(f'./{path}/{source}', 'r') as f:
        for line in f:
            counts_line = wc.process_text(line)
            counts_all.update(counts_line)

    wc.generate_from_frequencies(dict(counts_all.most_common(100)))
    wc.to_file(f'./{path}/wc_ring.png')

def main():
    stopwords = get_stopwords(STOPWORDS)
    mask = np.array(Image.open('./OneRing.jpg'))

    wc = WordCloud(
        width=2000,
        height=1000,
        stopwords=stopwords,
        colormap='rainbow',
        mask=mask,
    )

    # The Fellowship Of The Ring

    gen_wordcloud(wc, '1_The_Fellowship_Of_The_Ring', 'The_Fellowship_Of_The_Ring.txt')

    # The Two Towers

    gen_wordcloud(wc, '2_The_Two_Towers', 'The_Two_Towers.txt')

    # The Return Of The King

    gen_wordcloud(wc, '3_The_Return_Of_The_King', 'The_Return_Of_The_King.txt')

    # All

    gen_wordcloud(wc, './', 'lotr.txt')

if __name__ == '__main__':
    main()