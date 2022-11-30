package BackService.Dao;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class scenicInfoDao {
    private String scenicSpot;
    private String url;
    private String score;
    private String Comment;
    private String heat;
    private String address;

}
