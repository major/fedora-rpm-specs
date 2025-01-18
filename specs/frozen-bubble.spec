%global _hardened_build 1

Summary: Frozen Bubble arcade game
Name: frozen-bubble
Version: 2.2.1
Release: 0.50.beta1%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://www.frozen-bubble.org/
Source0: http://www.frozen-bubble.org/data/frozen-bubble-%{version}-beta1.tar.bz2
Source1: frozen-bubble.desktop
Source2: fb-server.service
Patch0:  frozen-bubble-2.2.1-setuid.patch
Patch1:  0001-Fix-buffer-size-when-formatting-current-date.patch
Patch2:  frozen-bubble-2.2.1-Use-true-number-instead-of-quoted-version-number.patch
BuildRequires: /usr/bin/appstream-util
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(Alien::SDL) >= 1.413
BuildRequires: perl(autodie)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(IO::File)
BuildRequires: perl(IPC::System::Simple)
BuildRequires: perl(lib)
BuildRequires: perl(Locale::Maketext::Extract)
BuildRequires: perl(Module::Build) >= 0.36
BuildRequires: perl(parent)
BuildRequires: perl(SDL) >= 2.511
BuildRequires: perl(Test::More)
BuildRequires: SDL_mixer-devel
BuildRequires: SDL_Pango-devel
Requires:      perl(SDL) >= 2.511
Requires:      perl(Alien::SDL) >= 1.413
Requires:      hicolor-icon-theme

%{?perl_default_filter}

%description
Full-featured, colorful animated penguin eye-candy, 100 levels of 1p game, hours
and hours of 2p game, 3 professional quality 20-channels musics, 15 stereo
sound effects, 7 unique graphical transition effects and a level editor.
You need this game.


%package server
Summary: Frozen Bubble network game dedicated server
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd

%description server
Frozen Bubble network game dedicated server. The server is already included
with the game in order to be launched automatically for LAN games, so you
only need to install this package if you want to run a fully dedicated
Frozen Bubble network game server.


%prep
%autosetup -p1 -n %{name}-%{version}-beta1
# Rename this README since the main server README has the same name
%{__mv} server/init/README server/README.init
# Change the example server configuration file to be a working one, which only
# launches a LAN server and doesn't try to register itself on the Internet
%{__sed} -ie "s#^a .*#z\nq\nL#" server/init/fb-server.conf


%build
export LDFLAGS="%{?__global_ldflags}"
export CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
sed -i "s|'-Wl,-rpath,/usr/.*',||" _build/build_params
./Build


%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
#%%find_lang %%{name}

# Clean up unneeded files
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

# Desktop file
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}

# Icons
%{__install} -D -p -m 0644 share/icons/frozen-bubble-icon-16x16.png \
    %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{__install} -D -p -m 0644 share/icons/frozen-bubble-icon-32x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{__install} -D -p -m 0644 share/icons/frozen-bubble-icon-48x48.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{__install} -D -p -m 0644 share/icons/frozen-bubble-icon-64x64.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Install server init script and default configuration
%{__install} -D -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_unitdir}/fb-server.service
%{__install} -D -p -m 0644 server/init/fb-server.conf \
    %{buildroot}%{_sysconfdir}/fb-server.conf

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: contact2@frozen-bubble.org
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">frozen-bubble.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>An addictive game about frozen bubbles</summary>
  <description>
    <p>
      Frozen Bubble is a free and open source game in which you throw colorful
      bubbles and build groups to destroy them.
    </p>
    <p>
      You can play this game locally or over the Internet.
      It also contains a level editor for you to create your own games.
    </p>
  </description>
  <url type="homepage">http://www.frozen-bubble.org/</url>
  <screenshots>
    <screenshot type="default">https://upload.wikimedia.org/wikipedia/commons/d/d6/Frozen-bubble.jpg</screenshot>
    <screenshot>http://www.frozen-bubble.org/data/fb2-5p.png</screenshot>
  </screenshots>
  <update_contact>contact2_at_frozen-bubble.org</update_contact>
</application>
EOF

%check
./Build test
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/frozen-bubble.appdata.xml



%post server
/usr/sbin/useradd -r -s /sbin/nologin -d %{_datadir}/%{name} fbubble \
    &>/dev/null || :
%systemd_post fb-server.service

%preun server
%systemd_preun fb-server.service

%postun server
%systemd_postun_with_restart fb-server.service


%files
%doc AUTHORS Changes HISTORY README
%license COPYING
%{_bindir}/%{name}*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Games/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man3/*.3pm*

%files server
%doc server/AUTHORS server/README*
%license COPYING
%config(noreplace) %{_sysconfdir}/fb-server.conf
%{_unitdir}/fb-server.service
%{_bindir}/fb-server


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.50.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.1-0.49.beta1
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.48.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.47.beta1
- Perl 5.40 rebuild

* Mon May 06 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.46.beta1
- Using a quoted version number in a version check instead of a true number
  is error since perl 5.39.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.45.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.44.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.43.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.42.beta1
- Perl 5.38 rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.41.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.40.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.39.beta1
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.38.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.37.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.36.beta1
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.1-0.35.beta1
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Sun Feb 21 2021 René Genz <liebundartig@freenet.de> - 2.2.1-0.34.beta1
- fix AppData screenshots and update_contact

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.33.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.32.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.31.beta1
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.30.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.29.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.28.beta1
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.27.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.26.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.25.beta1
- Perl 5.28 rebuild

* Thu Feb 08 2018 Hans de Goede <hdegoede@redhat.com> - 2.2.1-0.24.beta1
- Fix FTBFS (patch from Petr Písař) (rhbz#1541359)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.23.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.1-0.22.beta1
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.21.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 2.2.1-0.20.beta1
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.19.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Petr Pisar <ppisar@redhat.com> - 2.2.1-0.18.beta1
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.17.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.16.beta1
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-0.15.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 David King <amigadave@amigadave.com> - 2.2.1-0.14.beta1
- Use license macro for COPYING
- Validate AppData during check
- Update man pages glob in files section
- Update systemd scriptlet usage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-0.13.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.12.beta1
- Perl 5.22 rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.2.1-0.11.beta1
- Add an AppData file for the software center

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.10.beta1
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-0.9.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-0.8.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-0.7.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 2.2.1-0.6.beta1
- Perl 5.18 rebuild

* Fri May 17 2013 Hans de Goede <hdegoede@redhat.com> - 2.2.1-0.5.beta1
- Fix hardened build (rhbz#955273)
- Remove rpath

* Wed Mar  6 2013 Hans de Goede <hdegoede@redhat.com> - 2.2.1-0.4.beta1
- Fix FTBFS (rhbz#914013)
- Use new systemd macros for scripts (rhbz#850120)
- Drop sysv -> systemd conversion scripts

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 04 2012 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-0.1.beta1
- Updated to 2.2.1-beta1

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.2.0-13
- Perl 5.16 rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.0-12
- Add hardened build.

* Wed Mar 14 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.0-11
- Migrate to systemd, BZ 767621.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.2.0-9
- Perl mass rebuild
- change perl-SDL to correct perl(SDL)

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.2.0-8
- Perl 5.14 mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.2.0-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.2.0-5
- rebuild against perl 5.10.1

* Tue Dec  1 2009 Hans de Goede <hdegoede@redhat.com> 2.2.0-4
- Do not remove server user (#542423), per:
  http://fedoraproject.org/wiki/Packaging/UsersAndGroups

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Nils Philippsen <nils@redhat.com> 2.2.0-1
- Update to 2.2.0 (#479431)

* Sun Jul  6 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.1.0-9
- Fix audio on bigendian archs (bz 454109), patch by Ian Chapman

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.0-8
- rebuild for new perl (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.0-7
- Autorebuild for GCC 4.3

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.0-6
- rebuild for new perl

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 2.1.0-5
- Rebuild for new BuildID feature.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 2.1.0-4
- Update License field.

* Fri Jun 22 2007 Matthias Saou <http://freshrpms.net/> 2.1.0-3
- Fix build with perl-devel split (ExtUtils/MakeMaker.pm build requirement).
- Cosmetic changes to the spec file.
- Change fbubble user's home from / to %%{_datadir}/%%{name}.
- Remove the desktop file's "fedora" prefix.
- Remove executable bit from the man pages.

* Wed Nov 29 2006 Matthias Saou <http://freshrpms.net/> 2.1.0-2
- Silence useradd call so there is no output upon update (#217902).

* Wed Nov 29 2006 Matthias Saou <http://freshrpms.net/> 2.1.0-1
- Update to 2.1.0 (fixes #216248).

* Fri Oct 27 2006 Matthias Saou <http://freshrpms.net/> 2.0.0-1
- Update to 2.0.0.
- Add new SDL_Pango dependency.
- New server standalone sub-package for the dedicated server.

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.0-10
- FE6 Rebuild

* Wed Aug 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.0-9
- Filter out the autogenerated Provides for our private perl modules and also
  filter out the matching AutoRequires to still get an installable package

* Sun Aug 20 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.0-8
- Apply patch from Wart (wart@kobold.org) to move private perl stuff to
  %%{_libdir}/%%{_name}
- Drop unnescesarry perl BR (already implied by perl-SDL).
- Fix inconsistent use of $RPM_BUILD_ROOT vs ${RPM_BUILD_ROOT} (only use the
  former)

* Tue Aug 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.0-7
- Update to work with new perl-SDL-2.1.3 see BZ 202437

* Mon Aug 14 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.0-6
- Submit to Fedora Extras since perl-SDL is in FE now, so frozen-bubble can
  move to FE too
- Cleanup BR's a bit to match FE-guidelines
- Install all sizes icons into /usr/share/icons, instead of just the biggest
  one into /usr/share/pixmaps
- Add scriptlets to update icon cache

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Tue Nov 16 2004 Thorsten Leemmhuis <fedora [AT] leemhuis [DOT] info> - 0:1.0.0-0.lvn.5
- Update to new Debian patch

* Sat Jul  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0.0-0.lvn.4
- Apply patch from Debian to make fb work with perl-SDL >= 1.20.3.
- Install Perl modules into vendor install dirs, require (:MODULE_COMPAT_*).
- Fix Source0 URL.
- Remove unneeded files.
- Fix file permissions.
- s/fedora/livna/ in desktop entry, other small improvements.

* Fri Jun 27 2003 Phillip Compton <pcompton at proteinmedia dot com> 0:1.0.0-0.fdr.3
- Removed BuildConflicts.
- Added Epochs to BuildReqs.
- Split Desktop entry into seperate file.

* Sun Jun 22 2003 Phillip Compton <pcompton at proteinmedia dot com> 0:1.0.0-0.fdr.2
- Fixed file permissions.
- Added in suggested fixes from Adrian Reber.

* Tue May 27 2003 Phillip Compton <pcompton at proteinmedia dot com> 0:1.0.0-0.fdr.1
- Fedorafied.

* Tue Apr  1 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Replace the __find_requires with AutoReq: as it works better.
- Remove .xvpics from installed files.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.

* Tue Feb 18 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added missing man pages, thanke to Michal Ambroz.

* Mon Feb 17 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0.0.

* Mon Oct 28 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0 (at last!).
- New menu entry.

* Thu Feb  7 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.3.

* Thu Feb  7 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Spec file modifications for a Red Hat Linux release.

* Wed Feb  6 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.9.1-1mdk
- first mdk rpm

