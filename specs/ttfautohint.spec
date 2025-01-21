# RHEL 10 is dropping Qt5
%bcond gui %[%{undefined rhel} || 0%{?rhel} < 10]

Name:           ttfautohint
Version:        1.8.4
Release:        10%{?dist}
Summary:        Automated hinting utility for TrueType fonts
License:        FTL or GPL-2.0-only
URL:            http://www.freetype.org/ttfautohint
Source0:        http://download.savannah.gnu.org/releases/freetype/%{name}-%{version}.tar.gz

BuildRequires:  autoconf automake libtool
BuildRequires:  make
BuildRequires:  gcc gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  pkgconfig
%if %{with gui}
BuildRequires:  qt5-qtbase-devel
%endif
Provides:       bundled(gnulib)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
This is a utility which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

%if %{with gui}
%package        gui
Summary:        GUI for %{name} based on Qt
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    gui
%{name} is a utility which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

This is a GUI of %{name} based on Qt.
%endif

%package        libs
Summary:        Library for %{name}

%description    libs
lib%{name} is a library which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

%package        devel
Summary:        Development files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
lib%{name} is a library which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.


%prep
%autosetup
# drop this hack if --with-doc is enabled
echo %{version} > VERSION
sed -i -e '/dist_man_MANS/d' -e 's/manpages/dist_man_MANS/' frontend/local.mk
autoreconf -fiv

%build
# doc: requires help2man, ImageMagick, inkscape, pandoc, xelatex, xvfb-run
%configure \
  --disable-silent-rules --disable-static --without-doc \
  %{!?with_gui:--without-qt}
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets libs

%files
%doc AUTHORS NEWS README THANKS TODO *.TXT
%doc doc/img doc/ttfautohint.{html,pdf,txt}
%license COPYING
%{_bindir}/ttfautohint
%{_mandir}/man1/ttfautohint.1*

%if %{with gui}
%files gui
%license COPYING
%{_pkgdocdir}/
%{_bindir}/ttfautohintGUI
%{_mandir}/man1/ttfautohintGUI.1*
%endif

%files libs
%license COPYING
%{_libdir}/libttfautohint.so.1*

%files devel
%license COPYING
%{_includedir}/ttfautohint*.h
%{_libdir}/libttfautohint.so
%{_libdir}/pkgconfig/ttfautohint.pc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Parag Nemade <pnemade AT redhat DOT com> - 1.8.4-6
- Migrate to SPDX license expression

* Tue Jun 20 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1.8.4-5
- Disable Qt5 GUI in RHEL 10 builds

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 1.8.4-1
- new version (#1996278)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Yaakov Selkowitz <yselkowi@redhat.com> - 1.8.3-1
- new version (#1698372)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 1.8.2-1
- new version (#1607856)
- Fix stem width offset handling in storage area (#1646687)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 1.8.1-3
- Switch GUI to Qt5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 1.8.1-1
- new version (#1531029)
- add shared library

* Tue Nov 14 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 1.7-1
- new version (#1485670)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 1.6-1
- new version (#1400320)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 31 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.5-1
- new version (#1268839)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Christopher Meng <rpm@cicku.me> - 1.3-1
- Update to 1.3

* Sat Oct 11 2014 Christopher Meng <rpm@cicku.me> - 1.2-1
- Update to 1.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Christopher Meng <rpm@cicku.me> - 1.1-1
- Update to 1.1

* Sat Mar 22 2014 Christopher Meng <rpm@cicku.me> - 1.00-1
- Update to 1.00

* Wed Nov 13 2013 Christopher Meng <rpm@cicku.me> - 0.97-1
- Update to 0.97
- Share docs between main<->sub package.

* Fri Aug 09 2013 Christopher Meng <rpm@cicku.me> - 0.96-1
- Initial Package.
