import csv
import os
import os.path
import io
import chardet
import re


def splitfiles(indir='in', outdir='out', tmpdir='tmp', splitter='At Time TIN'):
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    if not os.path.exists(tmpdir):
        os.mkdir(tmpdir)

    for input_file in os.listdir(indir):
        full_input_file = os.path.join(indir, input_file)
        rows, d = [], {}
        (f_root, f_ext) = os.path.splitext(input_file)
        if f_ext == '.csv':
            print full_input_file

            encoding = get_encoding(full_input_file)

            with io.open(full_input_file, 'r', encoding=encoding) as fi:
                reader = csv.reader(fi, delimiter='\t', quotechar='"')
                rows = [r for r in reader]

            headers = rows[0]
            print headers
            splitter_index = headers.index(splitter)
            input_rows, output_rows, output_files = len(rows), 0, 0
            msgs = ''

            for row in rows:
                d[row[splitter_index]] = d.get(row[splitter_index], []) + [row]

            for i, k in enumerate(d.keys()):
                klean = ''.join([c for c in k if re.match(r'\w', c)])
                split_file_path = os.path.join(outdir, '{f_root}_{k}{f_ext}'.format(
                    f_root=f_root, k=klean, f_ext=f_ext))
                with open(split_file_path, 'wb') as csv_writefile:
                    w = csv.writer(csv_writefile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    w.writerow(headers)
                    r = [w.writerow(r) for r in d[k]]
                    check_r = len(r)
                    output_rows += check_r
                    output_files += 1
                    msgs += 'wrote {rows} rows in {f} #{i}\n'.format(rows=check_r, f=split_file_path, i=i)

            if input_rows != output_rows:
                print 'ERROR: input_rows = {input_rows}, output_rows = {output_rows}\n{msgs}'.format(
                    input_rows=input_rows, output_rows=output_rows, msgs=msgs)
            else:
                print '{input_rows} rows in {input_file} split to {output_files} files, exiting.'.format(
                    input_rows=input_rows, input_file=input_file, output_files=output_files)


def get_encoding(inputfile):
    f = open(inputfile, 'r')
    rawdata = f.read()
    f.close()
    return chardet.detect(rawdata)['encoding']


def linkings(url):
    urls = {'assignable':'https://{url}/#/site/A3696/views/PatientProfileList_twb/PatientInformationProfileExport'}


if __name__ == "__main__":
    splitfiles()
