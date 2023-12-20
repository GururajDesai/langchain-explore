from flask import Flask, render_template, request, jsonify

from llm_explore import llm_exlore_func

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary_and_facts, profile_pic_url = llm_exlore_func(
        name=name
    )
    print(summary_and_facts)
    print("Profile Picture")
    print(profile_pic_url)
    return jsonify(
        {
            "summary_and_facts": summary_and_facts.to_dict(),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
