Name:           dvdauthor
Version:        0.7.2
Release:        26%{?dist}
Summary:        Command line DVD authoring tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://dvdauthor.sourceforge.net/
Source0:        http://downloads.sourceforge.net/dvdauthor/%{name}-%{version}.tar.gz
# From openSUSE
Patch0:         dvdauthor-0.7.2-imagemagick7.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libdvdread-devel >= 0.9.4-4
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel >= 2.6.0
BuildRequires:  fontconfig-devel
BuildRequires:  fribidi-devel
BuildRequires:  freetype-devel
BuildRequires:  ImageMagick-devel >= 1:7.0

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
DVDAuthor is a set of tools to help you author the file and directory
structure of a DVD-Video disc, including programmatic commands for
implementing interactive behavior. It is driven by command lines and
XML control files, though there are other programs that provide
GUI-based front ends if you prefer.


%prep
%autosetup -n %{name} -p1


%build
export LDFLAGS="$RPM_LD_FLAGS -Wl,--as-needed" # *Magick-config linkage bloat
%configure --disable-rpath --enable-default-video-format=NTSC
%make_build


%install
%make_install


%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_bindir}/dvdauthor
%{_bindir}/dvddirdel
%{_bindir}/dvdunauthor
%{_bindir}/mpeg2desc
%{_bindir}/spumux
%{_bindir}/spuunmux
%{_datadir}/dvdauthor/
%{_mandir}/man1/dvdauthor.1*
%{_mandir}/man1/dvddirdel.1*
%{_mandir}/man1/dvdunauthor.1*
%{_mandir}/man1/mpeg2desc.1*
%{_mandir}/man1/spumux.1*
%{_mandir}/man1/spuunmux.1*
%{_mandir}/man7/video_format.7*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.2-25
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild
- Since it is now a leaf package, drop i686 per fedora leaf package policy, which also fix the build

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.7.2-19
- Rebuild for ImageMagick 7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 17 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.2-16
- Rebuild against new ImageMagick

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 17 2020 Dominik Mierzejewski <rpm@greysector.net> - 0.7.2-13
- rebuild for libdvdread-6.1 ABI bump

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Richard Shaw <hobbes1069@gmail.com> - 0.7.2-10
- Build with ImageMagik instead of GraphicsMagik, fixes #1711698.

* Fri Nov 15 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 0.7.2-9
- rebuild for libdvdread ABI bump

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Richard Shaw <hobbes1069@gmail.com> - 0.7.2-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 20 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.7.1-6
- Patch headers to fix build on F-21+
- Mark COPYING as %%license

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 24 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-2
- rebuild (GraphicsMagick)

* Mon Aug 20 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.7.1-1
- Update to 0.7.1.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov  5 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.7.0-5
- Fix build with libpng 1.5 (patch from upstream).
- Clean up specfile constructs no longer needed with Fedora or EL6+.

* Fri Sep 23 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.7.0-4
- Build with $RPM_LD_FLAGS.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov  8 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.7.0-2
- Patch to fix crash when $HOME is not set (#650433).
- Set compile time default video format to NTSC (#650433).

* Wed Oct 27 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.7.0-1
- Update to 0.7.0, all patches applied upstream.
- Improve %%description.

* Mon Jun  7 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.6.18-2
- Patch to fix subtitle creation with GraphicsMagick > 1.3.7 (#599000).

* Thu Mar 18 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.6.18-1
- Update to 0.6.18 ("official" again), all patches applied upstream.

* Sat Jan  2 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.6.17-1
- Update to 0.6.17 (new "unofficial" upstream: http://www.joonet.de/dvdauthor/).
- Patch to compile with FriBidi 0.19.x.
- Include HTML docs in package.
- Drop no longer needed libdvdread header dir hack.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.6.14-9
- rebuild (GraphicsMagick)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.14-7
- rebuild against new GraphicsMagick

* Tue Jul  8 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.6.14-6
- Fix build with changed libdvdread 4.1.3 header location.

* Wed Feb 13 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.6.14-5
- Build with GraphicsMagick, drop all build time conditionals (#245155).
- Patch to differentiate ImageMagick vs GraphicsMagick at build time, don't
  rely on GM's IM compat things installed, fix RGBA treatment with GM.
- Avoid linkage bloat from GraphicsMagick-config --libs.

* Wed Feb 13 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.6.14-4
- Add build time conditional for GraphicsMagick, disabled by default (#432651).
- Get rid of need for BuildConflicts.

* Fri Nov 16 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.6.14-3
- Rebuild.

* Tue Aug 14 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.6.14-2
- License: GPLv2+

* Sat Feb 24 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.6.14-1
- 0.6.14.

* Wed Jan 17 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.6.13-1
- 0.6.13.

* Mon Jan  8 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.6.12-1
- 0.6.12.

* Sun Jan  7 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.6.11-9
- First FE build (#219103).

* Thu Oct 26 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.6.11-8
- Build without ImageMagick by default due to dependency bloat (#212478).
- Prune pre-2006 changelog entries.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.6.11-7
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sun Sep 24 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.6.11-6
- Rebuild.

* Sun Jul  9 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.6.11-5
- Rebuild for new ImageMagick (#1087).

* Thu Mar 16 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.6.11-4
- Remove -ldl hacks, BR fixed libdvdread-devel.
