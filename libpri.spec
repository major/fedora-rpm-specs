Name:           libpri
Version:        1.6.1
%global so_version 1.4
Release:        %autorelease
Summary:        An implementation of Primary Rate ISDN

# The Makefile is GPL-2.0-or-later, but does not contribute to the licenses of
# the binary RPMs.
#
# The entire following expression applies to the entire package.
License:        %{shrink:
                GPL-2.0-only WITH libpri-OpenH323-exception AND
                GPL-2.0-only WITH Asterisk-exception
                }
URL:            https://www.asterisk.org/
%global src_base https://downloads.asterisk.org/pub/telephony/libpri/releases
Source0:        %{src_base}/libpri-%{version}.tar.gz
Source1:        %{src_base}/libpri-%{version}.tar.gz.asc
# Keyring with developer signatures created on 2023-08-16 with:
#   workdir="$(mktemp --directory)"
#   gpg2 --with-fingerprint libpri-1.6.1.tar.gz.asc 2>&1 |
#     awk '$2 == "using" { print "0x" $NF }' |
#     xargs gpg2 --homedir="${workdir}" \
#         --keyserver=hkps://keyserver.ubuntu.com --recv-keys
#   gpg2 --homedir="${workdir}" --export --export-options export-minimal \
#       > libpri.gpg
#   rm -rf "${workdir}"
# Inspect keys using:
#   gpg2 --list-keys --no-default-keyring --keyring ./libpri.gpg
Source2:        libpri.gpg

# Upstream bug PRI-186:
#   https://issues.asterisk.org/jira/browse/PRI-186
# Debian downstream bug:
#   https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=957470
# Patch from Debian, which we use unmodified:
#   https://bugs.debian.org/cgi-bin/bugreport.cgi?att=1;bug=957470;filename=zero-sized-members.patch;msg=32
Patch:          zero-sized-members.patch

BuildRequires:  gnupg2

BuildRequires:  make
BuildRequires:  gcc

BuildRequires:  dahdi-tools-devel

%description
libpri is a C implementation of the Primary Rate ISDN specification. It was
based on the Bellcore specification SR-NWT-002343 for National ISDN. As of May
12, 2001, it has been tested work to with NI-2, Nortel DMS-100, and Lucent 5E
Custom protocols on switches from Nortel and Lucent.


%package devel
Summary:        Development files for libpri
Requires:       libpri%{?_isa} = %{version}-%{release}

%description devel
The libpri-devel package contains libraries and header files for developing
applications that use libpri.


%package doc
Summary:        Documentation for libpri

BuildArch:      noarch

%description doc
Currently, the libpri-doc package contains the pseudocode for the finite state
machines used in its implementation.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%build
%make_build


%install
%make_install INSTALL_BASE=%{_prefix} libdir=%{_libdir}
# Remove the static library
find %{buildroot} -name '*.a' -print -delete


%check
./rosetest
./testprilib


%files
%license LICENSE
%{_libdir}/libpri.so.%{so_version}


%files devel
%{_includedir}/libpri.h
%{_libdir}/libpri.so


%files doc
%license LICENSE
# Symlinks
%doc CHANGES.md README.md
# Regular files
%doc ChangeLogs/
%doc README
%doc doc/*.fsm


%changelog
%autochangelog
