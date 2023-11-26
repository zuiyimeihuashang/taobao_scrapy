// ==UserScript==
// @name         贵州民族大学校园网快速自动登录脚本
// @namespace    https://github.com/zuiyimeihuashang/taobao_scrapy/blob/master/%E5%AE%9E%E9%AA%8C/001.js
// @version      1.1
// @description  ECUT校园网自动登录脚本
// @author       inventor
// @match        http://10.101.6.51/a79.html
// @icon         https://www.google.com/s2/favicons?sz=64&domain=79.141
// @grant        unsafeWindow
// @license MIT
// ==/UserScript==
 
var username = "2021***"//学号
var password = "***"//密码
var port = 2;//0办公网，1学生内网，2中国移动，3中国电信
 
(function() {
  // 定义一个数组，包含用于选择运营商的input元素的选择器
    var _port_text = ["input[value='@xyw']","input[value='']","input[value='@yd']","input[value='@lt']"];
   // 添加一个load事件监听器，用于在页面加载完成后执行以下操作
    window.addEventListener('load', function() {
     // 遍历_port_text数组，使用每个选择器选择一个input元素，并将其checked属性设置为true
    $(_port_text[port]).click();//$(_port_text[port]).attr('checked',true);//选择运行商
    $("input[name='DDDDD']").val(username);// 设置input[name='DDDDD']元素的值，即用户名
    $("input[name='upass']").val(password);// 设置input[name='upass']元素的值，即密码
    $("input[name='0MKKey']").click();// 点击input[name='0MKKey']元素，模拟用户输入密码
    }, false);

})();