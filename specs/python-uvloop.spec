%global _with_bootstrap %{defined el10}

%bcond_with bootstrap

Name:           python-uvloop
Version:        0.19.0
Release:        %autorelease
Summary:        Ultra fast implementation of asyncio event loop on top of libuv

License:        MIT OR Apache-2.0
URL:            https://github.com/MagicStack/uvloop
Source:         %{url}/archive/v%{version}/uvloop-%{version}.tar.gz

# Fix compatibility with Cython 3.
Patch:          https://github.com/MagicStack/uvloop/pull/587.patch

# Fix build with Python 3.13: _Py_RestoreSignals() has been moved to internals
Patch:          https://github.com/MagicStack/uvloop/pull/604.patch

# Fix test_create_server_4 with Python 3.12.5
Patch:          https://github.com/MagicStack/uvloop/pull/614.patch

BuildRequires:  gcc
BuildRequires:  libuv-devel

BuildRequires:  python3-devel

# We avoid generating this via the “dev” dependency, because that would bring
# in unwanted documentation dependencies too.
BuildRequires:  %{py3_dist pytest}

%global _description \
uvloop is a fast, drop-in replacement of the built-in asyncio event loop.\
uvloop is implemented in Cython and uses libuv under the hood.

%description %{_description}

%package -n python3-uvloop
Summary:        %{summary}

%description -n python3-uvloop %{_description}

%prep
%autosetup -p1 -n uvloop-%{version}

# There currently doesn’t appear to be a way to pass through these “build_ext
# options,” so we resort to patching the defaults. Some related discussion
# appears in https://github.com/pypa/setuptools/issues/3896.
#
# always use cython to generate code (and generate a build dependency on it)
sed -i -e "/self.cython_always/s/False/True/" setup.py
# use system libuv
sed -i -e "/self.use_system_libuv/s/False/True/" setup.py

# To be sure, no 3rd-party stuff
rm -vrf vendor/

# - https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# - Loosen SemVer pins; we must work with what we have available, especially
#   for test dependencies!
sed -r -i \
    -e "s/^([[:blank:]]*)([\"'](flake8|pycodestyle|mypy)\b)/\\1# \\2/" \
    -e 's/~=/>=/' \
    pyproject.toml

%if %{without bootstrap}
# We don’t have aiohttp==3.9.0b0; see if we can make do with the packaged
# version.
sed -r -i 's/aiohttp==3.9.0b0;/aiohttp>=3.9.0b0;/' pyproject.toml
%else
# Avoid the circular dependency with python-aiohttp in bootstrap mode, it is
# used only inside a test in uvloop.
sed -r -i '/aiohttp/d' pyproject.toml
%endif

# Require Cython 3.x
sed -i 's/\(Cython\)(>=0.29.36,<0.30.0)/\1>=3/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files uvloop

# Don’t ship C sources and headers.
find '%{buildroot}%{python3_sitearch}' -type f -name '*.[ch]' -print -delete
sed -r -i '/\.[ch]$/d' %{pyproject_files}

%check
%ifarch ppc64le
# ignore tests that fail on ppc64le
ignore="${ignore-} --ignore=tests/test_pipes.py"
%endif

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
ignore="${ignore-} --ignore=tests/test_sourcecode.py"

# Don’t import the “un-built” uvloop from the build directory.
mkdir -p _empty
cd _empty
ln -s ../tests/ .

# test_getaddrinfo_8 and _9 run getaddrinfo with zero-length inputs
# libuv 1.48.0+ rejects that
# reported as https://github.com/MagicStack/uvloop/issues/596
# test_create_unix_server_1 fails with Python 3.13
# https://github.com/MagicStack/uvloop/pull/604
%pytest -v ${ignore-} -k "not test_getaddrinfo_8 and not test_getaddrinfo_9 and not test_create_unix_server_1"

%files -n python3-uvloop -f %{pyproject_files}
#license LICENSE-APACHE LICENSE-MIT
%doc README.rst

%changelog
%autochangelog
