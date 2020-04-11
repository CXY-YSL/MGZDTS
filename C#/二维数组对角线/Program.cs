using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 二维数组对角线
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] arr = new int[3, 3];
            Random rand = new Random();
            Console.Write("随机二维数组：\n");
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    arr[i, j] = rand.Next(10, 100);
                    Console.Write(arr[i, j] + " ");
                } 
                Console.WriteLine("\r");
            }
            Console.Write("\n正对角线元素：");
            for (int i = 0; i < 3; i++)
            {
                Console.Write(arr[i, i]+" ");
            }
            Console.Write("\n斜对角线元素：");
            for (int j = 0; j < 3; j++)
            {
                Console.Write(arr[2 - j, j]+" ");
            }
            Console.ReadKey();
        }
    }
}
