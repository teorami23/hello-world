import random
import matplotlib.pyplot as plt

class Store:
change1
change2
change3
    def __init__(self, buyersNumber):
        self._buyersNumber = buyersNumber
        self._prices = {}
        self._generatedInventory = {}
        self._selledInventory = {}
    
    def generateInventory(self, step):
        numNewInventory = random.randint(2 * self._buyersNumber, 5 * self._buyersNumber)
        self._generatedInventory[step] = numNewInventory
    
    def sell(self, quantity, step):
        self._inventory[step] -= quantity
        
    def getCurrentInventory(self):
        totalGenerated = 0
        for step in self._generatedInventory:
            totalGenerated += self._generatedInventory[step]
        
        totalSelled = 0
        for step in self._selledInventory:
            totalSelled += self._selledInventory[step]
        
        return totalGenerated - totalSelled
    
    def getPrice(self, step):
        return self._prices[step]
    
    def calculatePrice(self, step):
        self._prices[step]= 100+(50+random.randint(0, 20))*step
        
    def sell(self, quantity, step):
        self._selledInventory[step] = quantity
        
    def getMoney(self):
        total = 0
        for step in self._selledInventory:
            quantity = self._selledInventory[step]
            price = self._prices[step]
            total += quantity * price
        return total
    
    def getPriceHistory(self):
        return self._prices

    def getStockHistory(self):
        stockHistory = {}
        
        return 0
    
    def generateStockHistory(self):
        history = {}
        total = 0
        for step in self._generatedInventory:
            generated = self._generatedInventory[step]
            selled = self._selledInventory[step]
            total += generated - selled
            history[step] = total
        
        return history


class Buyer:
    
    def __init__(self):
        self._money = 0
    
    def spendMoney(self, quantity):
        self._money -= quantity
    
    def receiveMoney(self):
        newMoney = random.randint(2000, 5000)
        print(f'\nReceive {newMoney}')
        self._money += newMoney
    
    def decideDemand(self):
        return 3
    
    def getMoney(self):
        return self._money
    
    def chooseStoreIndex(self, inventories, prices):
        return 0

    
class Experiment:
    
    def __init__(self, numBuyers, steps):
        self._buyers = [Buyer() for i in range(numBuyers)]
        self._stores = [Store(numBuyers), Store(numBuyers)]
        self._steps = steps
    
    def getNumBuyers(self):
        return len(self._buyers)
    
    def runStep(self, step):
        
        if step == 0 or step % self.getNumBuyers()  == 0:
            
            for store in self._stores:
                store.generateInventory(step)
            
            for buyer in self._buyers:
                buyer.receiveMoney()
                print(f'Buyer money {buyer.getMoney()}')
        
        prices = []
        inventories = []
        for store in self._stores:
            store.calculatePrice(step)
            prices.append(store.getPrice(step))
            inventories.append(store.getCurrentInventory())
            print(f'New Price: {store.getPrice(step)}')
            print(f'Inventory: {store.getCurrentInventory()}')
        print(f'Prices: {prices}')
        print(f'Inventories: {inventories}')
        
        buyer = self.chooseRandomBuyer()
        demand = buyer.decideDemand()
        print(f'New demand {demand}')
        
        storeIndex = buyer.chooseStoreIndex(inventories, prices)
        store = self._stores[storeIndex]
        inventory = store.getCurrentInventory()
        print(f'Choosen store inventory: {inventory}')
        
        numToBuy = demand
        if( inventory < demand):
            numToBuy = inventory
        print(f'Number of inventory to buy: {numToBuy}')
        store.sell(numToBuy, step)
        price = store.getPrice(step)
        buyer.spendMoney(numToBuy*price)
        
        inventoryAfterSelling = store.getCurrentInventory()
        print(f'Inventory after selling: {inventoryAfterSelling}')
        print(f'Buyer money after buying: {buyer.getMoney()}')
        print(f'Store money after selling: {store.getMoney()}')
        print("\n")
        
            
    def chooseRandomBuyer(self):
        randomIndex = random.randint(0, self.getNumBuyers()-1)
        return self._buyers[randomIndex]
        
    def run(self):
        for step in range(1, self._steps + 1):
            self.runStep(step)
        
    def plotPrice(self):
        for store in self._stores:
            priceHistory = store.getPriceHistory()
            x = priceHistory.keys()
            y = priceHistory.values()
            line = plt.scatter(x,y)
        plt.title('Price variation for the two stores')
        plt.legend(["Store 1", "Store 2"])
        plt.show()
        
    def plotPriceStock(self, storeIndex = 0):
        
        store = self._stores[storeIndex]
        fig, ax1 = plt.subplots()
        color = 'tab:red'
        ax1.set_xlabel('steps')
        ax1.set_ylabel('price($)')
        priceHistory1 = store.getPriceHistory()
        x1 = priceHistory1.keys()
        y1 = priceHistory1.values()
        ax1.plot(x1, y1, color)
        
        ax2 = ax1.twinx()
        
        color = 'tab:blue'
        ax2.set_xlabel('steps')
        ax2.set_ylabel('stock($)')
        stockHistory = store.generateStockHistory()
        x2 = stockHistory.keys()
        y2 = stockHistory.values()
        ax2.plot(x2, y2, color)
        
        ax1.tick_params(axis='y', labelcolor = color)
        
        fig.tight_layout()
        plt.title(f'Price and Stock variation for store {storeIndex+1}')
        plt.show()
        
experiment = Experiment(numBuyers=2, steps=20)
experiment.run()
experiment.plotPrice()
experiment.plotPriceStock(0)



    


