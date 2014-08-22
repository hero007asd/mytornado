#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-22 00:08:55
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

# import os

def html_string(headarr, navinfo, navarr):
    htmlarr = []
    htmlarr.append('<!DOCTYPE html> \
<html> \
  <head> \
    <meta charset="utf-8"> \
    <title>api接口说明</title> \
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> \
    <meta name="description" content=""> \
    <meta name="author" content=""> \
    <link href="http://netdna.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" \
    rel="stylesheet"> \
    <script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script> \
    <script type="text/javascript" src="http://netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script> \
  </head> \
   \
  <body> \
    <header id="top" class="navbar navbar-static-top bs-docs-nav" role="banner">\
      <style> \
        .body{padding-top:70px} \
      </style> \
      <div class="container"> \
        <div class="navbar-header"> \
          <a type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse"></a> \
          <span class="sr-only">Toggle navigation</span> \
          <span class="icon-bar"></span> \
          <span class="icon-bar"></span> \
          <span class="icon-bar"></span> \
          <a class="navbar-brand" href="#">后台接口</a> \
        </div> \
        <nav class="collapse navbar-collapse bs-navbar-collapse" role="navigation"> \
          <ul class="nav navbar-nav navbar-right"> \
          ') 
    for i in headarr:
        htmlarr.append('<li><a href="')
        htmlarr.append(i['url'])
        htmlarr.append('">')
        htmlarr.append(i['title'])
        htmlarr.append('</a></li>')

    htmlarr.append('</ul> \
        </nav> \
      </div> \
    </header> \
    <hr />\
    <div class="container"> \
      <div class="row"> \
        <div class="col-md-2"> \
          <ul class="nav affix">')

    htmlarr.append('<li class="disabled"><a href="#">')
    htmlarr.append(navinfo)
    htmlarr.append('</a></li>')

    for i in navarr:
        htmlarr.append('<li><a href="#')
        htmlarr.append(i.get('anchor','-'))
        htmlarr.append('">')
        htmlarr.append(i.get('title','-'))
        htmlarr.append('</a></li>')

    htmlarr.append('</ul></div><div class="col-md-10">')
    htmlarr.append('<div class="row show-grid">\
        <div class="col-md-2">额外必传参数:</div> \
        <div class="col-md-8">k:密钥或商户ID</div> \
        <div class="col-md-8 col-md-offset-2">timestamp:当前时间戳</div> \
        <div class="col-md-8 col-md-offset-2">signature:密钥签名(md5)</div> \
        </div>')
    htmlarr.append('<div class="row show-grid">\
        <div class="col-md-2">json响应格式:</div> \
        <div class="col-md-8">{"status":num,"message":"","data":{}}</div> \
        <div class="col-md-8 col-md-offset-2">status:返回码.200表示成功，其它表示失败</div> \
        <div class="col-md-8 col-md-offset-2">message:返回消息，对返回码的描述</div> \
        <div class="col-md-8 col-md-offset-2">data:所有业务相关的响应，以json格式在data内返回</div> \
        </div>')
    htmlarr.append('<hr>')

    for i in navarr:
        farray = []
        for f in i.get('field',[]):
            farray.append(f.get('fname','-'))
        htmlarr.append('<strong>接口名</strong>')
        htmlarr.append('<blockquote class="bg-info"><h4>')
        htmlarr.append(i.get('title','-'))
        htmlarr.append('</h4></blockquote>')
        htmlarr.append('<p><h6><strong>接口描述</strong></h6></p>')
        htmlarr.append('<div >')
        htmlarr.append(i.get('desc','-'))
        htmlarr.append('</div>')
        htmlarr.append('<p><h6><strong>请求类型及路径</strong></h6></p>')
        htmlarr.append('<div >')
        htmlarr.append(i.get('method','-').upper())
        htmlarr.append('---')
        htmlarr.append(i.get('url','-'))
        htmlarr.append('</div>')
        htmlarr.append('<p><h6><strong>请求示例</strong></h6></p>')
        htmlarr.append('<div >')
        htmlarr.append(i.get('url','-'))
        htmlarr.append('?k=密钥&amp;timestamp=时间戳&amp;signature=密钥签名&amp;')
        htmlarr.append('=参数&amp;'.join(farray))
        htmlarr.append('=参数</div>')
        htmlarr.append('<p><h6><strong>加密方式</strong></h6></p>')
        htmlarr.append('<div >md5(k=密钥&amp;timestamp=时间戳&amp;')
        htmlarr.append('=参数&amp;'.join(farray))
        htmlarr.append('=参数)</div>')
        htmlarr.append('<p>')

        htmlarr.append('<table id="')
        htmlarr.append(i.get('anchor','-'))
        htmlarr.append('" class="table table-bordered table-striped"> \
            <thead> \
              <tr> \
                <th>参数名称</th> \
                <th>参数说明</th> \
                <th>备注</th> \
              </tr> \
            </thead> ')
        htmlarr.append('')
        htmlarr.append('<tbody>')
        for f in i.get('field',[]):
            htmlarr.append('<tr>')
            htmlarr.append('<td>')
            htmlarr.append(f.get('fname','-'))
            htmlarr.append('</td>')
            htmlarr.append('<td>')
            htmlarr.append(f.get('fdesc','-'))
            htmlarr.append('</td>')
            htmlarr.append('<td>')
            htmlarr.append(f.get('fremark','-'))
            htmlarr.append('</td>')
            htmlarr.append('</tr>')

        htmlarr.append('</tbody></table>')
        htmlarr.append('<div><h6><strong>返回值说明</strong></h6></div>')
        htmlarr.append('<div></div>')
        htmlarr.append('<hr>')

    htmlarr.append(' \
        </div> \
      </div> \
    </div> \
  </body> \
</html>')

    return ''.join(htmlarr)