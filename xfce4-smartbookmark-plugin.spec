# Review at https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=219986

%global _hardened_build 1
%global minor_version 0.5
%global xfceversion 4.16

Name:           xfce4-smartbookmark-plugin
Version:        0.5.2
Release:        5%{?dist}
Summary:        Smart bookmarks for the Xfce panel

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2
# vendor specific patches
Patch10:        %{name}-%{version}-redhat.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       xfce4-panel >= %{xfceversion}
Requires:       webclient

%description
A plugin which allows you to do a search directly on Internet on sites like 
Google or Red Hat Bugzilla. It allows you to send requests directly to your 
browser and perform custom searches.

%prep
%autosetup -p1


%build
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
chmod 755 %{buildroot}/%{_libdir}/xfce4/panel/plugins/*.so
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.0-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.5.0-6
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.5.0-1
- Update to 0.5.0
- [gtk3] Bump dependencies to check for libxfce4ui-2/libxfce4panel-2.0
- Spec clean-up

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Kevin Fenzi <kevin@scrye.com> 0.4.6-2
- Fix permissions on library so we get debuginfo. Fixes bug #1204275

* Tue Mar 10 2015 Kevin Fenzi <kevin@scrye.com> 0.4.6-1
- Update to 0.4.6

* Tue Mar 10 2015 Kevin Fenzi <kevin@scrye.com> 0.4.5-2
- Fix BuildRequires

* Tue Mar 10 2015 Kevin Fenzi <kevin@scrye.com> 0.4.5-1
- Update to 0.4.5

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.4.4-10
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 0.4.4-4
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 0.4.4-3
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4
- Drop upstream patches

* Sun Jun 12 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-13
- Fix location of the desktop file (#711418)
- Update translations form Xfce transifex

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Kevin Fenzi <kevin@tummy.com> - 0.4.2-11
- Add patch to link against libxfcegui4 (#564846)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-9
- Fix path in desktop file (#509294)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-7
- Rebuild for Xfce 4.6 (Beta 3)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.2-6
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-5
- Rebuild for BuildID feature
- Update license tag

* Sat Jun 09 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-4
- Multilib fix for desktop file (#228168).

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-3
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-2
- Rebuild for Xfce 4.4.

* Sat Sep 23 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Initial Fedora Extras version.
