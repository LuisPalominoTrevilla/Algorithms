// I assume that both arrays are not ordered since no clarification was given
function solution(stores, houses) {
    // write your code in JavaScript (Node.js 8.9.4)
    // Sort only the stores
    stores.sort((a, b) => a-b);
    
    let nearStores = [];
    // Since the problem says that I should focus on correctness
    // The algorithm will be a brute force approach
    for (var house of houses) {
        let nearestStore = stores[0];
        for (var i = 1; i < stores.length; i++) {
            if (Math.abs(house - stores[i]) < Math.abs(house-nearestStore)) {
                nearestStore = stores[i];
            }else{
                break;
            }
        }
        nearStores.push(nearestStore);
    }
    return nearStores;
}

let stores = [1,5,20,16,11];
let houses = [5, 10, 17];

solution(stores, houses);