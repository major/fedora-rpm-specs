Name:           raidem
Version:        0.3.1
Release:        56%{?dist}
Summary:        2d top-down shoot'em up
License:        zlib
URL:            http://home.exetel.com.au/tjaden/raidem/
# This is an exacy copy of the upstream src except that lib/almp3 which is
# an included mp3 decoder has been removed.
Source0:        %{name}-%{version}-src.zip
Source1:        raidem.png
Source2:        raidem.desktop
Patch0:         raidem-0.3.1-syslibs.patch
Patch1:         raidem-0.3.1-zziplib.patch
Patch2:         raidem-libpng15.patch
Patch3:         raidem-gcc4.7-stdio.patch
Patch4:         raidem-new-api.patch
Patch5:         raidem-0.3.1-format-security.patch
Patch6:         raidem-0.3.1-system-flags.patch
Patch7:         raidem-0.3.1-Makefile-race-condition.patch
Patch8:		raidem-0.3.1-enum.patch
Patch9:		raidem-0.3.1-counter-dup.patch
BuildRequires: make
BuildRequires:  gcc-objc glyph-keeper-allegro-devel freetype-devel adime-devel
BuildRequires:  zziplib-devel libpng-devel AllegroOGG-devel
BuildRequires:  automake desktop-file-utils gnustep-base-devel
Requires:       hicolor-icon-theme

%description
Raid'em is a 2d top-down shoot'em up. It began as a remake of Raid II
(abandoned long ago), but has turned out very differently.
Features: Neat looking graphics, LOTS of explosions and scrap
metal, Eye candy a-plenty, Many different powerups, A desert. And a space
platform. And some snow, 2 player mode, Demo recording and playback, Loads of
fun.


%prep
%setup -q -n %{name}-%{version}-src
%patch -P 0 -p1 -z .syslibs
%patch -P 1 -p1
%patch -P 2 -z .libpng
%patch -P 3 -p0 -z .gcc47
%patch -P 4 -p0 -z .newapi
%patch -P 5 -p1 -z .format-security
%patch -P 6 -p1 -z .system-flags
%patch -P 7 -p1 -z .race-condition
%patch -P 8 -p0 -z .enum
%patch -P 9 -p0 -z .counter
# remove all included system libs, to avoid using the included system headers.
mv lib/loadpng .
rm -fr lib/*
mv loadpng lib
aclocal
autoconf


%build
# override _datadir otherwise it expects its datafile directly under /use/share
%configure --datadir=%{_datadir}/%{name} --disable-id3
%make_build


%install
# DIY, since the Makefile uses install -s and install -g games, etc.
# Fixable but this is easier
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a data demos maps $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install                            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

%files
%doc ChangeLog docs/README.txt docs/damages.txt
%license docs/LICENCE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-54
- Rebuild for gnustep-base 1.30.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 19 2023 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-51
- Rebuild for gnustep-base 1.29.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 16 2021 Bruno Wolff III <bruno@wolff.to> - 0.3.1-45
- Rebuild for new libgnustep-base

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 17 2020 Bruno Wolff III <bruno@wolff.to> - 0.3.1-42
- Rebuild for gnustep-base 1.27

* Sat Feb 08 2020 Bruno Wolff III <bruno@wolff.to> - 0.3.1-41
- Fix duplicate definition of counter
- A couple of enum definitions should be typedefs

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-35
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 0.3.1-32
- Add patch to solve race-condition in Makefile

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 0.3.1-31
- Add patch to respect system-flags for all built objects / binaries
- Update spec-file to recent guidelines

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 0.3.1-30
- Rebuilt for libgnustep-base
- Fix %%changelog
- Clean trailing whitespaces
- Regenerate patches
- Add patch for -Werror=format-security

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Bruno Wolff III <bruno@wolff.to> - 0.3.1-23
- Remove vendor prefix from desktop file

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 22 2012 Bruno Wolff III <bruno@wolff.to> - 0.3.1-20
- Switch to using modern objective C API (as the deprecated one has been dropped)
- This fixes bz 773185

* Wed Jan 11 2012 Bruno Wolff III <bruno@wolff.to> - 0.3.1-19
- Need to include stdio.h with gcc 4.7

* Wed Jan 04 2012 Bruno Wolff III <bruno@wolff.to> - 0.3.1-18
- Rebuild for gcc update

* Sun Nov 06 2011 Bruno Wolff III <bruno@wolff.to> - 0.3.1-17
- Include zlib.h since png.h no longer does for libpng 1.5.
- Use accessors instead of direct access to png structs.

* Sat Jul 16 2011 Hans de Goede <hdegoede@redhat.com> - 0.3.1-16
- Fix zziplib zzip_freopen abuse (fixes crash on startup, rhbz#710190)

* Thu Jul 14 2011 Bruno Wolff III <bruno@wolff.to> - 0.3.1-15
- Rebuild for allegro 4.4 and glyph-keeper
- Use the new glyph-keeper subpackage glyph-keeper-allegro-devel

* Wed Feb 23 2011 Bruno Wolff III <bruno@wolff.to> - 0.3.1-14
- Build against gcc-4.6.0-0.9.fc15 to get fix for bug 678928

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  8 2010 Hans de Goede <hdegoede@redhat.com> - 0.3.1-12
- Fix FTBFS (#599876)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Hans de Goede <hdegoede@redhat.com> 0.3.1-9
- Update description for new trademark guidelines

* Fri Feb  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-8
- Rebuild for new gcc-4.3 (libobjc soname change)

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-7
- Rebuild for buildId

* Tue Aug  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-6
- No longer build and link against libid3tag, as that would make us GPLv2+
  licensed instead of zlib licensed. Not that that would really be a problem,
  but since the id3tag functionality isn't used as we ship ogg music, this is
  better (bz 251055)
- Update License tag for new Licensing Guidelines compliance
- Fix invalid desktop file (fix building with latest desktop-file-utils)

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-5
- Fix build with new dynamic glyph-keeper lib
- FE6 Rebuild

* Tue Jul 18 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-4
- Fix building (configure test) with freetype 2.2.x .

* Thu Jul  6 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-3
- Rebuild against new allegro to remove executable stack requirement caused
  by previous versions of allegro.

* Mon May  1 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-2
- Fix big finger typo which put the datafiles under /use/share instead
  of /usr/share.

* Sat Apr 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.1-1
- New upstream release 0.3.1
- Upstream has merged most patches, dropped.
- Upstream has added ogg support (yeah!), add ogg and id3tag support.

* Sun Apr  2 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3-2
- Add missing RPM_OPT_FLAGS to CFLAGS
- Add missing -D__LINUX__ to CFLAGS with this patch2 is no longer needed
- Add -fsigned-char to CFLAGS this fixes crashing on startup on PPC (bz 185850)
- Add Patch3 which fixes funky colors on PPC (bz 185850)

* Sun Mar 12 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3-1
- Initial Fedora Extras package
