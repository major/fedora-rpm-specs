Name:           libbraiding
Version:        1.2
%global so_version 0
Release:        %autorelease
Summary:        Library for computations on braid groups

License:        GPL-2.0-or-later
URL:            https://github.com/miguelmarco/libbraiding
Source:         %{url}/archive/%{version}/libbraiding-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  make
BuildRequires:  gcc-c++

%description
This library allows various computations on braid groups, such as normal forms.


%package        devel
Summary:        Development files for libbraiding

Requires:       libbraiding%{?_isa} = %{version}-%{release}

%description    devel
The libbraiding-devel package contains libraries and header files for
developing applications that use libbraiding.


%prep
%autosetup


%build
# Upstream does not generate the configure script
autoreconf --force --install --verbose

%configure --disable-static

# Work around libtool reordering -Wl,--as-needed after all the libraries.
sed -i 's|CC=.g..|& -Wl,--as-needed|' libtool

%make_build


%install
%make_install

# We do not want the libtool files
find '%{buildroot}' -type f -name '*.la' -print -delete


%files
%license LICENSE
%doc README.md
%{_libdir}/libbraiding.so.%{so_version}{,.*}


%files devel
%doc CHANGELOG
%{_includedir}/braiding.h
%{_includedir}/cbraid*.h
%{_libdir}/libbraiding.so


%changelog
%autochangelog
