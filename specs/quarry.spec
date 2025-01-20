Name:           quarry
Version:        0.2.0
Release:        40%{?dist}
Summary:        A multi-purpose board game GUI

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://home.gna.org/quarry/
Source0:        http://download.gna.org/quarry/quarry-%{version}.tar.gz
Patch0:         quarry-format-security.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  librsvg2-devel
BuildRequires:  gtk2-devel
BuildRequires:  scrollkeeper

%description
Quarry is a multi-purpose GUI for several board games, at present Go, Amazons
and Reversi. It allows users to play against computer players (third-party
programs, e.g. GNU Go or GRhino) or other humans, view and edit game records.
Future versions will also support Internet game servers and provide certain
features for developers of board game-playing engines for enhancing their
programs.

%prep
%setup -q
%patch -P0 -p1


%build
export CFLAGS="%{optflags} -std=gnu89"
%configure --disable-scrollkeeper-update
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# desktop file
desktop-file-install \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    --remove-key Version \
    --delete-original \
    $RPM_BUILD_ROOT%{_datadir}/applications/quarry.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING-DOC NEWS README THANKS TODO
%{_bindir}/quarry
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/quarry.xml
%{_datadir}/pixmaps/quarry.png
%{_datadir}/omf/quarry/
%{_datadir}/quarry/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.0-39
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-29
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 25 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.2.0-18
- Restore accidentally dropped optimization flags

* Sat Jul 25 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.2.0-17
- Fix FTBFS with GCC 5+

* Fri Oct 03 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0.2.0-16
- fix sprintf call so -format-security works

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.2.0-15
- add/update desktop/mime/scrollkeeper scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.2.0-11
- Drop desktop vendor tag.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.0-8
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Jon Ciesla <limb@jcomserv.net> - 0.2.0-6
- Add gtk2-devel BR to fix FTBFS BZ 631185.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.0-3
- Autorebuild for GCC 4.3

* Mon Sep 24 2007 Michel Salim <michel.sylvan@gmail.com> - 0.2.0-2
- License field update
- Remove invalid version key from desktop file

* Sun Nov 19 2006 Michel Salim <michel.salim@gmail.com> - 0.2.0-1
- Update to 0.2.0, first stable version

* Tue Oct 31 2006 Michel Salim <michel.salim@gmail.com> - 0.1.20-1
- Update to 0.1.20

* Mon Oct  9 2006 Michel Salim <michel.salim@gmail.com> - 0.1.19-2
- Incorporated upstream patch to fix gtp-client string handling

* Sun Oct  8 2006 Michel Salim <michel.salim@gmail.com> - 0.1.19-1
- Update to 0.1.19

* Thu Mar  2 2006 Michel Salim <michel.salim@gmail.com> - 0.1.16-2
- Rebuild for Fedora Extras 5

* Sun Nov 13 2005 Michel Salim <michel.salim[AT]gmail.com> - 0.1.16-1
- New upstream version

* Sun Sep  4 2005 Michel Salim <michel.salim[AT]gmail.com> - 0.1.15-5
- removed references to trademarked names
- packaged modified tarball to prevent trademark infringement

* Fri Aug 19 2005 Michel Salim <michel.salim[AT]gmail.com> - 0.1.15-4
- actually use find_lang (Dawid)
- desktop file fixes (Dawid)
- fixed scrollkeeper patch
- add missing BuildRequires on desktop-file-utils

* Thu Aug 18 2005 Michel Salim <michel.salim[AT]gmail.com> - 0.1.15-3
- added ******* trademark notice (Jef Spaleta)

* Thu Aug 18 2005 Michel Salim <michel.salim[AT]gmail.com> - 0.1.15-2
- added scrollkeeper updates (Dawid Gajownik)
- file listing fixes (Dawid Gajownik)

* Tue Aug 16 2005 Michel Salim <michel.salim[AT]gmail.com> - 0.1.15-1
- initial package
