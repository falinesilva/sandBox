class BankAccount {
  private balance: number;
  private interestRate: number;
  private interestCeiling: number;
  private favoriteAccounts: BankAccount[] = [];
  private id: number;

  constructor(
    id: number,
    balance: number,
    interestRate: number,
    interestCeiling: number
  ) {
    this.id = id;
    this.balance = balance;
    this.interestRate = interestRate;
    this.interestCeiling = interestCeiling;
  }

  deposit(amount: number): void {
    this.balance += amount;
  }
  withdraw(amount: number): void {
    if (this.balance - amount < 0) {
      throw new Error(
        `Withdrawl of ${amount} failed due to insufficient funds.`
      );
    } else {
      console.log(`Withdraw of $${amount} was successful.`);
    }
  }

  transferMoney(amount: number, account: BankAccount): void {
    this.withdraw(amount);
    account.deposit(amount);
  }

  getBalance(): number {
    return this.balance;
  }

  getMensualInterest(): number {
    if (this.balance > this.interestCeiling) {
      return this.interestCeiling * this.interestRate;
    } else {
      return this.balance * this.interestRate;
    }
  }
  addAccountToFavorites(account: BankAccount): void {
    this.favoriteAccounts.push(account);
  }

  getFavoriteAccounts(): BankAccount[] {
    return this.favoriteAccounts;
  }

  removeFavoriteAccountByID(id: number): void {
    const indexToRemove = this.favoriteAccounts.findIndex(
      (account: BankAccount) => account.id === id
    );
    if (indexToRemove === -1) {
      throw new Error("Account does not exist in Favorites.");
    }
    this.favoriteAccounts.splice(indexToRemove, 1);
  }
}

const account1 = new BankAccount(777, 40000, 0.01, 50000);

const account2 = new BankAccount(999, 0, 0.01, 50000);

account1.deposit(5);

try {
  account1.withdraw(90000000000000);
} catch (err: unknown) {
  console.log((err as Error).message);
}

console.log("Tests:");
console.log("Account 1 balance:", account1.getBalance());

console.log("Account 2 balance:", account2.getBalance());

account1.transferMoney(5, account2);

console.log("Account 1 balance:", account1.getBalance());

console.log("Account 2 balance:", account2.getBalance());

console.log(account1.getMensualInterest());

account1.addAccountToFavorites(account2);

console.log(account1.getFavoriteAccounts()[0].getBalance());

console.log(account1.getFavoriteAccounts().length);

account1.removeFavoriteAccountByID(999);

console.log(account1.getFavoriteAccounts().length);

console.log("Story example:");

const accountA = new BankAccount(1, 40000, 0.01, 50000);
const accountB = new BankAccount(2, 100000, 0.01, 50000);

accountA.addAccountToFavorites(accountB);

accountA.transferMoney(20000, accountA.getFavoriteAccounts()[0]);

accountA.withdraw(25000);

console.log(accountA.getMensualInterest());

console.log(accountA.getBalance());

accountA.removeFavoriteAccountByID(2);
