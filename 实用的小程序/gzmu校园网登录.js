// ==UserScript==
// @name         贵州民族大学校园网快速自动登录脚本
// @namespace    https://github.com/zuiyimeihuashang/taobao_scrapy/blob/master/%E5%AE%9E%E7%94%A8%E7%9A%84%E5%B0%8F%E7%A8%8B%E5%BA%8F/gzmu%E6%A0%A1%E5%9B%AD%E7%BD%91%E7%99%BB%E5%BD%95.js
// @version      1.3
// @description  ECUT校园网自动登录脚本
// @author       inventor
// @match        *://*.101.6.51/a79.htm*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=79.141
// @grant        unsafeWindow
// @license MIT
// ==/UserScript==

/* globals jQuery, $, waitForKeyElements */

var username = "2022XXXXX"; // 学号
var password = "23XXXX"; // 密码
var port = 2; // 0办公网，1学生内网，2中国移动，3中国电信

(function() {
    // 定义一个数组，包含用于选择运营商的input元素的选择器
    var portSelectors = ["input[value='@xyw']", "input[value='']", "input[value='@yd']", "input[value='@lt']"];

    // 添加一个load事件监听器，用于在页面加载完成后执行以下操作
    window.addEventListener('load', function() {
        $(portSelectors[port]).click(); // 选择运行商
        $("input[name='DDDDD']").val(username); // 设置 input[name='DDDDD'] 元素的值，即用户名
        $("input[name='upass']").val(password); // 设置 input[name='upass'] 元素的值，即密码
        $("input[name='0MKKey']").click(); // 点击 input[name='0MKKey'] 元素，模拟用户登录
    }, false);
})();
/*
附：
1. 设置开机自动启动Chrom浏览器，win+R 打开运行框输入 shell:startup回车，打开一个文件夹，右击Chrom浏览器复制Chrom快捷方式，粘贴到打开的文件夹中。
2. 设置Chrom浏览器自动打开登录页面，设置->启动时->选择打开特定的网页->添加校园网登录页面。
 */