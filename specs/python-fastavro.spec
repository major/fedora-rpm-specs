# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-fastavro
Version:        1.12.2
Release:        %autorelease
Summary:        Fast Avro for Python

# The fastavro project is licensed MIT, but is derived from Apache Avro which
# is ASL 2.0; see LICENSE and also NOTICE.txt.
#
# The following source files are specifically known to include ASL 2.0 content:
#
#   • fastavro/_read_py.py
#   • fastavro/_write_py.py
#   • fastavro/_write.pyx
#   • fastavro/_read.pyx
#
# SPDX:
License:        MIT AND Apache-2.0
URL:            https://github.com/fastavro/fastavro
Source:         %{pypi_source fastavro}

# Upstream does not test, nor support 32 bit systems
# Issue: https://github.com/fastavro/fastavro/issues/526
# Fedora bug: https://bugzilla.redhat.com/show_bug.cgi?id=1943932
ExcludeArch:    %{ix86}

BuildSystem:    pyproject
# codecs includes snappy, zstandard, and lz4
BuildOption(generate_buildrequires): --extras codecs
BuildOption(install): --assert-license fastavro

BuildRequires:  gcc

BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
%if %{with doc_pdf}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

# See developer_requirements.txt, which also has many unwanted dependencies on
# linters, formatters, typecheckers, etc.:
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist Cython}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist cramjam}
BuildRequires:  %{py3_dist lz4}
BuildRequires:  %{py3_dist zlib_ng}

%global _description %{expand:
Because the Apache Python avro package is written in pure Python, it is
relatively slow. In one test case, it takes about 14 seconds to iterate through
a file of 10,000 records. By comparison, the JAVA avro SDK reads the same file
in 1.9 seconds.

The fastavro library was written to offer performance comparable to the Java
library. With regular CPython, fastavro uses C extensions which allow it to
iterate the same 10,000 record file in 1.7 seconds. With PyPy, this drops to
1.5 seconds (to be fair, the JAVA benchmark is doing some extra JSON
encoding/decoding).

Supported Features

  • File Writer
  • File Reader (iterating via records or blocks)
  • Schemaless Writer
  • Schemaless Reader
  • JSON Writer
  • JSON Reader
  • Codecs (Snappy, Deflate, Zstandard, Bzip2, LZ4, XZ)
  • Schema resolution
  • Aliases
  • Logical Types
  • Parsing schemas into the canonical form
  • Schema fingerprinting

Missing Features

  • Anything involving Avro’s RPC features}

%description %{_description}


%package -n python3-fastavro
Summary:        %{summary}

%description -n python3-fastavro %{_description}


%package doc
Summary:        %{summary}

BuildArch:      noarch

%description doc
Documentation for python-fastavro.


%pyproject_extras_subpkg --name python3-fastavro codecs snappy zstandard lz4


%prep -a
# Remove the already generated C files so we generate them ourselves
find fastavro/ -name '*.c' -print -delete

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py


%build -a
BLIB="${PWD}/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}"
PYTHONPATH="${BLIB}" %make_build --directory=docs man \
    SPHINXOPTS='--nitpicky --jobs=%{?_smp_build_ncpus}'
%if %{with doc_pdf}
PYTHONPATH="${BLIB}" %make_build --directory=docs latex \
    SPHINXOPTS='--nitpicky --jobs=%{?_smp_build_ncpus}'
%make_build --directory=docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install -a
install -D --target='%{buildroot}%{_mandir}/man1' \
    --preserve-timestamps --mode=0644 'docs/_build/man/fastavro.1'


%check -a
# These fail because there are no source lines in the tracebacks from Cython
# modules, even though this works in the upstream CI. We haven’t figured out
# the root cause, but it doesn’t seem to represent a real problem.
k="${k-}${k+ and }not test_regular_vs_ordered_dict_map_typeerror"
k="${k-}${k+ and }not test_regular_vs_ordered_dict_record_typeerror"

%pytest --import-mode=append -k "${k-}"


%files -n python3-fastavro -f %{pyproject_files}
%{_bindir}/fastavro
%{_mandir}/man1/fastavro.1*


%files doc
%license LICENSE NOTICE.txt
%doc ChangeLog
%doc README.md
%if %{with doc_pdf}
%doc docs/_build/latex/fastavro.pdf
%endif


%changelog
%autochangelog
