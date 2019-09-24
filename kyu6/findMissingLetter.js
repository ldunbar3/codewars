// https://www.codewars.com/kata/find-the-missing-letter/train/javascript

const findMissingLetter = array => {
    numArray = array.map((letter, index) => array.join('').charCodeAt(index))
    el = numArray.find((num, index) => num !== numArray[index + 1] - 1)
    return String.fromCharCode(el + 1);
  }