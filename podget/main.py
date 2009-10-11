#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
from xml.etree import cElementTree as etree

URL="http://radiofrance-podcast.net/podcast09/rss_13364.xml"


class Podcast():
    """
    Class to represent a podcast.

    It has a title, a date, and a url to download content.

    """
    def __init__(self):
        self.title = "Untitled"
        self.date  = "now"
        self.url   = None


def parse_podcast(xml_tree):
    """
    Parse a .xml file.

    Returns a podcast object:

    """
    res = Podcast()

    xml_channel = xml_tree.find("channel")
    xml_item    = xml_channel.find("item")
    xml_title   = xml_item.find("title").text
    xml_guid    = xml_item.find("guid").text

    res.title = xml_title
    res.url   = xml_guid

    return res



def main():
    """
    Manages options when called from command-line
    """
    xml_file = urlopen(URL)
    xml_tree = etree.parse(xml_file)
    podcast = parse_podcast(xml_tree)
    content = urlopen(podcast.url).read()
    output = open(podcast.title + ".mp3", "wb")
    output.write(content)
    output.close()


if __name__ == "__main__" :
    main()

