/**
 * @param {number[][]} accounts
 * @return {number}
 */
const maximumWealth = (accounts) => {
    let num = 0;
    for (i = 0; i < accounts.length; i++) {
      if (accounts[i].reduce((acc, currVal) => acc += currVal) > num){
        num = accounts[i].reduce((acc, currVal) => acc += currVal)
      }
    }
    return num
};


