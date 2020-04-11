using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 平均数
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr;
            int length = Convert.ToInt32(Console.ReadLine());
            arr = new int[length];
            for (int i = 0; i < length; i++)
            {
                Console.WriteLine("输入成绩：");
                arr[i] = Convert.ToInt32(Console.ReadLine());
            }
            Array.Sort(arr);
            double sum = 0;
			double avg=0;
            foreach (double n in arr)
            {
                sum = sum + n; 
            }
            avg = sum / arr.Length; 
			Console.WriteLine("平均成绩为："+avg);
        }
    }
}
