# this app assumes that each list entry is defined as follows:
# [ title, note1, note2, note3, etc. ]
# with the first item being the title of the section's notes
# and any/all remaining items containing all of the notes for that section
TEST_LIST = [
    ['Beginning Notes',
        'HTML is <b><em>reasonably</em> straightforward',
        'Line breaks (br)<br>are called inline tags while paragraph (p) tags are block tags.  Block tags can optionally have a defined height/width.',
        'This is how a <a href="google.com">link</a> works.'],
    ["Work Session 1",
        "Have realized that I am not a note-taker for some of this stuff... not much to put into 'code' for Work Session 1.",
        "'div' is used for blocks and the class can be used with css for styling.",
        "'span' is used inline and can also have classes that can be defined in css.",
        "Don't really see all of the point of 'span' yet... am guessing it will be more obvious once we get into css.",
        "I really wish the class had a better table of contents or more obvious way of seeing where you are at versus where you were last at.  Tried going back a few videos to review and then had to keep skipping through videos I had already seen before finally figuring out where I had been."],
    ["Adding CSS Style to HTML Structure",
        "Order matters when defining css.",
        "You could also use 'style' within the 'head' section of an html page to define styles, but using a separate css file allows you to apply/modify your style across multiple pages without having to update each html page.",
        "You could even add style settings in the 'div'.",
        "An exhaustive css reference is available at <a href='https://developer.mozilla.org/en-US/docs/Web/CSS/Reference'>mozilla</a>.",
        "Boxes have:  margin / border / padding / content"
        """HTML and CSS can be validated:
            <ul>
                <li>To verify HTML: <a href='http://validator.w3.org/#validate_by_input'>http://validator.w3.org/#validate_by_input</a></li>
                <li>To verify CSS: <a href='http://jigsaw.w3.org/css-validator/#validate_by_input'>http://jigsaw.w3.org/css-validator/#validate_by_input</a></li>
            </ul>"""],
    ["Telling Computers What To Do",
        "We will be using Python, which is an interpreted language versus compiled code.",
        """Backus-Naur Form: &lt;non-terminal&gt; -> &lt;replacement&gt; (terminal)
            <br>Derivation: Replacing non-terminals with replacements (terminals) until the non-terminals have all been replaced by terminal values.""",
        "<div class='subheading'>Python</div>"
        """Can get substrings using the expression &lt;string_variable&gt; [ &lt;expression&gt; : &lt;expression&gt; ]
            <br>strVariable[3:3] would return the same thing as strVariable[3]
            <br>strVariable[3:5] would return character positions 4-6
            <br>strVariable[3:] would return from position 4 to the end of the string
            <br>strVariable[-5:] would return the last 5 characters of the string""",
        """Search strings using .find, in the format &lt;string_variable&gt;.find(&lt;substring&gt;, &lt;starting_position&gt;)
            <br>the return value is the position of the first character of the substring, starting at the (optional) starting_position
            <br>a -1 return value indicates that the substring value was not found""",
        """Multi-line strings can be created using triple quotes:
            <br>print '''
                Here is the first line
                And here is the second line
                And here is the third line
            '''""",
        """Procedures/functions are defined as:
            <br>def function_name (input_variable[,input_variable...])
            <br>use 'return &lt;variable&gt;' to return a value from the function""",
        "Why use functions?  Portability - a function in one app might be usable in another; Efficiency - code that is repeated can be placed in a function and called multiple times; Readability - proper function names help to make your code more legible and easier to follow",
        "While (condition):",
        "if (condition): else:",
        "Lists can be created by specifying list_name = [item1, item2, ...]",
        "Lists are mutable.",
        "List assignments act more like pointers (called aliasing) so if p=[1,2,3] and you do q=p then q and p will both point to the same list!",
        """for &lt;variable&gt; in &lt;list_variable&gt;:
            <br>items to execute""",
        "&lt;value&gt; [not] in &lt;list&gt; allows us to locate items in a list, returning a boolean value.",
        "list_element.index(search_value) allows us to locate the index value for the first instance of search_value in list_element."]
    ]

def generate_html_header():
    # function will return the required html starting tags
    return_html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ron's Notes</title>
    <link rel="stylesheet" href="rons-notes.css">
</head>

<body>
    '''
    return return_html


def generate_html_footer():
    # function will return the required html closing tags
    return_html = '''

</body>
</html>
    '''
    return return_html


def generate_notes(str_text):
    # function will generate the HTML for the notes under a section
    return_html = '''
        <p>''' + str_text + '''</p>'''
    return return_html


def generate_section(section):
    # function will generate the HTML for a given section, with the notes under that section
    
    if ( len(section) >= 1 ):
        # the first element of section should be the title...
        # create the division for the section title
        section_html = '''
    <div class="title">''' + section[0] + '''</div>'''
    
        # all subsequent elements (if any) should be the notes for the section
        if ( len(section) >= 2 ):
            # so, generate the notes for the section

            # add the div 'header' for the notes
            section_html = section_html + '''
    <div class="notes">'''

            # add each note to the section
            int_position = 1    # start with the second element (since the first is the section title)
            while int_position < len(section):
                section_html = section_html + generate_notes(section[int_position])
                int_position = int_position + 1   # increment index position
            
            # add the div 'footer' for the notes
            section_html = section_html + '''
    </div>'''
        # ELSE there are no notes for this section

    else:
        # return nothing, we received a blank section
        section_html = ''

    return section_html


def generate_all_html(list_notes):
    # function will generate all of the HTML for all sections/notes
    all_html = ''  # initialize variable

    # start by creating the required html starting tags
    all_html = str(generate_html_header())
    
    for section in list_notes:
        all_html = all_html + generate_section(section)
    
    # and finish by adding the required html closing tags
    all_html = all_html + str(generate_html_footer())

    return all_html

print generate_all_html(TEST_LIST)
