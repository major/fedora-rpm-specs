Name:           python-blosc2
Version:        2.5.1
Release:        %autorelease
Summary:        Python wrapper for the Blosc2 compression library
License:        BSD-3-Clause
URL:            https://blosc.org/python-blosc2/python-blosc2.html
Source:         https://github.com/Blosc/python-blosc2/archive/v%{version}/python-blosc2-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc-g++
BuildRequires:  ninja-build
BuildRequires:  blosc2-devel >= 2.13.1

ExcludeArch:    %{ix86}

%global _description %{expand:
C-Blosc2 is the new major version of C-Blosc, and is backward compatible with
both the C-Blosc1 API and its in-memory format. Python-Blosc2 is a Python
package that wraps C-Blosc2, the newest version of the Blosc compressor.

In addition, Python-Blosc2 aims to leverage the new C-Blosc2 API so as to
support super-chunks, multi-dimensional arrays (NDArray), serialization and
other bells and whistles introduced in C-Blosc2. Although this is always and
endless process, it has already caught up with most of the C-Blosc2 API
capabilities.}

%description %_description

%package -n python3-blosc2
Summary:        %{summary}

%description -n python3-blosc2 %_description

%prep
%autosetup -p1

# This seems to be the best way to prevent the "bespoke build system" from doing
# a git clone.
rmdir blosc2/c-blosc2

# Did I say "bespoke build system"? Who needs configuration options.
# Configuration options are for woosies.
sed -r -i '/include_package_data=.*/a cmake_args=["-DUSE_SYSTEM_BLOSC2:BOOL=ON"],' \
    setup.py

# Those dependencies are generated incorrectly
sed -r -i 's/"(cmake|ninja)",//g; s/oldest-supported-//g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires requirements-test-wheels.txt

%build
export VERBOSE=1
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files blosc2

%check
OPTIONS=(
)

%pytest tests/ "${OPTIONS[@]}" -v \
%ifarch s390x
  || :    # https://github.com/Blosc/python-blosc2/issues/125
%endif

%files -n python3-blosc2 -f %{pyproject_files}
%doc README.rst RELEASE_NOTES.md

%changelog
%autochangelog
