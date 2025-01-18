# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.28

# Settings used for build from snapshots.
%{!?rel_build:%global commit 298c7255b82986eeba72fff06f59479deae0b9d0}
%{!?rel_build:%global commit_date 20131201}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           caja-extensions
Summary:        Set of extensions for caja file manager
Version:        %{branch}.0
%if 0%{?rel_build}
Release:        6%{?dist}
%else
Release:        0.25%{?git_rel}%{?dist}
%endif
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R caja.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

Source1:       caja-share-setup-instructions
Source2:       caja-share-smb.conf.example

BuildRequires: make
BuildRequires: mate-common
BuildRequires: caja-devel
BuildRequires: mate-desktop-devel
BuildRequires: dbus-glib-devel
BuildRequires: gstreamer1-plugins-bad-free-devel
BuildRequires: gtk3-devel
BuildRequires: gupnp-devel
BuildRequires: dbus-glib-devel

%if 0%{?rhel} <= 7 || 0%{?fedora}
# temporarily disabled
# BuildRequires:  gajim
%endif

%description
Extensions for the caja file-browser, open-terminal,
image-converter, sendto and share

%package common
Summary:    Common files for %{name}
BuildArch:  noarch

%description common
%{summary}.

%package -n caja-audio-video-properties
Summary:    MATE file manager audio-video-properties extension
Requires:   %{name}-common = %{version}-%{release}

%description -n caja-audio-video-properties
The caja-audio-video-properties extension allows you to
view audio and video properties in Caja.

%package -n caja-image-converter
Summary:    MATE file manager image converter extension
Requires:   %{name}-common = %{version}-%{release}
Requires:   ImageMagick

%description -n caja-image-converter
The caja-image-converter extension allows you to
re-size/rotate images from Caja.

%package -n caja-open-terminal
Summary:    Mate-file-manager extension for an open terminal shortcut
Requires:   %{name}-common = %{version}-%{release}

%description -n caja-open-terminal
The caja-open-terminal extension provides a right-click "Open
Terminal" option for mate-file-manager users who prefer that option.

%package -n caja-sendto
Summary:    MATE file manager sendto
Requires:   %{name}-common = %{version}-%{release}

%description -n caja-sendto
The caja-sendto extension provides 'send to' functionality
to the MATE Desktop file-manager, Caja.

%package -n caja-sendto-devel
Summary:    Development libraries and headers for caja-sendto
Requires:   %{name}-common = %{version}-%{release}
Requires:   caja-sendto%{?_isa} = %{version}-%{release}

%description -n caja-sendto-devel
Development libraries and headers for caja-sendto

%package -n caja-share
Summary:    Easy sharing folder via Samba (CIFS protocol)
Requires:   %{name}-common = %{version}-%{release}
Requires:   samba

%description -n caja-share
Caja extension designed for easier folders 
sharing via Samba (CIFS protocol) in *NIX systems.

%package -n caja-beesu
Summary:    MATE file manager beesu
Requires:   %{name}-common = %{version}-%{release}
Requires:   beesu

%description -n caja-beesu
Caja beesu extension for open files as superuser

%package -n caja-wallpaper
Summary:    MATE file manager wallpaper
Requires:   %{name}-common = %{version}-%{release}

%description -n caja-wallpaper
Caja wallpaper extension, allows to quickly set wallpaper.

%package -n caja-xattr-tags
Summary:    MATE file manager xattr-tags
Requires:   %{name}-common = %{version}-%{release}

%description -n caja-xattr-tags
Caja xattr-tags extension, allows to quickly set xattr-tags.


%prep
%if 0%{?rel_build}
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

cp %{SOURCE1} SETUP

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# for snapshots
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
%configure \
     --disable-schemas-compile \
     --enable-image-converter  \
     --enable-open-terminal    \
     --enable-sendto           \
%if 0%{?rhel} > 7
     --with-sendto-plugins=emailclient,caja-burn,pidgin,removable-devices,upnp \
%else
     --with-sendto-plugins=emailclient,caja-burn,pidgin,removable-devices,upnp \
%endif
     --enable-share            \
     --enable-totem-properties \
     --enable-gksu             \
     --enable-wallpaper        \
     --enable-totem-properties \
     --disable-static

make %{?_smp_mflags} V=1

%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

mkdir -p %{buildroot}/%{_sysconfdir}/samba/
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/samba/

%find_lang %{name} --with-gnome --all-name


%files common -f %{name}.lang
%doc AUTHORS COPYING README SETUP
%dir %{_datadir}/caja-extensions

%files -n caja-audio-video-properties
%{_libdir}/caja/extensions-2.0/libcaja-av.so
%{_datadir}/caja/extensions/libcaja-av.caja-extension

%files -n caja-image-converter
%{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja/extensions/libcaja-image-converter.caja-extension

%files -n caja-open-terminal
%{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml
%{_datadir}/caja/extensions/libcaja-open-terminal.caja-extension

%files -n caja-sendto
%{_bindir}/caja-sendto
%dir %{_libdir}/caja-sendto
%dir %{_libdir}/caja-sendto/plugins
%{_libdir}/caja-sendto/plugins/libnstburn.so
%{_libdir}/caja-sendto/plugins/libnstemailclient.so
%{_libdir}/caja-sendto/plugins/libnstpidgin.so
%{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_libdir}/caja-sendto/plugins/libnstupnp.so
%if 0%{?rhel} <= 7 || 0%{?fedora}
# temporarily disabled
#%{_libdir}/caja-sendto/plugins/libnstgajim.so
%endif
%{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/caja/extensions/libcaja-sendto.caja-extension
%dir %{_datadir}/gtk-doc/html/caja-sendto
%{_datadir}/gtk-doc/html/caja-sendto/*
%{_mandir}/man1/caja-sendto.1.gz

%files -n caja-sendto-devel
%dir %{_includedir}/caja-sendto
%{_includedir}/caja-sendto/caja-sendto-plugin.h
%{_libdir}/pkgconfig/caja-sendto.pc

%files -n caja-share
%config %{_sysconfdir}/samba/caja-share-smb.conf.example
%{_libdir}/caja/extensions-2.0/libcaja-share.so
%{_datadir}/caja-extensions/share-dialog.ui
%{_datadir}/caja/extensions/libcaja-share.caja-extension

%files -n caja-beesu
%{_libdir}/caja/extensions-2.0/libcaja-gksu.so
%{_datadir}/caja/extensions/libcaja-gksu.caja-extension

%files -n caja-wallpaper
%{_libdir}/caja/extensions-2.0/libcaja-wallpaper.so
%{_datadir}/caja/extensions/libcaja-wallpaper.caja-extension

%files -n caja-xattr-tags
%{_libdir}/caja/extensions-2.0/libcaja-xattr-tags.so
%{_datadir}/caja/extensions/libcaja-xattr-tags.caja-extension


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mo Jul 29 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-5
- disable gajim modul to fix building for f41

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.0-4
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 25 2024 Fabio Valentini <decathorpe@gmail.com> - 1.28.0-2
- Rebuild for gstreamer-plugins-bad 1.24.

* Fri Feb 23 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-1
- update to 1.28.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 14 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-5
- fix rhbz (#2249632) and (#2145142)
- enable gupnp for sendto-plugin again
- use upstream commit https://github.com/mate-desktop/caja-extensions/commit/91cc466

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-2
- disable gupnp for sendto-plugin

* Sat Aug 20 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-1
- update to 1.26.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-4
- add upstream patch from 1.26 branch

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 20 2021 Kalev Lember <klember@redhat.com> - 1.26.0-2
- Rebuilt for gupnp soname bump

* Fri Aug 06 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0 release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.1-1
- update to 1.24.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 15 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-3
- add upstream patch
- fix pt and pt_BR locale translation issues

* Thu Mar 12 2020 Kalev Lember <klember@redhat.com> - 1.24.0-2
- Rebuilt for gupnp 1.2

* Tue Feb 11 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0

* Mon Feb 03 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.23.1-1
- update to 1.23.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Thomas Batten <stenstorpmc@gmail.com> - 1.22.1-2
- Disable gajim for el > 7
- Fix double % in Source0

* Wed Sep 18 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-1
- update to 1.22.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.0-1
- update to 1.22.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-2
- bump version to fix conflicts with previous extenstion package from caja

* Tue Dec 11 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-1
- update to 1.20.2

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.1-2
- bumb version to avoid conflict with debuginfo package from caja

* Tue Jun 12 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.1-1
- update to 1.20.1 release

* Sun Feb 11 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.0-1
- update to 1.20.0 release
- drop GSettings Schema rpm scriptlet
- switch to using autosetup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.19.0-1
- update to 1.19.0 release

* Wed Aug 09 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.1-4
- remove virtual provides

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 16 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.1-1
- update to 1.18.1 release

* Tue Mar 14 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.0-1
- update to 1.18.0 release
- add caja-xattr-tags subpackage

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update to 1.17.0 release

* Thu Sep 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release
- switch to gtk+3

* Tue Apr 05 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Thu Oct 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- update to 1.11.0 release

* Thu Jul 16 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-1
- update to 1.10.1 release
- enable gajim sendto plugin

* Wed Jul 01 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-3
- disable gajim sendto plugin

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release

* Sun Apr 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-1
- update to 1.9.90 release

* Thu Jan 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release
- add caja-wallpaper subpackage
- cleanup build requires
- update configure flags
- update file section

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- update to 1.9.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-2
- rebuild for libgtop2 soname bump

* Wed Mar 05 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90

* Mon Feb 10 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.2-1
- update to 1.7.2 release

* Fri Jan 24 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-1
- update to 1.7.1
- add --with-gnome --all-name for find language
- fix bogus date in %%changelog

* Wed Dec 18 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-0.4.git20131201.298c725
- make Maintainers life easier and use better git snapshot usage, Thanks to Björn Esser
- fix provides/obsoletes

* Sat Dec 14 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-0.3.git298c725
- remove isa tags from obsoletes/provides

* Fri Dec 06 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-0.2.git298c725
- fix all the macro-in-comment warnings
- add versioned provides for the obsoleted packages
- remove NEWS, zero-length
- fix spelling-errors

* Thu Dec 05 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-0.1.git298c725
- initial build for fedora rawhide (f21)
- this package obsoletes mate-file-manager-image-converter,
- mate-file-manager-open-terminal, mate-file-manager-sendto,
- mate-file-manager-share
- add new extension caja-beesu

