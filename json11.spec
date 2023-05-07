Name: json11
Version: 1.0.0
Release: 10%{?dist}

Summary: A tiny JSON library for C++11
License: MIT
URL: https://github.com/dropbox/%{name}
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake

%description
Json11 is a tiny JSON library for C++11, providing JSON parsing
and serialization.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup
sed -i 's@lib/@%{_lib}/@g' CMakeLists.txt
sed -i 's@lib/@%{_lib}/@g' json11.pc.in
echo "set_property(TARGET json11 PROPERTY SOVERSION 0)" >> CMakeLists.txt

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DJSON11_BUILD_TESTS=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/lib%{name}.so.0

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.hpp
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild
