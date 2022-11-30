package BackService.Mapper;
import BackService.Dao.scenicInfoDao;
import BackService.Dao.userInfoDao;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;
import java.util.List;

@Mapper
@Repository
public interface scenicInfoMapper {
     List<scenicInfoDao> queryAll();
     List<scenicInfoDao> queryByKeyWord(String cc);
     List<scenicInfoDao> queryScenicSpot(String scenicSpot);

}
