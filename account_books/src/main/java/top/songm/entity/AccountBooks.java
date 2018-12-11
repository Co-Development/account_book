package top.songm.entity;

import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name="account_books")
public class AccountBooks {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    @Column(name = "create_name", nullable = false,length = 50)
    private String create_name;
    private Integer money;
    private Date create_tiem;
    private String note;
    private String avatar_url;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getCreate_name() {
        return create_name;
    }

    public void setCreate_name(String create_name) {
        this.create_name = create_name;
    }

    public Integer getMoney() {
        return money;
    }

    public void setMoney(Integer money) {
        this.money = money;
    }

    public Date getCreate_tiem() {
        return create_tiem;
    }

    public void setCreate_tiem(Date create_tiem) {
        this.create_tiem = create_tiem;
    }

    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }

    public String getAvatar_url() {
        return avatar_url;
    }

    public void setAvatar_url(String avatar_url) {
        this.avatar_url = avatar_url;
    }
}
