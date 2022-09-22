# Review at https://bugzilla.redhat.com/show_bug.cgi?id=351531

%global majorversion 0.12
%global xfceversion 4.16


Name:           ristretto
Version:        0.12.3
Release:        2%{?dist}
Summary:        Image-viewer for the Xfce desktop environment
Summary(de):    Bildbetrachter für die Xfce Desktop-Umgebung

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/applications/ristretto/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{majorversion}/%{name}-%{version}.tar.bz2
#VCS: git:git://git.xfce.org/apps/ristretto

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  dbus-glib-devel >= 0.34
BuildRequires:  gtk2-devel >= 2.20.0
BuildRequires:  exo-devel >= 0.12.0
BuildRequires:  libexif-devel >= 0.6.0
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  desktop-file-utils, gettext, intltool
BuildRequires:  libappstream-glib
Requires:       tumbler


%description
Ristretto is a fast and lightweight image-viewer for the Xfce desktop 
environment.

%description -l de
Ristretto ist ein schneller und leichtgewichtiger Bildbetrachter für die Xfce
Desktop-Umgebung.


%prep
%autosetup

%build
%configure
%make_build


%install
%make_install

%find_lang %{name}

desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        --add-mime-type=image/x-bmp \
        --add-mime-type=image/x-png \
        --add-mime-type=image/x-pcx \
        --add-mime-type=image/x-tga \
        --add-mime-type=image/xpm \
        --delete-original \
        %{buildroot}%{_datadir}/applications/org.xfce.%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%if 0%{?el7}
%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/*.appdata.xml

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.3-1
- Update to v0.12.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2

* Thu Dec 02 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Wed Oct 13 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.10.0-2
- Update xfce version

* Fri Aug 09 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.10.0-1
- Update to 0.10.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Sun Apr 07 2019 Kevin Fenzi <kevin@scrye.com> - 0.8.4-1
- Update to 0.8.4. Fixes bug #1684190

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.3-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.3-2
- Add EL conditional

* Thu Jun 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.3-1
- Update to 0.8.3
- Modernize spec

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Kevin Fenzi <kevin@scrye.com> - 0.8.2-3
- Drop 0 length README

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Kevin Fenzi <kevin@scrye.com> - 0.8.2-1
- Update to 0.8.2.

* Thu Oct 06 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.1-3
- Fix dates/days in changelog (no build)

* Thu Oct 06 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.1-2
- Drop upstreamed patch

* Thu Oct 06 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.1-1
- Update to bugfix release (0.8.1)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Kevin Fenzi <kevin@scrye.com> 0.8.0-1
- Rebuild for Xfce 4.12
- Upgrade to 0.8.0

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.6.3-7
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.3-3
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 01 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3 (#891037)

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0
- Update to 0.6.0

* Fri Apr 27 2012 Kevin Fenzi <kevin@scrye.com> - 0.3.7-1
- Update to 0.3.7

* Wed Apr 04 2012 Kevin Fenzi <kevin@scrye.com> - 0.3.6-2
- Rebuild for Xfce 4.10

* Tue Apr 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.6-1
- Update to 0.3.6
- Add VCS key

* Sat Mar 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5

* Sat Jan 28 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4

* Sat Jan 14 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-2
- Require tumbler for thumbnail generation

* Sun Nov 06 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Sun Nov 06 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3 (fixes #750657)

* Sat Oct 29 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for glibc bug#747377

* Sun Oct 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Tue Oct 18 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Sun Oct 09 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1
- Drop DSO patch, fixed upstream

* Thu Oct 06 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-1
- Update to 0.1.0

* Tue Aug 16 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.93-2
- Fix two major memory leaks (bugzilla.xfce.org #7882)

* Thu Mar 03 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.93-1
- Update to 0.0.93 (fixes #542141 and #679808)
- No longer require xfce4-doc
- Run update-desktop-database in %%post and %%postun

* Wed Feb 09 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.91-2
- BR xfconf-devel to fix build after Xfce 4.8 update

* Tue Jul 13 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.91-1
- Update to 0.0.91 (Development release for next major version)
- Require xfce4-doc for directory ownership of the nex docs

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.22-3
- Add patch to fix DSO linking (#565114)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 15 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.22-1
- Update to 0.0.22

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.21-1
- Update to 0.0.21
- Remove marshaller fix, included upstream now

* Tue Jul 01 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.20-2
- Add patch to fix x86_64 bit bug caused by a wrong marshaller (#351531)

* Sat May 24 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.20-1
- Update to 0.0.20

* Sat May 10 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.19-1
- Update to 0.0.19

* Sat Apr 05 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.18-1
- Update to 0.0.18

* Sun Feb 17 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.17-1
- Update to 0.0.17

* Wed Jan 30 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.16-1
- Update to 0.0.16

* Mon Dec 03 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.15-1
- Update to 0.0.15

* Mon Dec 03 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.14-1
- Update to 0.0.14

* Mon Nov 26 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.13-1
- Update to 0.0.13

* Wed Nov 21 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.12-2
- Try manual_adjustments.patch

* Tue Nov 20 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.12-1
- Update to 0.0.12

* Wed Nov 07 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.11-1
- Update to 0.0.11
- BuildRequire dbus-glib-devel

* Sat Nov 03 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.10-1
- Update to 0.0.10
- Add more mimetypes: tiff, x-bmp, x-png, x-pcx, x-tga and xpm
- Correct build requirements

* Fri Oct 19 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.9-1
- Update to 0.0.9

* Sun Oct 14 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.8-1
- Update to 0.0.8

* Sun Sep 30 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.7-1
- Update to 0.0.7

* Sun Sep 09 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.4-1
- Update to 0.0.4

* Wed Sep 05 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.3-1
- Initial RPM package
