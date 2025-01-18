%global __cmake_in_source_build 1
Name: crossfire-client
Version: 1.75.3
Release: 3%{?dist}
Summary: Client for connecting to crossfire servers
License: GPL-2.0-or-later
URL: http://crossfire.real-time.com
Source0: http://downloads.sourceforge.net/crossfire/%{name}-%{version}.tar.gz

BuildRequires: SDL2-devel SDL2_image-devel SDL2_mixer-devel
BuildRequires: gtk2-devel libpng-devel curl-devel
BuildRequires: desktop-file-utils ImageMagick
BuildRequires: lua-devel
BuildRequires: cmake perl-interpreter vala
BuildRequires: make
# Disabled sound for Fedora until it's working again
#BuildRequires: alsa-lib-devel
Requires: crossfire-client-images

%description
Crossfire is a graphical role-playing adventure game with
characteristics reminiscent of rogue, nethack, omega, and gauntlet. 
It has multiplayer capability and presently runs under X11.

Client for playing the new client/server based version of Crossfire.
This package allows you to connect to crossfire servers around the world.
You do not need install the crossfire program in order to use this
package.

%prep
%setup -q

for size in 48x48 32x32 16x16 ; do 
    convert -transparent white pixmaps/${size}.png temp.png
    mv temp.png pixmaps/${size}.png
done

%build
# Disable sound for Fedora until it's working again.
export  LDFLAGS+=" -lX11"
%cmake
%cmake_build

%install
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -d $RPM_BUILD_ROOT%{_datadir}/icons/locolor/16x16/apps
install -d $RPM_BUILD_ROOT%{_datadir}/icons/locolor/32x32/apps
install -d $RPM_BUILD_ROOT%{_datadir}/icons/locolor/48x48/apps

make install DESTDIR=%{buildroot}

install -m 644 pixmaps/16x16.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/crossfire-client.png
install -m 644 pixmaps/32x32.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/crossfire-client.png
install -m 644 pixmaps/48x48.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/crossfire-client.png
install -m 644 pixmaps/16x16.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/locolor/16x16/apps/crossfire-client.png
install -m 644 pixmaps/32x32.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/locolor/32x32/apps/crossfire-client.png
install -m 644 pixmaps/48x48.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/locolor/48x48/apps/crossfire-client.png

sed -i -e 's/^Name=.*/Name=Crossfire/' gtk-v2/crossfire-client.desktop
desktop-file-install                            \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        --add-category Game                                     \
        --add-category RolePlaying                              \
        gtk-v2/crossfire-client.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat > $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
EmailAddress: crossfire@metalforge.org
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">crossfire-client.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A multiplayer co-operative RPG involving exploration, magic and treasure hunting</summary>
  <description>
    <p>
      Crossfire is an open source RPG with numerous maps that can be explored
      for treasures and artifacts.
    </p>
  </description>
  <url type="homepage">http://crossfire.real-time.com</url>
  <screenshots>
    <screenshot type="default">http://crossfire.real-time.com/clients/gtkv2images/caelestis_790x600.png</screenshot>
  </screenshots>
</application>
EOF

#install lib
mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp common/libcfclient.so $RPM_BUILD_ROOT%{_libdir}/

%ldconfig_scriptlets

%files
%{_bindir}/crossfire-client-gtk2
# Sound support is too broken to use in Fedora right now.
#%%{_bindir}/cfsndserv
#%%{_bindir}/cfsndserv_alsa9
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/locolor/16x16/apps/%{name}.png
%{_datadir}/icons/locolor/32x32/apps/%{name}.png
%{_datadir}/icons/locolor/48x48/apps/%{name}.png
%{_datadir}/%{name}/
%doc ChangeLog COPYING README* TODO
%{_libdir}/libcfclient.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 11 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.75.3-1
- 1.75.3

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.75.2-6
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 09 2022 Leigh Scott <leigh123linux@gmail.com> - 1.75.2-3
- Remove unused gtk+-devel
- Spec file clean up

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.75.2-1
- 1.75.2

* Thu Aug 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.75.1-1
- 1.75.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.75.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.75.0-1
- 1.75.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.74.0-4
- Fix FTBFS.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.74.0-2
- EVR bump for koji error.

* Fri Dec 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.74.0-1
- 1.74.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.72.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.72.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.72.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.72.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.72.0-2
- Remove obsolete scriptlets

* Tue Nov 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.72.0-1
- 1.72.0

* Mon Aug 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.71.0-5svnr20223
- BR perl-interpreter

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-4svnr20223
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-3svnr20223
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.71.0-2svnr20223
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 01 2016 Jon Ciesla <limburgher@gmail.com> - 1.71.0-1svnr20223
- Latest upstream svn checkout to fix GTK bugs.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.70.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.70.0-8
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Tom Callaway <spot@fedoraproject.org> - 1.70.0-4
- rebuild for lua 5.2

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 1.70.0-3
- Drop desktop vendor tag.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Jon Ciesla <limburgher@gmail.com> - 1.70.0-1
- New upstream.
- Curl patch upstreamed.
- libpng patch upstreamed.

* Wed Jan 11 2012 Jon Ciesla <limburgher@gmail.com> - 1.60.0-1
- New upstream.

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.11.0-5
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 24 2008 Wart <wart@kobold.org> 1.11.0-1
- Update to 1.11.0

* Sat Feb 9 2008 Wart <wart@kobold.org> 1.10.0-4
- Rebuild for gcc 4.3

* Sat Aug 18 2007 Wart <wart@kobold.org> 1.10.0-3
- License tag clarification

* Wed Jul 18 2007 Wart <wart@kobold.org> 1.10.0-2
- Remove unused data directory

* Sat Mar 3 2007 Wart <wart@kobold.org> 1.10.0-1
- Update to 1.10.0

* Sat Mar 3 2007 Wart <wart@kobold.org> 1.9.1-3
- Use more precise desktop file categories
- Use better sourceforge download url
- Added dependency on crossfire-client-images so that the default
  install doesn't look so ugly.

* Thu Aug 31 2006 Wart <wart@kobold.org> 1.9.1-2
- Rebuild for Fedora extras
- Add transparency to desktop icon backgrounds

* Thu Jul 6 2006 Wart <wart@kobold.org> 1.9.1-1
- Update to 1.9.1

* Fri May 12 2006 Wart <wart@kobold.org> 1.9.0-3
- Create and own the directory for client sounds and images

* Thu Mar 9 2006 Wart <wart@kobold.org> 1.9.0-2
- Initial spec file following Fedora Extras conventions
