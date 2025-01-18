%global _hardened_build 1
Name:           diffpdf
Version:        2.1.3
Release:        33%{?dist}
Summary:        PDF files comparator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.qtrac.eu/diffpdf.html
Source0:        http://www.qtrac.eu/%{name}-%{version}.tar.gz
Source1:        %{name}.1
Source3:        %{name}.desktop

Patch0:         qt5.patch

BuildRequires:  poppler-qt5-devel, desktop-file-utils, ImageMagick
BuildRequires:  qt5-linguist
# /usr/include/poppler/cpp/poppler-version.h
BuildRequires:  poppler-cpp-devel
BuildRequires:  make
Requires:       hicolor-icon-theme

%description
DiffPDF is used to compare two PDF files. By default the comparison is
of the text on each pair of pages, but comparing the appearance of pages
is also supported (for example, if a diagram is changed or a paragraph
reformatted). It is also possible to compare particular pages or page
ranges.

%prep
%setup -q
%patch -P0 -p1 -b .qt5


%build
lrelease-qt5 diffpdf.pro
%{qmake_qt5}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 diffpdf $RPM_BUILD_ROOT%{_bindir}

for f in 32 16; do
   mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/"$f"x$f/apps
   convert images/icon.png -size "$f"x$f diffpdf-$f.png
   install -p diffpdf-$f.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/"$f"x$f/apps/diffpdf.png
done

desktop-file-install                                    \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications         \
  %{SOURCE3}

%{__install} -m 644 %{SOURCE1} -D $RPM_BUILD_ROOT%{_mandir}/man1/diffpdf.1



%files
%doc CHANGES gpl-2.0.txt help_cz.html help_de.html help_fr.html help.html README
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/??x??/apps/*.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/diffpdf.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.3-32
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Marek Kasik <mkasik@redhat.com> - 2.1.3-22
- Add BuildRequires of qt5-linguist

* Tue Jan 05 2021 Marek Kasik <mkasik@redhat.com> - 2.1.3-21
- Migrate diffpdf to Qt5

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 2.1.3-18
- Rebuild for poppler-0.84.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.3-13
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Jonathan Wakely <jwakely@redhat.com> - 2.1.3-9
- Add man page.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.1.3-7
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.3-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 20 2013 Till Maas <opensource@till.name> - 2.1.3-2
- Harden build

* Sun Oct 20 2013 Till Maas <opensource@till.name> - 2.1.3-1
- Update to new release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Till Maas <opensource@till.name> - 2.1.2-1
- Update to new release

* Tue Oct 02 2012 Till Maas <opensource@till.name> - 2.1.1-1
- Update to new release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 1.2.2-4
- Rebuild (poppler-0.20.0)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 1.2.2-2
- Rebuild (poppler-0.17.3)

* Mon Jul 25 2011 Till Maas <opensource@till.name> - 1.2.2-1
- Update to new release

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 1.0.0-3
- Rebuild (poppler-0.17.0)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 19 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0.0-1
- diffpdf 1.0.0 new/improved algorithm

* Sat May 01 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.6.0-1
- diffpdf 0.6.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 14 2008 Rafał Psota <rafalzaq@gmail.com> - 0.3.8-4
- forgot about ImageMagick
* Fri Dec 12 2008 Rafał Psota <rafalzaq@gmail.com> - 0.3.8-3
- drop vendor for desktop file
* Thu Nov 27 2008 Rafał Psota <rafalzaq@gmail.com> - 0.3.8-2
- forgot about desktop file
* Tue Nov 11 2008 Rafał Psota <rafalzaq@gmail.com> - 0.3.8-1
- Initial release
