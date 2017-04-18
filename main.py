# -*- coding: utf8 -*-

import random


PLAYER_COUNT = 10
CARD_COUNT   = 4


ROCK     = 1
SCISSORS = 2
PAPER    = 3

WIN  = "win"
LOSE = "lose"
DRAW = "draw"


class Player:

    ROCK_COUNT     = CARD_COUNT * PLAYER_COUNT
    SCISSORS_COUNT = CARD_COUNT * PLAYER_COUNT
    PAPER_COUNT    = CARD_COUNT * PLAYER_COUNT
    
    def __init__(self, name="", isHuman=False):
        self.rockCount     = CARD_COUNT
        self.scissorsCount = CARD_COUNT
        self.paperCount    = CARD_COUNT
        self.cardCount     = CARD_COUNT * 3

        self.winCount  = 0
        self.loseCount = 0
        self.drawCount = 0

        self.name    = name
        self.isHuman = isHuman

    def choiceCard(self):
        if self.isHuman:
            while True:
                h = input("카드 선택(주먹: 1, 가위: 2, 보자기: 3): ")

                if (h == ROCK and self.rockCount > 0) or \
                   (h == SCISSORS and self.scissorsCount > 0) or \
                   (h == PAPER and self.paperCount > 0):
                       break
                elif h not in [ROCK, SCISSORS, PAPER]:
                    print "유효하지 않은 입력입니다."
                else:
                    print "해당 카드가 없습니다."
        else:
            cardList = []
            cardList += [ROCK]     * self.rockCount
            cardList += [SCISSORS] * self.scissorsCount
            cardList += [PAPER]    * self.paperCount

            h = random.choice(cardList)

        if   h == ROCK:
            self.rockCount  -= 1
            Player.ROCK_COUNT -= 1
        elif h == SCISSORS:
            self.scissorsCount  -= 1
            Player.SCISSORS_COUNT -= 1
        elif h == PAPER:
            self.paperCount  -= 1
            Player.PAPER_COUNT -= 1

        self.cardCount -= 1

        return h

    def win(self):
        self.winCount += 1

    def lose(self):
        self.loseCount += 1

    def draw(self):
        self.drawCount += 1

    def showInfo(self):
        print "ROCK: %d, SCISSORS: %d, PAPER: %d" % (Player.ROCK_COUNT, Player.SCISSORS_COUNT, Player.PAPER_COUNT)

    def showResult(self):
        print "name: %s" % self.name
        print "win: %d, lose: %d, draw: %d" % (self.winCount, self.loseCount, self.drawCount)

    def isEnd(self):
        return self.cardCount == 0


def getResultList(handList):

    countList = [0, 0, 0]

    for hand in handList:
        if   hand == ROCK:     countList[0] += 1
        elif hand == SCISSORS: countList[1] += 1
        elif hand == PAPER:    countList[2] += 1

    handCount = len(handList)

    if handCount in countList \
       or all(c > 0 for c in countList):
        return [DRAW] * handCount

    if   countList[0] > 0 and countList[1] > 0:
        winHand  = ROCK
        loseHand = SCISSORS
    elif countList[1] > 0 and countList[2] > 0:
        winHand  = SCISSORS
        loseHand = PAPER
    else:
        winHand  = PAPER
        loseHand = ROCK

    resultList = []

    for hand in handList:
        if hand == winHand: result = WIN
        else:               result = LOSE

        resultList.append(result)

    return resultList


def test():
    
    p = Player()
    assert p.choiceCard() in [ROCK, SCISSORS, PAPER]
    assert p.rockCount == CARD_COUNT - 1 or p.scissorsCount == CARD_COUNT - 1 or p.paperCount == CARD_COUNT - 1

    p2 = Player(True)
    assert p2.choiceCard() in [ROCK, SCISSORS, PAPER]
    assert p2.rockCount == CARD_COUNT - 1 or p2.scissorsCount == CARD_COUNT - 1 or p2.paperCount == CARD_COUNT - 1

    p3 = Player()
    p4 = Player()

    resultList = getResultList([p3.choiceCard(), p4.choiceCard()])

    for p, result in zip([p3, p4], resultList):
        if result == WIN:
            p.win()
        elif result == LOSE:
            p.lose()
        else:
            p.draw()

    p3.showResult()
    p4.showResult()

    p.showInfo()

    print "Success"


def main():

    playerList = [Player("You", True)]

    for i in range(PLAYER_COUNT - 1):
        playerList.append(Player("Player %d" % (i + 1)))

    roundNum = 1
    while roundNum <= CARD_COUNT * 3:
        
        print "-" * 30
        print "Round %d" % roundNum
        playerList[0].showInfo()
        print "-" * 30
        print

        random.shuffle(playerList)

        pairList = []
        for i in range(PLAYER_COUNT / 2):
            i *= 2
            pairList.append(playerList[i:i+2])

        for p1, p2 in pairList:
            resultList = getResultList([p1.choiceCard(), p2.choiceCard()])

            for p, result in zip([p1, p2], resultList):
                if result == WIN:
                    p.win()
                elif result == LOSE:
                    p.lose()
                else:
                    p.draw()

        print
        for p in playerList:
            p.showResult()
        print

        roundNum += 1

        

    


if __name__ == "__main__":
    #test()
    main()
