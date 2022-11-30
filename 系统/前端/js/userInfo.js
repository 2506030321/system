// 对userinfo组件进行特效渲染及事务逻辑处理
// 1.登录注册成功后反转到userInfoEhart页面
document.write("<script src='../js/jquery-3.6.0.js'></script>")
let $LoginAndRegister = document.querySelector('.LoginAndRegister')
let $userInfoEhart = document.querySelector('.userInfoEhart')
$('#blo').click(function(){
    $LoginAndRegister.style.transform='rotateY(-180deg)'
    $LoginAndRegister.style.transition='2s'  
    $userInfoEhart.style.transform='rotateY(0deg)'
    $userInfoEhart.style.transition='2s'
})
$('#bre').click(function(){
    $LoginAndRegister.style.transform='rotateY(-180deg)'
    $LoginAndRegister.style.transition='2s'  
    $userInfoEhart.style.transform='rotateY(0deg)'
    $userInfoEhart.style.transition='2s'
})
$('#return').click(function(){
    $LoginAndRegister.style.transform='rotateY(0deg)'
    $LoginAndRegister.style.transition='2s'  
    $userInfoEhart.style.transform='rotateY(180deg)'
    $userInfoEhart.style.transition='2s'
})
//登录注册页面的滑动
let $userlogin=document.querySelector('.userLogin')
let $userRegister=document.querySelector('.userRegister')
$('#blopage').click(function(){  
    $userRegister.style.visibility='hidden'         
    $userRegister.style.transform='translate(100%)' 
    $userlogin.style.transform='translate(0%)'
    $userlogin.style.visibility='visible'
})
$('#brepage').click(function(){
    $userlogin.style.transform='translate(100%)'
    $userlogin.style.visibility='hidden'
    $userRegister.style.transform='translate(0%)'
    $userRegister.style.visibility='visible'
})