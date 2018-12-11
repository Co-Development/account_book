package top.songm.service;

import org.springframework.stereotype.Service;
import top.songm.entity.User;
public interface UserServices {
    User findbyid (int id);
}
