import argparse
from os import path
from default import DEFAULT_ARGS_VALUES

def greatings():
    print(''' 
        TODO /// 
    '''
    )
    print('Generate an awesome international and national day calendar for your house / office ...')
    print('Made with love by @Vald○R - github.com/valdesche \n\n')

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--format',
                        help = 'Output format',
                        choices= DEFAULT_ARGS_VALUES['format_choices'],
                        default= DEFAULT_ARGS_VALUES['format'],
                        required = False)       
    parser.add_argument('-outdir', '--outputdirectory',
                        help = 'Output folder path',
                        default= DEFAULT_ARGS_VALUES['outputdirectory'],
                        required = False)                                      
    return parser.parse_args()


"""
    Start the scrapper
"""
def start_scrapper():
    return


def main():
    greatings()
    args = parse_args()
    output_format = args.format
    output_directory = args.outputdirectory

    if (path.isdir(output_directory)):
        # result = start_scrapper()
        print( 'Successfull Execution !!!')
    else:
        raise ValueError('Incorrect Directory path...')
    

if __name__ == '__main__':
    main()
