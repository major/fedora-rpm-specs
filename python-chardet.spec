# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-chardet
Version:        5.1.0
Release:        %autorelease
Summary:        Python character encoding detector

# The entire source, after tests/ are filtered, is LGPL-2.0-or-later. See the
# comment above Source0 for more details on tests/.
License:        LGPL-2.0-or-later
URL:            https://github.com/chardet/chardet
# A filtered source tarball, obtained by (see Source1):
#
#   ./get_source %%{version}
#
# is required because the contents of tests/ are under various undocumented
# licenses and are, for the most part, not freely redistributable. See:
#
#   problematic licensing of /tests?
#   https://github.com/chardet/chardet/issues/231
Source0:        chardet-%{version}-filtered.tar.xz
Source1:        get_source
# Hand-written for Fedora in groff_man(7) format based on --help output
Source2:        chardetect.1

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  tex-xetex-bin
BuildRequires:  /usr/bin/xindy
%endif

%global common_description %{expand:
Chardet: The Universal Character Encoding Detector

Detects:

  • ASCII, UTF-8, UTF-16 (2 variants), UTF-32 (4 variants)
  • Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (Traditional and Simplified
    Chinese)
  • EUC-JP, SHIFT_JIS, CP932, ISO-2022-JP (Japanese)
  • EUC-KR, ISO-2022-KR, Johab (Korean)
  • KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (Cyrillic)
  • ISO-8859-5, windows-1251 (Bulgarian)
  • ISO-8859-1, windows-1252 (Western European languages)
  • ISO-8859-7, windows-1253 (Greek)
  • ISO-8859-8, windows-1255 (Visual and Logical Hebrew)
  • TIS-620 (Thai)

ISO-8859-2 and windows-1250 (Hungarian) probers have been temporarily
disabled.}

%description
%{common_description}


%package -n python3-chardet
Summary:        %{summary}

%description -n python3-chardet
%{common_description}


%package        doc
Summary:        Documentation for python-chardet

%description    doc
%{common_description}


%prep
%autosetup -n chardet-%{version}

# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/conf.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files chardet
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE2}'


%check
# We cannot run the upstream tests because they would require data files with
# problematic license status.
%pyproject_check_import


%files -n python3-chardet -f %{pyproject_files}
%{_bindir}/chardetect
%{_mandir}/man1/chardetect.1*


%files doc
%license LICENSE
%doc README.rst
%if %{with doc_pdf}
%doc docs/_build/latex/chardet.pdf
%endif


%changelog
%autochangelog
