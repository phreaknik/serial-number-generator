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
@click.option('--filename', prompt='File name (csv)',
              help='The number of serial numbers to generate.')
def generateSerials(model, variant, first, count, filename):
    """Write serial numbers to specified file, formatted as <model_id>-<variant_code>-<serial>"""
    file_handle = open(filename, 'w')
    file_handle.write('Model: ,S/N: ,Bar-code: \n')
    for i in range(int(count)):
        serial = format(i+int(first), '08')
        file_handle.write(model + '-' + variant + ',' + serial + ',' + model + '-' + 
                          variant + '-' + serial + '\n')
    file_handle.close()

if __name__ == '__main__':
    generateSerials()