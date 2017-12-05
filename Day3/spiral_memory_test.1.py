import spiral_memory
if __name__ == '__main__':
    # part 1
    assert spiral_memory.execute(1) == 0
    assert spiral_memory.execute(12) == 3
    assert spiral_memory.execute(23) == 2
    assert spiral_memory.execute(1024) == 31
    assert spiral_memory.execute(368078) == "?"
