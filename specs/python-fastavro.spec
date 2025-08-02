# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-fastavro
Version:        1.12.0
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
ExcludeArch:    %{arm32} %{ix86}

BuildRequires:  python3-devel
BuildRequires:  gcc

BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
%if %{with doc_pdf}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

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


%pyproject_extras_subpkg -n python3-fastavro codecs snappy zstandard lz4


%package doc
Summary:        %{summary}
%description doc
Documentation for python-fastavro.


%prep
%autosetup -p1 -n fastavro-%{version}

# Remove the already generated C files so we generate them ourselves
find fastavro/ -name '*.c' -print -delete

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py

# Do not generate dependencies on linters, formatters, typecheckers, etc.:
sed -r -e '/^(black|check-manifest|flake8|mypy|twine)\b/d' \
    -e '/^(coverage|pytest-cov)\b/d' \
    developer_requirements.txt | tee developer_requirements-filtered.txt


%generate_buildrequires
# codecs includes snappy, zstandard, and lz4
%pyproject_buildrequires -x codecs
# For some reason, combining this with the above does not work, even though it
# should. It would be nice to investigate this.
%pyproject_buildrequires developer_requirements-filtered.txt


%build
%pyproject_wheel

BLIB="${PWD}/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}"
PYTHONPATH="${BLIB}" %make_build -C docs man \
    SPHINXOPTS='-n -j%{?_smp_build_ncpus}'
%if %{with doc_pdf}
PYTHONPATH="${BLIB}" %make_build -C docs latex \
    SPHINXOPTS='-n -j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l fastavro

install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D \
    'docs/_build/man/fastavro.1'


%check
# Avoid importing the “un-built” package. The tests really assume we have built
# the extensions in-place, and occasionally use relative paths to the package
# source directory. We would prefer to test the extensions as installed (and
# avoid an extra build step), so we use a symbolic link to make the tests
# appear alongside the built package.
mkdir -p _empty
cd _empty
cp -rp ../tests/ .
ln -s '%{buildroot}%{python3_sitearch}/fastavro' .

# These fail because there are no source lines in the tracebacks from Cython
# modules, even though this works in the upstream CI. We haven’t figured out
# the root cause, but it doesn’t seem to represent a real problem.
k="${k-}${k+ and }not test_regular_vs_ordered_dict_map_typeerror"
k="${k-}${k+ and }not test_regular_vs_ordered_dict_record_typeerror"

%pytest -k "${k-}"


%files -n python3-fastavro -f %{pyproject_files}
%{_bindir}/fastavro
%{_mandir}/man1/fastavro.*


%files doc
%license LICENSE NOTICE.txt
%doc ChangeLog
%doc README.md
%if %{with doc_pdf}
%doc docs/_build/latex/fastavro.pdf
%endif


%changelog
%autochangelog
