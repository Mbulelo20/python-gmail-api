from rich.console import Console
from rich.table import Table
import Fetch_Email_Data as email_data



email_data = email_data.main()
table = Table(title="Star Wars Movies")


table.add_column("Details", justify="right", style="cyan", no_wrap=True)
table.add_column("Email", style="magenta")

for email_data_x in email_data:
    table.add_row(email_data_x[0][:22]+"\n"+email_data_x[1][:50]+"\n"+ email_data_x[4]+"\n", email_data_x[3]+"\n")

print()
print()
# table.add_row(j, "Star Wars: The Rise of Skywalker", "$952,110,690")
# table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
# table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
# table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)