// Comment.
// A Test class based on Paul Hunter's Selection.java in MathToWeb.
/*
 * Another comment.
 */
// A third comment.
public class Test implements AnInterface
{
	// Constructor
	public Test(int par1, int par2)
	{
		if (par1 > par2)
		{
			this.attr1 = par2;
			this.attr2 = par1;
		}
		else
		{
			attr1 = par1;
			attr2 = par2;
		}
	}

	public Test(Test original)
	{
		attr1 = original.attr2;
		attr2 = original.attr2;
	}

	// Empty constructor.
	public Test()
	{
		attr1 = -1;
		attr2 = -1;
	}

	public Object clone()  // Embedded comment.
	{
		try
		{
			return super.clone();  // Another embedded comment
		}
		catch (CloneNotSupportedException e)
		{
			return null;
		}
	}

	public String toString()
	{	return ("attr1 = " + attr1 + ", " + "attr2 = " + attr2);
	}
	public void message(String message)
	{
		for (int i = 0; i < message.length(); i++)
		{
			if(message.charAt(i) == '\'')
			{
				System.out.println("Quote in message");
			}
			else if (message.charAt(i) == 'P')
			{
				System.out.println("P in message");
			}
			try
			{
				System.out.println("Hullo");
			}
			catch (Exception e)
			{
				// nothing to do here
			}
		}
	}
	public void runThread()
	{
		new Thread(new Runnable()
		{
			public void run()
			{
				total = 0;
				int i = 0;
				while (i < 100)
				{
					total += i;
				}
			}
		}).start();
	}

	public int attr1;
	public int attr2;
}
