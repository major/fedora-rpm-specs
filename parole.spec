%global fullname org.xfce.Parole
%global minorversion 4.16

Name:           parole
Version:        4.16.0
Release:        5%{?dist}
Summary:        Media player for the Xfce desktop

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/applications/parole
#VCS: git:git://git.xfce.org/apps/parole
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk3-devel >= 3.2.0
BuildRequires:  glib2-devel >= 2.32.0
BuildRequires:  clutter-devel >= 1.16.4
BuildRequires:  clutter-gtk-devel >= 1.4.4
BuildRequires:  gstreamer1-plugins-base-devel >= 0.10.11
BuildRequires:  dbus-devel >= 0.60
BuildRequires:  dbus-glib-devel >= 0.70
BuildRequires:  libxfce4ui-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  xfconf-devel
BuildRequires:  libnotify-devel >= 0.4.1

BuildRequires:  libappstream-glib
BuildRequires:  taglib-devel >= 1.4
BuildRequires:  desktop-file-utils
BuildRequires:  gettext 
BuildRequires:  intltool >= 0.35
BuildRequires:  gtk-doc

# If you checkout from git rather than using a release tarball, uncomment these
# so that ./autogen.sh runs.
# BuildRequires:  xfce4-dev-tools
# BuildRequires:  libtool

Requires:       gstreamer1-plugins-good
# Obsolete the dead mozilla plugin
Obsoletes:      %{name}-mozplugin <= 2.0.2-7

%description
Parole is a modern simple media player based on the GStreamer framework and 
written to fit well in the Xfce desktop. Parole features playback of local 
media files, DVD/CD and live streams. Parole is extensible via plugins.

The project still in its early developments stage, but already contains the 
following features:
* Audio playback
* Video playback with optional subtitle
* Playback of live sources


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains header files for developing plugins for 
%{name}.


%prep
%setup -q

%build
# If you checkout from git rather than using a release tarball, uncomment this.
# The tarballs contain ./configure & friends INSTEAD of ./autogen.sh
# ./autogen.sh

%configure --disable-static --enable-gtk-doc --enable-clutter
%{make_build}

%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name}

desktop-file-install                                    \
  --delete-original                                     \
  --remove-mime-type=video/x-totem-stream               \
  --dir=%{buildroot}%{_datadir}/applications            \
  %{buildroot}/%{_datadir}/applications/%{fullname}.desktop

# clean up appdata file
sed -i 's/<\/em>//' %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
sed -i 's/<em>//' %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS TODO THANKS README.md
%{_bindir}/%{name}
%dir %{_libdir}/%{name}-0/
%{_libdir}/%{name}-0/*.so
%{_datadir}/applications/%{fullname}.desktop
%{_datadir}/icons/hicolor/*/apps/*parole*
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.appdata.xml

%files devel
%doc %{_datadir}/gtk-doc/
%{_includedir}/%{name}/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.16.0-1
- Update to 4.16.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Tue Jul 30 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.3-2
- Fix appdata installation

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 07 2019 Kevin Fenzi <kevin@scrye.com> - 1.0.2-1
- Upgrade to 1.0.2.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0.1-3
- Rebuilt for new libxfconf version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 14 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1
- Modernize spec

* Fri Mar 02 2018 Kevin Fenzi <kevin@scrye.com> - 1.0.0-1
- Update to 1.0.0. 

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Mike DePaulo <mikedep333@gmail.com> - 0.9.2-1
- Upgrade to 0.9.2
- Patch parole.appdata.xml so that it validates
- Clean up parole-0.8.0-appdata.patch
- Run autogen.sh to regenerate ./configure (because Fedora suggests to do so)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 15 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1
- Remove appdata patch (added by upstream)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 07 2015 Kevin Fenzi <kevin@scrye.com> 0.8.0-2
- Switch to gstreamer1 and build clutter backend
- Clean up BuildRequires versions
- Properly validate and install appdata

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.8.0-1
- Upgrade to 0.8.0
- Rebuild for Xfce 4.12

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.5.4-7
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Feb 01 2015 Richard Hughes <richard@hughsie.com> 0.5.4-6
- Fix the AppData file; you can only use <_p> in a file that gets passed to
  intltool, i.e. translated upstream. Downstream files have to be valid.

* Tue Nov 11 2014 Kevin Fenzi <kevin@scrye.com> 0.5.4-5
- Add appdata file. Fixes #1162380

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 04 2014 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.4-2
- Add upstream patch to correctly close dir-handle (#963428)

* Fri Dec 20 2013 Kevin Fenzi <kevin@scrye.com> 0.5.4-1
- Update to 0.5.4 (fixes #1045255)

* Fri Jul 26 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2 (fixes #972567)

* Fri Jun 07 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1 (#971293)

* Wed Mar 06 2013 Kevin Fenzi <kevin@scrye.com> 0.5.0-1
- Update to 0.5.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
- BR xfconf-devel as configuration is now stored in xfconf

* Wed Aug 22 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0.3-1
- Update to 0.3.0.3
- Build gtk documentation again (bugzilla.xfce.org #9232)

* Tue Aug 21 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0.2-1
- Update to 0.3.0.2
- For now, don't build with --enable-gtk-doc
- Drop DSO patch, fixed upstream

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 0.2.0.6-4
- Rebuild for Xfce 4.10

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.0.6-2
- Rebuild for new libpng

* Sun Jun 05 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0.6-1
- Update to 0.2.0.6
- Obsolete parole-mozplugin
- Drop libnotify patch, no longer needed

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 05 2010 Kevin Fenzi <kevin@tummy.com> - 0.2.0.2-5
- Add patch to build against new libnotify 

* Wed Sep 29 2010 jkeating - 0.2.0.2-4
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0.2-3
- Remove mime-type "video/x-totem-stream" (#633304)
- Make parole-devel no longer require gtk-doc (#604409)

* Thu Feb 18 2010 Kevin Fenzi <kevin@tummy.com> - 0.2.0.2-2
- Add patch to fix DSO issue. Fixes bug #565207

* Mon Jan 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0.2-1
- Update to 0.2.0.2

* Thu Jan 14 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0.1-1
- Update to 0.2.0.1

* Tue Jan 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Tue Dec 01 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.99-1
- Update to 0.1.99 and drop all patches
- Make the plugin require mozilla-filesystem

* Sun Nov 29 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.98-1
- Update to 0.1.98
- Cherry pick some patches to build the browser plugin with xulrunner 1.9.2

* Wed Nov 25 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.96-1
- Update to 0.1.96
- Build gtk-doc files

* Wed Nov 25 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.95-1
- Update to 0.1.95

* Fri Oct 30 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.91-1
- Update to 0.1.91

* Thu Oct 08 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.90-3
- Set locale before loading the GtkBuilder interface definition for dialogs
- Translation updates

* Thu Oct 08 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.90-2
- BuildRequire taglib-devel and fix libnotify requirement

* Wed Oct 07 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.90-1
- Update to 0.1.90
- Loads of additional translations

* Fri Sep 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1-0.1
- Initial package
