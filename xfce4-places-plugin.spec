# Review: https://bugzilla.redhat.com/show_bug.cgi?id=238349

%global _hardened_build 1
%global minorversion 1.8
%global xfceversion 4.14

Name:           xfce4-places-plugin
Version:        1.8.2
Release:        1%{?dist}
Summary:        Places menu for the Xfce panel

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-places-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  exo-devel >= 0.5.0
BuildRequires:  libnotify-devel >= 0.4.0
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       xfce4-panel >= %{xfceversion}

%description
A menu with quick access to folders, documents, and removable media. The 
Places plugin brings much of the functionality of GNOME’s Places menu to 
Xfce. It puts a simple button on the panel. Clicking on this button opens up 
a menu with 4 sections:
1) System-defined directories (home folder, trash, desktop, file system)
2) Removable media
3) User-defined bookmarks (reads ~/.gtk-bookmarks)
4) Recent documents submenu (requires GTK v2.10 or greater) 


%prep
%autosetup -p1

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
%doc AUTHORS COPYING ChangeLog NEWS README.md TODO
%license COPYING
%{_bindir}/xfce4-popup-places
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
* Mon Sep 19 2022 Kevin Fenzi <kevin@scrye.com> - 1.8.2-1
- Update to 1.8.2.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Kevin Fenzi <kevin@scrye.com> - 1.8.0-1
- Update to 1.8.0.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.7.0-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.7.0-9
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 Kevin Fenzi <kevin@scrye.com> 1.7.0-3
- Add patch to fix fault on start. Thanks Shivaji Sathe for patch.
- Fixes bug #1225713

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 09 2015 Kevin Fenzi <kevin@scrye.com> 1.7.0-1
- Update to 1.7.0

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.6.0-4
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 20 2013 Kevin Fenzi <kevin@scrye.com> 1.6.0-1
- Update to 1.6.0 (fixes #1045259)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 01 2012 Kevin Fenzi <kevin@scrye.com> 1.5.0-1
- Update to 1.5.0

* Fri Aug 31 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.4.0-2
- Bump release for koji miracle

* Fri Aug 31 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (fixes #757180)
- Bring back the icon naming patch
- No longer require Thunar (not using thunar-vfs any more)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 21 2012 Kevin Fenzi <kevin@scrye.com> - 1.3.0-1
- Update to 1.3.0

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.2.0-10
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.2.0-9
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2.0-7
- Rebuild for new libpng

* Sat Apr 30 2011 Kevin Fenzi <kevin@scrye.com> - 1.2.0-6
- Add patch to port to GIO and libxfce4ui and exo1
- Fixes bug #678655 and bug #700123

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Kevin Fenzi <kevin@tummy.com> - 1.2.0-4
- Add patch from Debian for new exo version. 

* Sat Nov 06 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-3
- Fix missing icons (#650504)

* Tue Feb 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-2
- Add patch to fix DSO linking (#564693)

* Fri Jul 31 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0
- Drop Andea Santilli's xdg-userdir-compat.patch because it got upstreamed

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-4
- Rebuild for Xfce 4.6 (Beta 3)

* Sun Aug 31 2008 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-3
- Update xdg-userdir-compat.patch to use upstream's variable names

* Wed Aug 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-2
- Respect xdg user directory paths (#457740)

* Thu Jun 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- Fix changelog

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.0-3
- Autorebuild for GCC 4.3

* Fri Dec 07 2007 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-2
- Rebuild for Xfce 4.4.2 and Thunar 0.9.0

* Wed Nov 07 2007 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.992-1
- Update to 0.9.992

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.991-1
- Update to 0.9.991
- Update license tag

* Thu May 17 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Sun Apr 29 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Sun Apr 08 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-1
- Initial package.
