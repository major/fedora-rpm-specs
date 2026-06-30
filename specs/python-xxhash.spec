Name:           python-xxhash
Version:        3.8.0
Release:        %autorelease
Summary:        Python Binding for xxHash

# The entire source is BSD-2-Clause. When the PyPI sdist is used (vs. the
# GitHub archive), a bundled copy of portions of the xxhash C library is also
# present in the source archive; it is under the same license and is removed in
# %%prep.
License:        BSD-2-Clause
URL:            https://github.com/ifduyue/python-xxhash
Source:         %{pypi_source xxhash}

# Register the “benchmark” pytest mark
# https://github.com/ifduyue/python-xxhash/pull/164
# Cherry-picked to v3.8.0.
Patch:          0001-Register-the-benchmark-pytest-mark.patch

BuildSystem:    pyproject
BuildOption(install): --assert-license xxhash

BuildRequires:  gcc
BuildRequires:  pkgconfig(libxxhash) >= 0.8.2

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
xxhash is a Python binding for the xxHash library by Yann Collet.}

%description %{common_description}


%package -n python3-xxhash
Summary:        %{summary}

%description -n python3-xxhash %{common_description}


%prep -a
# Remove bundled xxhash library
rm --recursive --verbose deps


%build -p
# Normally, no extra flags are required to link the xxhash shared library, but
# we are prepared:
export CFLAGS="${CFLAGS} $(pkgconf --cflags libxxhash)"
export LDFLAGS="${LDFLAGS} $(pkgconf --libs-only-L libxxhash)"
export LDFLAGS="${LDFLAGS} $(pkgconf --libs-only-other libxxhash)"
export XXHASH_LINK_SO='1'


%check -a
# Benchmarks are not useful to run downstream, and they would not print results
# when run with the test suite anyway.
%pytest --import-mode=append --verbose -m 'not benchmark'


%files -n python3-xxhash -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
