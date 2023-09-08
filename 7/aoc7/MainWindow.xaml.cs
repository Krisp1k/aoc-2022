using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace aoc7
{
    public enum FileOrFolder
    {
        file, folder
    }

    public class Item
    {
        FileOrFolder type;
        int fileSize;
        string name;
        Item parent;
        List <Item> items = new List<Item>();

        public string GetItemNames()
        {
            string names = "";

            foreach (Item item in this.items)
            {
                names += item.name + " ";
            }
            return names;
        }

        public Item(Item parent, FileOrFolder type, int fileSize, string name)
        {
            this.parent = parent;
            this.type = type;
            this.fileSize = fileSize;
            this.name = name;
        }

        public void AddItem(Item newItem)
        {
            this.items.Add(newItem);
        }

        public Item returnParent()
        {
            return this.parent;
        }

        public long GetSize()
        {
            if (this.type == FileOrFolder.file)
            {
                return this.fileSize;
            } 
            else
            {
                long count = 0;

                foreach (Item item in this.items)
                {
                    count += item.GetSize();
                }
                return count;
            }
        }

        public Item returnChildren(string name)
        {
            foreach(Item item in this.items)
            {
                if (item.name == name && item.type == FileOrFolder.folder)
                {
                    return item;
                }
            }
            return null;
        }

    }

    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            StreamReader sr = new StreamReader("data.txt");
            Item activeDirectory;
            Item root = new Item(null, FileOrFolder.folder, 0, "/");

            string line = sr.ReadLine();
            activeDirectory = root;

            while (!sr.EndOfStream)
            {
                line = sr.ReadLine();
                string[] lineParts = line.Split(" ");

                if (lineParts.Length == 3)
                { // přišlo cd

                    if (lineParts[2] == "..")
                    {
                        activeDirectory = activeDirectory.returnParent();
                    } 
                    else
                    {
                        activeDirectory = activeDirectory.returnChildren(lineParts[2]);
                    }
                } 
                else
                {
                    switch(lineParts[0])
                    {
                        case "$":
                            break;

                        case "dir":
                            activeDirectory.AddItem(new Item(activeDirectory, FileOrFolder.folder, 0, lineParts[1]));
                            break;

                        default:
                            activeDirectory.AddItem(new Item(activeDirectory, FileOrFolder.file, Convert.ToInt32(lineParts[0]), lineParts[1]));
                            break;

                    }
                }
               
                Console.WriteLine(line);
            }

            //strom done

            MessageBox.Show(root.GetSize() + "");

        }
    }
}
