%global forgeurl https://github.com/jeremyevans/aqualung

# We need -fcommon for this to build
%define _legacy_common_support 1

Name:           aqualung
Version:        1.2
Release:        9%{?dist}
Summary:        Music Player for GNU/Linux
License:        GPL-2.0-or-later
URL:            https://aqualung.jeremyevans.net
Source:         %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
Source:         %{name}.desktop
# Add more supported formats to FFmpeg decoder
Patch:          %{forgeurl}/commit/0ecc6721d5078c0bc9cae771d485c8d676443c23.patch
# Add support for recent versions of Monkey's Audio
Patch:          %{forgeurl}/commit/a991c13d0df734a5d0fea7db6b181176858f3e58.patch
# Fix the Monkey's Audio decoder to work with current Monkey's Audio
Patch:          %{forgeurl}/commit/d2c88317b6042a05c236faf3c09f600337c6379e.patch
# Remove now unnecessary glib include in mac decoder
Patch:          %{forgeurl}/commit/1c2a295a72e1e3abc6df40714d9753e311541550.patch
# Add platform define when enabling mac
Patch:          %{forgeurl}/pull/34.patch

# autogen.sh
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  gettext-devel
# GUI
BuildRequires:  atk-devel
BuildRequires:  cairo-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  pango-devel
BuildRequires:  pixman-devel
BuildRequires:  zlib-devel
# Desktop
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
# Output
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(samplerate)
# Encode/Decode
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(oggz)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  libmpcdec-devel
BuildRequires:  mac-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  lame-devel
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(lrdf)
# CD
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  pkgconfig(libcddb)
# Others
BuildRequires:  pkgconfig(libusb)
BuildRequires:  libifp-devel
BuildRequires:  pkgconfig(lua)
BuildRequires:  sed

Requires:       hicolor-icon-theme

%description
Aqualung is an advanced music player originally targeted at the GNU/Linux
operating system. It plays audio CDs, internet radio streams and pod casts as
well as sound files in just about any audio format and has the feature of
inserting no gaps between adjacent tracks.

%prep
%autosetup -p1 -n %{name}-%{version}

# Fix lib64 path
sed -i 's@/usr/lib/@%{_libdir}/@g' src/plugin.c

# Regenerate autotools
./autogen.sh

%build
%configure \
    --without-sndio \
    --with-oss \
    --with-alsa \
    --with-jack \
    --with-pulse \
    --with-src \
    --with-sndfile \
    --with-flac \
    --with-vorbisenc \
    --with-speex \
    --with-mpeg \
    --with-mod \
    --with-mpc \
    --with-mac \
    --with-lavc \
    --with-lame \
    --with-wavpack \
    --with-ladspa \
    --with-cdda \
    --with-cddb \
    --with-ifp \
    --with-lua

%make_build

%install
%make_install

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

for i in 16 24 32 48 64; do
  install -Dpm0644 src/img/icon_${i}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

cat <<EOF > %{name}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
    <id>net.jeremyevans.aqualung</id>
    <name>Aqualung</name>
    <summary>Advanced music player</summary>
    <metadata_license>FSFAP</metadata_license>
    <project_license>GPL-2.0-or-later</project_license>
    <description>
        <p>
            Aqualung is an advanced music player originally targeted at the GNU/Linux
            operating system. It plays audio CDs, internet radio streams and pod casts as
            well as sound files in just about any audio format and has the feature of
            inserting no gaps between adjacent tracks.
        </p>
    </description>
    <launchable type="desktop-id">%{name}.desktop</launchable>
    <provides>
        <binary>aqualung</binary>
    </provides>
    <content_rating type="oars-1.1"/>
    <developer_name>Jeremy Evans</developer_name>
    <releases>
        <release version="%{version}" date="%(date +%F -r %{SOURCE0})" />
    </releases>
    <screenshots>
      <screenshot type="default">
        <caption>Default skin (Music Store builder)</caption>
        <image>https://aqualung.jeremyevans.net/images/default.png</image>
      </screenshot>
      <screenshot>
        <caption>Woody skin (File Info and volume calculation)</caption>
        <image>https://aqualung.jeremyevans.net/images/woody.png</image>
      </screenshot>
      <screenshot>
        <caption>Metal skin (Playlist featuring Album mode)</caption>
        <image>https://aqualung.jeremyevans.net/images/metal.png</image>
      </screenshot>
      <screenshot>
        <caption>Dark skin (LADSPA plugin support)</caption>
        <image>https://aqualung.jeremyevans.net/images/dark.png</image>
      </screenshot>
      <screenshot>
        <caption>Plain skin (Settings dialog and album cover)</caption>
        <image>https://aqualung.jeremyevans.net/images/plain.png</image>
      </screenshot>
      <screenshot>
        <caption>Ocean skin (Search in Music Store)</caption>
        <image>https://aqualung.jeremyevans.net/images/ocean.png</image>
      </screenshot>
    </screenshots>
    <url type="homepage">%{url}</url>
</component>
EOF
install -D -p -m 644 %{name}.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%doc %{_pkgdocdir}/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 1.2-8
- Rebuild for ffmpeg 7

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 05 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 1.2-4
- Unconditionally enable Monkey's Audio support
- Add upstream backports:
  - Add more supported formats to FFmpeg decoder
  - Add support for recent versions of Monkey's Audio
  - Fix the Monkey's Audio decoder to work with current Monkey's Audio
  - Remove now unnecessary glib include in mac decoder
- Backport upstream PR#34 to fix a build issue with Monkey's Audio
- Drop obsolete patches

* Fri Aug 04 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 1.2-3
- Convert license tag to SPDX
- Rework specfile to follow the Fedora packaging guidelines

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 11 2023 Leigh Scott <leigh123linux@gmail.com> - 1.2-1
- Update aqualung to 1.2

* Sun Mar 26 2023 Leigh Scott <leigh123linux@gmail.com> - 1.1-5
- rebuilt

* Wed Feb 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1.1-4
- Rebuild for new flac

* Sat Aug 06 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 16 2022 Sérgio Basto <sergio@serjux.com> - 1.1-2
- Fix 32bit builds and builds on Fedora < 36

* Tue Feb 15 2022 Sérgio Basto <sergio@serjux.com> - 1.1-1
- Update aqualung to 1.1, patches copied from altlinux and use compat-ffmpeg4

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0-0.26.rc1git72c1ab1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Leigh Scott <leigh123linux@gmail.com> - 1.0-0.25.rc1git72c1ab1
- Rebuilt for new ffmpeg snapshot

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0-0.24.rc1git72c1ab1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0-0.23.rc1git72c1ab1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 1.0-0.22.rc1git72c1ab1
- Rebuilt for new ffmpeg snapshot

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0-0.21.rc1git72c1ab1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 Leigh Scott <leigh123linux@gmail.com> - 1.0-0.20.rc1git72c1ab1
- Rebuild for new libcdio version

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0-0.19.rc1git72c1ab1
- Rebuild for ffmpeg-4.3 git

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0-0.18.rc1git72c1ab1
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0-0.17.rc1git72c1ab1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 1.0-0.16.rc1git72c1ab1
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0-0.15.rc1git72c1ab1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0-0.14.rc1git72c1ab1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0-0.13.rc1git72c1ab1
- Rebuilt for new ffmpeg snapshot

* Wed Feb 28 2018 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0-0.12.rc1git72c1ab1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Sérgio Basto <sergio@serjux.com> - 1.0-0.11.rc1git72c1ab1
- Rebuild (libcdio)

* Wed Jan 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0-0.10.rc1git72c1ab1
- Rebuilt for ffmpeg-3.5 git

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0-0.9.rc1git72c1ab1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0-0.8.rc1git72c1ab1
- Rebuild for ffmpeg update

* Sat Mar 18 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0-0.7.rc1git72c1ab1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0-0.6.rc1git72c1ab1
- Update to 1.0-0.6.rc1git72c1ab1

* Thu Nov 17 2016 Adrian Reber <adrian@lisas.de> - 1.0-0.5.rc1git05dfcb7
- Rebuilt for libcdio-0.94

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.0-0.4.rc1git05dfcb7
- Rebuilt for ffmpeg-3.1.1

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.0-0.3.rc1git05dfcb7
- Rebuilt for ffmpeg-3.1.1

* Fri Jul 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0-0.2.rc1git05dfcb7
- Switched from svn to git
- Update to 1.0-0.2.rc1git05dfcb7
- Added %%{_docdir}/%%{name}

* Fri Aug 28 2015 Martin Gansser <martinkg@fedoraproject.org> - 1.0-0.1.svn1311
- Update to SVN r1311

* Mon Mar 02 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.9-0.8.svn1309
- dropped aqualung-fsf-fix.patch

* Sun Mar 01 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.9-0.7.svn1309
- added link to upstream patch %%{name}-fsf-fix.patch
- corrected lincese tag
- Mark license files as %%license where available
- dropped %%defattr does not need any longer
- dropped macro %%{buildroot}
- take ownership of unowned directory %%{_datadir}/%%{name}/
- added pkgconfig based BR

* Sun Mar 01 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.9-0.6.svn1309
- Update to SVN r1309.
- added BR libcdio-paranoia-devel
- dropped unrecognized %%configure options
- added %%{name}-fsf-fix.patch
- corrected license tag

* Tue Feb 2 2010 Akio Idehara <zbe64533 at gmail.com> 0.9-0.5.svn1115
- Disable mac support, this is mac's the license issue

* Mon Feb 1 2010 Akio Idehara <zbe64533 at gmail.com> 0.9-0.4.svn1115
- Add post/postun

* Mon Feb 1 2010 Akio Idehara <zbe64533 at gmail.com> 0.9-0.3.svn1115
- Update to SVN r1115

* Sun Jan 31 2010 Akio Idehara <zbe64533 at gmail.com> 0.9-0.2.svn1109
- Change Socket test routine

* Sat Jan 23 2010 Akio Idehara <zbe64533 at gmail.com> 0.9-0.1.svn1109
- Initial RPM release
