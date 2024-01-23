Name:           lib3mf
Version:        2.2.0
Release:        6%{?dist}
Summary:        Implementation of the 3D Manufacturing Format file standard
License:        BSD-2-Clause
URL:            https://3mf.io

Source0:        https://github.com/3MFConsortium/lib3mf/archive/v%{version}/lib3mf-%{version}.tar.gz

# Adjust the cmake files to:
#  - work with cmake3 command (EPEL 7)
Patch289:       https://github.com/3MFConsortium/lib3mf/pull/289.patch
#  - don't strip the library (breaks debuginfo)
Patch290:       https://github.com/3MFConsortium/lib3mf/pull/290.patch

BuildRequires:  act
BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  libzip-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%bcond_without  tests
%if %{with tests}
BuildRequires:  gtest-devel
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

# Get the pre-Fedora 33 behavior for now until diverged from EPEL 7
%define __cmake_in_source_build 1

%global _description %{expand:
lib3mf is a C++ implementation of the 3D Manufacturing Format standard.
This is a 3D printing standard for representing geometry as meshes.}

%description %_description


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel %_description


%prep
%autosetup -p1
%if 0%{?rhel} && 0%{?rhel} < 9
# The tests FTBFS with old gtest
# https://github.com/google/googletest/issues/2065
sed -i 's/INSTANTIATE_TEST_SUITE_P/INSTANTIATE_TEST_CASE_P/' Tests/CPP_Bindings/Source/*.cpp
%endif

# A bundled x86 executable, we use the packaged one instead
# https://github.com/3MFConsortium/lib3mf/issues/199
rm AutomaticComponentToolkit/bin/act.linux
ln -s /usr/bin/act AutomaticComponentToolkit/bin/act.linux

# c++11 does not work with gtest 1.13+
sed -i 's/ -std=c++11//' CMakeLists.txt


%build
mkdir -p build
cd build
%cmake3 %{!?with_tests:-DLIB3MF_TESTS=OFF} \
  -DUSE_INCLUDED_ZLIB=OFF \
  -DUSE_INCLUDED_LIBZIP=OFF \
  -DUSE_INCLUDED_GTEST=OFF \
  -DUSE_INCLUDED_SSL=OFF \
  -DSTRIP_BINARIES=OFF \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DCMAKE_INSTALL_INCLUDEDIR=include/%{name} \
  ..
%make_build
cd ..


%install
%make_install -C build

# Also include the other headers
cp -a Include/* %{buildroot}%{_includedir}/%{name}/
# ...but not the 3rd party libraries
rm -r %{buildroot}%{_includedir}/%{name}/Libraries

# Backward compatibility links (compatibility with 2.0.x)
ln -s Bindings/C/lib3mf.h \
      Bindings/Cpp/lib3mf_abi.hpp \
      Bindings/CDynamic/lib3mf_dynamic.h \
      Bindings/CppDynamic/lib3mf_dynamic.hpp \
      Bindings/Cpp/lib3mf_implicit.hpp \
      Bindings/NodeJS/lib3mf_nodewrapper.h \
      Bindings/C/lib3mf_types.h \
      Bindings/Cpp/lib3mf_types.hpp \
  %{buildroot}%{_includedir}/%{name}/
ln -s lib3mf.pc %{buildroot}%{_libdir}/pkgconfig/lib3MF.pc


%if %{with tests}
%check
%make_build test -C build
%endif


%ldconfig_scriptlets


%files
%doc README.md
%license LICENSE
%{_libdir}/%{name}.so.2
%{_libdir}/%{name}.so.%{version}.0


%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/lib3mf.pc
%{_libdir}/pkgconfig/lib3MF.pc


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 26 2023 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Don't force C++11 to fix FTBFS with gtest 1.13+
- Convert the License tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 09 2022 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 17 2021 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-1
- Update to 2.0.1 to fix CVE-2021-21772
- Resolves: rhbz#1939895
- Resolves: rhbz#1939896
- Resolves: rhbz#1939897

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Include lib3MF.pc file
- Include all headers

* Mon Mar 30 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Minor packaging adjustments (#1818945)

* Fri Feb 14 2020 Danny Hindson <danny.hindson@stfc.ac.uk> - 2.0.0-1
- Initial Fedora/EPEL RPM
