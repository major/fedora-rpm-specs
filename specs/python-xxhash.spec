Name:           python-xxhash
Version:        4.0.1
Release:        %autorelease
Summary:        Python Binding for xxHash

License:        BSD-2-Clause
URL:            https://github.com/ifduyue/python-xxhash
# If the PyPI sdist were used (vs. the GitHub archive), a bundled copy of
# portions of the xxhash C library would also be present in the source archive;
# it is under the same license and should be removed in %%prep.
Source:         %{url}/archive/v%{version}/python-xxhash-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(install): --assert-license xxhash

BuildRequires:  gcc
BuildRequires:  pkgconfig(libxxhash) >= 0.8.3

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
xxhash is a Python binding for the xxHash library by Yann Collet.}

%description %{common_description}


%package -n python3-xxhash
Summary:        %{summary}

%description -n python3-xxhash %{common_description}


%build -p
# Normally, no extra flags are required to link the xxhash shared library, but
# we are prepared:
export CFLAGS="${CFLAGS} $(pkgconf --cflags libxxhash)"
export LDFLAGS="${LDFLAGS} $(pkgconf --libs-only-L libxxhash)"
export LDFLAGS="${LDFLAGS} $(pkgconf --libs-only-other libxxhash)"
export XXHASH_LINK_SO='1'


%check -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
ignore="${ignore-} --ignore=tests/test_stubs_pyright.py"

# Avoid importing the “unbuilt” source copy of the package. Simply passing
# --import-mode=append would handle this almost everywhere, but tests involving
# subprocesses and subinterpreters assume “in-tree” testing. We emulate that by
# carefully preparing a directory with just the tests and the “built” package.
# Note that symlinking the tests into the empty directory is not enough: import
# paths are constructed relative to the tests, so we must copy them.
mkdir _empty
ln --symbolic '%{buildroot}%{python3_sitearch}/xxhash' _empty/
cp --preserve --recursive tests _empty/
cd _empty

# Benchmarks are not useful to run downstream, and they would not print results
# when run with the test suite anyway.
%pytest --verbose ${ignore-} -m 'not benchmark'


%files -n python3-xxhash -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
