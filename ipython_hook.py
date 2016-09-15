from IPython.core.inputtransformer import StatelessInputTransformer
from IPython.core.inputtransformer import TokenInputTransformer

from replace_emoji import replace_emoji


@TokenInputTransformer.wrap
def emoji_transformer(line):
    #for t in line: print(t)
    return replace_emoji(line)

def load_ipython_extension(ip):
    ip.input_splitter.python_line_transforms.append(emoji_transformer())
    ip.input_transformer_manager.python_line_transforms.append(emoji_transformer())
    ip.set_hook('pre_prompt_hook', lambda x: print('🐍'))

