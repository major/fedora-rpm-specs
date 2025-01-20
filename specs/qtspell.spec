Name:           qtspell
Version:        1.0.1
Release:        14%{?dist}
Summary:        Spell checking for Qt text widgets

License:        GPL-3.0-or-later
URL:            https://github.com/manisandro/qtspell
Source0:        https://github.com/manisandro/qtspell/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  enchant2-devel
BuildRequires:  doxygen

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-enchant2
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-qt5-qttools
BuildRequires: mingw32-qt5-qttools-tools
BuildRequires: mingw32-qt6-qtbase
BuildRequires: mingw32-qt6-qttools

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-enchant2
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-qt5-qttools
BuildRequires: mingw64-qt5-qttools-tools
BuildRequires: mingw64-qt6-qtbase
BuildRequires: mingw64-qt6-qttools

Requires:      iso-codes

%description
QtSpell adds spell-checking functionality to Qt's text widgets, using the
enchant spell-checking library.


%package        qt5
Summary:        Spell checking for Qt5 text widgets

%description    qt5
QtSpell adds spell-checking functionality to Qt5's text widgets, using the
enchant spell-checking library.


%package        qt5-devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}

%description    qt5-devel
The %{name}-qt5-devel package contains libraries and header files for
developing applications that use %{name}-qt5.


%package        qt5-translations
Summary:        Translations for %{name}-qt5
BuildArch:      noarch
Requires:       %{name}-qt5 = %{version}-%{release}
Requires:       qt5-qttranslations

%description    qt5-translations
The %{name}-qt5-translations contains translations for %{name}-qt5.


%package        qt6
Summary:        Spell checking for Qt5 text widgets

%description    qt6
QtSpell adds spell-checking functionality to Qt5's text widgets, using the
enchant spell-checking library.


%package        qt6-devel
Summary:        Development files for %{name}-qt6
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}

%description    qt6-devel
The %{name}-qt6-devel package contains libraries and header files for
developing applications that use %{name}-qt6.


%package        qt6-translations
Summary:        Translations for %{name}-qt6
BuildArch:      noarch
Requires:       %{name}-qt6 = %{version}-%{release}
Requires:       qt6-qttranslations

%description    qt6-translations
The %{name}-qt6-translations contains translations for %{name}-qt6.


%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the documentation for developing applications
that use %{name}.


%package -n mingw32-%{name}-qt5
Summary:       MinGW Windows %{name}-Qt5 library
Requires:      mingw32-qt5-qttranslations
BuildArch:     noarch
Obsoletes:     mingw32-%{name}-qt5-static

%description -n mingw32-%{name}-qt5
MinGW Windows %{name}-Qt5 library.


%package -n mingw64-%{name}-qt5
Summary:       MinGW Windows %{name}-Qt5 library
Requires:      mingw64-qt5-qttranslations
BuildArch:     noarch
Obsoletes:     mingw64-%{name}-qt5-static

%description -n mingw64-%{name}-qt5
MinGW Windows %{name}-Qt5 library.


%package -n mingw32-%{name}-qt6
Summary:       MinGW Windows %{name}-Qt6 library
Requires:      mingw32-qt6-qttranslations
BuildArch:     noarch

%description -n mingw32-%{name}-qt6
MinGW Windows %{name}-Qt6 library.


%package -n mingw64-%{name}-qt6
Summary:       MinGW Windows %{name}-Qt6 library
Requires:      mingw64-qt6-qttranslations
BuildArch:     noarch

%description -n mingw64-%{name}-qt6
MinGW Windows %{name}-Qt6 library.


%{?mingw_debug_package}


%prep
%autosetup


%build
%define _vpath_builddir %{_target_platform}-qt5
%cmake -DQT_VER=5
%cmake_build

%define _vpath_builddir %{_target_platform}-qt6
%cmake -DQT_VER=6
%cmake_build

make doc -C %{__cmake_builddir}

export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%mingw_cmake -DQT_VER=5
%mingw_make_build

MINGW_BUILDDIR_SUFFIX=qt6 %mingw_cmake -DQT_VER=6
MINGW_BUILDDIR_SUFFIX=qt6 %mingw_make_build


%install
%define _vpath_builddir %{_target_platform}-qt5
%cmake_install

%define _vpath_builddir %{_target_platform}-qt6
%cmake_install

%mingw_make_install
MINGW_BUILDDIR_SUFFIX=qt6 %mingw_make_install


%mingw_debug_install_post


%files qt5
%license COPYING
%{_libdir}/libqtspell-qt5.so.*

%files qt5-devel
%{_includedir}/QtSpell-qt5/
%{_libdir}/libqtspell-qt5.so
%{_libdir}/pkgconfig/QtSpell-qt5.pc

%files qt5-translations
%{_qt5_translationdir}/QtSpell_*.qm

%files qt6
%license COPYING
%{_libdir}/libqtspell-qt6.so.*

%files qt6-devel
%{_includedir}/QtSpell-qt6/
%{_libdir}/libqtspell-qt6.so
%{_libdir}/pkgconfig/QtSpell-qt6.pc

%files qt6-translations
%{_qt6_translationdir}/QtSpell_*.qm

%files -n mingw32-%{name}-qt5
%license COPYING
%{mingw32_bindir}/libqtspell-qt5-1.dll
%{mingw32_libdir}/libqtspell-qt5.dll.a
%{mingw32_libdir}/pkgconfig/QtSpell-qt5.pc
%{mingw32_includedir}/QtSpell-qt5/
%{mingw32_datadir}/qt5/translations/QtSpell_*.qm

%files -n mingw64-%{name}-qt5
%license COPYING
%{mingw64_bindir}/libqtspell-qt5-1.dll
%{mingw64_libdir}/libqtspell-qt5.dll.a
%{mingw64_libdir}/pkgconfig/QtSpell-qt5.pc
%{mingw64_includedir}/QtSpell-qt5/
%{mingw64_datadir}/qt5/translations/QtSpell_*.qm

%files -n mingw32-%{name}-qt6
%license COPYING
%{mingw32_bindir}/libqtspell-qt6-1.dll
%{mingw32_libdir}/libqtspell-qt6.dll.a
%{mingw32_libdir}/pkgconfig/QtSpell-qt6.pc
%{mingw32_includedir}/QtSpell-qt6/
%{mingw32_datadir}/qt6/translations/QtSpell_*.qm

%files -n mingw64-%{name}-qt6
%license COPYING
%{mingw64_bindir}/libqtspell-qt6-1.dll
%{mingw64_libdir}/libqtspell-qt6.dll.a
%{mingw64_libdir}/pkgconfig/QtSpell-qt6.pc
%{mingw64_includedir}/QtSpell-qt6/
%{mingw64_datadir}/qt6/translations/QtSpell_*.qm

%files doc
%license COPYING
%doc %{__cmake_builddir}/doc/html


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Sandro Mani <manisandro@gmail.com> - 1.0.1-13
- Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 01 2024 Sandro Mani <manisandro@gmail.com> - 1.0.1-11
- Rebuild (enchant2)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 31 2022 Sandro Mani <manisandro@gmail.com> - 1.0.1-5
- Make mingw subpackages noarch

* Sat Feb 19 2022 Sandro Mani <manisandro@gmail.com> - 1.0.1-4
- Add mingw subpackage

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Fri Jan 14 2022 Sandro Mani <manisandro@gmail.com> - 1.0-1
- Update to 1.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 21 2020 Sandro Mani <manisandro@gmail.com> - 0.9.0-1
- Update to 0.9.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Sandro Mani <manisandro@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 0.8.4-3
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Sandro Mani <manisandro@gmail.com> - 0.8.4-1
- Update to 0.8.4

* Fri Dec 15 2017 Sandro Mani <manisandro@gmail.com> - 0.8.3-1
- Update to 0.8.3

* Mon Aug 07 2017 Sandro Mani <manisandro@gmail.com> - 0.8.2-5
- Rebuild for ppc64le binutils bug

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 08 2016 Sandro Mani <manisandro@gmail.com> - 0.8.2-1
- QtSpell 0.8.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Sandro Mani <manisandro@gmail.com> - 0.8.1-1
- QtSpell 0.8.1

* Fri Oct 16 2015 Sandro Mani <manisandro@gmail.com> - 0.8.0-1
- QtSpell 0.8.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Sandro Mani <manisandro@gmail.com> - 0.7.4-1
- QtSpell 0.7.4

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 30 2015 Sandro Mani <manisandro@gmail.com> - 0.7.2-1
- QtSpell 0.7.2

* Mon Feb 09 2015 Sandro Mani <manisandro@gmail.com> - 0.7.1-1
- QtSpell 0.7.1

* Thu Feb 05 2015 Sandro Mani <manisandro@gmail.com> - 0.7.0-1
- QtSpell 0.7.0

* Sat Dec 27 2014 Sandro Mani <manisandro@gmail.com> - 0.6.0-1
- QtSpell 0.6.0

* Fri Dec 12 2014 Sandro Mani <manisandro@gmail.com> - 0.5.0-2
- Use %%license
- Add -Wl,--as-needed

* Fri Dec 12 2014 Sandro Mani <manisandro@gmail.com> - 0.5.0-1
- QtSpell 0.5.0
