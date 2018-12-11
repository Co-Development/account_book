package top.songm.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import top.songm.entity.User;
import top.songm.service.UserServices;

@RestController
public class Account_Controller {
    @Autowired
    UserServices userServices;

    @RequestMapping("/")
    public User index(){
        return userServices.findbyid(1);
    }
}
