Summary:       Serial terminal for the gnome desktop
Name:          moserial
Version:       3.0.21
Release:       12%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           https://wiki.gnome.org/moserial/
Source0:       http://ftp.gnome.org/pub/GNOME/sources/moserial/3.0/moserial-%{version}.tar.xz
BuildRequires: GConf2-devel
BuildRequires: desktop-file-utils
BuildRequires: gnome-doc-utils
BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: make
BuildRequires: perl(XML::Parser)
BuildRequires: rarian-compat
BuildRequires: sed
BuildRequires: vala
Requires:      yelp
Requires:      lrzsz
Requires:      hicolor-icon-theme
%description
Moserial is a clean, friendly gtk-based serial terminal for the gnome
desktop. It is written in Vala for extra goodness.

%prep
%autosetup
find -name *.c -delete
find -name moserial.vala.stamp -delete
chmod 0644 AUTHORS ChangeLog* NEWS COPYING README

%build
%configure
%make_build

%install
%make_install
desktop-file-install --delete-original         \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/moserial.desktop

for book in %{buildroot}%{_datadir}/help/[a-z]*/moserial/index.docbook ; do
    sed -i -e 's|fileref="figures|fileref="../../C/moserial/figures|' $book
done
for dir in %{buildroot}%{_datadir}/help/[a-z]*/moserial/figures ; do
    rm -rf $dir
done

%find_lang moserial

%files -f moserial.lang
%license COPYING
%doc AUTHORS ChangeLog ChangeLog.pre-git NEWS README
%{_bindir}/moserial
%{_datadir}/applications/moserial.desktop
%{_datadir}/metainfo/moserial.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/moserial.svg
%{_datadir}/help/*/moserial
%{_mandir}/man1/moserial.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.21-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 20 2024 Terje Rosten <terje.rosten@ntnu.no> - 3.0.21-9
- Avoid symlinks, patch docbook files instead

* Mon Feb 19 2024 Terje Rosten <terje.rosten@ntnu.no> - 3.0.21-8
- Fix FTBFS

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Terje Rosten <terje.rosten@ntnu.no> - 3.0.21-1
- 3.0.21

* Sat Sep 04 2021 Terje Rosten <terje.rosten@ntnu.no> - 3.0.20-1
- 3.0.20

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 20 2021 Terje Rosten <terje.rosten@ntnu.no> - 3.0.16-1
- 3.0.16

* Sun Feb 07 2021 Terje Rosten <terje.rosten@ntnu.no> - 3.0.15-1
- 3.0.15

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Terje Rosten <terje.rosten@ntnu.no> - 3.0.13-1
- 3.0.13

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Terje Rosten <terje.rosten@ntnu.no> - 3.0.12-9
- Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Terje Rosten <terje.rosten@ntnu.no> - 3.0.12-3
- Remove group

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.12-2
- Remove obsolete scriptlets

* Sun Jan 14 2018 Terje Rosten <terje.rosten@ntnu.no> - 3.0.12-1
- 3.0.12

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Terje Rosten <terje.rosten@ntnu.no> - 3.0.11-1
- 3.0.11

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 02 2016 Terje Rosten <terje.rosten@ntnu.no> - 3.0.10-3
- New website

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Terje Rosten <terje.rosten@ntnu.no> - 3.0.10-1
- 3.0.10

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 23 2014 Richard Hughes <richard@hughsie.com> - 3.0.9-1
- New upstream release.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 21 2013 Terje Rosten <terje.rosten@ntnu.no> - 3.0.8-1
- 3.0.8

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Terje Rosten <terje.rosten@ntnu.no> - 3.0.7-1
- 3.0.7

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 31 2012 Terje Rosten <terje.rosten@ntnu.no> - 3.0.6-1
- 3.0.6
- Add lrzsz to req, fixing bz #804147

* Wed Feb 01 2012 Terje Rosten <terje.rosten@ntnu.no> - 3.0.5-1
- 3.0.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 11 2011 Terje Rosten <terje.rosten@ntnu.no> - 3.0.1-2
- Fix buildreq

* Wed Sep 07 2011 Terje Rosten <terje.rosten@ntnu.no> - 3.0.1-1
- 3.0.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Terje Rosten <terje.rosten@ntnu.no> - 2.30.0-2
- Fix buildreq (#660805)

* Thu Jun 17 2010 Terje Rosten <terje.rosten@ntnu.no> - 2.30.0-1
- 2.30.0

* Sat Dec 05 2009 Terje Rosten <terje.rosten@ntnu.no> - 2.28.0-2
- rarian-compat needed to build

* Sat Dec 05 2009 Terje Rosten <terje.rosten@ntnu.no> - 2.28.0-1
- 2.28.0
- Fix file perms

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.27.3-2
- Use bzipped upstream tarball.

* Fri Jul 31 2009 Terje Rosten <terje.rosten@ntnu.no> - 2.27.3-1
- 2.27.3

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 30 2009 Terje Rosten <terje.rosten@ntnu.no> - 2.26.1-2
- add req. on yelp and hicolor-icon-theme
- fix dir ownership
- fix license
- preserve timestamps
- detect README changes

* Fri May 29 2009 Terje Rosten <terje.rosten@ntnu.no> - 2.26.1-1
- initial package
