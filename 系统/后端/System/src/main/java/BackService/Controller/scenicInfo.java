package BackService.Controller;

import BackService.Dao.scenicInfoDao;
import BackService.Dao.userInfoDao;
import BackService.Mapper.scenicInfoMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class scenicInfo {
    @Autowired
    BackService.Mapper.scenicInfoMapper scenicInfoMapper;
//    查询所有景点信息
    @GetMapping("/scenicSpot")
    public List<scenicInfoDao> scenicSpot(){
        List<scenicInfoDao> scenicSpot = scenicInfoMapper.queryAll();
        return scenicSpot;
    }
//    搜索栏功能实现
    @GetMapping("keyword")
    public List<scenicInfoDao> queryByKeyWord(String key){
        List<scenicInfoDao> keyScenicList = scenicInfoMapper.queryByKeyWord(key);
        return keyScenicList;

    }
//    根据搜索内容展示景点信息
    @GetMapping("scenicspot")
    public List<scenicInfoDao> queryScenicSpot(String scenic){
        List<scenicInfoDao> scenicSpot = scenicInfoMapper.queryScenicSpot(scenic);
        return scenicSpot;


    }

}
