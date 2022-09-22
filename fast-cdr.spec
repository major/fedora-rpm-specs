%global project Fast-CDR
%global soversion 1

Name:       fast-cdr
Version:    1.0.23
Release:    2%{?dist}
Summary:    Fast Common Data Representation (CDR) Serialization Library

License:    ASL 2.0
URL:        http://www.eprosima.com
Source0:    https://github.com/eprosima/%{project}/archive/v%{version}/%{name}-%{version}.tar.gz    

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
eProsima FastCDR is a C++ library that provides two serialization mechanisms.
One is the standard CDR serialization mechanism, while the other is a faster
implementation that modifies the standard.

%package devel
Summary:    Development files and libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and libraries for %{name}

%prep
%setup -q -n %{project}-%{version} 

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc "doc/Users Manual.odt"
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}
%{_datadir}/fastcdr

%files devel
%{_libdir}/*.so
%{_includedir}/fastcdr
%{_libdir}/cmake/fastcdr

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 29 2022 Rich Mattes <richmattes@gmail.com> - 1.0.23-1
- Update to release 1.0.23

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Rich Mattes <richmattes@gmail.com> - 1.0.14-1
- Update to release 1.0.14
- Fix CMake FTBFS (rhbz#1863527)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Rich Mattes <richmattes@gmail.com> - 1.0.10-2
- Move CMake script installation to libdir

* Tue Jul 02 2019 Rich Mattes <richmattes@gmail.com> - 1.0.10-1
- Update to release 1.0.10

* Sat Jun 09 2018 Rich Mattes <richmattes@gmail.com> - 1.0.7-0.1.git8d14897
- Update to 1.0.7 pre-release

* Sat Jun 10 2017 Rich Mattes <richmattes@gmail.com> - 1.0.6-2
- Rename endian define to avoid conflicts

* Fri Jun 9 2017 Rich Mattes <richmattes@gmail.com> - 1.0.6-1
- Initial package
