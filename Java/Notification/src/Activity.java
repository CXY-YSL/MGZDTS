
public class Activity {
    HeroConfig 韩信=
            new HeroConfig.HeroBuilder("无情冲锋","背水一战","大招!--国士无双")
            .buildSkin("白龙吟")
            .create();
    
    HeroConfig 李白=
            new HeroConfig.HeroBuilder("将进酒","神来之笔","大招!--青莲剑歌")
            .buildSkin("凤求凰")
            .create();
    
    HeroConfig 后裔=
            new HeroConfig.HeroBuilder("炙热之风","燎原箭雨","大招!--一支穿云箭")
            .buildAttack("远程攻击")
            .buildSkin("黄金射手座")
            .create();
    
    HeroConfig 诸葛亮=
            new HeroConfig.HeroBuilder("东风破袭","时空穿梭","大招!--元气弹")
            .buildAttack("远程攻击")
            .buildSkin("桃矢")
            .create();

 //   Log.e("韩信"+韩信.toString());
 //  Log.e("李白"+李白.toString());
 //  Log.e("后裔"+后裔.toString());
 //  Log.e("诸葛亮"+ 诸葛亮.toString());
    
}
