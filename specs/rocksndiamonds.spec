Name:		rocksndiamonds
Version:	4.3.2.0
Release:	9%{?dist}
License:	GPL-1.0-or-later
Summary:	Underground digging game
URL:		http://www.artsoft.org/rocksndiamonds/
# We no longer have legal issues with the bundled copy of libsmpeg2, but we don't use it either
# so we just delete it along with the other prebuilt libs in prep
Source0:	https://www.artsoft.org/RELEASES/linux/rocksndiamonds/rocksndiamonds-%{version}.tar.gz
Source1:	rocksndiamonds.desktop
Source2:	rocksndiamonds.png
# Additional music files we have permission for!
Source3:	rocksndiamonds-distributable-music.tar.bz2
Patch3:		rocksndiamonds-4.3.2.0-music-info-url.patch
Patch4:		rocksndiamonds-4.0.0.1-CVE-2011-4606.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	SDL2-devel, libX11-devel, desktop-file-utils, xorg-x11-proto-devel
BuildRequires:	SDL2_image-devel, SDL2_mixer-devel, SDL2_net-devel, zlib-devel
Requires:	libmodplug%{_isa}

%description
Dig for treasure and solve puzzles underground, but watch out for falling
rocks and strange creatures!

%prep
%setup -q -a 3
%patch -P3 -p1 -b .url
%patch -P4 -p1

# Stawp!
rm -rf lib/*

%build
make %{?_smp_mflags} BASE_PATH=%{_datadir}/%{name}/ RW_GAME_DIR=%{_localstatedir}/games/%{name}/ EXTRA_CFLAGS="$RPM_OPT_FLAGS -DUSE_USERDATADIR_FOR_COMMONDATA"

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/games/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0755 rocksndiamonds $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/scores
for i in graphics levels music sounds; do
	cp -a $i $RPM_BUILD_ROOT%{_datadir}/%{name}/
done
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

# Get rid of unnecessary patch files.
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/levels/Tutorials/*/*.orig $RPM_BUILD_ROOT%{_datadir}/%{name}/levels/Tutorials/*/tapes/*.orig

desktop-file-install 				\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications	\
  --mode 0644					\
  %{SOURCE1}

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
<!-- Copyright 2014 Your Name <email@address.com> -->
<!--
BugReportURL: waiting for admin approval to post
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">rocksndiamonds.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Gem collecting puzzle game</summary>
  <description>
    <p>
      Rocks 'n' Diamonds is a action puzzle game where you have to navigate a maze
      of dirt, rocks, enemies and quicksand, while collecting gems and making it
      safely to the exit.
      Be careful not to get crushed by falling rocks or killed by an enemy.
    </p>
  </description>
  <url type="homepage">http://www.artsoft.org/rocksndiamonds/</url>
  <screenshots>
    <screenshot type="default">http://www.artsoft.org/rocksndiamonds/screenshots/emeraldmine.gif</screenshot>
  </screenshots>
</application>
EOF

%files
%license COPYING
%doc ChangeLog COPYING CREDITS INSTALL
%doc docs/elements/
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_localstatedir}/games/%{name}/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun  17 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3.2.0-7
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 26 2022 Tom Callaway <spot@fedoraproject.org> - 4.3.2.0-1
- update to 4.3.2.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 2021 Tom Callaway <spot@fedoraproject.org> - 4.2.3.1-1
- update to 4.2.3.1

* Tue Feb 23 2021 Tom Callaway <spot@fedoraproject.org> - 4.2.3.0-1
- update to 4.2.3.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Tom Callaway <spot@fedoraproject.org> - 4.2.2.1-1
- update to 4.2.2.1

* Mon Dec 14 2020 Tom Callaway <spot@fedoraproject.org> - 4.2.1.0-1
- update to 4.2.1.0

* Thu Dec 10 2020 Tom Callaway <spot@fedoraproject.org> - 4.2.0.5-1
- update to 4.2.0.5

* Thu Nov 12 2020 Tom Callaway <spot@fedoraproject.org> - 4.2.0.4-1
- update to 4.2.0.4

* Tue Oct  6 2020 Tom Callaway <spot@fedoraproject.org> - 4.2.0.3-1
- update to 4.2.0.3

* Mon Sep 14 2020 Tom Callaway <spot@fedoraproject.org> - 4.2.0.2-1
- update to 4.2.0.2

* Mon Aug 24 2020 Tom Callaway <spot@fedoraproject.org> - 4.2.0.1-1
- update to 4.2.0.1

* Mon Aug 17 2020 Tom Callaway <spot@fedoraproject.org> - 4.2.0.0-1
- update to 4.2.0.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Tom Callaway <spot@fedoraproject.org> - 4.1.4.1-3
- fix FTBFS

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Tom Callaway <spot@fedoraproject.org> - 4.1.4.1-1
- update to 4.1.4.1

* Mon Jan  6 2020 Tom Callaway <spot@fedoraproject.org> - 4.1.4.0-1
- update to 4.1.4.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Tom Callaway <spot@fedoraproject.org> - 4.1.0.0-1
- update to 4.1.0.0

* Mon Mar 19 2018 Tom Callaway <spot@fedoraproject.org> - 4.0.1.4-1
- update to 4.0.1.4

* Thu Feb  8 2018 Tom Callaway <spot@fedoraproject.org> - 4.0.1.1-1
- update to 4.0.1.1

* Sun Oct 29 2017 Tom Callaway <spot@fedoraproject.org> - 4.0.1.0-1
- update to 4.0.1.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Tom Callaway <spot@fedoraproject.org> - 4.0.0.2-1
- update to 4.0.0.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb  2 2016 Tom Callaway <spot@fedoraproject.org> - 3.3.1.2-1
- update to 3.3.1.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.3.0.1-12
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 3.3.0.1-8
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Tom Callaway <spot@fedoraproject.org> - 3.3.0.1-5
- apply fix for user configuration/cache directory permission issue (CVE-2011-4606, bz766805)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 02 2011 Tom Callaway <spot@fedoraproject.org> - 3.3.0.1-3
- drop unnecessary .orig files (bz597737)
- clean up spec file

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  8 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3.0.1-1
- 3.3.0.1 (upstream finally dropped bad music files!)

* Tue Sep 22 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2.6.1-1
- update to 3.2.6.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.2.6.0-2
- fix desktop file (bz 485365)

* Wed Feb 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 3.2.4-1
- update to 3.2.4
- keep music in their own tarball

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.2.3-3.2
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 3.2.3-2.2
- license fix

* Tue Aug 14 2007 Tom "spot" Callaway <tcallawa@redhat.com> 3.2.3-2
- use clean tarball
- patch in support for displaying url on music info page

* Thu Jan 18 2007 Tom "spot" Callaway <tcallawa@redhat.com> 3.2.3-1
- bump to 3.2.3

* Tue Nov 21 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.2.2-4
- actually cvs add the devel patches

* Tue Nov 21 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.2.2-3
- add patches from bz 210767

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.2.2-1
- bump to 3.2.2

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.1.2-1
- bump to 3.1.2

* Thu Sep 22 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.1.1-2
- add missing BR: SDL_net-devel

* Thu Sep 22 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.1.1-1
- initial package for Fedora Extras
