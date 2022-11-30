package BackService.Dao;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class userInfoDao {
    private String username;
    private String email;
    private String password;
}
