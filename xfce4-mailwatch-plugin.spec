# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=187569
%global minorversion 1.3
%global xfceversion 4.16

Name:           xfce4-mailwatch-plugin
Version:        1.3.0
Release:        6%{?dist}
Summary:        Mail Watcher plugin for the Xfce panel

License:        GPLv2
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-weather-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  exo-devel >= 0.7.2
BuildRequires:  gnutls-devel >= 1.2.0
BuildRequires:  libgcrypt-devel >= 1.2.0
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       xfce4-panel >= %{xfceversion}


%description
Mailwatch is a plugin for the Xfce 4 panel. It is intended to replace the 
current (4.0, 4.2) mail checker plugin in Xfce 4.4. It supports IMAP and POP, 
local mailboxes in Mbox, Maildir and MH-Maildir format as well as Gmail.

%prep
%autosetup
# Fix icon in 'Add new panel item' dialog
sed -i 's|Icon=xfce-mail|Icon=mail-unread|g' panel-plugin/mailwatch.desktop.in


%build
%configure
%make_build


%install
%make_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Kevin Fenzi <kevin@scrye.com> - 1.3.0-1
- Update to 1.3.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.0-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.0-13
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.2.0-6
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Tomáš Mráz <tmraz@redhat.com> - 1.2.0-3
- Rebuild for new libgcrypt

* Fri Oct 25 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.2-0-2
- Fix the icon in the panel's "Add new Item" dialog

* Fri Oct 25 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0
- Remove upstreamed/obsolete patches

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar  7 2013 Tomáš Mráz <tmraz@redhat.com> - 1.1.0-15
- Make it build with new GnuTLS

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.1.0-13
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.1.0-12
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.1.0-10
- Rebuild for new libpng

* Sat Jun 04 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-9
- Make mail check interval configurable (#710752)

* Fri Apr 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-8
- Fix icon in 'Add new panel item' dialog (#694904)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Adam Williamson <awilliam@redhat.com> - 1.1.0-6
- fix a couple of underlinking issues (underlink.patch)

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-5
- Add patch to fix DSO linking (#564814)
- Update icon-cache scriptlets

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-2
- Rebuild for Xfce 4.6 (Beta 3)

* Wed Oct 01 2008 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 fixes crash due to obscure GTK hash error (#463412)

* Mon Jul 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.1-10
- fix conditional comparison

* Fri Jun 06 2008 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-9
- BuildRequire libXt-devel for all releases (#449496)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.1-8
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-7
- Rebuild for BuildID feature
- Update license tag

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-6
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-5
- Rebuild for Xfce 4.4.
- Update gtk-icon-cache scriptlets.

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-4
- Bump release for devel checkin.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-3
- Recompile against XFCE 4.3.90.2.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-2
- Mass rebuild for Fedora Core 6.

* Sat Jun 17 2006 Christoph Wickert <fedora wickert at arcor de> - 1.0.1-1
- Update to 1.0.1.

* Mon Apr 10 2006 Christoph Wickert <fedora wickert at arcor de> - 1.0.0-2
- Fix description.
- Fix files section.
- Require xfce4-panel.

* Sat Feb 18 2006 Christoph Wickert <fedora wickert at arcor de> - 1.0.0-1
- Initial Fedora Extras release.
