Name:           python-pdfminer
Version:        20250416
Release:        %autorelease
Summary:        Tool for extracting information from PDF documents

# The entire source is MIT except:
#
# LicenseRef-Fedora-Public-Domain:
#   pdfminer/arcfour.py
#     - If this is a bundled library, its origin is unclear
#   pdfminer/ascii85.py
#     - If this is a bundled library, its origin is unclear
# The public-domain dedication text was added to public-domain-text.txt in
# fedora-license-data in commit e75b02b91633c17388b6e67dc5884702f8bee22b:
# https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/194
#
# APAFML:
#   pdfminer/fontmetrics.py
#     - Data extracted and converted from the AFM files:
#       https://www.ctan.org/tex-archive/fonts/adobe/afm/
#
# BSD-3-Clause:
#   pdfminer/cmap/*
#     - Both the original bundled data and the data generated from the
#       adobe-mappings-cmap package are BSD-3-Clause-licensed.
#
# Apache-2.0 AND MIT:
#   pdfminer/_saslprep.py
#     - Forked from from Apache-2.0 code by MongoDB, Inc.—originally
#       pymongo/saslprep.py in mongo-python-driver (python-pymongo), with
#       additional modifications in pyHanko (not yet packaged); see
#       docs/licenses/LICENSE.pyHanko.
#
# Adobe-Glyph:
#   pdfminer/glyphlist.py
#     - Contains both code under the base MIT license and data extracted and
#       converted from
#       https://partners.adobe.com/public/developer/en/opentype/glyphlist.txt
#       under the Adobe Glyph List License
License:        %{shrink:
                MIT AND
                LicenseRef-Fedora-Public-Domain AND
                APAFML AND
                BSD-3-Clause AND
                (Apache-2.0 AND MIT) AND
                Adobe-Glyph
                }
URL:            https://github.com/pdfminer/pdfminer.six
# This has the samples/ directory stripped out. While upstream claims the
# sample PDFs are “freely distributable”, they have unclear or unspecified
# licenses, which makes them unsuitable for Fedora. This applies especially,
# but not exclusively, to the contents of samples/nonfree.
#
# Generated with ./get_source.sh %%{version}
Source0:        pdfminer.six-%{version}-filtered.tar.zst
# Script to generate Source0; see comments above.
Source1:        get_source.sh
# Man pages written by hand for Fedora in groff_man(7) format using the
# command’s --help output
Source2:        dumppdf.1
Source3:        pdf2txt.1

BuildSystem:            pyproject
BuildOption(prep):      -S git
BuildOption(generate_buildrequires): -x image
BuildOption(install):   -l pdfminer

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  make

# We use the Japan1, Korea1, GB1, and CNS1 CMaps:
BuildRequires:  adobe-mappings-cmap-devel >= 20190730

# We do not generate BR’s from the “dev” extra because it includes an exact
# version requirement on mypy (and we do not intend to do typechecking), and it
# pulls in nox and black. We just want to use plain pytest.
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
Pdfminer.six is a community maintained fork of the original PDFMiner. It is a
tool for extracting information from PDF documents. It focuses on getting and
analyzing text data. Pdfminer.six extracts the text from a page directly from
the sourcecode of the PDF. It can also be used to get the exact location, font
or color of the text.

It is built in a modular way such that each component of pdfminer.six can be
replaced easily. You can implement your own interpreter or rendering device
that uses the power of pdfminer.six for other purposes than text analysis.

Check out the full documentation on Read the Docs
(https://pdfminersix.readthedocs.io/).

Features:

  • Written entirely in Python.
  • Parse, analyze, and convert PDF documents.
  • PDF-1.7 specification support. (well, almost).
  • CJK languages and vertical writing scripts support.
  • Various font types (Type1, TrueType, Type3, and CID) support.
  • Support for extracting images (JPG, JBIG2, Bitmaps).
  • Support for various compressions (ASCIIHexDecode, ASCII85Decode, LZWDecode,
    FlateDecode, RunLengthDecode, CCITTFaxDecode)
  • Support for RC4 and AES encryption.
  • Support for AcroForm interactive form extraction.
  • Table of contents extraction.
  • Tagged contents extraction.
  • Automatic layout analysis.}

%description %{common_description}


%package -n     python3-pdfminer
Summary:        %{summary}

# The import name is pdfminer. The upstream project name (as specified in
# setup.py) is pdfminer.six, which results in a canonical project name of
# pdfminer-six.
%py_provides python3-pdfminer-six

# One file, pdfminer/_saslprep.py, is forked from from ASL 2.0 code by MongoDB,
# Inc.—originally pymongo/saslprep.py in mongo-python-driver
# (python-pymongo)—with additional modifications in pyHanko (not yet packaged),
# where it is pyhanko/pdf_utils/_saslprep.py.
#
# Since this is a fork of the python-pymongo module, and since the fork is not
# part of pyHanko’s public API, there is no possibility of using an unbundled
# version.
#
# The version history of the fork is not clear. We add unversioned virtual
# Provides for both libraries of origin.
Provides:       bundled(python3dist(pymongo))
Provides:       bundled(python3dist(pyhanko))

# We no longer bother to build and install the PDF manual. Since we removed the
# -doc package for Fedora 43, this can be removed after Fedora 45.
Obsoletes:      python-pdfminer-doc < 20240706-4

%description -n python3-pdfminer %{common_description}


%pyproject_extras_subpkg -n python3-pdfminer image


%prep -a
# Unbundle cmap data; it will be replaced in %%build.
rm -vf cmaprsrc/* pdfminer/cmap/*

# Remove shebang line in non-script source
sed -r -i '1{/^#!/d}' pdfminer/psparser.py

# Copy the pyHanko license to the top-level directory so it is automatically
# included in the licenses in the installed dist-info directory.
cp -p docs/licenses/LICENSE.pyHanko ./


%build -p
# Symlink the unbundled CMap resources and convert to the pickled format.
for cmap in Japan1 Korea1 GB1 CNS1
do
  ln -s "%{adobe_mappings_rootpath}/${cmap}/cid2code.txt" \
      "cmaprsrc/cid2code_Adobe_${cmap}.txt"
done
%make_build cmap PYTHON='%{python3}'

# Make an updated git commit and set a tag for setuptools_git_version.
#
# Normally this kind of thing would be in %%prep, but we must do this
# immediately before building the wheel, and after any other changes such as
# rebuilding the pickled CMap resources, lest setuptools_git_version determine
# that the tree is “dirty” and produce a “post” version, appearing in the
# binary RPMs as something like YYYYMMDD^post0.
#
# We *also* need to ensure that git ignores anything that might be written
# during %%pyproject_wheel, or we will still end up with a dirty/postrelease
# version.
echo '*pyproject*' >> .gitignore
git add -A
git commit -m 'Imitate upstream release %{version}'
git tag '%{version}'


# %%build -a
# Debug dynamic versioning:
# git status
# %%{python3} -m setuptools_git_versioning --verbose


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE2}' '%{SOURCE3}'

%py3_shebang_fix '%{buildroot}%{_bindir}'

# Also, ship symlinks of the scripts without the .py extension.
for script in pdf2txt dumppdf
do
  ln -sf "${script}.py" "%{buildroot}%{_bindir}/${script}"
done


%check -a
# Skipped tests (and ignored files) are those that require the sample PDFs,
# which are not included in our version of the source tarball.
k="${k-}${k+ and }not TestColorSpace"
k="${k-}${k+ and }not TestDumpImages"
k="${k-}${k+ and }not TestDumpPDF"
k="${k-}${k+ and }not TestExtractPages"
k="${k-}${k+ and }not TestExtractText"
k="${k-}${k+ and }not TestOpenFilename"
k="${k-}${k+ and }not TestPdf2Txt"
k="${k-}${k+ and }not TestPdfDocument"
k="${k-}${k+ and }not TestPdfPage"
k="${k-}${k+ and }not test_font_size"
k="${k-}${k+ and }not test_paint_path_quadrilaterals"
k="${k-}${k+ and }not test_pdf_with_empty_characters_horizontal"
k="${k-}${k+ and }not test_pdf_with_empty_characters_vertical"

ignore="${ignore-} --ignore=tests/test_tools_dumppdf.py"
ignore="${ignore-} --ignore=tests/test_tools_pdf2txt.py"

%pytest -k "${k-}" ${ignore-}


%files -n python3-pdfminer -f %{pyproject_files}
%doc CHANGELOG.md README.md

%{_bindir}/pdf2txt
%{_bindir}/pdf2txt.py
%{_mandir}/man1/pdf2txt.1*
%{_bindir}/dumppdf
%{_bindir}/dumppdf.py
%{_mandir}/man1/dumppdf.1*


%changelog
%autochangelog
