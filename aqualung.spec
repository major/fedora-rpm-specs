# "Monkey's Audio Source Code License Agreement" needs to be vetted
%bcond_with mac

%if 0%{with mac}
%global with_mac  --with-mac
%endif

# We need -fcommon for this to build
%define _legacy_common_support 1

Name:           aqualung
Version:        1.2
Release:        3%{?dist}
Summary:        Music Player for GNU/Linux
License:        GPL-2.0-or-later
URL:            http://aqualung.jeremyevans.net/
Source:         https://github.com/jeremyevans/aqualung/archive/%{version}/%{name}-%{version}.tar.gz
Source:         %{name}.desktop
# Fix MAC decoder build
Patch:          aqualung-ALT-new_mac.patch
# C11 build fixes
Patch:          aqualung-ALT-C11.patch

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
%if %{with mac}
BuildRequires:  pkgconfig(mac)
%endif
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
%if 0%{with mac}
    --with-mac \
%else
    --without-mac \
%endif
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

install -Dpm0644 src/img/icon_48.png \
  %{buildroot}%{_datadir}/pixmaps/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%doc %{_pkgdocdir}/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
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
