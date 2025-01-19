Name:		gtorrentviewer
Version:	0.2b
Release:	56%{?dist}
Summary:	A GTK2-based viewer and editor for BitTorrent meta files
License:	GPL-1.0-or-later
URL:		http://gtorrentviewer.sourceforge.net/
Source0:	http://downloads.sf.net/gtorrentviewer/GTorrentViewer-%{version}.tar.gz
Patch0:		gtorrentviewer-0.2b-desktop.patch
Patch1:		gtorrentviewer-0.2b-dso-linking.patch
Patch2:		GTorrentViewer-0.2b-tracker-details-refresh.patch
Patch3:		gtorrentviewer-0.2b-trackerdetails.patch
Patch4:		GTorrentViewer-0.2b-curl-types.patch
Patch5:		GTorrentViewer-0.2b-format.patch
Patch6:		GTorrentViewer-0.2b-missing-tracker.patch
Patch7:		gtorrentviewer-configure-c99.patch
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	gtk2-devel >= 2.4
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libcurl-devel

# Scriptlets replaced by File Triggers from Fedora 26 onwards
%if 0%{?fedora} < 26 && 0%{?rhel} < 8
Requires(post):	  desktop-file-utils
Requires(postun): desktop-file-utils
%endif

%description
GTorrentViewer gives you the ability to see and modify all the possible
information from .torrent files without having to start downloading, and
the ability to see in real time the current number of seeds and peers on
the torrent, so you will always know the status before starting the
download.

%prep
%setup -q -n GTorrentViewer-%{version}

# Let drag and drop work with URIs as well as files (#206262)
# Also drop ".png" suffix from icon filename, as per Icon Theme spec
%patch -P0

# mainwindow.c requires ceil() from libm (#564928)
%patch -P1 -p1

# Fix crash due to use of uninitialized GValue (#542502, #572806)
%patch -P2 -p1

# Improve tracker support (#674726)
%patch -P3 -p1

# <curl/types.h> went away in curl 7.22.0
%patch -P4 -p1

# Add missing format strings in g_warning() invocations
%patch -P5

# Avoid segfault when dealing with torrent that has no tracker (#1178062)
%patch -P6

# C99 compatibility issues
%patch -P7 -p1

%build
# This package includes its own implementation of SHA1, but with LTO
# on it wants to use openssl's version instead, which we don't link against
# and isn't the same as the local version
%define _lto_cflags %{nil}

%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_datadir}/GTorrentViewer/README
desktop-file-install \
	--vendor "" \
	--add-category X-Fedora \
	--delete-original \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/gtorrentviewer.desktop

# Scriptlets replaced by File Triggers from Fedora 26 onwards
%if 0%{?fedora} < 26 && 0%{?rhel} < 8
%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/gtorrentviewer
%{_datadir}/GTorrentViewer
%{_datadir}/applications/gtorrentviewer.desktop
%{_datadir}/pixmaps/gtorrentviewer.png
%{_datadir}/pixmaps/gtorrentviewer.xpm
%{_mandir}/man1/gtorrentviewer.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul  9 2024 Software Management Team <packaging-team-maint@redhat.com> - 0.2b-54
- Eliminate use of obsolete %%patchN syntax (rhbz#2283636)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Florian Weimer <fweimer@redhat.com> - 0.2b-49
- Port configure to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Paul Howarth <paul@city-fan.org> - 0.2b-45
- Disable LTO due to issues with local SHA1() implementation
- Use %%license unconditionally

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Paul Howarth <paul@city-fan.org> - 0.2b-38
- Specify all explicitly-used build dependencies
- Remove some legacy cruft
  - Drop BuildRoot: and Group: tags
  - Drop explicit %%clean section
  - Drop explicit buildroot cleaning in %%install section
  - Scriptlets replaced by file triggers from Fedora 26 onwards
  - Vendor field in desktop file always empty now

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2b-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2b-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Paul Howarth <paul@city-fan.org> - 0.2b-31
- Avoid segfault when dealing with torrent that has no tracker (#1178062)
- Use %%license where possible
- Drop %%defattr, redundant since rpm 4.4

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2b-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2b-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 21 2013 Paul Howarth <paul@city-fan.org> 0.2b-28
- Add missing format strings in g_warning() invocations

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2b-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Paul Howarth <paul@city-fan.org> 0.2b-26
- Drop vendor prefix from desktop file in Fedora 19 onwards and EL builds
- Drop ".png" suffix from icon filename in desktop file, as per Icon Theme spec

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2b-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan  6 2012 Paul Howarth <paul@city-fan.org> 0.2b-24
- Rebuilt for gcc 4.7

* Fri Nov  4 2011 Paul Howarth <paul@city-fan.org> 0.2b-23
- Don't include no-longer-existing <curl/types.h>
- Nobody else likes macros for commands

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2b-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb  3 2011 Paul Howarth <paul@city-fan.org> 0.2b-21
- Improve tracker support (#674726)

* Fri Jun 25 2010 Paul Howarth <paul@city-fan.org> 0.2b-20
- Fix crash when "Refresh" button in "Tracker Details" tab is pressed
  (#542502, #572806)

* Tue Feb 23 2010 Paul Howarth <paul@city-fan.org> 0.2b-19
- Fix FTBFS due to missing -lm linking for ceil function (#564928)
- Try to maintain timestamps of data files

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.2b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.2b-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Paul Howarth <paul@city-fan.org> 0.2b-16
- Use downloads.sf.net rather than dl.sf.net for source URL

* Thu Feb 14 2008 Paul Howarth <paul@city-fan.org> 0.2b-15
- Rebuild with gcc 4.3.0 for Fedora 9

* Sun Aug 12 2007 Paul Howarth <paul@city-fan.org> 0.2b-14
- Clarify license as GPL (unspecified/any version)
- Update %%post & %%postun to redirect stderr to the bitbucket
- Update desktop file to spec version 1.0

* Tue Oct 31 2006 Paul Howarth <paul@city-fan.org> 0.2b-13
- rebuild for libcurl.so.4

* Tue Oct  3 2006 Paul Howarth <paul@city-fan.org> 0.2b-12
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Paul Howarth <paul@city-fan.org> 0.2b-11
- drag and drop works with files but not URIs (#206262);
  apply patch from Denis Leroy to fix desktop file accordingly
- escape macros in changelog entries
- use tabs rather than spaces

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> 0.2b-10
- rebuild for dynamic linking speedups (FE6)

* Sun May 28 2006 Paul Howarth <paul@city-fan.org> 0.2b-9
- add missing buildreq intltool

* Tue Feb 14 2006 Paul Howarth <paul@city-fan.org> 0.2b-8
- cosmetic tweak: use macros instead of variables
- don't use macros in command paths, hardcode them instead

* Wed Nov  9 2005 Paul Howarth <paul@city-fan.org> 0.2b-7
- rebuild

* Mon Oct 17 2005 Paul Howarth <paul@city-fan.org> 0.2b-6
- rebuild

* Tue May 10 2005 Paul Howarth <paul@city-fan.org> 0.2b-5
- fix URL for SOURCE0 not to point to a specific sf.net mirror
- remove redundant build dependencies
- tidy URL

* Mon May  9 2005 Paul Howarth <paul@city-fan.org> 0.2b-4
- remove hard-coded dist tag, no longer needed
- remove duplicate README file from %%{_datadir}/GTorrentViewer

* Mon May  9 2005 Paul Howarth <paul@city-fan.org> 0.2b-3
- reverted desktop file pathname to relative paths
- run update-desktop-database in post-scripts; add post and
  postun dependencies on desktop-file-utils
- use full URL for SOURCE0
- tidy up description

* Mon May  9 2005 Paul Howarth <paul@city-fan.org> 0.2b-2
- lowercased package name
- removed zero sized NEWS file
- add dist tag to release

* Fri May  6 2005 Paul Howarth <paul@city-fan.org> 0.2b-1
- initial build for Fedora Extras
