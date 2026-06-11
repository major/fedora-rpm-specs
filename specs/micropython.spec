%global debug_package %{nil}

# NLR code is incompatible with Link Time Optimizations
# https://github.com/micropython/micropython/issues/8421
%global _lto_cflags %nil

# Add -Wformat as it's required along with -Wformat-security
# set by redhat-rpm-config
%global _warning_options %_warning_options -Wformat

Name:           micropython
Version:        1.28.0
Release:        %autorelease
Summary:        Implementation of Python 3 with very low memory footprint

# micropython itself is MIT
# micropython-libs is MIT
# berkeley-db is BSD-4-Clause-UC
# mbedtls is Apache-2.0
License:        MIT AND BSD-4-Clause-UC AND Apache-2.0

URL:            http://micropython.org/
Source0:        https://github.com/micropython/micropython/archive/v%{version}.tar.gz

%global berkley_commit 0f3bb6947c2f57233916dccd7bb425d7bf86e5a6
Source1:       https://github.com/pfalcon/berkeley-db-1.xx/archive/%{berkley_commit}/berkeley-db-1.xx-%{berkley_commit}.tar.gz

%global mbedtls_commit 0bebf8b8c7f07abe3571ded48a11aa907a1ffb20
Source2:       https://github.com/Mbed-TLS/mbedtls/archive/%{mbedtls_commit}/mbedtls-%{mbedtls_commit}.tar.gz

%global micropython_lib_commit 8380c7bb8f9e5e5260e9539156742925e00366b2
Source3: https://github.com/micropython/micropython-lib/archive/%{micropython_lib_commit}/micropython-lib-%{micropython_lib_commit}.tar.gz

# Other arches need active porting, i686 removed via:
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExclusiveArch:  %{arm} aarch64 x86_64 riscv64

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  libffi-devel
BuildRequires:  readline-devel
BuildRequires:  execstack
BuildRequires:  openssl-devel

# Part of the tests runs MicroPython and CPython and compares the results.
# MicroPython is ~3.4, but the testing framework supports newer Pythons as well.
# We use the latest working CPython version in those test, setting the
# MICROPY_CPYTHON3 environment variable.
# Normal %%{python3} is used anywhere else.
# There is no runtime dependency on this CPython (or any other).
%global cpython_version_tests 3.13
BuildRequires:  %{_bindir}/python%{cpython_version_tests}

Provides:       bundled(mbedtls) = 3.6.2
Provides:       bundled(libdb) = 1.85
Provides:       bundled(micropython-lib) = %{version}

%description
Implementation of Python 3 with very low memory footprint

%package -n mpy-cross
Summary:        MicroPython cross-compiler
License:        MIT

%description -n mpy-cross
The MicroPython cross-compiler. Compiles .py scripts into .mpy bytecode
files that can be loaded on MicroPython devices.

%package -n micropython-tools
Summary:        MicroPython device tools and utilities
# mpremote, pyboard.py, pydfu.py, uf2conv.py are MIT
# dfu.py is LGPL-3.0-only
License:        MIT AND LGPL-3.0-only
BuildArch:      noarch
Recommends:     python3dist(pyusb)
Recommends:     mpy-cross
%py_provides    python3-mpremote

%description -n micropython-tools
Tools for interacting with MicroPython devices, including mpremote
(remote device interaction), pyboard (serial REPL access), and
DFU/UF2 firmware flashing utilities.

%prep
%autosetup -p1 -n %{name}-%{version}

# git submodules
rmdir lib/berkeley-db-1.xx
tar -xf %{SOURCE1}
mv berkeley-db-1.xx-%{berkley_commit} lib/berkeley-db-1.xx

head -n 32 lib/berkeley-db-1.xx/db/db.c > LICENSE.libdb

rmdir lib/mbedtls
tar -xf %{SOURCE2}
mv mbedtls-%{mbedtls_commit} lib/mbedtls

mv lib/mbedtls/LICENSE LICENSE.mbedtls

rmdir lib/micropython-lib
tar -xf %{SOURCE3}
mv micropython-lib-%{micropython_lib_commit}/ lib/micropython-lib

# Fix shebangs
files=$(grep -rEl '#!/usr/bin/(env )?python' .)
%py3_shebang_fix $files

# Removing pre-built binary; not required for build
rm ports/cc3200/bootmgr/relocator/relocator.bin

# Patch uf2conv.py to find uf2families.json in the installed data directory
sed -i 's|pathname = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)|pathname = os.path.join("%{_datadir}/micropython-tools", filename)|' tools/uf2conv.py

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -d tools/mpremote

%build
# Build the cross-compiler
%make_build -C mpy-cross

# Build the interpreter
%make_build -C ports/unix PYTHON=%{python3} V=1

execstack -c ports/unix/build-standard/micropython

# Build mpremote wheel
pushd tools/mpremote
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
popd

%check
# Reference: https://git.alpinelinux.org/aports/tree/testing/micropython/APKBUILD
# float rounding fails https://github.com/micropython/micropython/issues/4176
%ifarch riscv64
rm tests/float/float_parse.py tests/float/float_parse_doubleprec.py
%endif
pushd ports/unix
export MICROPY_CPYTHON3=python%{cpython_version_tests}
make PYTHON=%{python3} V=1 test
popd

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 755 ports/unix/build-standard/micropython %{buildroot}%{_bindir}

# mpy-cross
install -pm 755 mpy-cross/build/mpy-cross %{buildroot}%{_bindir}

# mpremote
pushd tools/mpremote
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files mpremote
popd

# Utility scripts
install -pm 755 tools/pyboard.py %{buildroot}%{_bindir}/micropython-pyboard
install -pm 755 tools/dfu.py %{buildroot}%{_bindir}/micropython-dfu
install -pm 755 tools/pydfu.py %{buildroot}%{_bindir}/micropython-pydfu
install -pm 755 tools/uf2conv.py %{buildroot}%{_bindir}/micropython-uf2conv

# Data files for uf2conv
mkdir -p %{buildroot}%{_datadir}/micropython-tools
install -pm 644 tools/uf2families.json %{buildroot}%{_datadir}/micropython-tools/

%files
%doc README.md
%license LICENSE LICENSE.libdb LICENSE.mbedtls
%{_bindir}/micropython

%files -n mpy-cross
%doc mpy-cross/README.md
%license LICENSE
%{_bindir}/mpy-cross

%files -n micropython-tools -f %{pyproject_files}
%doc tools/mpremote/README.md
%license LICENSE
%{_bindir}/mpremote
%{_bindir}/micropython-pyboard
%{_bindir}/micropython-dfu
%{_bindir}/micropython-pydfu
%{_bindir}/micropython-uf2conv
%{_datadir}/micropython-tools/

%changelog
%autochangelog
