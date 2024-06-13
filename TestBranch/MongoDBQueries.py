#Players from Germany

germanplayers = {
    'country': 'Germany'
}
#Players from china and under the age of 10

{
    'country': 'China', 
    'age': {
        '$lt': 10
    }
}

#Players who have the lastname Guo, are older than 15 and from Germany
    
{
        'lastname': 'Guo', 
        'age': {
            '$gt': 15
        }, 
        'country': 'Germany'
}