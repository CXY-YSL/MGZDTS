using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 选择排序法
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] array = new int[] { 2, 18, 9, 26, 3, 7, 5, 10 };
            Console.WriteLine("数组选择排序前的结果为：");
            foreach (int n in array)
            {
                Console.Write("{0}", n + " ");
            }
            Console.WriteLine();
            int min;
            for (int i = 0; i < array.Length - 1; i++)
            {
                min = i;
                for (int j = i + 1; j < array.Length; j++)
                {
                    if (array[j] < array[min])
                        min = j;
                }
                int t = array[min];
                array[min] = array[i];
                array[i] = t;
            }
            Console.WriteLine("数组选择排序后的结果为：");
            foreach (int n in array)
            {
                Console.Write("{0}", n + " ");
            }
            Console.ReadLine();
        }
    }
}
