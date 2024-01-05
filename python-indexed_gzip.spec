# Tests are not meant to be run against installed version, says upstream
# (https://github.com/pauldmccarthy/indexed_gzip/issues/13). Still, we manage
# to make it work. Note that some tests are very slow.
%bcond tests 1

%bcond nibabel 1

Name:           python-indexed_gzip
Version:        1.8.7
Release:        %autorelease
Summary:        Fast random access of gzip files in Python

License:        Zlib
URL:            https://github.com/pauldmccarthy/indexed_gzip
Source:         %{pypi_source indexed_gzip}

%global desc %{expand:
The indexed_gzip project is a Python extension which aims to provide a drop-in
replacement for the built-in Python gzip.GzipFile class, the IndexedGzipFile.

indexed_gzip was written to allow fast random access of compressed NIFTI image
files (for which GZIP is the de-facto compression standard), but will work with
any GZIP file. indexed_gzip is easy to use with nibabel.

The standard gzip.GzipFile class exposes a random access-like interface (via
its seek and read methods), but every time you seek to a new point in the
uncompressed data stream, the GzipFile instance has to start decompressing from
the beginning of the file, until it reaches the requested location.

An IndexedGzipFile instance gets around this performance limitation by building
an index, which contains *seek points*, mappings between corresponding
locations in the compressed and uncompressed data streams. Each seek point is
accompanied by a chunk (32KB) of uncompressed data which is used to initialize
the decompression algorithm, allowing us to start reading from any seek point.
If the index is built with a seek point spacing of 1MB, we only have to
decompress (on average) 512KB of data to read from any location in the file.}

%description %{desc}

%package -n python3-indexed-gzip
Summary:        %{summary}
BuildRequires:  python3-devel

BuildRequires:  gcc
BuildRequires:  zlib-devel

%if %{with tests}
# tests_require in setup.py:
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist numpy}
%if %{with nibabel}
BuildRequires:  %{py3_dist nibabel}
%endif
# added downstream to run tests in parallel:
BuildRequires:  %{py3_dist pytest-xdist}
%endif

# The binary subpackage was renamed to match the project canonical name
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_canonical_project_name).
# Ideally, the whole package would be renamed to python-indexed-gzip. This
# provides a clean upgrade path.
%py_provides python3-indexed_gzip
Obsoletes:      python3-indexed_gzip < 1.7.0-4

%description -n python3-indexed-gzip %{desc}

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n indexed_gzip-%{version} -p1
# Remove shebangs from non-script sources
find indexed_gzip -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'
# Make sure Cythonized C source files are not present in the tarball; they must
# be regenerated. Retain “hand-written” C sources.
find indexed_gzip -type f -name '*.pyx' | sed -r 's/\.pyx$/.c/' | xargs -r rm -vf

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l indexed_gzip

%check
%if %{with tests}
%pytest %{buildroot}%{python3_sitearch}/indexed_gzip -n auto -k "${k-}"
%endif

%files -n python3-indexed-gzip -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
