import asyncio
from reactpy import component, event, html, run, use_state
import pandas as pd

@component
def App():
    message, set_message = use_state("")
    submitted_message, set_submitted_message = use_state("")

    @event(prevent_default=True)
    async def handle_submit(event):
        set_submitted_message(message)
        set_message("")

        df = pd.read_csv("predictions.csv")
        mapper = pd.read_csv("country_mapper.csv")        


        df = df[df["Sport"] == message]

        if len(df) == 0:
            print(set_submitted_message("Invalid sport! Try again."))
            return

        df = df.sort_values(by=["0"], ascending=False)
        print(df)
        df = df.head(3)

        gold_place = None
        silver_place = None
        bronze_place = None

        if len(df) >= 1:
            gold_place = mapper[mapper["noc"] == df.iloc[0]["NOC"]]
        
        if len(df) >= 2:
            silver_place = mapper[mapper["noc"] == df.iloc[1]["NOC"]]
        
        if len(df) >= 3:
            bronze_place = mapper[mapper["noc"] == df.iloc[2]["NOC"]]
            
        
        prediction = {
            "gold": gold_place.iloc[0]["country_name"],
            "silver": silver_place.iloc[0]["country_name"],
            "bronze": bronze_place.iloc[0]["country_name"]
        }

        print(gold_place)
        
        result_message = f"🥇: {prediction['gold']}‎ ‎ ‎ ‎ ‎ 🥈: {prediction['silver']}‎ ‎ ‎ ‎ ‎ 🥉: {prediction['bronze']}"
        
        set_submitted_message(result_message)

    return html.div(
        {
            "style": {
                "display": "flex",
                "flex-direction": "column",
                "justify-content": "space-between",
                "align-items": "center",
                "height": "100vh",
                "background-color": "#0f1d33",
                "font-family": "monospace",
                "color": "white",
                "width": "100%",
                "margin": "0",
                "padding": "0",
                "box-sizing": "border-box",
                "overflow": "hidden",
                "text-align": "center"
            }
        },
        html.style(
            """
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
                background-color: #0f1d33; /* Ensure no white corners */
                font-family: 'Roboto', sans-serif; /* Apply font to the entire page */
            }
            """
        ),
        html.div(
            {
                "style": {
                    "margin-top": "40px",
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "center",
                    "width": "100%"
                }
            },
            html.h1(
                {"style": {"font-size": "32px", "font-weight": "700", "margin-bottom": "10px"}},
                "Predict the 2024 Olympics!"
            ),
            html.h2(
                {"style": {"font-size": "20px", "font-weight": "400", "margin-bottom": "40px"}},
                "Enter a sport from the upcoming 2024 Paris Olympics, and we'll predict your winners."
            )
        ),
        html.div(
            {
                "style": {
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "center",
                    "justify-content": "center",
                    "flex-grow": "1"
                }
            },
            html.form(
                {"on_submit": handle_submit, "style": {"display": "flex", "flex-direction": "column", "align-items": "center"}},
                html.input(
                    {
                        "type": "text",
                        "placeholder": "Type your message...",
                        "value": message,
                        "on_change": lambda event: set_message(event["target"]["value"]),
                        "style": {
                            "padding": "10px",
                            "margin-bottom": "10px",
                            "border": "1px solid #ccc",
                            "border-radius": "4px",
                            "width": "300px",
                            "font-size": "16px",
                            "background-color": "#26426e",
                            "color": "white",
                            "font-family": "monospace"
                        }
                    }
                ),
                html.button(
                    {
                        "type": "submit",
                        "style": {
                            "padding": "10px 20px",
                            "border": "none",
                            "border-radius": "4px",
                            "background-color": "#26426e",
                            "color": "white",
                            "font-size": "16px",
                            "cursor": "pointer",
                            "font-family": "monospace"
                        }
                    },
                    "Enter"
                ),
            ),
            html.div(
                {"style": {"margin-top": "20px"}},
                html.p(
                    {"style": {"font-size": "18px"}},
                    f"{submitted_message}"
                ) if submitted_message else ""
            )
        )
    )

run(App)