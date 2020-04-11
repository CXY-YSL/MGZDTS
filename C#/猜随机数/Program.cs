using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 猜随机数
{
    class Program
    {
        static void Main(string[] args)
        {
            Random A = new Random();

            int a = A.Next(0, 100);          

            //Console.WriteLine("产生的随机数为" + a);

            Console.WriteLine("猜猜电脑产生的随机数（1~100）是多少，请输入");

            int b = int.Parse(Console.ReadLine());

            int counts = 1;

            while (b != a)

            {
                if (b < a)
                {
                    Console.WriteLine("你猜小了，再猜");
                }
                
                else if (b > a)
                {
                    Console.WriteLine("你猜大了，再猜");
                }

                counts++;

                b = int.Parse(Console.ReadLine());

                continue;

            }

            Console.WriteLine("恭喜你，猜对了！第" + counts.ToString() + "次猜对");
        }
    }
}
