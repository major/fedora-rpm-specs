Name:           gifticlib
Version:        1.0.9
Release:        17%{?dist}
Summary:        IO library for the GIFTI cortical surface data format
License:        Public Domain
URL:            http://www.nitrc.org/projects/gifti/
Source0:        http://www.nitrc.org/frs/download.php/2262/%{name}-%{version}.tgz
# Taken from Debian
Source1:        http://anonscm.debian.org/cgit/pkg-exppsy/gifticlib.git/plain/debian/gifti_test.1
Provides:       gifti = %{version}-%{release}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  expat-devel
BuildRequires:  nifticlib-devel

%description
GIFTI is an XML-based file format for cortical surface data. This reference
IO implementation is developed by the Neuroimaging Informatics Technology
Initiative (NIfTI).
This package also provides the tools that are shipped with the GIFTI library
(gifti_tool and gifti_test).

%package        devel
Summary:        Development files for %{name}
Provides:       gifti-devel = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup
# Remove using ITK-bundled EXPAT and ZLIB (we're not shipping them
# and use proper libsuffix
sed -i \
  -e '/FIND_PACKAGE(ITK)/d' \
  -e '/SET(GIFTI_INSTALL_LIB_DIR/s/lib/%{_lib}/' \
  CMakeLists.txt
rm -rf build/

%build
%cmake
%cmake_build

%install
%cmake_install

# Remove static libs
rm -f %{buildroot}%{_libdir}/*.a
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/


%files
%license LICENSE.gifti
%{_bindir}/gifti_*
%{_libdir}/libgifti*.so.*
%{_mandir}/man1/gifti_*.1.*

%files devel
%doc README.gifti
%{_includedir}/gifti/
%{_libdir}/libgifti*.so

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.9-13
- Update cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.9-1
- Initial package
