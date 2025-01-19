Name:           gtkterm
Version:        1.3.1
Release:        2%{?dist}
Summary:        Serial port terminal
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://github.com/wvdakker/gtkterm
Source0:        https://github.com/wvdakker/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  intltool
BuildRequires:  meson
Requires:       hicolor-icon-theme

%description
Simple GUI terminal used to communicate with the serial port.
Similar to minicom or hyperterminal.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc COPYING NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 15 2024 Dan Horák <dan[at]danny.cz> - 1.3.1-1
- updated to 1.3.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 16 2023 Florian Weimer <fweimer@redhat.com> - 1.2.1-4
- Port to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 Dan Horák <dan[at]danny.cz> - 1.2.1-1
- updated to 1.2.1 (rhbz#2103808)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Dan Horák <dan[at]danny.cz> - 1.1.1-1
- updated to 1.1.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.9.git7b4076d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.8.git7b4076d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.7.git7b4076d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.6.git7b4076d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.5.git7b4076d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.4.git7b4076d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.3.git7b4076d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.2.git7b4076d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Dan Horák <dan[at]danny.cz> - 1.0-0.1.git7b4076d
- switch to new upstream with Gtk+3 support

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.7-0.11.rc1.git26021e33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.7-0.10.rc1.git26021e33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.7-0.9.rc1.git26021e33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.7-0.8.rc1.git26021e33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.7-0.7.rc1.git26021e33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.7-0.6.rc1.git26021e33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.7-0.5.rc1.git26021e33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 04 2013 Hans de Goede <hdegoede@redhat.com> - 0.99.7-0.4.rc1.git26021e33
- Fix lockfile creation (rhbz#991517)

* Mon Aug 05 2013 Hans de Goede <hdegoede@redhat.com> - 0.99.7-0.3.rc1.git26021e33
- Fix FTBFS (rhbz#992450)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.7-0.2.rc1.git26021e33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May  2 2013 Hans de Goede <hdegoede@redhat.com> - 0.99.7-0.1.rc1.git26021e33
- upgrade to 0.99.7-rc1 + some fixes from git
- run autoreconf for aarch64 support (rhbz#925523)

* Tue Apr 23 2013 Jon Ciesla <limburgher@gmail.com> - 0.99.6-7
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.99.6-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 13 2010 Hans de Goede <hdegoede@redhat.com> 0.99.6-1
- New upstream release 0.99.6
- Drop all our patches (all merged)
- Fixes: Add scrollbar for scrollback (#623485)
- Fixes: Add copy / paste edit menu entries (#623462)
- Fixes: FTBFS (#631235)
- Add some bugfixes from Ubuntu

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.99.5-9
- Autorebuild for GCC 4.3

* Sun Dec 09 2007 Dan Horak <dan[at]danny.cz> 0.99.5-8
- update the scrollback patch
- close port after unsuccesful read of control signals (#414811)

* Wed Nov 21 2007 Dan Horak <dan[at]danny.cz> 0.99.5-7
- fix buffer usage (bz 394891)

* Wed Nov  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.99.5-6
- Add patch adding a scrollback-buffer (configurable through gtktermrc)
  by Dan Horak (bz 369491)

* Tue Aug  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.99.5-5
- Update License tag for new Licensing Guidelines compliance

* Sat Jun 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.99.5-4
- Fix various CR LF handling issues (bug 244182)

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.99.5-3
- FE6 Rebuild

* Thu May 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.99.5-2
- Rebuild for new vte release.

* Fri Mar 31 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.99.5-1
- Taking over as new FE maintainer
- Bump to new upstream 0.99.5

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Nov 28 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.99.4-0.fdr.3
- Add ncurses-devel as BuildRequires for RH9.
- full URL to Sources in .spec file
* Sat Nov 22 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.99.4-0.fdr.2
- add missing BuildRequires.
* Sat Sep 06 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.99.4-0.fdr.1
- Initial RPM release.
