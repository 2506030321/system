package BackService.Mapper;

import BackService.Dao.userInfoDao;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Component;

import java.util.List;

@Mapper
@Component
public interface userInfoMapper {
    List<userInfoDao> queryAll();
    void insertUser(userInfoDao user);
    void delete(String email);

}
