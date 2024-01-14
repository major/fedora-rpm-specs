%global forgeurl https://github.com/groonga/groonga-normalizer-mysql
Version:        1.2.3
%forgemeta

Name:           groonga-normalizer-mysql
Release:        %autorelease
Summary:        A MySQL compatible normalizer plugin for Groonga

License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  groonga-devel
BuildRequires:  msgpack-devel

Requires:       groonga-libs

%description
Groonga-normalizer-mysql is a Groonga plugin. It provides MySQL compatible
normalizers and a custom normalizers to Groonga.

%package        devel
Summary:        Development files for groonga-normalizer-mysql
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides development files for groonga-normalizer-mysql.

%prep
%autosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \

%cmake_build

%install
%cmake_install

rm -r %{buildroot}%{_datadir}/doc/groonga-normalizer-mysql

%files
%license doc/text/lgpl-2.0.txt
%doc README.md
%dir %{_libdir}/groonga
%dir %{_libdir}/groonga/plugins/
%dir %{_libdir}/groonga/plugins/normalizers
%{_libdir}/groonga/plugins/normalizers/mysql.so

%files devel
%{_libdir}/pkgconfig/groonga-normalizer-mysql.pc

%changelog
%autochangelog
