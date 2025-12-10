%global sover   1
%global libname libcryptopant%{sover}
%global upname cryptopANT

Version:        1.3.2
Name:           cryptopant
Release:        %autorelease
Summary:        IP address anonymization library shared library

License:        GPL-2.0-only
URL:            http://ant.isi.edu/software/cryptopANT
Source0:        %{url}/%{upname}-%{version}.tar.gz
# TODO: Include LICENSE file in sources archive.
Source1:        https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt#/LICENSE

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Provides:       %{libname}%{?_isa} = %{version}-%{release}
Provides:       %{upname}%{?_isa} = %{version}-%{release}

%description
cryptopANT is a library for IP address anonymization. It implements
a widely used prefix-preserving technique known as "cryptopan".
This is ANT's project implementation of this technique for
anonymization of ipv4 and ipv6 addresses.

%package devel
Summary:        IP address anonymization library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel
Provides:       %{upname}-devel%{?_isa} = %{version}-%{release}

%description devel
cryptopANT is a library for IP address anonymization. It implements
a widely used prefix-preserving technique known as "cryptopan".
This is ANT's project implementation of this technique for
anonymization of ipv4 and ipv6 addresses.

%package utils
Summary:        IP address anonymization library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
cryptopANT is a library for IP address anonymization. It implements
a widely used prefix-preserving technique known as "cryptopan".
This is ANT's project implementation of this technique for
anonymization of ipv4 and ipv6 addresses.

%prep
%autosetup -n %{upname}-%{version}
[ -f LICENSE ] || install -p -m 0644 %{SOURCE1} LICENSE # < TODO: remove this


%build
autoreconf -fsi
%configure --with-scramble_ips
%make_build


%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{upname}.{a,la}


%check
%make_build test


%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{upname}.so.%{sover}*


%files devel
%{_includedir}/%{upname}*
%{_mandir}/man3/%{upname}*
%{_libdir}/lib%{upname}.so


%files utils
%{_bindir}/scramble_ips


%changelog
%autochangelog
