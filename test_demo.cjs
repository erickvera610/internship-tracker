const assert=require('node:assert/strict');
const {run}=require('./docs/demo.js');
let saved='[]';global.localStorage={getItem:()=>saved,setItem:(k,v)=>saved=v};assert.equal(run({}).applications.length,0);assert.throws(()=>run({company:'',role:'a',status:'Saved'}));run({company:'Example',role:'Intern',status:'Applied',deadline:''});assert.equal(run({}).counts.Applied,1);
console.log('Browser demo behavior checks passed');
