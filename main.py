def main():
	bpath = "books/frankenstein.txt"
	text = get_text(bpath)
	wcount = cnt(text)
	lowcas = lowercase(text)
	charcount = count_char(lowcas)
	charlist = build_list(charcount)
	charlist.sort(reverse=True, key=charsort)
	print(f"--- Begin report of {bpath} ---")
	print(f"{wcount} words found in the document")
	for chardata in charlist:
		print(f"The character '{chardata['character']}' was found {chardata['num']} times.")
	print("--- End report ---")

def get_text(con):
	with open(con) as f:
		return f.read()

def cnt(text):
	words = text.split()
	return len(words)

def lowercase(text):
	lowstr = text.lower()
	return lowstr

def count_char(lowcas):
	cc = {}
	for x in lowcas:
		if x.isalpha():
			if x in cc:
				cc[x] += 1
			else:
				cc[x] = 1
	return cc

def build_list(charcount):
	charlist = []
	for y, z in charcount.items():
		charinfo = {"character": y, "num": z}
		charlist.append(charinfo)
	return charlist

def charsort(charlist):
	return charlist["num"]




main()