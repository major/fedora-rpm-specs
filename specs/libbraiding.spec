Name:           libbraiding
Version:        1.3.1
%global so_version 0
Release:        %autorelease
Summary:        Library for computations on braid groups

License:        GPL-2.0-or-later
URL:            https://github.com/miguelmarco/libbraiding
Source:         %{url}/archive/%{version}/libbraiding-%{version}.tar.gz

# Correct typo in configure.ac
# https://github.com/miguelmarco/libbraiding/commit/b174832026c2412baec83277c461e4df71d8525c
Patch:          %{url}/commit/b174832026c2412baec83277c461e4df71d8525c.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  make
BuildRequires:  gcc-c++

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
This library allows various computations on braid groups, such as normal forms.


%package        devel
Summary:        Development files for libbraiding

Requires:       libbraiding%{?_isa} = %{version}-%{release}

%description    devel
The libbraiding-devel package contains libraries and header files for
developing applications that use libbraiding.


%prep
%autosetup -p1


%conf
# Upstream does not generate the configure script
autoreconf --force --install --verbose

%configure --disable-static

# Work around libtool reordering -Wl,--as-needed after all the libraries.
sed -i 's|CC=.g..|& -Wl,--as-needed|' libtool


%build
%make_build


%install
%make_install


# Upstream does not provide any tests.


%files
%license LICENSE
%doc README.md
%doc CHANGELOG
%{_libdir}/libbraiding.so.%{so_version}{,.*}


%files devel
%{_includedir}/braiding.h
%{_includedir}/cbraid*.h
%{_libdir}/libbraiding.so
%{_libdir}/pkgconfig/libbraiding.pc


%changelog
%autochangelog
