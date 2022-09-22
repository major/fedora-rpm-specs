%global majorversion 1.5

Name:           xfce4-taskmanager
Version:        1.5.4
Release:        2%{?dist}
Summary:        Taskmanager for the Xfce desktop environment

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/applications/%{name}
Source0:        http://archive.xfce.org/src/apps/%{name}/%{majorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel
BuildRequires:  libXmu-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  intltool

%description
A simple taskmanager for the Xfce desktop environment.


%prep
%setup -q


%build
%configure --enable-gtk3

%make_build


%install
%make_install

%find_lang %{name}

desktop-file-install \
    --delete-original \
    --add-category GTK \
    --add-category Monitor \
    --add-category X-Xfce \
    --remove-category Utility \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop



%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS THANKS
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/16x16/actions/xc_crosshair.png
%{_datadir}/icons/hicolor/24x24/actions/xc_crosshair.png
%{_datadir}/icons/hicolor/scalable/actions/xc_crosshair.svg
%{_datadir}/icons/hicolor/*/apps/org.xfce.taskmanager.*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4

* Tue Mar 1 2022 Ali Erdinc Koroglu <ali.erdinc.koroglu@intel.com> - 1.5.2-1
- Upstream update to 1.5.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 09 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Sun Feb 07 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 <nonamedotc@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.1-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 03 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-5
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.0-2
- Add icon files
- Fix buildrequires

* Sun Feb 12 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.0-1
-Update to 1.2.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.0-3
- Removed libxfcegui4 build requires
- Fixes 1209549

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.1.0-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Fri Dec 26 2014 Kevin Fenzi <kevin@scrye.com> 1.1.0-1
- Update to 1.1.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1
- Remove aarch64 patch, no longer needed
- Add patch to fix some German translations (submitted upstream via Transifex)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 19 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-7
- Make desktop vendor conditional
- Add aarch64 support (#926791)

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.0.0-6
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.0-3
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 15 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 final

* Sun Jun 06 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.92-1
- Update to 0.5.91 (0.6 Beta 3)

* Tue May 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.91-1
- Update to 0.5.91 (0.6 Beta 2)

* Thu Jul 30 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 21 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-2
- Rebuild for i586 and SHA 256 hashes in RPM
- Rework categories of desktop file to allow nested menus

* Tue Sep 30 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1
- Remove patches (fixed upstream)

* Sat May 24 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0 stable which has finally been released
- Add patch to fix 0%%-CPU bug (rebased version of Enrico Tröger's patch)
- Add patch to fix some compiler warnings (also based on Enrico's work)
- Update license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.0-0.3.rc2
- Autorebuild for GCC 4.3

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-0.2.rc2
- Bump release for devel checkin.

* Tue Oct 03 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-0.1.rc2
- Update to 0.4-rc2.
- Add BR on perl(XML::Parser), drop intltool.

* Mon Oct 02 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.1-6
- Rebuild for XFCE 4.4.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.1-5
- Mass rebuild for Fedora Core 6.
- Fix %%defattr.

* Sat Jun 03 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-4
- Add intltool BR (#193444).

* Thu Feb 16 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-3
- Rebuild for Fedora Extras 5.

* Thu Dec 15 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-2
- Initial Fedora Extras version.
- Add xfce4-taskmanager.desktop.
- Remove useless NEWS from %%doc.
- Clean up specfile.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-1.fc4.cw
- Updated to version 0.3.1.
- Rebuild for Core 4.

* Thu Apr 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.1-1.fc3.cw
- Initial RPM release.
