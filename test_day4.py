import pandas as pd 

df = pd.DataFrame(
    {
        "Name": [
                "Braund, Mr. Owne Harris",
                "Allen, Mr. William Henry",
                "Donnel, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

df.to_csv("mynewfile.csv", index=False)

