Name:           cjose
Version:        0.6.2.8
Release:        %autorelease
Summary:        C library implementing the Javascript Object Signing and Encryption (JOSE)

License:        MIT
URL:            https://github.com/OpenIDC/cjose
Source0:        https://github.com/OpenIDC/cjose/releases/download/v%{version}/cjose-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  openssl-devel
BuildRequires:  jansson-devel
BuildRequires:  check-devel
BuildRequires: make

%description
Implementation of JOSE for C/C++


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
%make_build


%install
%make_install
find %{buildroot} -name '*.a' -exec rm -f {} ';'
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%check
make check || (cat test/test-suite.log; exit 1)

%files
%license LICENSE
%doc CHANGELOG.md README.md
%doc /usr/share/doc/cjose
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/cjose.pc


%changelog
%autochangelog
