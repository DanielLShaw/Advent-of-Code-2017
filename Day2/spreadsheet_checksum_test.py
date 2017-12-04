import spreadsheet_checksum
if __name__ == '__main__':
    assert spreadsheet_checksum.execute("example.tsv") == 6
    assert spreadsheet_checksum.execute("input.tsv") == 0
