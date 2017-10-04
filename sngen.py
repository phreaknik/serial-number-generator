import click

@click.command()
@click.option('--model', prompt='Model ID',
              help='The product model id code.')
@click.option('--variant', prompt='Variant code',
              help='The product variant code.')
@click.option('--first', prompt='First serial',
              help='The unique serial number to start generation with.')
@click.option('--count', prompt='Quantity',
              help='The number of serial numbers to generate.')
def generateSerials(model, variant, first, count):
    """Print serial number formatted as <model_id>-<variant_code>-<serial>"""
    for i in range(int(count)):
        print(model + '-' + variant + '-' + format(i+int(first), '08'))

if __name__ == '__main__':
    generateSerials()