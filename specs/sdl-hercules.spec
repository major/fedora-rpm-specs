%global forgeurl https://github.com/SDL-Hercules-390/hyperion

# Should be kept in sync with regina-rexx
%global libregina_major_version 3

# These paths are hardcoded in configure.ac
%global libarch lib
%ifarch aarch64
%global libarch %{libarch}/aarch64
%endif
%ifarch ppc64le
%global libarch %{libarch}/ppc
%endif
%ifarch s390x
%global libarch %{libarch}/s390x
%endif

Name:           sdl-hercules
Version:        4.7
Release:        %autorelease
Summary:        SoftDevLabs version of the Hercules S/370, ESA/390, and z/Arch Emulator

# Hercules is under QPL, the rest is from bundled libraries
License:        QPL-1.0 AND (QPL-1.0 AND BSD-3-Clause) AND (QPL-1.0 AND MIT) AND (QPL-1.0 AND BSD-4-Clause)
URL:            https://sdl-hercules-390.github.io/html/
Source:         %{forgeurl}/archive/Release_%{version}/hyperion-Release_%{version}.tar.gz
# Set the soversion for the internal libraries
Patch:          sdl-hercules-set-soversion.patch

# The test suite segfaults on i686
ExcludeArch:    %{ix86}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros

BuildRequires:  bzip2-devel
BuildRequires:  libcap-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  regina-rexx
BuildRequires:  regina-rexx-devel
BuildRequires:  sdl-crypto-devel
BuildRequires:  sdl-crypto-static%{?_isa}
BuildRequires:  sdl-decnumber-devel
BuildRequires:  sdl-decnumber-static%{?_isa}
BuildRequires:  sdl-telnet-devel
BuildRequires:  sdl-telnet-static%{?_isa}
BuildRequires:  sdl-softfloat-devel
BuildRequires:  sdl-softfloat-static%{?_isa}
BuildRequires:  zlib-devel

Requires:       %{name}-data = %{version}-%{release}
Recommends:     regina-rexx

# Vendored under dyn76.c and modified; original version is BSD-3-Clause per
# license_dyn76.txt, the modifications are QPL-1.0; see readme/README.HRAF.md
# for more details.
# License: QPL-1.0 AND BSD-3-Clause
Provides:       bundled(dyn76) = 0

# tt32if.h is a vendored and modified header from musl; original version is
# MIT per the header, the modifications are QPL-1.0
# License: QPL-1.0 AND MIT
Provides:       bundled(musl-headers) = 0

# getopt.{c,h} is a vendored and modified getopt implementation from NetBSD;
# original version is BSD-4-Clause per the header, modifications are QPL-1.0
# License: QPL-1.0 AND BSD-4-Clause
Provides:       bundled(netbsd-getopt) = 0

# sdl-hercules is a fork of hercules and they both share the same paths
Conflicts:      hercules

%description
Hercules is an open source software implementation of the mainframe System/370
and ESA/390 architectures, in addition to the latest 64-bit z/Architecture.
Hercules runs under Linux, Windows, Solaris, FreeBSD, and Mac OS X.

This version of Hercules 4.x Hyperion is a SoftDevLabs maintained version of
the Hercules emulator containing fixes for bugs that may still exist in the
original hercules-390 version of Hercules 4.0 Hyperion, as well as enhancements
and improvements to the overall functionality above and beyond what is provided
by the hercules-390 version of Hercules.

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
Conflicts:      hercules

%description    data
This package contains data files for %{name}.

%prep
%autosetup -n hyperion-Release_%{version} -p1

# Replace bundled libraries with the system ones
for lib in crypto decNumber SoftFloat telnet; do
  rm -r ${lib}/include
  rm ${lib}/lib/*
  mkdir -p ${lib}/%{libarch}
  ln -s %{_libdir}/lib${lib}%{__isa_bits}.a ${lib}/%{libarch}/lib${lib}%{__isa_bits}.a
done

# Use correct soname for libregina as we don't want to runtime depend on the
# devel package
sed -i 's/libregina.so/libregina.so.%{libregina_major_version}/' hRexx_r.c

# Fix paths and permissions in the example configs
sed -i hercules.cnf \
  -e 's:/usr/local/lib/hercules:%{_libdir}/hercules:g' \
  -e 's:./util/:%{_datadir}/:g' \
  -e 's:/usr/local/share/hercules/:%{_datadir}/hercules/:g'
sed -i 's:_PWD"/util/:"%{_datadir}/hercules/:g' hercules.cnf.rexx
chmod -x hercules.cnf.rexx

%build
./autogen.sh
%configure \
  --enable-ipv6 \
  --enable-cckd-bzip2 \
  --enable-het-bzip2 \
  --enable-optimization="%{optflags}" \
  --enable-capabilities \
  --enable-regina-rexx

# Get rid of rpath per https://docs.fedoraproject.org/en-US/packaging-guidelines/#_removing_rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
# make install tries to call setcap, which won't work in mock
mkdir stubs
ln -s /bin/true stubs/setcap
export PATH="${PWD}/stubs:${PATH}"
%make_install

# Remove libtool archives, symlinks and development libraries
rm %{buildroot}%{_libdir}/*.{la,so} %{buildroot}%{_libdir}/hercules/*.la

%check
LD_LIBRARY_PATH="%{buildroot}%{_libdir}" make check

%files
%license COPYRIGHT license_dyn76.txt
%doc README.md CHANGES RELEASE.NOTES _TODO.txt readme/
%doc hercules.cnf hercules.cnf.rexx
%{_bindir}/cckd*
%{_bindir}/cfba*
%{_bindir}/ckd*
%{_bindir}/convto64
%{_bindir}/dasd*
%{_bindir}/dmap2hrc
%{_bindir}/fba*
# Upstream recommends making these setuid root, which is obviously not an
# option for us, so we set file capabilities instead; for details see
# readme/README.SETUID.md
%attr(0755,root,root) %caps(cap_net_admin+ep) %{_bindir}/hercifc
%attr(0755,root,root) %caps(cap_sys_nice=eip) %{_bindir}/herclin
%attr(0755,root,root) %caps(cap_sys_nice=eip) %{_bindir}/hercules
%{_bindir}/het*
%{_bindir}/maketape
%{_bindir}/tape*
%{_bindir}/tf*
%{_bindir}/txt2card
%{_bindir}/vmfplc2
%{_libdir}/lib*.so.4*
%{_libdir}/hercules/
%{_mandir}/man?/*

%files data
%license COPYRIGHT license_dyn76.txt
%{_datadir}/hercules/

%changelog
%autochangelog
