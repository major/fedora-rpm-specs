
%undefine __cmake_in_source_build

Name:           prison
Summary:        A Qt-based barcode abstraction library
Version:        1.1.1
Release:        27%{?dist}

License:        MIT
URL:            https://projects.kde.org/projects/kdesupport/prison
Source0:        http://download.kde.org/stable/prison/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches
# post 1.1.1 commits from master/ branch
Patch1: 0001-Add-automoc-increase-cmake-version.patch
Patch2: 0002-Allow-to-build-with-qt5-and-qt4.patch
Patch3: 0003-Generate-cmake-config-version-file.patch
Patch4: 0004-Fix-option-description.patch
Patch5: 0005-Fix-major-for-qt5.patch
Patch6: 0006-Use-ECM-to-locate-the-correct-install-paths-on-a-Qt5.patch
Patch7: 0007-Use-PRISON_VERSION_MAJOR-for-SOVERSION.patch
Patch8: 0008-increase-ECM.patch
Patch9: 0009-Set-also-QT_QTGUI_LIBARARY-as-that-this-variable-is-.patch
## upstreamable patch
# make -qt5 build fully parallel-installable
# needs work to be upstreamable, see 'sed' down in %%install section
Patch10: 0010-parallel-installable-prison-qt5.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(libdmtx)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(QtGui)
%if 0%{?qt5}
BuildRequires:  pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets) pkgconfig(Qt5Test)
%endif

%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%package qt5
Summary: A Qt5-based barcode abstraction library
%description qt5
Prison is a Qt5-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package qt5-devel
Summary: Development files for %{name}-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}



%prep
%autosetup -p1


%build
%cmake

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libprison.so.0*

%files devel
%{_includedir}/prison/
%{_libdir}/libprison.so
%{_libdir}/cmake/Prison/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.1.1-17
- FTBFS, use new cmake macros, drop qt5 support (in kf5-prison these days)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 1.1.1-12
- Rebuilt (libqrencode.so.4)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-5
- drop qt5 support, wait for proper kf5-prison to land instead

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 20 2015 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-3
- use %%cmake_kf5 (to get some paths right without patching)

* Tue Oct 20 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.1.1-2
- pull in upstream fixes
- provide parallel-installable -qt5 -qt5-devel subpkgs
- pkgconfig-style deps

* Tue Oct 20 2015 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-1
- prison-1.1.1, .spec polish

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.0-3
- %%files: track soname
- minor cosmetics

* Fri May 20 2011 Jaroslav Reznik <jreznik@redhat.com> - 1.0-2
- prison is qt only library

* Fri May 20 2011 Jaroslav Reznik <jreznik@redhat.com> - 1.0-1
- initial package
