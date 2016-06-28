using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace StreamChecker
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Form f1 = new Form1();
            f1.Text = "Twitch to VLC";
            Application.EnableVisualStyles();
            Application.Run(f1);
            
        }
    }
}
