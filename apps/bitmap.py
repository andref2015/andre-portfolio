import random

def load_bitmap():
    greetings = ["Welcome!", "Hola!", "Bonjour!", "Konnichiwa!", "Tere!", "Howdy!", 
         "Ahoy!", "What's up?", "Greetings!", "Salutations!", "Yo!", "Hi there!", 
         "Miao!", "Namaste!", "Yello!", "Howdy do!"]
    random_greeting = random.choice(greetings)
    message = f"{random_greeting} "
    bitmap = """
     **************   *  *** **  *      ******************************
    ********************* ** ** *  * ****************************** *
    **      *****************       ******************************
            *************          **  * **** ** ************** *
             *********            *******   **************** * *
              ********           ***************************  *
     *        * **** ***         *************** ******  ** *
                 ****  *         ***************   *** ***  *
                   ******         *************    **   **  *
                   ********        *************    *  ** ***
                     ********         ********          * *** ****
                     *********         ******  *        **** ** * **
                     *********         ****** * *           *** *   *
                       ******          ***** **             *****   *
                       *****            **** *            ********
                      *****             ****              *********
                      ****              **                 *******   *
                      ***                                       *    *
                      **     *                    *
    """.strip()
    page = ""
    message_index = 0

    # Iterate through each line of the bitmap
    for line in bitmap.splitlines():
        for char in line:
          if char == '*':
              if message_index >= len(message):
                  message_index = 0  # Reset index if it exceeds message length
              page += message[message_index]
              message_index += 1
          else:
              page += char
        page += "<br>"
    return page
