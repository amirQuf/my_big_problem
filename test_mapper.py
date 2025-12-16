from keyboard_mapper import map_en_to_fa ,map_fa_to_en


def test_map_fa_to_en():
    fa_input  = "فثسف"
    result  = map_fa_to_en(fa_input)
    
    assert  result == "test"
    
    
    
    

def test_map_en_to_fa():
    en_input = "jsj"
    result = map_en_to_fa(en_input)
    
    assert result == "تست"    
    
