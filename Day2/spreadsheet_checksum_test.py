import spreadsheet_checksum
if __name__ == '__main__':
    # part 1
    assert spreadsheet_checksum.part1("example.tsv") == 18
    assert spreadsheet_checksum.part1("input.tsv") == 44887
    # part 2
    assert spreadsheet_checksum.part2("example.tsv") == 18
    assert spreadsheet_checksum.part2("input.tsv") == 44887
