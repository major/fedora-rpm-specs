Name:           teeworlds
Version:        0.7.5
Release:        16%{?dist}
Summary:        Online multi-player platform 2D shooter

# zlib: src/engine/externals/md5/*
# BSD:  src/engine/externals/json-parser/*
License:        LicenseRef-Callaway-Teeworlds AND Zlib AND BSD-2-Clause AND BSD-3-Clause
URL:            https://www.teeworlds.com/
Source0:        https://github.com/teeworlds/teeworlds/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/teeworlds/teeworlds-maps/archive/1d3401a37a3334e311faf18a22aeff0e0ac9ee65/%{name}-%{version}-maps.tar.gz
Source2:        https://github.com/teeworlds/teeworlds-translation/archive/4ed69dd7497ca6e04bab0b042f137bf97f3c5d0a/%{name}-%{version}-translation.tar.gz
Source3:        %{name}.png
# systemd unit definition
Source4:        %{name}-server@.service
# example configs file for server
Source5:        server_dm.cfg
Source6:        server_tdm.cfg
Source7:        server_ctf.cfg

#Patch for CVE-2021-43518
Patch0: 3018.patch
#Patch1: fminimum.patch

BuildRequires:  python3-devel
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pnglite-devel
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pkgconfig(wavpack)
#BuildRequires:  pkgconfig(json-parser)
Provides:       bundled(md5)
# TODO: unbundle
Provides:       bundled(json-parser)
Requires:       %{name}-data = %{version}

%description
The game features cartoon-themed graphics and physics, 
and relies heavily on classic shooter weaponry and gameplay. 
The controls are heavily inspired by the FPS genre of computer games. 

%package        server
Summary:        Server for %{name}
Requires:       %{name}-data = %{version}
Provides:       bundled(md5)
Requires(pre):  shadow-utils
%{?systemd_requires}
BuildRequires:  systemd

%description    server
Server for %{name}, an online multi-player platform 2D shooter. 

%package        data
Summary:        Data-files for %{name}
License:        CC-BY-SA-4.0
Requires:       font(dejavusans)
BuildArch:      noarch

%description    data
Data-files for %{name}, an online multi-player platform 2D shooter.

%prep
%setup -q -a1 -a2
%autopatch -p1
rm -vrf datasrc/{maps,languages}
mv teeworlds-maps-* datasrc/maps
mv teeworlds-translation-* datasrc/languages
# https://github.com/teeworlds/teeworlds/issues/1882
%ifnarch x86_64
sed -i -e "/_mm_pause/d" src/engine/client/client.cpp
%endif
sed -i "s/\/usr/\%{_prefix}/g" src/engine/shared/storage.cpp

%build
%cmake . -B%{_vpath_builddir} -GNinja -DCMAKE_BUILD_TYPE=RELEASE \
  -DPREFER_BUNDLED_LIBS=OFF \
  -DSERVER_EXECUTABLE=%{name}-srv \
  -DPYTHON_EXECUTABLE=%{__python3} \
  %{nil}
%ninja_build -C %{_vpath_builddir}

%install
%ninja_install -C %{_vpath_builddir}
install -Dpm0644 -t %{buildroot}%{_datadir}/pixmaps/ %{S:3}
install -Dpm0644 -t %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/ %{S:3}
install -Dpm0644 -t %{buildroot}%{_metainfodir} other/%{name}.appdata.xml
install -Dpm0644 -t %{buildroot}%{_unitdir} %{S:4}
install -Dpm0644 -t %{buildroot}%{_datadir}/applications other/%{name}.desktop
install -Dpm0664 %{S:5} %{buildroot}%{_sysconfdir}/%{name}/dm.cfg
install -Dpm0664 %{S:6} %{buildroot}%{_sysconfdir}/%{name}/tdm.cfg
install -Dpm0664 %{S:7} %{buildroot}%{_sysconfdir}/%{name}/ctf.cfg
ln -sf %{_datadir}/fonts/dejavu-sans-fonts/DejaVuSans.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/DejaVuSans.ttf

%pre server
getent group teeworlds >/dev/null || groupadd -f -r teeworlds
if ! getent passwd teeworlds >/dev/null ; then
      useradd -r -g teeworlds -d %{_sysconfdir}/%{name} -s /sbin/nologin \
              -c "%{name} server daemon account" teeworlds
fi
exit 0

%post server
%systemd_post %{name}-server@dm.service
%systemd_post %{name}-server@tdm.service
%systemd_post %{name}-server@ctf.service

%preun server
%systemd_preun %{name}-server@dm.service
%systemd_preun %{name}-server@tdm.service
%systemd_preun %{name}-server@ctf.service

%postun server
%systemd_postun_with_restart %{name}-server@dm.service
%systemd_postun_with_restart %{name}-server@tdm.service
%systemd_postun_with_restart %{name}-server@ctf.service

%files
%license license.txt
%doc readme.md
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%files data
%license datasrc/{languages,maps}/license.txt
%{_datadir}/%{name}/

%files server
%license license.txt
%doc readme.md
%{_bindir}/%{name}-srv
%{_unitdir}/%{name}-server@.service
%attr(-,teeworlds,teeworlds)%{_sysconfdir}/%{name}/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.7.5-12
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.7.5-10
- Patch for CVE-2021-43518

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.5-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.7.5-2
- Fix dejavu font path.

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.7.5-1
- 0.7.5

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.7.4-2
- bump EVR for koji error

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.7.4-1
- 0.7.4

* Fri Aug 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.7.3.1-5
- Path fix.

* Fri Aug 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.7.3.1-4
- Put a copy of icon in a place flatpak will use.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.7.3.1-2
- Patch to fix s390x build.

* Fri Apr 26 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.7.3.1-1
- 0.7.3.1

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Sat Dec 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-4
- Depend on same version of data from server

* Sat Dec 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-3
- Add BSD to license list

* Sat Dec 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-2
- Make data subpackage noarch

* Sat Dec 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Mon Oct 22 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.6.5-1
- 0.6.5

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.6.4-8
- Bam patch.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.4-7
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.4-4
- Explicitly require bin/python

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 18 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.4-2
- Backport freetype patch from upstream

* Wed Nov 09 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.4-1
- Update to 0.6.4

* Wed Feb 24 2016 Jon Ciesla <limburgher@gmail.com> - 0.6.3-6
- Fix FTBFS, BZ 1308180.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.3-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.6.3-2
- Add an AppData file for the software center

* Mon Nov 24 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.3-1
- 0.6.3 (RHBZ #1167167,#1167168)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 25 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.2-7
- fix permissions (allow access from teeworlds group to server cfgs)

* Sat Aug 17 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.2-6
- Fixed port in example tdm server cfg

* Tue Jul 30 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.2-5
- Typo fix in source list in server cfgs

* Tue Jul 23 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.2-4
- Add sample tdm server config
- Few fixes in existing server configs
- Droped BuildRoot target (since Fedora 18 was deprecated)
- Dropped %%clean section (since Fedora 18 was deprecated)
- Dropped %%defattr directives (since Fedora 18 was deprecated)
- %%{buildroot} instead of $RPM_BUILD_ROOT

* Fri Jul  5 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.2-3
- systemd instead of systemd-units in spec file

* Wed Jul  3 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.2-2
- Update systemd daemon for multiple server configs
- Some fixes in spec

* Tue Jul  2 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.2-1
- Update to 0.6.2
- Drop unnecessary patches and fix need patches for new version
- Add systemd daemon with example server cfg
- Some fixes in spec

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 0.6.1-4
- Add hardened build.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 27 2011 Jon Ciesla <limb@jcomserv.net> - 0.6.1-2
- Fix to extlib patch to correct sound loading issue.

* Mon Aug 22 2011 Jon Ciesla <limb@jcomserv.net> - 0.6.1-1
- New upstream release

* Tue Apr 26 2011 Jon Ciesla <limb@jcomserv.net> - 0.6.0-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 24 2009 Simon Wesp <cassmodiah@fedoraproject.org> 0.5.2-2
- convert iso files to utf8

* Thu Dec 24 2009 Simon Wesp <cassmodiah@fedoraproject.org> 0.5.2-1
- New upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 09 2009 Simon Wesp <cassmodiah@fedoraproject.org> 0.5.1-1
- New upstream release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Lubomir Rintel <lkundrak@v3.sk> 0.5.0-1
- New upstream release

* Fri Jan 02 2009 Simon Wesp <cassmodiah@fedoraproject.org> 0.4.3-5
- Remove requires from subpackage 'data'
- Correct description 

* Thu Jan 01 2009 Simon Wesp <cassmodiah@fedoraproject.org> 0.4.3-4
- Drop desktop-file and icon for subpackage 'server'
- Honor timestamp for converted file
- Add and correct Lubomir's changes
- Remove all comments
- Correct License-Tag (again)
- Add datadir patch

* Wed Dec 31 2008 Lubomir Rintel <lkundrak@v3.sk> 0.4.3-3
- Outsource the dependencies (extlib-patch)
- Use optflags

* Thu Sep 18 2008 Simon Wesp <cassmodiah@fedoraproject.org> 0.4.3-2
- Recheck and conform licensing and list it in a comment
- Correct BuildRequires

* Sat Sep 13 2008 Simon Wesp <cassmodiah@fedoraproject.org> 0.4.3-1
- Initial Release

