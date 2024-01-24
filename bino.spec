Name:           bino
Version:        2.1
Release:        3%{?dist}
Summary:        3D video player

License:        GPL-3.0-or-later
URL:            https://bino3d.org
Source0:        %{url}/releases/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://marlam.de/key.txt

Requires:       hicolor-icon-theme

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  pandoc

BuildRequires:  libGL-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qvr-devel

%description
Bino is a 3D video player. It supports stereoscopic 3D video with a wide
variety of input and output formats. It also supports multi-display video
and it can be used for powerwalls, virtual reality installations and other
multi-projector setups.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/org.bino3d.bino.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.bino3d.bino.metainfo.xml

%files
%license LICENSE.md
%doc README.md NEWS.md
%doc %{_pkgdocdir}/%{name}-manual.*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/org.bino3d.bino.desktop
%{_datadir}/icons/hicolor/*/apps/org.bino3d.bino.*
%{_metainfodir}/org.bino3d.bino.metainfo.xml

%changelog
* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 2.1-1
- Update to 2.1
- Drop info logic as it's no longer needed
- Rework build requirements and drop arch restriction
- Convert license tag to SPDX
- Rework specfile to follow the Fedora packaging guidelines

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Aug 06 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Sérgio Basto <sergio@serjux.com> - 1.6.8-1
- Update bino to 1.6.8

* Thu Nov 11 2021 Leigh Scott <leigh123linux@gmail.com> - 1.6.7-10
- Rebuilt for new ffmpeg snapshot

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
- Add upstream patch for GCC 11

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 1.6.7-7
- Rebuilt for new ffmpeg snapshot

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.6.7-5
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 1.6.7-3
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.6.7-1
- New version

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.6.6-5
- Rebuild for new libass version

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.6.6-4
- Rebuilt for new ffmpeg snapshot

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.6.6-3
- Rebuilt for new ffmpeg snapshot

* Wed Feb 28 2018 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.6.6-1
- New version

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.6.5-4
- Rebuilt for ffmpeg-3.5 git

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.6.5-2
- Rebuild for ffmpeg update

* Wed Mar 22 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.6.5-1
- New version
- Patch for glew-2.0 changes
- Build is x86 only

* Sat Mar 18 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec  5 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 1.6.4-1
- New version
  Resolves: rfbz#4366
- Dropped ffmpeg_2.9 patch (upstreamed)

* Tue Aug 16 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.6.3-3
- Add requires hicolor-icon-theme (rfbz#4191)
- Add mime scriptlets

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.6.3-2
- Rebuilt for ffmpeg-3.1.1

* Sat Jul 09 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.6.3-1
- update to 1.6.3 release
- patch for ffmpeg-3.0
- switch to qt5
- add exclude armhfp

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 1.4.4-6
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.4.4-5
- Rebuilt for FFmpeg 2.4.x

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 1.4.4-4
- Rebuilt for ffmpeg-2.3

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 1.4.4-3
- Rebuilt for ffmpeg-2.3

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 1.4.4-2
- Rebuilt for ffmpeg-2.2

* Wed Nov 27 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.4-1
- New version

* Wed Oct 02 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.4.2-4
- Rebuilt

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.4.2-3
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.4.2-2
- Rebuilt for x264/FFmpeg

* Thu May 23 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.2-1
- New version
- Workarounded FTBFS due to glew fedora bug rhbz#966649
  Resolves: rfbz#2774

* Sun Apr 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.4.1-3
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.4.1-2
- Rebuilt for FFmpeg 1.0

* Thu Oct 18 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.1-1
- New version
- Dropped ld-fix patch (upstreamed)
- Dropped unbundle-icons patch (not needed)

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.1-4
- Rebuilt for FFmpeg

* Thu Mar  1 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2.1-3
- Unbundled oxygen icons

* Thu Mar 01 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2.1-2
- Used RPM macros instead of variables
- Added requires for post and preun sections
- Removed pkg dir in prep
- Added LGPLv3+ license to license tag (oxygen icons)

* Wed Nov 09 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2.1-1
- New version

* Tue Nov 01 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.3-3
- Explicit link with glew, needed if compiled with Equalizer

* Wed Sep 14 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.3-2
- Removed defattr
- Moved docs to one dir

* Sat Aug 20 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.3-1
- Update to new version

* Sat Aug 20 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-1
- Update to new version

* Sat Aug 20 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.2-1
- Initial release
