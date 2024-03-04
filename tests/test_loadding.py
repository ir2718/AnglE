# -*- coding: utf-8 -*-

def test_loadding():
    import numpy as np
    from angle_emb import AnglE, Prompts

    angle = AnglE.from_pretrained('WhereIsAI/UAE-Large-V1')
    vecs = angle.encode('hello world')
    assert isinstance(vecs, np.ndarray)
    vecs = angle.encode(['hello world', 'hi there👋'])
    assert isinstance(vecs, np.ndarray)
    # test prompt
    angle.set_prompt(prompt=Prompts.C)
    vecs = angle.encode({'text': 'hello world'})
    assert isinstance(vecs, np.ndarray)
    vecs = angle.encode([{'text': 'hello world', 'text': 'hi there👋'}])
    assert isinstance(vecs, np.ndarray)


def test_2dmse_loadding():
    import numpy as np
    from angle_emb import AnglE

    angle = AnglE.from_pretrained('WhereIsAI/UAE-Large-V1')
    vecs = angle.encode('hello world', layer_index=20)
    assert isinstance(vecs, np.ndarray)
    vecs = angle.encode(['hello world', 'hi there👋'], layer_index=20, embedding_size=512)
    assert isinstance(vecs, np.ndarray)
