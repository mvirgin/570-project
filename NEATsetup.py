import neat

def fitFunc(genomes, config):
    pass

def run_NEAT(configFile):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         configFile)

    # Create the population, which is the top-level object for a NEAT run.
    pop = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    # Run for up to 60 generations.
    winner = pop.run(fitFunc, 60)    # fitFunc implementation critical

    # show winner
    print('\nBest genome:\n{!s}'.format(winner))