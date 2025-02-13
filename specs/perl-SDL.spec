Name:           perl-SDL
Version:        2.548
Release:        27%{?dist}
Summary:        Simple DirectMedia Layer for Perl
# COPYING:                      GPL-2.0 text
# lib/pods/SDL.pod:             GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDL/Platform.pod:    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDL/Tutorial.pod:    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDL/Tutorial/Animation.pod:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDL/Tutorial/LunarLander.pod:    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/Layer.pod:          GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/LayerManager.pod:   GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/Music.pod:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/Rect.pod:       GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/SFont.pod:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/Sound.pod:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/pods/SDLx/Text.pod:       GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/SDL.pm:                       LGPL-2.1-or-later
# lib/SDL_perl.pm:                  LGPL-2.1-or-later
# lib/SDL/SMPEG/Info.pm:            LGPL-2.1-or-later
# lib/SDL/TTFont.pm:                LGPL-2.1-or-later
# lib/SDL/Tutorial.pm:              LGPL-2.1-or-later
# lib/SDL/Tutorial/Animation.pm:    LGPL-2.1-or-later
# src/defines.h:        LGPL-2.1-or-later
# src/ppport.h:         GPL-1.0-or-later OR Artistic-1.0-Perl
# src/SDL.xs:           LGPL-2.1-or-later
# src/SDLx/SFont.h:     LGPL-2.1-or-later
# src/SDLx/SFont.xs:    LGPL-2.1-or-later
## Used at build-time, but not in any binary package
# Build.PL:                 refers to LGPL
# inc/My/Builder.pm:        LGPL-2.1-or-later
# test/data/5x7.fnt:        LGPL-2.1-only (see test/data/README)
# test/data/tribe_i.wav:    GPL-3.0-only OR LGPL-2.0-only OR CC-BY-SA-3.0
#                           (see test/data/README; there is a typo in the file
#                           name)
## Not in any binary package and not used
# META.json:    refers to LGPL-2.1
# OFL.txt:      OFL-1.1-RFN text
## Unbundled:
# share/GenBasR.ttf:    OFL-1.1-RFN
License:        LGPL-2.1-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
SourceLicense:  %{license} AND LGPL-2.1-only AND (GPL-3.0-only OR LGPL-2.0-only OR CC-BY-SA-3.0) AND OFL-1.1-RFN
URL:            http://sdl.perl.org/
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FROGGS/SDL-%{version}.tar.gz
# Fix an implicit function declaration, proposed to the upstream,
# bug #2177189, <https://github.com/PerlGameDev/SDL/pull/299>.
Patch0:         SDL-2.548-Fix-implicit-declaration-of-_calc_offset.patch
# Unbundle Gentium Book Basic font, not suitable for the upstream, the file is
# delete in %%prep section.
Patch1:         SDL-2.548-Unbundle-Gentium-Book-Basic-regular-font.patch
# Adapt to perl 5.37.1, proposed to upstream,
# <https://github.com/PerlGameDev/SDL/issues/303>
Patch2:         SDL-2.548-Adapt-to-perl-5.37.1.patch
# Fix reference counting an event filter callback, bug #2272636,
# proposed to the upstream, <https://github.com/PerlGameDev/SDL/pull/308>
Patch3:         SDL-2.548-Fix-reference-counting-in-set_event_filter.patch
# Adapt to GCC 15, bug #2341036,
# <https://github.com/PerlGameDev/SDL/issues/294>, proposed upstream
# <https://github.com/PerlGameDev/SDL/pull/309>
Patch4:         SDL-2.548-Fix-building-in-ISO-C23.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Alien::SDL) >= 1.446
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(lib)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# ExtUtils::CBuilder::Base not used at tests
BuildRequires:  perl(File::Find)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Simple)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  sil-gentium-basic-book-fonts
# Tests:
BuildRequires:  perl(bytes)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most) >= 0.21
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
Requires:       sil-gentium-basic-book-fonts

%{?perl_default_filter}

%description
SDL_perl is a package of Perl modules that provide both functional and
object oriented interfaces to the Simple DirectMedia Layer for Perl 5. This
package takes some liberties with the SDL API, and attempts to adhere to
the spirit of both the SDL and Perl.


%package -n perl-Module-Build-SDL
Summary:        Module::Build subclass for building SDL applications
License:        LGPL-2.1-or-later
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(ExtUtils::CBuilder::Base)

%description -n perl-Module-Build-SDL
Module::Build::SDL is a subclass of Module::Build created to make easy
some tasks specific to SDL applications - e.g. packaging SDL
application/game into PAR archive.


%prep
%autosetup -p1 -n SDL-%{version}
# Delete a bundled font file, code removed with
# Unbundle-Gentium-Book-Basic-regular-font.patch.
rm -r share
# Move the pod files directly to directory lib to have correctly generated
# man pages without prefix pods::
cd lib/pods
find * -type d -exec mkdir -p ../{} \;
find * -type f -exec mv {} ../{} \;
cd ..
rm -r pods
cd ..
sed -i -e 's|lib/pods|lib|' MANIFEST
# Disable the sdlx_controller_interface.t test, it hangs on arm
rm t/sdlx_controller_interface.t
sed -i -e '/t\/sdlx_controller_interface\.t/d' MANIFEST

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*

%files
%license COPYING
%doc CHANGELOG TODO
%{perl_vendorarch}/auto/SDL
%{perl_vendorarch}/auto/SDL_perl
%{perl_vendorarch}/auto/SDLx
%{perl_vendorarch}/SDL
%{perl_vendorarch}/SDL.pm
%{perl_vendorarch}/SDL.pod
%{perl_vendorarch}/SDL_perl.pm
%{perl_vendorarch}/SDLx
%{_mandir}/man3/SDL.*
%{_mandir}/man3/SDL::*
%{_mandir}/man3/SDLx::*

%files -n perl-Module-Build-SDL
%dir %{perl_vendorarch}/Module
%dir %{perl_vendorarch}/Module/Build
%{perl_vendorarch}/Module/Build/SDL.pm
%{_mandir}/man3/Module::Build::SDL.*

%changelog
* Tue Feb 11 2025 Petr Pisar <ppisar@redhat.com> - 2.548-27
- Adapt to GCC 15 (bug #2341036)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.548-24
- Perl 5.40 rebuild

* Tue Apr 02 2024 Petr Pisar <ppisar@redhat.com> - 2.548-23
- Fix reference counting an event filter callback (bug #2272636)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Petr Pisar <ppisar@redhat.com> - 2.548-19
- Adapt to perl 5.37.1 (upstream bug #303)

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.548-18
- Perl 5.38 rebuild

* Fri Mar 10 2023 Petr Pisar <ppisar@redhat.com> - 2.548-17
- Fix an implicit function declaration (bug #2177189)
- Correct a license to "LGPL-2.1-or-later AND (GPL-1.0-or-later OR
  Artistic-1.0-Perl)"
- Use a system-provided Gentium Book Basic font

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.548-14
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.548-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.548-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.548-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.548-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.548-2
- Perl 5.28 rebuild

* Mon Jun 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.548-1
- 2.548 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.546-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.546-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 2.546-10
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.546-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.546-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.546-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.546-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.546-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Petr Pisar <ppisar@redhat.com> - 2.546-4
- Specify all dependencies
- Move Module::Build::SDL to perl-Module-Build-SDL sub-package

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.546-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.546-2
- Perl 5.22 rebuild

* Fri Jun  5 2015 Hans de Goede <hdegoede@redhat.com> - 2.546-1
- 2.546 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.544-5
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.544-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 2.544-3
- Rebuild for new SDL_gfx (rhbz#1106197)
- Disable the sdlx_controller_interface.t test, it hangs on arm

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.544-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Pisar <ppisar@redhat.com> - 2.544-1
- 2.544 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.540-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 2.540-4
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.540-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.540-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 04 2012 Jitka Plesnikova <jplesnik@redhat.com> - 2.540-1
- Update to 2.540

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.2.6-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.2.6-5
- Rebuild for new libpng

* Mon Jul 18 2011 Petr Sabata <contyk@redhat.com> - 2.2.6-4
- Perl mass rebuild

* Fri Jul 15 2011 Hans de Goede <hdegoede@redhat.com> - 2.2.6-3
- Rebuild for new SDL_gfx

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.2.6-2
- Perl mass rebuild

* Tue Feb 22 2011 Hans de Goede <hdegoede@redhat.com> - 2.2.6-1
- Rebase to 2.2.6 upstream release (#679313)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.1.3-14
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.1.3-13
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.1.3-12
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.3-9
- rebuild for new perl (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.3-8
- Autorebuild for GCC 4.3

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.3-7
- rebuild for new perl

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.1.3-6
- Rebuild for buildId

* Sun Aug 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.1.3-5
- Update License tag for new Licensing Guidelines compliance
- Add BuildRequires: perl(Test::More) to fix building with the new splitup
  perl

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 2.1.3-4
- Rebuild against SDL_gfx 2.0.16.

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.1.3-3
- FE6 Rebuild

* Wed Aug 16 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.1.3-2
- Filter wrong perl(main) and perl(Walker) out of Provides

* Tue Aug 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.1.3-1
- Major new upstream version 2.1.3
- Thanks to the rpmforge crew for the filter depends hack!

* Mon Aug 14 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.20.3-8
- Submit to Fedora Extras since it will build without the patented smpeg
  and none of the packages currently using perl-SDL need the smpeg part.
- Drop smpeg BR (see above).
- Cleanup BR's a bit to match FE-guidelines

* Sat Mar 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.20.3-7
- Sync with Debian's 1.20.3-4.
- Default SDL_mixer tests to off.

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 1.20.3-6
- switch to new release field
- fix BR

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Thu Sep 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.20.3-0.lvn.5
- Clean up obsolete pre-FC3 support (SDL_gfx support is now unconditional).
- Drop zero Epochs.

* Mon Jul  4 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.20.3-0.lvn.4
- Clean up obsolete pre-FC2 support.

* Fri Feb 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.20.3-0.lvn.3
- Build with SDL_gfx support by default, add "--without gfx" build option.
- Patch to sync with SDL_gfx >= 2.0.12 API changes (bug 374).

* Sun Jul 11 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.20.3-0.lvn.2
- Add "--without mixertest" build option for build roots without audio devices,
  and "--without tests" option to disable tests altogether, needed in FC1
  due to buggy libtiff package (bug 107).

* Sat Jul  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.20.3-0.lvn.1
- Update to 1.20.3.
- Clean up list of searched include dirs.

* Wed Jun 30 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.20.0-0.lvn.4
- Partial specfile rewrite according to current fedora.us Perl spec template.
- Use tarball + patch from Debian.
- Borrow libGLU fix from Ian Burrell and Matthias Saou, and adjust it a bit:
  http://lists.freshrpms.net/pipermail/freshrpms-list/2003-December/006843.html
- BuildRequire SDL_ttf-devel.

* Fri Jun 27 2003 Phillip Compton <pcompton at proteinmedia dot com> 0:1.20.0-0.fdr.3
- Applied patch to spec from Ville Skyttä changeing:
- BuildRequires: smpeg-devel.
- Run make tesst during build.
- Get rid of unneeded files in installation directories.
- Make installed files writable so that non-root strip works.

* Sun Jun 22 2003 Phillip Compton <pcompton at proteinmedia dot com> 0:1.20.0-0.fdr.2
- Used cpanflute2 to redo the build and install sections.

* Tue May 27 2003 Phillip Compton <pcompton at proteinmedia dot com> 0:1.20.0-0.fdr.1
- Fedorafied

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.

* Mon Feb 17 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.20.0.

* Mon Oct 28 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.19.0.
- Major spec file adaptation :-/

* Fri Sep 20 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.18.7.
- Minor spec cleanups.

* Mon Apr 15 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.16.

* Thu Feb  7 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.
