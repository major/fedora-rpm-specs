Name:           python-uvloop
Version:        0.18.0
Release:        %autorelease
Summary:        Ultra fast implementation of asyncio event loop on top of libuv

License:        MIT OR Apache-2.0
URL:            https://github.com/MagicStack/uvloop
Source:         %{url}/archive/v%{version}/uvloop-%{version}.tar.gz

# Fix compatibility with Cython 3.
# Notice that it doesn't work with older Cython (<3).
# From https://github.com/MagicStack/uvloop/issues/586#issuecomment-1862458472
# Amended metadata changes to BuildRequire Cython>=3.
Patch:          cython3.patch

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

# We don’t have aiohttp==3.9.0b0; see if we can make do with the packaged
# version.
sed -r -i 's/aiohttp==3.9.0b0;/aiohttp>=3.8.5;/' pyproject.toml

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

%pytest -v ${ignore-}

%files -n python3-uvloop -f %{pyproject_files}
#license LICENSE-APACHE LICENSE-MIT
%doc README.rst

%changelog
%autochangelog
