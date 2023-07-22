%global __cmake_in_source_build 1

# Some tests are failing:
# https://github.com/hoene/libmysofa/issues/129
%ifarch s390x
%global _without_tests 1
%endif
%if 0%{?el7:1}
%ifarch ppc64le
%global _without_tests 1
%endif
%endif

Name:           libmysofa
Version:        1.2.1
Release:        5%{?dist}
Summary:        C functions for reading HRTFs

License:        BSD
URL:            https://github.com/hoene/libmysofa
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(zlib)
BuildRequires: make
# for tests
%{?!_without_tests:BuildRequires: nodejs}


%description
This is a simple set of C functions to read AES SOFA files, if they
contain HRTFs stored according to the AES69-2015 standard.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n mysofa
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n mysofa
Tools for %{name}.


%prep
%autosetup -p1


%build
mkdir -p build
cd build
%cmake3 \
  -DBUILD_STATIC_LIBS=OFF \
  -DCODE_COVERAGE=OFF \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  ..

%make_build


%install
cd build
%make_install


%{?!_without_tests:
%check
cd build
make test || (cat Testing/Temporary/LastTest.log && exit 1)
}


%ldconfig_scriptlets


%files
%license LICENSE
%doc README.md
%{_libdir}/libmysofa.so.1*

%files -n mysofa
%{_bindir}/mysofa2json
%dir %{_datadir}/libmysofa
%{_datadir}/libmysofa/default.sofa
%{_datadir}/libmysofa/MIT_KEMAR_normal_pinna.sofa

%files devel
%doc CODE_OF_CONDUCT.md
%{_includedir}/mysofa.h
%{_libdir}/libmysofa.so
%{_libdir}/pkgconfig/libmysofa.pc


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Nicolas Chauvet <kwizart@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 08 2021 Nicolas Chauvet <kwizart@gmail.com> - 1.2-4
- Update to 1.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.1-1
- Update to 1.1

* Mon Apr 13 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.0-1
- Initial spec file
