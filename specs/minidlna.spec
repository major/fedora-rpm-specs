Name:           minidlna
Version:        1.3.3
Release:        10%{?dist}
Summary:        Lightweight DLNA/UPnP-AV server targeted at embedded systems

# see minidlna-licensing-breakdown.txt for complete breakdown
License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later
URL:            http://sourceforge.net/projects/minidlna/
Source0:        http://downloads.sourceforge.net/%{name}/%{version}/%{name}-%{version}.tar.gz
# Systemd unit file
Source1:        %{name}.service
# tmpfiles configuration for the /run directory
Source2:        %{name}-tmpfiles.conf
Source3:        %{name}-licensing-breakdown.txt
Source4:        %{name}.logrotate
Source5:        %{name}.sysusers
# Fix core dump
# https://sourceforge.net/p/minidlna/bugs/333/
Patch0:         %{name}-1.3.0-select_use_after_free.patch
# Add compatibility with FFMPEG 7.0
# https://sourceforge.net/p/minidlna/git/merge-requests/58/
Patch1:         0001-Add-compatibility-with-FFMPEG-7.0.patch

BuildRequires:  avahi-devel
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libexif-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libuuid-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
Recommends:     logrotate
Requires(pre):  shadow-utils
%{?systemd_requires}

%description
MiniDLNA (aka ReadyDLNA) is server software with the aim of being fully
compliant with DLNA/UPnP-AV clients.

The minidlna daemon serves media files (music, pictures, and video) to clients
on your local network.  Example clients include applications such as Totem and
XBMC, and devices such as portable media players, smartphones, and televisions.


%prep
%autosetup -p1

# Edit the default config file
sed -i 's|#log_dir=/var/log|#log_dir=/var/log/minidlna|' \
  %{name}.conf


%build
%configure \
  --disable-silent-rules \
  --with-db-path=%{_localstatedir}/cache/%{name} \
  --with-log-path=%{_localstatedir}/log/%{name} \
  --enable-tivo

%make_build


%install
%make_install

# Install config file
mkdir -p %{buildroot}%{_sysconfdir}/
install -p -m 644 minidlna.conf %{buildroot}%{_sysconfdir}/

# Install systemd unit file
mkdir -p %{buildroot}%{_unitdir}/
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/

# Install man pages
mkdir -p %{buildroot}%{_mandir}/man5/
install -p -m 644 minidlna.conf.5 %{buildroot}%{_mandir}/man5/
mkdir -p %{buildroot}%{_mandir}/man8/
install -p -m 644 minidlnad.8 %{buildroot}%{_mandir}/man8/

# Install sysusers.d configuration
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/%{name}.conf

# Install tmpfiles configuration
mkdir -p %{buildroot}%{_tmpfilesdir}/
install -p -m 644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}/run/
install -d -m 755 %{buildroot}/run/%{name}/

# Install logrotate configuration
mkdir -p %{buildroot}/etc/logrotate.d
install -p -m 644 %{SOURCE4} %{buildroot}/etc/logrotate.d/minidlna

# Create cache and log directories
mkdir -p %{buildroot}%{_localstatedir}/cache/
install -d -m 755 %{buildroot}%{_localstatedir}/cache/%{name}/
mkdir -p %{buildroot}%{_localstatedir}/log/
install -d -m 755 %{buildroot}%{_localstatedir}/log/%{name}/

%find_lang %{name}


%pre
%sysusers_create_compat %{SOURCE5}


%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files -f %{name}.lang
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(-,minidlna,minidlna) %config(noreplace) %{_sysconfdir}/minidlna.conf
%{_sbindir}/minidlnad
%{_unitdir}/minidlna.service
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/minidlnad.8*
%dir %attr(-,minidlna,minidlna) /run/%{name}/
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%dir %attr(-,minidlna,minidlna) %{_localstatedir}/cache/%{name}/
%dir %attr(-,minidlna,minidlna) %{_localstatedir}/log/%{name}/
%license COPYING LICENCE.miniupnpd
%doc AUTHORS NEWS README TODO


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 22 2024 Dominik Mierzejewski <dominik@greysector.net> - 1.3.3-9
- rebuilt for FFmpeg 7

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 04 2024 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.3-7
- Add patch for FFMPEG 7 compatibility

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.3.3-3
- drop broken patch

* Wed Jul 05 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.3.3-2
- fix missing-call-to-setgroups-before-setuid rpmlint error
- add weak dependency on logrotate

* Tue Jul 04 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.3.3-1
- update to 1.3.3

* Wed Mar 29 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.3.2-5
- use sysusers.d to pre-create system user account
- make the sed expression easier to read
- adjust description

* Tue Feb 28 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.3.2-4
- call tmpfiles_create macro to create /run/minidlna after installation
- add logrotate config drop-in based on Debian

* Wed Feb 15 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.3.2-3
- add missing GPLv2 only to license field
- add licensing breakdown

* Wed Feb 08 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.3.2-2
- sort BRs alphabetically
- limit build dependencies to only those strictly required
- update license field with SPDX identifiers

* Thu Sep 01 2022 Andrea Musuruane <musuruan@gmail.com> - 1.3.2-1
- Updated to new upstream release

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Leigh Scott <leigh123linux@gmail.com> - 1.3.0-6
- Rebuilt for new ffmpeg snapshot

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 20 2021 Andrea Musuruane <musuruan@gmail.com> - 1.3.0-4
- Fix core dump (BZ #5938)
- Fix leaked sockets by correctly initialising the ev struct

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 1.3.0-2
- Rebuilt for new ffmpeg snapshot

* Wed Dec  9 11:29:39 CET 2020 Andrea Musuruane <musuruan@gmail.com> - 1.3.0-1
- Updated to new upstream release

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.2.1-11
- Rebuild for ffmpeg-4.3 git

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 1.2.1-9
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-6
- Rebuild for ffmpeg-4.0 release

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.2.1-5
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-3
- Rebuilt for ffmpeg-3.5 git

* Mon Oct 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-2
- Rebuild for ffmpeg update

* Thu Sep 21 2017 Andrea Musuruane <musuruan@gmail.com> - 1.2.1-1
- Updated to upstream 1.2.1

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Andrea Musuruane <musuruan@gmail.com> - 1.2.0-2
- Fixed systemd service unit configuration (#4517)
- Updated systemd snippets
- Preserve timestamps
- Dropped obsolete Group tag

* Fri Jun 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-1
- Updated to upstream 1.2.0
- Add build requires avahi-devel

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.1.5-5
- Rebuild for ffmpeg update

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.1.5-3
- Patch for libavformat-57 compatibility

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.1.5-2
- Rebuilt for ffmpeg-3.1.1

* Sun Oct 04 2015 Andrea Musuruane <musuruan@gmail.com> - 1.1.5-1
- Updated to upstream 1.1.5

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 1.1.4-3
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.1.4-2
- Rebuilt for FFmpeg 2.4.x

* Sat Aug 30 2014 Andrea Musuruane <musuruan@gmail.com> - 1.1.4-1
- Updated to upstream 1.1.4

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 1.1.3-2
- Rebuilt for ffmpeg-2.3

* Sat Jun 07 2014 Andrea Musuruane <musuruan@gmail.com> - 1.1.3-1
- Updated to upstream 1.1.3

* Sat Mar 29 2014 Andrea Musuruane <musuruan@gmail.com> - 1.1.2-2
- Rebuilt for new ffmpeg

* Sat Mar 08 2014 Andrea Musuruane <musuruan@gmail.com> - 1.1.2-1
- Updated to upstream 1.1.2

* Sun Jan 12 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-2
- Rebuilt

* Sun Sep 15 2013 Andrea Musuruane <musuruan@gmail.com> - 1.1.0-1
- Updated to upstream 1.1.0
- Better systemd integration

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.26-3
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.26-2
- Rebuilt for x264/FFmpeg

* Wed May 08 2013 Andrea Musuruane <musuruan@gmail.com> - 1.0.26-1
- Updated to upstream 1.0.26

* Wed Jan 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.25-4
- Rebuilt for ffmpeg

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.25-3
- Rebuilt for FFmpeg 1.0

* Sat Nov 03 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.25-2
- Fixed FTBFS caused by ffmpeg 1.0
- Updated minidlna.service I forgot to commit (BZ #2294)

* Sat Jul 14 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.25-1
- Updated to upstream 1.0.25

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.24-3
- Rebuilt for FFmpeg

* Wed Apr 25 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.24-2
- Run the daemon with the minidlna user (BZ #2294)
- Updated Debian man pages

* Sun Feb 19 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.24-1
- Updated to upstream 1.0.24

* Sat Jan 28 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.23-1
- Updated to upstream 1.0.23

* Sun Jan 22 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.22-2
- Fixed systemd unit file

* Sun Jan 15 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.22-1
- Updated to upstream 1.0.22
- Removed default Fedora RPM features (defattr, BuildRoot, clean section)
- Better consistent macro usage

* Sat Jul 23 2011 Andrea Musuruane <musuruan@gmail.com> 1.0.21-1
- Updated to upstream 1.0.21

* Sat Jun 18 2011 Andrea Musuruane <musuruan@gmail.com> 1.0.20-1
- First release
- Used Debian man pages

