from hstest import StageTest, CheckResult, dynamic_test, TestedProgram


class TextBasedAdventureGameTest(StageTest):

    @dynamic_test
    def test1(self):
        main = TestedProgram()
        output = main.start()
        return self.check_welcome(output)

    @dynamic_test
    def test2(self):
        main = TestedProgram()
        output = main.start()
        message = "1- Press key '1' or type 'start' to start a new game"
        if message.lower() not in output.lower():
            return CheckResult.wrong(f"You didn't output: '{message}' in your menu.")
        if main.is_waiting_input():
            output = main.execute("1")
            feedback = "Your program couldn't process input '1' to start a new game! Make sure to output 'Starting a new game...'."
            return self.check_start_new(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test3(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("start")
            feedback = "Your program couldn't process the input 'start' to start a new game! Make sure to output 'Starting a new game...'."
            return self.check_start_new(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test4(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("StARt")
            feedback = "Your program shouldn't be case sensitive when starting a new game!"
            return self.check_start_new(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test5(self):
        main = TestedProgram()
        output = main.start()
        message = "2- Press key '2' or type 'load' to load your progress"
        if message.lower() not in output.lower():
            return CheckResult.wrong(f"You didn't output: '{message}' in your menu.")

        if main.is_waiting_input():
            output = main.execute("2")
            feedback = "Your program couldn't process input '2' to load a game! Make sure to say 'No save data found!'."
            return self.check_start_load(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test6(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("load")
            feedback = "Your program couldn't process input 'load' to load a game! Make sure to say 'No save data found!'."
            return self.check_start_load(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test7(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("lOAd")
            feedback = "Your program shouldn't be case sensitive when loading a game!."
            return self.check_start_load(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test8(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("5")
            if main.is_waiting_input():
                return self.check_unknown(output)
            return CheckResult.wrong("Your program didn't ask for another input after an unknown input!")
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test9(self):
        main = TestedProgram()
        output = main.start()
        message = "3- Press key '3' or type 'quit' to quit the game"
        if message.lower() not in output.lower():
            return CheckResult.wrong(f"You didn't output: '{message}' in your menu.")

        if main.is_waiting_input():
            output = main.execute("3")
            if main.is_finished():
                feedback = "Your program didn't output 'Goodbye!' before you exit with '3' as input!"
                return self.check_quit(output, feedback)
            return CheckResult.wrong("Your program should end with input '3'!")
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test10(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("quIt")
            if main.is_finished():
                feedback = "Your program didn't output 'Goodbye!' before you exit with 'quIt' as input! Your program must be case insensitive!"
                return self.check_quit(output, feedback)
            return CheckResult.wrong(
                "Your program should end with input 'quIt'! Your program must be case insensitive!")
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test11(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("quit")
            if main.is_finished():
                feedback = "Your program didn't output 'Goodbye!' before you exit with 'quit' as input!"
                return self.check_quit(output, feedback)
            return CheckResult.wrong("Your program should end with input 'quit'!")
        return CheckResult.wrong("Your program didn't ask for input!")

    def check_welcome(self, output, feedback=""):
        required_tokens = ["welcome", "to", "***"]
        if all(token in output.lower() for token in required_tokens):
            return CheckResult.correct()
        return CheckResult.wrong(
            feedback or "Your welcome message doesn't include the following: '***Welcome to <game-title>***'!")

    def check_start_new(self, output, feedback):
        if "starting a new game" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong(feedback)

    def check_start_load(self, output, feedback):
        if "no save data found" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong(feedback)

    def check_unknown(self, output):
        if "unknown input! please enter a valid one" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong(
            "Your program couldn't process unknown input. Make sure to say 'Unknown input! please enter a valid one'. ")

    def check_quit(self, output, feedback):
        if "goodbye" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong(feedback)


if __name__ == '__main__':
    TextBasedAdventureGameTest('game.game').run_tests()