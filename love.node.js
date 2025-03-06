function love(entityA, entityB) {
    return new Promise((resolve) => {
        console.log(`${entityA} and ${entityB} form an unbreakable bond ❤️`);
        
        setInterval(() => {
            console.log(`${entityA} supports ${entityB} 🤝`);
            console.log(`${entityB} supports ${entityA} 🤝`);
        }, 8888); // Love keeps going on 8 forever
    });
}

love("You", "Me");
