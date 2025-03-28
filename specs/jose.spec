Name:           jose
Version:        14
Release:        %autorelease
Summary:        Tools for JSON Object Signing and Encryption (JOSE)

License:        Apache-2.0
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  jansson-devel >= 2.10
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  asciidoc
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
José is a command line utility for performing various tasks on JSON
Object Signing and Encryption (JOSE) objects. José provides a full
crypto stack including key generation, signing and encryption.

%package -n lib%{name}
Summary:        Library implementing JSON Object Signing and Encryption
Conflicts:      jansson < 2.10
Provides:       lib%{name}-openssl = %{version}-%{release}
Obsoletes:      lib%{name}-openssl < %{version}-%{release}
Provides:       lib%{name}-zlib = %{version}-%{release}
Obsoletes:      lib%{name}-zlib < %{version}-%{release}

%description -n lib%{name}
This package contains a C library for performing JOSE operations.

%package -n lib%{name}-devel
Summary:        Development files for lib%{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       jansson-devel
Provides:       lib%{name}-openssl-devel = %{version}-%{release}
Obsoletes:      lib%{name}-openssl-devel < %{version}-%{release}
Provides:       lib%{name}-zlib-devel = %{version}-%{release}
Obsoletes:      lib%{name}-zlib-devel < %{version}-%{release}

%description -n lib%{name}-devel
This package contains development files for lib%{name}.

%prep
%autosetup -S git

%build
%meson
%meson_build

%install
rm -rf %{buildroot}
%meson_install
rm -rf %{buildroot}/%{_libdir}/lib%{name}.la

%check
%meson_test

%ldconfig_scriptlets -n lib%{name}

%files
%{_bindir}/%{name}
%{_mandir}/man1/jose*.1*
%license COPYING

%files -n lib%{name}
%license COPYING
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}-devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/jose*.3*

%changelog
%autochangelog
