from sys import exit
from textwrap import dedent

from academia_intro import intro

intro()

# Decision class initialization - will this work without this class?
class Decision(object):
    def enter(self):
        print("Decision not yet configured.")
        print("Subclass with enter().")
        exit(1)

# Engine class initialization: this moves you through the game
class Engine(object):

    def __init__(self, choice_map):
        self.choice_map = choice_map

    def play(self):
        current_choice = self.choice_map.opening_choice()
        last_choice = self.choice_map.next_choice('finished')

        while current_choice != last_choice:
            next_choice_name = current_choice.enter()
            current_choice = self.choice_map.next_choice(next_choice_name)

        current_choice.enter()

class HappyLife(Decision):

    def enter(self):
        print(dedent("""
                     When you look back on your life, you will be proud of yourself and many of the choices you made.
                     Well done!
                     """))
        return 'finished'

class SadLife(Decision):

    def enter(self):
        print(dedent("""
                    You might have done a lot of work that no one really noticed, and walked across campus
                    on a lot of pretty mornings.
                    But you were never happy, and at the end of your life you will wish you had 
                    taken more chances and had richer experiences.
                    """))
        return 'finished'

class CollegePath(Decision):

    def enter(self):
        print(dedent("""
                    It's been four long but happy years, and you've just graduated from State U with your 
                    Bachelor's in Something.
                    There's been a lot of hard work, and a lot of drinking beer, and you are sad to say goodbye 
                    to these carefree days and all the friends you've met here.
                    But now you need to decide what your next step is.\n
                    Do you:
                    1. Apply to a PhD program to keep studying Something.
                    2. Go to a trade school and learn to become a plumber.
                    3. Take some time off and travel the world. 
                    """))
        
        choice = int(input("> "))

        if choice == 1:
            print(dedent("""
                        Initially, this feels like the best option.\n
                        You spend about a year working and studying for your GREs, and researching programs and universities 
                        where you think you'd want to go.
                        You live with your parents and fit in time at a dead-end job around this.
                        Another six months or so later, you've taken your tests and submitted your applications, 
                        and the acceptances start rolling in.
                        Now you'll have to decide where to go to grad school.
                         """))
            return 'pick_program'

        elif choice == 2:
            print(dedent("""
                        You know, this is a very solid choice.
                        After a quick spell in trade school and apprenticing, you are ready to work.
                        The life of a plumber is (for obvious reasons) not always pleasant, but you make it work for you.
                        You are well-paid, a small businessperson of sorts, and you have a comfortable life 
                        in which you get to set your own hours.
                        You end up settling in the town you grew up in, getting married, raising your kids.
                         """))
            return 'happy_life'

        elif choice == 3:
            print(dedent("""
                        Wow, that was a good call.
                        The "year off" you sell your parents on turns into something more open-ended.
                        You head first to Mexico and South America for about five years. 
                        You manage to support yourself teaching English and tutoring kids in Something.
                        These five years turn into more years on more continents. 
                        You grow up into a very open-minded person who makes friends very easily.
                        You gradually learn the world of business through personal relationships. You become rich.
                        You meet the love of your life abroad, and raise a beautiful family.
                         """))
            return 'happy_life'

        else:
            print("I don't want to knock the education you got at State U, but you need to pick a number between 1 and 3. Try again.\n")
            return 'college_path'

class PickProgram(Decision):
    
    def enter(self):
        print(dedent("""
                    You got good grades at State U and did pretty well on those GREs, so you've been accepted 
                    by some of the leading Something departments.
                    Quickly you narrow things down to your top 2.
                    The first program is in the best department in the country, at the highly prestigious Elite U.
                    Unfortunately, Elite U is in a small, isolated town in eastern Wyoming, and you are single, in your early 20s, 
                    and used to living in a sizable coastal city.
                    There is one main street in the town, with two rough townie bars and no coffee. 
                    Other than that, Elite U is all that's going on there.
                    You've also been accepted to Lesser U's Something department. 
                    Lesser U is located in a large, cosmopolitan coastal city much like where you're from.
                    The main downside is that its' Something program is nowhere near as prestigious or good for your career, 
                    and a PhD from there won't be as valuable.\n
                    Do you:
                    1. Go to Elite U and accept having no life for 4-8 years.
                    2. Go to Lesser U and have fun for 4-8 years but possibly struggle for a job afterwards.
                    """))

        choice = int(input("> "))

        if choice == 1:
            print(dedent("""
                        Well, you will at least have one item on your resume that impresses people who don't know better.
                        Unfortunately, when it comes to highly regarded departments, there's really no benefit to picking one over another.
                        So it really didn't make any sense to go Elite U. 
                        You will spend 5 years there doing nothing but working, hanging around the university library, 
                        and drinking beer by yourself.\n
                        But that's all in the future. 
                        Now that you've moved to rural Wyoming, you're faced with 
                        the most important choice in your grad school career: your advisor.\n
                        """))
            return 'pick_advisor'

        elif choice == 2:
            print(dedent("""
                        This at least makes some sense; 
                        there's no real benefit to picking one high-ranking department over another, 
                        so you might as well enjoy your life these next few years.
                        Though you'll be spending your down time in these years dating, going to parties, 
                        and developing hobbies, now that you're here, 
                        you're faced with the most important choice in your grad school career: your advisor.\n
                        """))
            return 'pick_advisor'

        else:
            print("You need to pick either 1 or 2. If you can't get that, you might struggle at either of these schools.\n")
            return 'pick_program'

class PickAdvisor(Decision):

    def enter(self):
        print(dedent("""
                    This is a tough one. On one hand, you want to choose someone who can help your career in Something 
                    by mentoring you in doing really promising research.
                    On the other hand, academia is filled with stories of advisors 
                    who behave like unstable, paranoid tyrants, 
                    and there's not much you can do if you end up with someone like this. 
                    Except quit the program, I guess.
                    After a few months in your new department, you've narrowed down your options to two professors.\n
                    Do you pick:
                    1. Pammy Dengs, a rising star in the Something field. 
                    Pammy has 100 publications and several ongoing research grants, and did her doctorate at Really Elite U. 
                    She is, however, known to be very hard to work with, and has never actually mentored a PhD student.
                    2. Barry Ringsley, a laid-back full professor who's been in the department 20 years. 
                    You don't really have many research interests in common, 
                    but Barry has a reputation for being easy to work with.
                    3. Bailing on the program rather than make a choice.
                    """))
        
        choice = int(input("> "))

        if choice == 1:
            print(dedent("""
                        Unfortunately, you should have listened to the other students and university staff 
                        who warned you about Dr. Dengs.
                        She turns out to be just as unstable as you'd feared, and she works you 20 hours a day 
                        for the better part of 2 years. She takes all the credit for your work, 
                        so it doesn't even benefit you professionally.
                        You have no time for exercise or a social life, 
                        and your health suffers from the combination of overwork, lack of sleep, stress, and alcohol.
                        One day, a few weeks before your third year, 
                        Pammy abruptly leaves your department for a faculty position at Super Elite U. 
                        She does not offer to take you with her.
                        For good measure (and for no good reason), Pammy badmouthed you to all the faculty behind your back, 
                        and you quickly discover that you're unable to find another advisor. 
                        Despondent, you quit the program.\n                   
                        """))
            return 'sad_life'

        elif choice == 2:
            print(dedent("""
                        Barry turns out to be a good choice for you. His research isn't very inspiring, 
                        but you like him personally and decide to put your head down and move forward in this collaboration.
                        You work very hard for him, and he turns out to be a very good mentor who works very hard for you. 
                        Four years after you entered the program, you are ready to graduate.
                        Barry offers you very general advice, but as a new PhD, 
                        you are now facing a very difficult choice: where to take your career now.\n
                        """))
            return 'first_job'

        elif choice == 3:
            print(dedent("""
                        Wow, a bold choice that absolutely pays off!
                        You only spend about a year in your program before deciding to leave. 
                        Fortunately, the economy is booming when you do so, and you're hired right into a high-paying job.
                        You settle into a fine life while working in the private sector. You get married and start a family. 
                        With some friends you start a business, and after a while you've become wealthy.\n
                        """))
            return 'happy_life'

        else:
            print("Professors Dengs and Ringsley would be disappointed if they knew you couldn't pick a number between 1 and 3.\n")
            return 'pick_advisor'

class FirstJob(Decision):

    def enter(self):
        print(dedent("""
                    Fortunately for you, Barry is a great advocate for your career, 
                    and once you've been on the job market for a while, you discover you have a lot of options.
                    Option 1 is taking a job in the private sector, in the booming Something industry. 
                    But there are other interesting alternatives.
                    Thanks to Barry's connections, you've been offered a tenure-track job at Super Elite U, 
                    which is exciting. There is also a tenure-track job available at Third Rate U, 
                    one of the fallback options you've lined up.\n
                    Do you:
                    1. Take the job in private industry.
                    2. Go for tenure at Super Elite U.
                    3. Take the job at Third Rate U.
                    """))
        
        choice = int(input("> "))

        if choice == 1:
            print(dedent("""
                        This turns out to be a great move for you. 
                        You are welcomed and valued in your new corporate workplace.
                        And you end up building a nice, comfortable life for yourself, 
                        raising a family, taking regular vacations. You are happy.\n
                        """))
            return 'happy_life'

        elif choice == 2:
            print(dedent("""
                        Unfortunately, it looks like Barry forgot to give you a key piece of advice: 
                        elite universities never, ever award tenure to tenure-track faculty.
                        Six years of hard work later, your tenure case is turned down 
                        and your appointment at Super Elite ends.
                        You spend the next few years wandering from school to school 
                        as a non-faculty lecturer with no benefits, working nine months at a time.
                        You never settle anywhere or find any sort of community or connection with people.\n
                        """))
            return 'sad_life'

        elif choice == 3:
            print(dedent("""
                        Though it seems counter-intuitive, this decision actually works out well for you.
                        The training you've gotten from Barry serves you well, 
                        and you do well to make friends and form collaborations with the faculty at Third Rate.
                        You successfully publish many papers, and in your third year there, 
                        you submit your case for tenure, which is accepted.
                        Shortly after that you are offered a lateral move with tenure 
                        to the Something department at Pretty Elite U. 
                        It comes with a sizable raise, and no one at Third Rate blames you for taking it.\n
                        Now, in your new office at Pretty Elite, you have a new decision to make: 
                        what direction will your scholarly work take?\n
                        """))
            return 'work_direction'

        else:
            print("None of these options are going to work out for you if you can't pick one that's available. Try a number between 1 and 3.")
            return 'first_job'

class WorkDirection(Decision):

    def enter(self):
        print(dedent("""
                    Basically, the choice you face now is this: 
                    will you focus on playing politics and ingratiating yourself with your colleagues at Pretty Elite U, 
                    or will you focus on good scholarship regardless of whether others like it?\n
                    Do you:
                    1. Chart your own path, and try to be a great scientist no matter what the cost.
                    2. Focus your energies on status and the internal politics of the university, 
                    and try to ingratiate yourself to your superiors as a professional advancement strategy.\n
                    """))
        
        choice = int(input("> "))

        if choice == 1:
            print(dedent("""
                        This sounds really cool at the time, but it's a disaster as a career path.
                        The senior faculty in your department quickly get sick of you. 
                        Editors and peer reviewers stop publishing your work. All of your applications for grants fail.
                        You spend the next 30 years at Pretty Elite U, 
                        getting assignments to teach undergrads at 8am on Mondays, 
                        but otherwise being unwanted and ignored by your "colleagues."
                        This sucks, of course, but at least you have tenure. So there's that.\n
                        """))
            return 'sad_life'
        
        elif choice == 2:
            print(dedent("""
                        It sucks to embrace groveling for approval as a career path; 
                        it's just as soul-crushing and humiliating as it sounds.
                        But it has its rewards. 
                        Soon enough you are promoted to full professor, your applications for research funding are successful, 
                        and you publish lots of research.
                        Other than the fact that you're bored and miserable, 
                        and that your boredom and misery affects all your personal relationships and your health, it's great.\n
                        """))
            return 'personal_integrity'

        else:
            print("Sorry, there's no ducking this choice if you're going to have a career in academia. Pick 1 or 2.\n")
            return 'work_direction'

class PersonalIntegrity(Decision):

    def enter(self):
        print(dedent("""
                    You've been a full professor for about 10 years, when a global political crisis suddenly erupts, 
                    and the field of Something is at the center of it.
                    All of the leading figures in your field, including your department chair, 
                    are loudly advocating for extremist government policies you find appalling.
                    Nevertheless, you're important enough in your field that everyone expects some action from you.\n
                    Do you:
                    1. Maintain your integrity, and boldly denounce the things you don't agree with.
                    2. Say nothing and hope the whole things blows over.
                    3. Realize that having principles only makes sense when they're professionally convenient, 
                    and loudly support everything the leaders in your field are saying.\n
                    """))
        
        choice = int(input("> "))

        if choice == 1:
            print(dedent("""
                        You can sleep reasonably well at night, knowing you've stuck to your principles 
                        and done the right thing. But your colleagues throughout academia don't see it that way.
                        Abruptly you are treated as a pariah by everyone at Pretty Elite U and all your colleagues elsewhere. 
                        Your department moves your office to a basement. Your sponsors cut off your funding. 
                        Journals stop publishing your work.
                        You spend 20 more years like this at the university. 
                        You're just as bored and miserable as you were before the crisis, but now there are no rewards to it.
                        But at least you have tenure.\n
                        """))
            return 'sad_life'

        elif choice == 2:
            print(dedent("""
                        You've spent much of your adult life learning to play organizational politics, 
                        so you know how to be just agreeable enough that all your colleagues assume you agree with them.
                        Eventually the crisis blows over, and the massive backlash 
                        against the leaders of the Something field doesn't come back against you. 
                        You continue doing as you've done before.
                        Nevertheless, the next 20 years are a special sort of hell for you. 
                        Other Something scholars don't forget that you didn't join them during the crisis, 
                        so your career stagnates. Others get promoted when you expect to.
                        And at the same time, knowing that you didn't stand on principle fills you with guilt, 
                        especially as you ponder the horrible effects of the government's actions during the crisis.
                        This guilt follows you the rest of your days. But, you know, at least you have tenure.\n
                        """))
            return 'sad_life'

        elif choice == 3:
            print(dedent("""
                        Using the cover that you and other Something researchers have given them, 
                        the government employs awful policies that harm millions of people.
                        Your colleagues in the field reward you for supporting them so enthusiastically, 
                        in spite of the public backlash you all face.
                        You are promoted to department chair, 
                        and then to the chair of the broader school in which the Something department sits. 
                        The government funds even more of your research, 
                        and you are more successful than ever in the publishing world.
                        Unfortunately, you are torn apart by guilt over what you've done, 
                        and this follows you the rest of your days. 
                        You retire to great ceremony in your late 60s, 
                        but are never able to look yourself in the mirror again.\n
                        """))
            return 'sad_life'

        else:
            print("I get that this is a really terrible choice, but you have to pick a number between 1 and 3.\n")
            return 'personal_integrity'

class Finished(Decision):

    def enter(self):
        return 'finished'

# Map class initialization: this tells the game where you're going
class Map(object):

    choices = {
        'college_path': CollegePath(),
        'pick_program': PickProgram(),
        'pick_advisor': PickAdvisor(),
        'first_job': FirstJob(),
        'work_direction': WorkDirection(),
        'personal_integrity': PersonalIntegrity(),
        'happy_life': HappyLife(),
        'sad_life': SadLife(),
        'finished': Finished()
    }

    def __init__(self, start_choice):
        self.start_choice = start_choice

    def next_choice(self, choice_name):
        val = Map.choices.get(choice_name)
        return val
    
    def opening_choice(self):
        return self.next_choice(self.start_choice)
    

a_map = Map('college_path')
a_game = Engine(a_map)
a_game.play()