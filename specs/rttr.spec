%global commit0 7edbd580cfad509a3253c733e70144e36f02ecd4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           rttr
Version:        0.9.7
Release:        0.11git%{shortcommit0}%{?dist}
Summary:        Run Time Type Reflection

License:        MIT
URL:            https://www.rttr.org
Source0:        https://github.com/rttrorg/rttr/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         0001-cmake-Don-t-set-non-default-permissions.patch

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  cmake3
BuildRequires:  make

%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  catch2-devel
%else
BuildRequires:  catch-devel
%endif
BuildRequires:  rapidjson-devel


%description
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%package -n librttr
Summary:        Run Time Type Reflection for C++
Provides:       bundled(nonius) = 1.1.2

%description -n librttr
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%package  -n librttr-devel
Summary:        Header files for the C++ Run Time Type Reflection library
Requires:       librttr%{?_isa} = %{version}-%{release}

%description  -n librttr-devel
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-documentation documentations for %{name}.


%prep
%autosetup -p1 -n %{name}-%{commit0}
find . -type f -exec chmod -x {} ';'
sed -i 's/PERMISSIONS OWNER_READ//' CMake/*.cmake

# Unbundle
rm -rf 3rd_party/catch-1.12.0 3rd_party/rapidjson-1.1.0

# Fix catch2 include
%if ! 0%{?el7}
find src/unit_tests/ -name *.cpp -exec sed -i -e 's|catch/catch.hpp|catch2/catch.hpp|' {} ';'
find src/unit_tests/ -name *.h -exec sed -i -e 's|catch/catch.hpp|catch2/catch.hpp|' {} ';'
%endif

# Disable compiler Werror
# See also https://github.com/rttrorg/rttr/issues/317
# and https://github.com/rttrorg/rttr/issues/357
sed -i -e 's/target_compile_options/#target_compile_options/' CMake/utility.cmake


%build
%cmake3 \
  -DCMAKE_INSTALL_CMAKEDIR=cmake \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DBUILD_EXAMPLES=OFF \
  -DBUILD_PACKAGE=OFF \
  -DUSE_PCH=OFF

%cmake3_build


%install
rm -rf __doc
%cmake3_install

# Rework doc
mkdir -p __doc
mv %{buildroot}%{_prefix}/doc/* __doc
find __doc -type f -exec chmod 0644 {} ';'
rm -rf %{buildroot}%{_datadir}/rttr/{LICENSE.txt,README.md}


%check
%ctest3 run_tests


%files -n librttr
%license LICENSE.txt
%doc README.md
%{_libdir}/librttr_core.so.%{version}

%files -n librttr-devel
%{_includedir}/rttr/
%{_libdir}/librttr_core.so
%{_datadir}/rttr/cmake/

%files doc
%doc __doc/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-0.11git7edbd58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-0.10git7edbd58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Michel Lind <salimma@fedoraproject.org> - 0.9.7-0.9git7edbd58
- Use catch2-devel on EL9 as well, for the catch 3 / catch2 upgrade

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-0.8git7edbd58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-0.7git7edbd58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-0.6git7edbd58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Nicolas Chauvet <kwizart@gmail.com> - 0.9.7-0.5git7edbd58
- Disable Werror on rttr - rhbz#2113682

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-0.4git7edbd58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-0.3git7edbd58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-0.2git7edbd58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 16 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.9.7-0.1git7edbd58
- Update to pre 0.9.7

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.9.6-3
- Drop main package
- Split docs

* Wed Feb 24 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.9.6-2
- Backport patch for aarch64

* Mon Feb 08 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.9.6-1
- Initial spec file
