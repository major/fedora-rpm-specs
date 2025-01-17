# NOTE: The spasm build produces binaries with names that clash with
# existing Fedora packages (e.g., bitmap).  Therefore, we use environment
# modules to isolate the binaries.

Name:           spasm
Version:        1.2
Release:        %autorelease
Summary:        Sparse gaussian elimination modulo a small prime

# GPL-2.0-or-later: the project as a whole
# BSD-3-Clause:
# - src/arm_instruction_set_select.h
# - src/cycleclock.h
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://github.com/cbouilla/spasm
VCS:            git:%{url}.git
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        spasm.module.in
# Update some obsolete m4 macros
Patch:          %{name}-m4-update.patch
# Fix some bitwise AND operators that should be logical AND operators
# Included in this upstream commit:
# https://github.com/cbouilla/spasm/commit/25741a99cabd87736890e3d07cc012584a98e7cb
Patch:          %{name}-wrong-and.patch
# Fix an incorrect printf format specifier
# Included in this upstream commit:
# https://github.com/cbouilla/spasm/commit/25741a99cabd87736890e3d07cc012584a98e7cb
Patch:          %{name}-printf-format.patch
# Fix a variable that might be clobbered by longjmp
# The affected file no longer exists in upstream git
Patch:          %{name}-clobbered.patch
# Update cycleclock.h to support s390x and fix an aarch64 bug
# The affected file no longer exists in upstream git
Patch:          %{name}-cycleclock.patch
# Fix binary file reading on big endian architectures
# The affected code no longer exists in upstream git
Patch:          %{name}-endian.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  environment(modules)
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  metis-devel
BuildRequires:  pkgconfig(fflas-ffpack)
BuildRequires:  pkgconfig(flint)
BuildRequires:  pkgconfig(givaro)
BuildRequires:  pkgconfig(lemon)
BuildRequires:  pkgconfig(linbox)
BuildRequires:  pkgconfig(mpfr)

Requires:       environment(modules)
Requires:       libspasm%{?_isa} = %{version}-%{release}

%global _desc %{expand:
SpaSM is a software library devoted to sparse gaussian elimination
modulo a small prime _p_.}

%description %_desc

This package contains command line binaries for accessing spasm
functionality.

%package     -n libspasm
Summary:        Sparse gaussian elimination modulo a small prime

%description -n libspasm %_desc

This package contains the spasm shared library.

%package     -n libspasm-devel
Summary:        Development files for libspasm

%description -n libspasm-devel %_desc

This package contains headers and library links for developing
applications that use libspasm.

%prep
%autosetup -p1

%conf
# Generate the configure script
autoreconf -fi .

%build
%configure --disable-static --with-givaro --with-fflas-ffpack --with-linbox

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install

# Move the binaries
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_bindir} %{buildroot}%{_libdir}/%{name}

# Make the environment-modules file
mkdir -p %{buildroot}%{_modulesdir}
sed 's,@LIBDIR@,'%{_libdir}/%{name}',g;' < %{SOURCE1} \
  > %{buildroot}%{_modulesdir}/%{name}-%{_arch}

# We don't install cycleclock.h or config.h, so don't try to include them
# from the public header
sed -e '/define SPASM_TIMING/d' \
    -e '/include "config.h"/d' \
    -i.orig %{buildroot}%{_includedir}/spasm.h
touch -r %{buildroot}%{_includedir}/spasm.h.orig %{buildroot}%{_includedir}/spasm.h
rm %{buildroot}%{_includedir}/spasm.h.orig

%check
make check

%files
%doc AUTHORS README.md
%license COPYING
%{_libdir}/%{name}/
%{_modulesdir}/%{name}-%{_arch}

%files -n libspasm
%{_libdir}/libspasm.so.0*

%files -n libspasm-devel
%{_includedir}/spasm.h
%{_libdir}/libspasm.so

%changelog
%autochangelog
