%global __cmake_in_source_build 1

## build/include liblastfm_fingerprint
%define fingerprint 1

# see http://fedoraproject.org/wiki/Packaging:SourceURL#Github
%global commit 2e8e40d78a331d8e39fe39113bcb7571a7b1d4d6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:    liblastfm
Summary: Libraries to integrate Last.fm services
Version: 1.1.0
Release: 20%{?dist}

License: GPL-2.0-or-later
URL:     https://github.com/drfiemost/liblastfm
Source0: https://github.com/drfiemost/liblastfm/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

# https://github.com/drfiemost/liblastfm/pull/9
Patch0: make_work_with_stricter_compilation_flags.patch

BuildRequires: make
BuildRequires: cmake >= 2.8.6
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Sql)
BuildRequires: pkgconfig(Qt6Xml)
BuildRequires: ruby
%if 0%{?fingerprint}
BuildRequires: fftw3-devel
BuildRequires: pkgconfig(samplerate)
%endif
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)

%description
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software.

%package qt6
Summary: Libraries to integrate Last.fm services

%description qt6
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software.

%package qt6-fingerprint
Summary: Liblastfm fingerprint library
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-fingerprint
%{summary}.

%package qt6-devel
Summary: Development files for %{name}
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%if 0%{?fingerprint}
Requires: %{name}-qt6-fingerprint%{?_isa} = %{version}-%{release}
%endif
%description qt6-devel
%{summary}.

%package qt5
Summary: Qt5 libraries to integrate Last.fm services
%description qt5
%{summary}.

%package qt5-fingerprint
Summary: Liblastfm5 fingerprint library
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-fingerprint
%{summary}.

%package qt5-devel
Summary: Development files for liblastfm-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%if 0%{?fingerprint}
Requires: %{name}-qt5-fingerprint%{?_isa} = %{version}-%{release}
%endif
%description qt5-devel
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{commit}


%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
mkdir %{_target_platform}
pushd %{_target_platform}
%cmake .. \
  -DBUILD_FINGERPRINT:BOOL=%{?fingerprint:ON}%{!?fingerprint:OFF} \
  -DBUILD_WITH_QT5:BOOL=OFF \
  -DCMAKE_BUILD_TYPE:STRING="Release"

%cmake_build
popd

mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%cmake .. \
  -DBUILD_FINGERPRINT:BOOL=%{?fingerprint:ON}%{!?fingerprint:OFF} \
  -DBUILD_WITH_QT5:BOOL=ON \
  -DCMAKE_BUILD_TYPE:STRING="Release"

%cmake_build


%install
pushd %{_target_platform}-qt5
%cmake_install
popd

pushd %{_target_platform}
%cmake_install
popd

%check
## skip UrlBuilderTest, requires net access
export CTEST_OUTPUT_ON_FAILURE=1
pushd %{_target_platform}
%ctest -E UrlBuilderTest
popd
%if 0%{?qt5}
pushd %{_target_platform}-qt5
%ctest -E UrlBuilderTest
popd
%endif


%ldconfig_scriptlets -n liblastfm6-qt6

%files qt6
%doc COPYING
%doc README.md
%{_libdir}/liblastfm6.so.1*

%if 0%{?fingerprint}
%ldconfig_scriptlets fingerprint

%files qt6-fingerprint
%{_libdir}/liblastfm_fingerprint6.so.1*
%endif

%files qt6-devel
%{_includedir}/lastfm6/
%{_libdir}/liblastfm6.so
%{_libdir}/cmake/lastfm6/
%if 0%{?fingerprint}
%{_libdir}/liblastfm_fingerprint6.so
%endif

%ldconfig_scriptlets qt5

%files qt5
%doc COPYING
%doc README.md
%{_libdir}/liblastfm5.so.1*

%if 0%{?fingerprint}
%ldconfig_scriptlets qt5-fingerprint

%files qt5-fingerprint
%{_libdir}/liblastfm_fingerprint5.so.1*

%files qt5-devel
%{_includedir}/lastfm5/
%{_libdir}/liblastfm5.so
%{_libdir}/cmake/lastfm5/
%if 0%{?fingerprint}
%{_libdir}/liblastfm_fingerprint5.so
%endif
%endif


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 16 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.1.0-19
- cmake fixes

* Sun Apr 27 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.0-18
- Change upstream source
- Update to latest commit
- Backport Amarok developer patch
- Build on Qt5 and Qt6
- Remove Qt4 support

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.0-12
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 1.1.0-6
- Force C++14 as this code is not C++17 ready

* Tue Aug 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.1.0-5
- Fix FTBFS.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.1.0-1
- 1.1.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 08 2015 Rex Dieter <rdieter@fedoraproject.org> 1.0.9-4
- enable qt5 support, build in Release mode, %%check: exclude UrlBuilderTest

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.9-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Jan 08 2015 Rex Dieter <rdieter@fedoraproject.org> 1.0.9-2
- drop cmake28/el6 hacks

* Thu Jan 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.0.9-1
- 1.0.9
- start work on qt5 support

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.8-1
- liblastfm-1.0.8 (#1090909)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.7-1
- liblastfm-1.0.7

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 15 2012 Rex Dieter <rdieter@fedoraproject.org> 
- 1.0.3-1
- liblastfm-1.0.3
- include fingerprint support

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-1
- liblastfm-1.0.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-5
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.3.3-2
- Rebuilt for gcc bug 634757

* Sat Sep 25 2010 Rex Dieter <rdieter@fedoraproject.org> 0.3.3-1
- liblastfm-0.3.3
- missing symbols in liblastfm-0.3.2 (#636729)

* Fri Sep 17 2010 Rex Dieter <rdieter@fedoraproject.org> 0.3.2-1
- liblastfm-0.3.2

* Tue Jun 30 2009 Rex Dieter <rdieter@fedoraproject.org> 0.3.0-2
- rpmlint clean(er)
- BR: libsamplerate-devel
- -devel: fix Requires (typo, +%%?_isa)

* Tue Jun 09 2009 Rex Dieter <rdieter@fedoraproject.org> 0.3.0-1
- liblastfm-0.3.0

* Tue May 05 2009 Rex Dieter <rdieter@fedoraproject.org> 0.2.1-1
- liblastfm-0.2.1, first try
