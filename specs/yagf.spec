%global __cmake_in_source_build 1

Name:           yagf
Version:        0.9.5
Release:        24%{?dist}
Summary:        Graphical front-end for cuneiform

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://sourceforge.net/projects/yagf-ocr/
Source:         https://downloads.sourceforge.net/yagf-ocr/files/%{name}-%{version}.tar.gz

# fix .desktop file
Patch1:         yagf-0.9.1-Source-desktop.patch
Patch2:         yagf-0.9.5-nothreads.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  aspell-devel
BuildRequires:  qt4-devel
BuildRequires:  dos2unix
Requires:       tesseract

%description
YAGF is a graphical interface for the cuneiform text
recognition program. With YAGF you can scan images via
XSane, perform images preprocessing and recognize
texts using cuneiform from a single command center.
YAGF also makes it easy to scan and recognize
several images sequentially.

%prep
%setup -q
%patch -P1 -p1 -b .desktop
%patch -P2 -p1 -b .nothreads

# fix line brake for debug package
dos2unix src/mainform.cpp src/mainform.h

# fix permisions
chmod 644 src/mainform.cpp src/mainform.h src/main.cpp

%build
# CMakeLists.txt constructed in such a way that
# translations can't be installed from %%{_target_platform}
%cmake
%cmake_build

%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/YAGF.desktop

%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING DESCRIPTION README
%{_bindir}/%{name}
%{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/applications/YAGF.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/YAGF.appdata.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.5-23
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 22 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 0.9.5-13
- Requres: cuneiform -> Requers: tesseract

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.5-7
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> 0.9.5-4
- Possible fix for rhbz #1429052.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 01 2015 Dmitrij S. Kryzhevich <krege@land.ru> 0.9.5-1
- Update to new 0.9.5.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.4.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Aug 28 2014 Dmitrij S. Kryzhevich <krege@land.ru> 0.9.4.2-2
- Fix YAGF.appdata installation.

* Thu Aug 28 2014 Dmitrij S. Kryzhevich <krege@land.ru> 0.9.4.2-1
- Update to new 0.9.4.2 version.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Dmitrij S. Kryzhevich <krege@land.ru> 0.9.3.2-1
- Update to 0.9.3.2.

* Wed Apr 02 2014 Dmitrij S. Kryzhevich <krege@land.ru> 0.9.3.1-1
- Update to 0.9.3.1.

* Sat Feb 22 2014 Dmitrij S. Kryzhevich <krege@land.ru> 0.9.3-1
- Update to 0.9.3.
- Fix prev. bogus dates (Thu -> Tue).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Dmitrij S. Kryzhevich <krege@land.ru> 0.9.2-1
- Update to 0.9.2.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Dmitrij S. Kryzhevich <krege@land.ru> 0.9.1-3
- Patch modify.

* Tue Apr 24 2012 Dmitrij S. Kryzhevich <krege@land.ru> 0.9.1-2
- Fix setup tag.

* Tue Apr 24 2012 Dmitrij S. Kryzhevich <krege@land.ru> 0.9.1-1
- Update to 0.9.1.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Dmitrij S. Kryzhevich <krege@land.ru> 0.8.9-1
- Update to 0.8.9.

* Mon Sep 05 2011 Dmitrij S. Kryzhevich <krege@land.ru> 0.8.7-1
- Update to 0.8.7.
- Permissions for files including into debug package are OK now.

* Mon Aug 15 2011 Dmitrij S. Kryzhevich <krege@land.ru> 0.8.6-6
- Update patch for desktop file.
- Some spelling and readability.

* Wed Jul 13 2011 Dmitrij S. Kryzhevich <krege@land.ru> 0.8.6-5
- Own /usr/share/yagf/translations.

* Tue Jul 12 2011 Dmitrij S. Kryzhevich <krege@land.ru> 0.8.6-4
- find_lang magic.
- spec clean up.

* Tue Jul 12 2011 Dmitrij S. Kryzhevich <krege@land.ru> 0.8.6-3
- Move previouse fix to %%prep section.

* Fri Jul 08 2011 Dmitrij S. Kryzhevich <krege@land.ru> 0.8.6-2
- Fix permesions for debug package.

* Tue Apr 05 2011 Dmitrij S. Kryzhevich <krege@land.ru> 0.8.6-1
- First try.
