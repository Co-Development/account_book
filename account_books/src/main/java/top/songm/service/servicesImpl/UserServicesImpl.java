package top.songm.service.servicesImpl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import top.songm.entity.User;
import top.songm.repository.UserRepository;
import top.songm.service.UserServices;

@Service
public class UserServicesImpl implements UserServices {


    @Autowired
    UserRepository userRepository;
    @Override
    public User findbyid(int id) {
        return userRepository.findById(id);
    }
}
