def Regenerate(pdfile):
    newfile = open('NewTest.txt','w')
    newfile.close()
    from pdfquery import PDFQuery 
    import os
    from dotenv import load_dotenv
    from openai import OpenAI
    #py -m pip install allat ^^^^^^^^^^^

    load_dotenv()
    pdf = PDFQuery(pdfile)
    pdf.load()

    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq('LTTextLineHorizontal')

    # Extract the text from the elements
    question =  [t.text for t in text_elements]
    #print(question) #for debugging

    api_key = os.getenv('API_TOKEN')
    printstatement = []
    client = OpenAI(api_key=api_key)
    output_text = ''
    for i in range(len(question)-1):
        MODEL = "gpt-3.5-turbo"
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You will be given a question, your task is to return the same question with different NUMERICAL values, do not remove variables, do not repeat questions, and do not respond with anything but the generated question:"},
                {"role": "user", "content": question[i]},
            ],
            temperature=0,
        )
        output_text+=response.choices[0].message.content + '\n \n'
    return output_text

print(Regenerate('test4.pdf'))