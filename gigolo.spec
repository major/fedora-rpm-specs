%global minorversion 0.5

Name:           gigolo
Version:        0.5.2
Release:        5%{?dist}
Summary:        GIO/GVFS management application

License:        GPLv2
URL:            http://goodies.xfce.org/projects/applications/gigolo/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make

Requires:       gvfs-fuse

Obsoletes: sion < 0.1.0-3

%description
A frontend to easily manage connections to remote filesystems using GIO/GVFS. 
It allows you to quickly connect/mount a remote filesystem and manage
bookmarks of such. 

%prep
%setup -q

%build
#rm -f waf
%configure
%make_build


%install
%make_install
%find_lang %{name}

# remove duplicate docs
rm -rf %{buildroot}/%{_datadir}/doc/gigolo

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS TODO THANKS
%{_bindir}/gigolo
%{_datadir}/icons/hicolor/*/apps/org.xfce.gigolo.*
%{_datadir}/applications/gigolo.desktop
%{_mandir}/man1/gigolo.1.gz

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2
- Drop old patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 03 2020 Kevin Fenzi <kevin@scrye.com> - 0.5.0-4
- Drop python2 BuildRequires. Fixes bug #1808323

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.0-2
- Add gtk3-devel as buildrequires

* Tue Aug 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0
- Minor spec changes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Kevin Fenzi <kevin@scrye.com> - 0.4.2-13
- Fix FTBFS by adding BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.2-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Kevin Fenzi <kevin@scrye.com> 0.4.2-4
- Add patch to change desktop icon from gtk-network to folder-remote. Fixes bug #1176115

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2
- Drop included upstream patches

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Kevin Fenzi <kevin@scrye.com> 0.4.1-8
- Switch to bundled waf for now, doesn't work with waf-1.6.11

* Thu Jun 21 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-7
- Require gvfs-fuse, fuse and gvfs are not enough (#834261)

* Sat Jan 21 2012 Kevin Fenzi <kevin@scrye.com> - 0.4.1-6
- Use system waf to get around configure hang.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for glibc bug#747377

* Sun Oct 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-3
- Fix crash when closing gigolo from the toolbar (#748228)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 01 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.1
- Patch to fix German translation
 
* Thu Dec 31 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Kevin Fenzi <kevin@tummy.com> - 0.3.2-1
- Update to 0.3.2

* Sat Apr 04 2009 Kevin Fenzi <kevin@tummy.com> - 0.3.1-1
- Update to 0.3.1

* Tue Mar 31 2009 Kevin Fenzi <kevin@tummy.com> - 0.3.0-1
- Update to 0.3.0 

* Sun Feb 22 2009 Kevin Fenzi <kevin@tummy.com> - 0.2.1-1
- Update to 0.2.1
- Add THANKS
- Fix waf configure line and use local waf.

* Sun Feb 15 2009 Kevin Fenzi <kevin@tummy.com> - 0.2.0-2
- Fix CFLAGS
- Fix build to be verbose
- Use Fedora waf
- Remove vendor

* Sun Feb 15 2009 Kevin Fenzi <kevin@tummy.com> - 0.2.0-1
- Change name to gigolo
- Update to 0.2.0

* Sun Jan 04 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.0-2
- Fix License tag
- Add Requires for needed binaries

* Fri Jan 02 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.0-1
- Initial version for Fedora
