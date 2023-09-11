Version:        0.4.1

%global forgeurl https://github.com/freifunk-gluon/ecdsautils
%forgemeta

Name:           ecdsautils
Release:        %autorelease
Summary:        Tiny collection of programs used for ECDSA (keygen, sign, verify)

License:        BSD-2-Clause AND MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  libuecc-devel

%description
This collection of ECDSA utilities can be used to sign and verify data in a
simple manner.


%package        libs
Summary:        Shared libraries for %{name}

%description    libs
The %{name}-libs package contains shared libraries providing
functionality from %{name} to other applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%doc README.md
%license COPYRIGHT
%{_bindir}/ecdsakeygen
%{_bindir}/ecdsasign
%{_bindir}/ecdsaverify
%{_bindir}/ecdsautil


%files libs
%doc README.md
%license COPYRIGHT
%{_libdir}/libecdsautil.so.*


%files devel
%doc README.md
%license COPYRIGHT
%{_includedir}/ecdsautil-%{version}
%{_libdir}/libecdsautil.so
%{_libdir}/pkgconfig/ecdsautil.pc


%changelog
%autochangelog
