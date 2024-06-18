from django.shortcuts import render, redirect
import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

def index(request):
    if request.method == "POST":
        guess = int(request.POST.get('guess', ''))
        if 'attempts' not in request.session:
            request.session['attempts'] = 0

        request.session['attempts'] += 1

        if guess == target_number:
            message = f"Congratulations! You guessed the number in {request.session['attempts']} attempts."
            request.session['attempts'] = 0  # Reset attempts
            return render(request, 'game/result.html', {'message': message})
        elif abs(guess - target_number) <= 5:
            if guess < target_number:
                message = "A little low. Try again!"
            else:
                message = "A little high. Try again!"
        else:
            if guess < target_number:
                message = "Too low. Try again!"
            else:
                message = "Too high. Try again!"

        return render(request, 'game/index.html', {'message': message})

    return render(request, 'game/index.html')
