programa {
  inclua biblioteca Matematica --> mat
 
  funcao inicio() {
    

    real peso
    real estatura
    real imc

    escreva("digite seu peso: ")
    leia(peso)

    escreva("digite sua estatura: ")
    leia(estatura)

    imc =  peso / (estatura * estatura)

    escreva("seu IMC e: ", mat.arredondar(imc,2))

  }
}
