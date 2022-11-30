package BackService.Controller;

import BackService.Dao.userInfoDao;
import BackService.Mapper.userInfoMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class userInfo {
    @Autowired
    userInfoMapper userInfomapper;
//      查询user表的全部信息
    @GetMapping("/user")
    public List<userInfoDao> user(){
        List<userInfoDao> user = userInfomapper.queryAll();
        return user;
    }
//      向user表中插入一条用户信息
    @GetMapping("insert")
    public void insert(userInfoDao user){
        String username = user.getUsername();
        String email = user.getEmail();
        String password = user.getPassword();
//        userInfoDao user = new userInfoDao("zhangxubo", "22333", "38394");
        userInfomapper.insertUser(user);
    }
//     删除指定用户
    @GetMapping("delete")
    public void delete(String email){
        userInfomapper.delete(email);
    }
//    用户登录功能实现
    @GetMapping("login")
    public userInfoDao login(userInfoDao user){
        userInfoDao result =new userInfoDao();
        String email = user.getEmail();
        String password = user.getPassword();
        List<userInfoDao> userInfoList= userInfomapper.queryAll();
        for(userInfoDao obj:userInfoList){
           if(obj.getEmail().equals(user.getEmail()) && obj.getPassword().equals(user.getPassword())){
                result=obj;
           }
        }
        return result;
    }
//    用户注册功能实现
    @GetMapping("register")
    public String register(userInfoDao user){
        String result = "";
        String username = user.getUsername();
        String useremail = user.getEmail();
        String userpassword = user.getPassword();
        List<userInfoDao> userList = userInfomapper.queryAll();
        for(userInfoDao obj:userList){
            if(user.getEmail().equals(obj.getEmail())){
                result="此账号已经存在";
            }
            else {
                userInfomapper.insertUser(user);
                result="此账号注册成功";
            }
        }
        return result;

    }


}
