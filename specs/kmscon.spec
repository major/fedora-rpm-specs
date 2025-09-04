Name:           kmscon
Version:        9.1.0
Release:        1%{?dist}
Summary:        Linux KMS/DRM based virtual Console Emulator
License:        MIT
URL:            https://github.com/Aetf/kmscon/
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  check-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  libtsm-devel >= 4.1.0
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  xsltproc
BuildRequires:  xz
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev) >= 172
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0

%description
Kmscon is a simple terminal emulator based on linux kernel mode setting (KMS).
It is an attempt to replace the in-kernel VT implementation with a userspace
console.


%prep
%autosetup -p1

%conf
%meson

%build
%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_post kmscon.service
%systemd_post kmsconvt@.service

%preun
%systemd_preun kmscon.service
%systemd_preun kmsconvt@.service

%postun
%systemd_postun_with_reload kmscon.service
%systemd_postun_with_reload kmsconvt@.service

%files
%license COPYING
%{_bindir}/%{name}
%{_libdir}/kmscon/
%dir %{_libexecdir}/kmscon
%{_libexecdir}/kmscon/kmscon
%{_mandir}/man1/kmscon.1*
%{_unitdir}/kmscon.service
%{_unitdir}/kmsconvt@.service

%changelog
* Tue Aug 12 2025 Jocelyn Falempe <jfalempe@redhat.com>
- Remove selinux rules, as they are now part of the global policies.
- Add systemd scriptlets

* Fri Jul 4 2025  Jocelyn Falempe <jfalempe@redhat.com> - 9.1.0
- Bump version to 9.1.0

* Fri May 16 2025 Jocelyn Falempe <jfalempe@redhat.com> - 9.0.0^4.gitf4d9b6bb-0
- Bump to commit f4d9b6bb, with fix for keyboard layout, unifont, and selinux.

* Thu Apr 17 2025 Jocelyn Falempe <jfalempe@redhat.com> - 9.0.0^3.gita81941f4-1
- Add selinux policies

* Thu Jan 9 2025 Jocelyn Falempe <jfalempe@redhat.com> - 9.0.0^3.gita81941f4-0
- Fix kmscon not restarting the login shell

* Tue Dec 24 2024 Jocelyn Falempe <jfalempe@redhat.com> - 9.0.0^2.git76b6c96b-1
- Fix a segfault in bind_display()

* Fri Dec 20 2024 Jocelyn Falempe <jfalempe@redhat.com> - 9.0.0^2.git76b6c96b-0
- Update to the upstream develop branch, and remove the patch that is merged upstream

* Fri Dec 13 2024 Jocelyn Falempe <jfalempe@redhat.com> - 9.0.0^1.git0f73dc37-0
- Update to the upstream develop branch, which hasn't seen a release yet.

* Sun Jun 09 2024 Michael Bryant <shadow53@shadow53.com> - 9.0.0-0
- Update to 9.0.0

* Mon Aug 29 2022 Jan Engelhardt <jengelh@inai.de>
- Update to release 9.0.0
  * uxkb: add Compose (dead-key) support
  * Add --xkb-compose-file option
  * Custom palette support
- Delete kmscon-x-linking.patch (obsolete)
- Add 0001-Use-correct-systemd-system-unit-directory.patch

* Sun Jan 19 2020 Michael Bryant <shadow53@shadow53.com> - 8.1-1
- Fix dependencies

* Sun Jan 19 2020 Michael Bryant <shadow53@shadow53.com> - 8-11
- Update upstream to Aetf's fork (master)

* Thu Mar  7 2019 Fabian Vogt <fvogt@suse.com>
- Update to git 01dd0a2:
  * build: update systemd dependency
  * Update helper script to point to correct location of the binary
  * Fix file conflict during instal
  * Initial support for 24bit fbdev
  * Use a startup script to get default XKB settings from localed

* Wed Jul 18 2018 Fabian Vogt <fvogt@suse.com>
- Switch to https://github.com/Aetf/kmscon:
  * text: font: implement underlines
  * Use background color rather than hardcoded black color to fill margin
  * drm3d: fix coordinate in uterm_display_fill, finally fixed margin color issue
  * pty: remove deprecated signal constant SIGUNUSED
  * build: fix compiler warnings
  * text: font: implement italics
  * font: fix caching issues
  * Missing check for underlines in kmscon_font_attr_match
- Only build the drm2d backend

* Sat Jul 11 2015 Nicolas Chauvet <kwizart@gmail.com> - 8-10
- Remove prelink workaround of glibc#16744

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug  3 2014 Jan Engelhardt <jengelh@inai.de>
- Update to new upstream release 8
  * wlterm and libuvt were removed (in a separate package now)
  * The freetype2 font backend and cairo text renderer were removed
  * Dynamic font resizing is now supported.
  Use Ctrl-Plus and Ctrl-Minus for this.

* Tue Jun 10 2014 Peter Robinson <pbrobinson@fedoraproject.org> 8-7
- ifnarch the execstack calls not just the build dependencies

* Sun Jun  8 2014 Peter Robinson <pbrobinson@fedoraproject.org> 8-6
- No prelink on aarch64/ppc64le

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Nicolas Chauvet <kwizart@gmail.com> - 8-4
- Clear execstack
- Add verbose check and fix description

* Fri Mar 07 2014 Nicolas Chauvet <kwizart@gmail.com> - 8-3
- Add man page
- Spec file clean-up
- Enable pixman as a renderer

* Thu Feb 27 2014 Nicolas Chauvet <kwizart@gmail.com> - 8-2
- Update to libxslt libgbm

* Thu Feb 27 2014 Nicolas Chauvet <kwizart@gmail.com> - 8-1
- Initial spec file

* Wed Oct  9 2013 Cristian Rodríguez <crrodriguez@opensuse.org>
- version 7+git52
- Corrects systemd units so they work correctly with current
  versions
- add uvtd new Virtual Terminal daemon, disabled by default
  in upstream and here as well.
- bugfixes
- Use scanelf to remove executable stack from mod_unifont
  while the problem is fixed at its roots.

* Mon Apr 22 2013 Dominique Leuenberger <dimstar@opensuse.org>
- Add kmscon-x-linking.patch: Fix inclusion of xkbcommon: this all
  used wrongly to be pulled in by SDL. kmscon though does include
  the xkbcommon headers on its own and as such must take care of
  finding them appropriately.

* Sat Mar  2 2013 Jan Engelhardt <jengelh@inai.de>
- Updated to version 7
  * TSM, font and text subsystems were extended for multi-width fonts,
  which allows using CJK characters if the glyphs are available
  * The environment variable COLORTERM is set to kmscon
  * /bin/login is called with -p
  * The Freetype2 backend is now deprecated. Use the built-in 8x16,
  unifont or pango backends.
- Merge -service package into (main)
- Build and ship manpage

* Sat Feb  9 2013 Cristian Rodríguez <crrodriguez@opensuse.org>
- install kmsconvt@.service too

* Sat Feb  9 2013 Jan Engelhardt <jengelh@inai.de>
- Do not mark service file as %%config
- Set RPM group for library packages
- Use more robust make install call

* Sat Feb  9 2013 Cristian Rodríguez <crrodriguez@opensuse.org>
- Update to 6.git110
  * Allow arbitrary paths with --vt (kmscon)
  * xkbcommon is now mandatory. We need it to handle keyboard input
  properly and since xkbcommon-0.2.0 is released, there is no
  reason to not depend on it.
  We also removed the plain-input backend with this change.
  * Snap window to console/font-size on resize (wlterm)
  * Adjust to new libwayland-1.0 (wlterm)
  * Many new command-line options for wlterm including --term,
  - -login, --palette, --sb-size and many --grab-* options.
  * fake-VTs no longer react on SIGUSR1/2. This was always broken and
  now removed.
  * --switchvt works again and is now enabled by default.
  * --xkb-model was introduced. The other --xkb-<rmlvo> options also
  use system-defaults instead of us-keymap as default value now.
  * wlterm works properly in maximized and fullscreen mode now
  * key-presses are now properly marked as "handled" so it is no
  longer
  possible for two subsystems to handle the same key-press.
  * wlterm can now zoom the font size with ctrl+Plus/Minus
  * TSM now supports screen selections. wlterm is hooked up with this
  and supports this, too. However, the VTE layer has not seen this
  yet so everything is computed in the terminal for now. Next
  kmscon release will include client-side mouse-protocol support.
  * Copy/Paste now works with wlterm
  * Key-repeat has been reworked and now allows adjusting repeat and
  delay times.
  * Session support allows for multiple terminals (sessions) inside
  of each seat. You can switch between the sessions, kill them and
  create new terminals via keyboard shortcuts. Also several other
  sessions than terminal sessions were introduced. However, all of
  them are experimental and shouldn't be used.
  * TSM now supports alternate screen buffers. They're enabled by
  default.
  * Configuration handling has been reworked. Multiple config-files
  can now be parsed and each seat has its own configuration file in
  /etc/kmscon/<seat>.seat.conf.
  * The build-tools have been reworked. They should now work properly
  with any option-combination imaginable.
  * --login option can now be used in config-files.
  * We print hints if keyboard-shortcut names are written with wrong
  capitalization.
  * Improve systemd integration
  * CDev sessions emulate enough of the VT API to make X-Server run
  as kmscon session. You can even run kmscon in default-mode as
  client in another kmscon manager.
  * Bold fonts are now supported.
  * kmscon.1 manpage is available now.
  * ... and a lot of bugfixes

* Mon Dec 10 2012 Dominique Leuenberger <dimstar@opensuse.org>
- Do not buildrequier systemd: pkgconfig(systemd-login) is
  perfectly sufficient.

* Thu Oct 25 2012 Jan Engelhardt <jengelh@inai.de>
- Kill _service and instate actual version number
  for used commit kmscon-5-153-g8b30e6c

* Wed Oct 24 2012 Adam Mizerski <adam@mizerski.pl>
- enabled wlterm

* Wed Oct 24 2012 Adam Mizerski <adam@mizerski.pl>
- update to 5.git

* Sat Sep 15 2012 Adam Mizerski <adam@mizerski.pl>
- new package
