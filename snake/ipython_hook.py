from IPython.core.inputtransformer import StatelessInputTransformer
from IPython.core.inputtransformer import TokenInputTransformer

from snake.replace_emoji import replace_emoji, output_formatter


@TokenInputTransformer.wrap
def emoji_transformer(line):
    #for t in line: print(t)
    return replace_emoji(line)

def load_ipython_extension(ip):
    ip.input_splitter.python_line_transforms.append(emoji_transformer())
    ip.input_transformer_manager.python_line_transforms.append(emoji_transformer())

    for _type  in (bool, int):
        ip.display_formatter.formatters['text/plain'].for_type(_type, output_formatter)
        ip.display_formatter.formatters['text/html'].for_type(_type, output_formatter)

    ip.set_hook('pre_prompt_hook', lambda x: print('🐍>>>'))

