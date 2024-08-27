import pandas
import pandas as pd

# Data from the image in a dictionary format
data = {
    "Module": ["BMG704", "BMG705", "BMG814", "MKT744", "BMG847", "BMG871", "BMG872", "BMG880", "BMG936"],
    "CRN": [30740, 30746, 28373, 35521, 46877, 49370, 49373, 47934, 43038],
    "Sem": [1, 1, 1, 1, 2, 2, 2, 2, 3],
    "Module Title": [
        "International Finance",
        "Global Business in Context",
        "The Digital Landscape",
        "Global Marketing & Sales Dev",
        "International Busn Res Skills",
        "Global Strategy Dev & Implem",
        "Data Analytics for Intern Bus",
        "International Entrepreneurship",
        "Dissertation"
    ],
    "CW": [83, 70, 73, 70, 75, 66, 70, 67, "-"],
    "Lvl": [7, 7, 7, 7, 7, 7, 7, 7, 7]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

