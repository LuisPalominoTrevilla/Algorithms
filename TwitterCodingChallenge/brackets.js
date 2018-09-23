function braces(values) {
    let stack = [];
    let result = [];
    for (let brackets of values) {
        stack = [];
        let valid = true;
        for (let bracket of brackets) {
            if (bracket == '[' || bracket == '(' || bracket == '{') {
                stack.push(bracket);
                continue;
            }
            if (stack.length == 0){
                valid = false;
                break;
            }
            const prevBracket = stack.pop();
            if (bracket == ']' && prevBracket != '[' || bracket == '}' && prevBracket != '{' || bracket == ')' && prevBracket != '(') {
                valid = false;
                break;
            }
        }
        if (valid && stack.length == 0) {
            result.push('YES');
        }else{
            result.push('NO');
        }
    }
    return result;
}

console.log(braces(['{[()]}','{[(])}','{{[[(())]]}}']));