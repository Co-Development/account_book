package top.songm.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import top.songm.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {
    User findById(Integer id);
}
