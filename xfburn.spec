# Review: https://bugzilla.redhat.com/show_bug.cgi?id=473679

%global majorversion 0.6

Name:           xfburn
Version:        0.6.2
Release:        7%{?dist}
Summary:        Simple CD burning tool for Xfce

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/applications/%{name}
#VCS: git:git://git.xfce.org/apps/xfburn
Source0:        http://archive.xfce.org/src/apps/%{name}/%{majorversion}/%{name}-%{version}.tar.bz2

# https://bugzilla.redhat.com/show_bug.cgi?id=1284977
Patch1:         xfburn-0.5.4-tmpdir.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libxfce4ui-devel >= 4.12.0
BuildRequires:  exo-devel
BuildRequires:  libburn-devel >= 0.4.2
BuildRequires:  libisofs-devel >= 0.6.2
BuildRequires:  dbus-glib-devel >= 0.34 
BuildRequires:  gstreamer1-devel >= 0.10.2
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk2-devel >= 2.10.0
BuildRequires:  desktop-file-utils 
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libgudev1-devel
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

%description
Xfburn is a simple CD/DVD burning tool based on libburnia libraries. It can 
blank CD-RWs, burn and create iso images, as well as burn personal 
compositions of data to either CD or DVD.


%prep
%autosetup -p1

# fix appdata installation location
sed -i 's/\$(datadir)\/appdata/\$(datadir)\/metainfo/' Makefile.in


%build
%configure
%make_build


%install
%make_install INSTALL='install -p'

%find_lang %{name}
desktop-file-install --vendor ""                            \
    --dir %{buildroot}%{_datadir}/applications              \
    --delete-original                                       \
    --add-category=Utility                                  \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.xfce.%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/Thunar/sendto/*.desktop
%{_datadir}/icons/hicolor/*/stock/media/stock_%{name}*.png
%{_datadir}/icons/hicolor/scalable/stock/media/stock_%{name}*.svg
%{_datadir}/metainfo/org.xfce.%{name}.appdata.xml
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.ui
%{_mandir}/man1/%{name}.*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6.2-3
- Drop thunar-vfs from BR (not required for a while)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 07 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Kevin Fenzi <kevin@scrye.com> - 0.6.1-1
- Update to 0.6.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5
- Fix appdata installation location
- Drop upstreamed patch

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 24 2016 Richard Shaw <hobbes1069@gmail.com> - 0.5.4-5
- Change temp directory from /tmp to /var/tmp as images can get quite big.
- Modernize spec and bring up to current guidelines.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 Kevin Fenzi <kevin@scrye.com> 0.5.4-3
- Fix icon. Fixes bug #1265310

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Kevin Fenzi <kevin@scrye.com> 0.5.4-1
- Update to 0.5.4 and switch to gstreamer1

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.5.2-5
- Rebuild for Xfce 4.10

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.5.2-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 09 2014 Kevin Fenzi <kevin@scrye.com> 0.5.2-1
- Update to 0.5.2

* Thu Feb 20 2014 Kevin Fenzi <kevin@scrye.com> 0.5.0-1
- Update to 0.5.0

* Tue Nov 12 2013 Frantisek Kluknavsky <fkluknav@redhat.com> - 0.4.3-13
- support for aarch64, patch from https://bugzilla.redhat.com/show_bug.cgi?id=926769
- modified bogus dates in changelog

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 28 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.3-10
- Fix crash when creating directory (#639804, #676086 and #851900)
- Fix crash when adding lots of files (#669971)
- Make sure desktop file validates

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 01 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.3-8
- Fix build with latest glib
- Add VCS key and review #

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.3-6
- Rebuild for new libpng

* Tue Apr 26 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.3-5
- No longer BuildRequire obsolete hal (#699692)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 04 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.3-3
- Switch from Thunar-devel to thunar-vfs-devel

* Thu Apr 22 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.3-2
- Rebuild for libburn 0.8.0

* Sun Feb 14 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Fri Jan 29 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-3
- Properly unmount drive before burning (#525514)

* Thu Oct 29 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-2
- Fix infinite loop in blank disk dialog (#525515)
- Don't crash on burning ISO image (#525518)

* Fri Jul 24 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Wed Feb 25 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1
- Include new manpage

* Mon Jan 26 2009 Denis Leroy <denis@poolshark.org> - 0.4.0-1
- Update to upstream 0.4.0

* Tue Nov 04 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.91-2
- Don't enable debug
- Require hicolor-icon-theme

* Tue Nov 04 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.91-1
- Update to 0.3.91

* Wed Jul 16 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Fri Jul 11 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Wed Jun 11 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0 stable

* Mon Jan 07 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-0.1.20080107svn26552
- Update to 0.3.0svn-26552.
. Switch to libburn and drop requirements for genisoimage, cdrdao and wodim

* Sun Feb 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.1-0.1.20070225svn25032
- Initial package.
