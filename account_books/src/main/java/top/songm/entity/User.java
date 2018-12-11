package top.songm.entity;


import javax.persistence.*;

@Entity
@Table(name="user")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    @Column(name = "name", nullable = true, length = 50)
    private String name;
    @Column(name = "avatar_url", nullable = true, length = 50)
    private String avatar_url;
    @Column(name = "eat_count", nullable = true)
    private Integer eat_count;
    @Column(name = "type", nullable = true,length = 255)
    private String type;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAvatar_url() {
        return avatar_url;
    }

    public void setAvatar_url(String avatar_url) {
        this.avatar_url = avatar_url;
    }

    public Integer getEat_count() {
        return eat_count;
    }

    public void setEat_count(Integer eat_count) {
        this.eat_count = eat_count;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
}
