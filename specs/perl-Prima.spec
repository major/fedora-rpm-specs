# Run X11 tests
%{bcond_without perl_Prima_enables_x11_test}
# Support bidirectional text with FriBidi library
%{bcond_without perl_Prima_enables_fribidi}
# Support GIF image format
%{bcond_without perl_Prima_enables_gif}
# Use GTK2 file dialogs and fonts. GTK3 takes precedence.
%{bcond_with perl_Prima_enables_gtk2}
# Use GTK3 file dialogs and fonts
%{bcond_without perl_Prima_enables_gtk3}
# Use HarfBuzz library for rendering a text
%{bcond_without perl_Prima_enables_harfbuzz}
# Use libheif for rendering HEIF images
%{bcond_without perl_Prima_enables_heif}
# Use LibThai library for wrapping a Thai text
%{bcond_without perl_Prima_enables_libthai}
# Support colorful cursor via Xcursor
%{bcond_without perl_Prima_enables_xcursor}
# Support FreeType fonts via xft
%{bcond_without perl_Prima_enables_xft}
# Support WebP image format
%{bcond_without perl_Prima_enables_wepb}

%define use_gtk2 0
%define use_gtk3 0
%if %{with perl_Prima_enables_gtk3}
%define use_gtk3 1
%else
%if %{with perl_Prima_enables_gtk2}
%define use_gtk2 1
%endif
%endif


Name:           perl-Prima
Version:        1.75
Release:        2%{?dist}
Summary:        Perl graphic toolkit
# Copying:              BSD-2-Clause text
# examples/tiger.eps:   AGPL-3.0-or-later (bundled from GhostScript? CPAN RT#122271)
# img/codec_jpeg.c:     LGPL-2.0-or-later (EXIF parser is based on io-jpeg.c
#                       from gdk-pixbuf)
# img/codec_X11.c:      MIT-open-group
# img/imgscale.c:       ImageMagick (resizing filters are based on magick/resize.c
#                       from ImageMagick)
# img/polyfill.c:       MIT-open-group AND HPND
# include/unix/queue.h: BSD-4-Clause
# LICENSE:              BSD-2-Clause text and (AGPL-3.0-or-later notice for examples/tiger.eps file)
# pod/Prima/Widget/pack.pod:    TCL
# pod/Prima/Widget/place.pod:   TCL
# pod/prima-gencls.pod: "under the BSD License"
# Prima.pm:             "under the BSD License"
# Prima/PS/Unicode.pm:  BSD-3-Clause
# unix/render.c:        HPND-sell-variant
License:        BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND MIT-open-group AND HPND AND HPND-sell-variant AND TCL AND ImageMagick AND LGPL-2.0-or-later AND AGPL-3.0-or-later
URL:            https://metacpan.org/dist/Prima
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARASIK/Prima-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
%if %{with perl_Prima_enables_gtk3}
BuildRequires:  giflib-devel >= 4
%endif
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# pkgconfig is optional, but it provides better compiler options, so use it
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
%if %{with perl_Prima_enables_fribidi}
BuildRequires:  pkgconfig(fribidi)
%endif
%if %{use_gtk2}
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.7
%endif
%if %{use_gtk3}
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9
%endif
%if %{with perl_Prima_enables_harfbuzz}
BuildRequires:  pkgconfig(harfbuzz)
%endif
%if %{with perl_Prima_enables_heif}
BuildRequires:  pkgconfig(libheif) >= 1.12.0
%endif
BuildRequires:  pkgconfig(libpng)
%if %{with perl_Prima_enables_libthai}
BuildRequires:  pkgconfig(libthai)
%endif
BuildRequires:  pkgconfig(libtiff-4)
%if %{with perl_Prima_enables_wepb}
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
%if %{with perl_Prima_enables_xcursor}
BuildRequires:  pkgconfig(xcursor)
%endif
BuildRequires:  pkgconfig(xext)
%if %{with perl_Prima_enables_xft}
BuildRequires:  pkgconfig(xft)
%endif
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr) >= 1.5
BuildRequires:  pkgconfig(xrender)
# Run-time:
# AnyEvent not used, t/misc/syntax.t fakes it.
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
# Getopt::Long not used at tests
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::RefHash)
# Optional run-time:
BuildRequires:  perl(Compress::Raw::Zlib)
# gv not used at a tests
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
%if %{with perl_Prima_enables_x11_test}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
# Tests exhibit a proportional font
BuildRequires:  liberation-sans-fonts
%endif
Recommends:     perl(Compress::Raw::Zlib)
Suggests:       gv
# Public modules without a package keyword:
Provides:       perl(Prima::noARGV) = %{version}
Provides:       perl(Prima::PS::Drawable::Path) = %{version}
Provides:       perl(Prima::PS::Drawable::Region) = %{version}
Provides:       perl(Prima::PS::Setup) = %{version}

%{?perl_default_filter}

# Do not export private modules (not starting with "Prima")
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((am|apc|bi|bs|bt|ci|cl|cm|CodeEditor|cr|cs|CustomPodView|Divider|dmfp|dt|Editor|fdo|fds|fe|fp|fr|fra|frr|fs|fw|gm|gr|grow|gsci|gt|gui|ict|im|is|ItemsOutline|kb|km|le|lj|lp|mb|mbi|MenuOutline|MPropListViewer|mt|MyOutline|nt|PackPropListViewer|PropListViewer|rop|Round3D|sbmp|ss|sv|ta|tb|tka|tm|tno|tns|tw|wc|ws)\\)

# Filter under-specified provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Prima\\)$

%description
Prima is a general purpose extensible graphical user interface toolkit with
a rich set of standard widgets and an emphasis on 2D image processing tasks.
A Perl program using PRIMA looks and behaves identically on X, Win32.

%package AnyEvent
Summary:        AnyEvent bridge for Prima Perl graphic toolkit
License:        BSD-2-Clause
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description AnyEvent
This is an experiment to bring in AnyEvent::Impl::Prima into the
Prima toolkit's core.

%package Test
Summary:        Test tools for Prima Perl graphic toolkit
License:        BSD-2-Clause
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Test
This Perl module contains a small set or tool used for testing of
Prima-related code together with standard Perl Test:: suite.

%package tests
Summary:        Tests for %{name}
License:        BSD-2-Clause
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Test = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%if %{with perl_Prima_enables_x11_test}
Requires:       xorg-x11-server-Xvfb
Requires:       font(:lang=en)
# Tests exhibit a proportional font
Requires:       liberation-sans-fonts
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Prima-%{version}
# Normalize end-of-lines
find -type f \( -name '*.pm' -o -name '*.pl' -o -name '*.PL' -o -name '*.t' \
     -o -name Changes -o -name README.md \) -exec perl -i -pe 's/\r\n/\n/' {} +
# Help generators to recognize Perl scripts
for F in $(find t -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
unset AUTOMATED_TESTING NONINTERACTIVE_TESTING PERL_BATCH
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="$RPM_OPT_FLAGS" \
    DEBUG=0 \
    VERBOSE=1 \
    WITH_COCOA=0 \
    WITH_FONTCONFIG=1 \
    WITH_FREETYPE=1 \
    WITH_FRIBIDI=%{with perl_Prima_enables_fribidi} \
    WITH_GTK2=%{use_gtk2} \
    WITH_GTK3=%{use_gtk3} \
    WITH_HARFBUZZ=%{with perl_Prima_enables_harfbuzz} \
    WITH_ICONV=1 \
    WITH_LIBTHAI=%{with perl_Prima_enables_libthai} \
    WITH_OPENMP=1 \
    WITH_XFT=%{with perl_Prima_enables_xft}
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
find %{buildroot} -type f -name '*.a' -size 0 -delete
find %{buildroot}/%{_mandir} -type f -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/misc/syntax.t
find %{buildroot}%{_libexecdir}/%{name}/t -name '*.xt' -delete
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/misc/fs.t writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
pushd "$DIR"
unset DISPLAY XDG_SESSION_TYPE
%if %{with perl_Prima_enables_x11_test}
    xvfb-run -d prove -I . -r -j 1 t
%else
    prove -I . -r -j 1 t
%endif
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset DISPLAY XDG_SESSION_TYPE
# Not parallel-safe
%if %{with perl_Prima_enables_x11_test}
    xvfb-run -d make test
%else
    make test
%endif

%files
%license Copying LICENSE AGPLv3
# "examples" directory is installed into perl_vendorarch
%doc Changes README.md
%{_bindir}/podview
%{_bindir}/prima-*
%{_bindir}/VB
%{perl_vendorarch}/auto/Prima
%{perl_vendorarch}/prima-gencls.pod
%{perl_vendorarch}/Prima.pm
%{perl_vendorarch}/Prima
%exclude %{perl_vendorarch}/Prima/examples/socket_anyevent1.pl
%exclude %{perl_vendorarch}/Prima/examples/socket_anyevent2.pl
%exclude %{perl_vendorarch}/Prima/Stress.*
%exclude %{perl_vendorarch}/Prima/sys/AnyEvent.pm
%exclude %{perl_vendorarch}/Prima/sys/Test.*
%{perl_vendorarch}/vb-large.png
%{_mandir}/man1/podview.*
%{_mandir}/man1/prima-*.*
%{_mandir}/man1/VB.*
%{_mandir}/man3/pod::Prima::*
%{_mandir}/man3/pod::prima-gencls.*
%{_mandir}/man3/Prima.*
%{_mandir}/man3/Prima::*
%exclude %{_mandir}/man3/Prima::Stress.*
%exclude %{_mandir}/man3/Prima::sys::AnyEvent.*
%exclude %{_mandir}/man3/Prima::sys::Test.*

%files AnyEvent
%{perl_vendorarch}/Prima/examples/socket_anyevent1.pl
%{perl_vendorarch}/Prima/examples/socket_anyevent2.pl
%{perl_vendorarch}/Prima/sys/AnyEvent.pm
%{_mandir}/man3/Prima::sys::AnyEvent.*

%files Test
%{perl_vendorarch}/Prima/Stress.*
%{perl_vendorarch}/Prima/sys/Test.*
%{_mandir}/man3/Prima::Stress.*
%{_mandir}/man3/Prima::sys::Test.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Petr Pisar <ppisar@redhat.com> - 1.75-1
- 1.75 bump

* Thu Aug 29 2024 Petr Pisar <ppisar@redhat.com> - 1.74-1
- 1.74 bump

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.73-2
- Perl 5.40 rebuild

* Thu May 16 2024 Petr Pisar <ppisar@redhat.com> - 1.73-1
- 1.73 bump

* Wed Feb 14 2024 Petr Pisar <ppisar@redhat.com> - 1.72-2
- Fix a coredump when enumerating font-config fonts (CPAN RT#151594)
- Use an upstream fix for a Bool type (bug #2261449)

* Fri Feb 02 2024 Petr Pisar <ppisar@redhat.com> - 1.72-1
- 1.72 bump

* Fri Feb 02 2024 Petr Pisar <ppisar@redhat.com> - 1.71-4
- Fix Bool type to build with GCC 14 (bug #2261449)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 07 2023 Petr Pisar <ppisar@redhat.com> - 1.71-1
- 1.71 bump

* Wed Sep 06 2023 Petr Pisar <ppisar@redhat.com> - 1.70-1
- 1.70 bump

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.69-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.69-2
- Perl 5.38 rebuild

* Fri Jun 02 2023 Petr Pisar <ppisar@redhat.com> - 1.69-1
- 1.69 bump (default skin is flat)

* Mon Mar 20 2023 Petr Pisar <ppisar@redhat.com> - 1.68.2-2
- Enable support for HEIF images (bug #2178600)

* Fri Mar 03 2023 Petr Pisar <ppisar@redhat.com> - 1.68.2-1
- 1.68002 bump

* Wed Mar 01 2023 Petr Pisar <ppisar@redhat.com> - 1.68.1-1
- 1.68001 bump

* Mon Feb 27 2023 Petr Pisar <ppisar@redhat.com> - 1.68-1
- 1.68 bump

* Tue Feb 14 2023 Petr Pisar <ppisar@redhat.com> - 1.67.1-1
- 1.67001 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Petr Pisar <ppisar@redhat.com> - 1.67-2
- Fix un undefined behaviour triggering _FORTIFY_SOURCE=3 abort (bug #2160077)
- Prevent from desynchronizing Gtk and Perl locale
- Fix an invalid memory access in handling Thai script (upstream bug #71)
- Fix a crash in finding a font
- Make Prima compatible with multihreaded X11 applications (upstream bug #75)
- Fix a crash when processing an event queue

* Wed Nov 30 2022 Petr Pisar <ppisar@redhat.com> - 1.67-1
- 1.67 bump

* Wed Sep 21 2022 Petr Pisar <ppisar@redhat.com> - 1.66-2
- perl-Prima-Test package to require the same version of perl-Prima

* Mon Aug 22 2022 Petr Pisar <ppisar@redhat.com> - 1.66-1
- 1.66 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.65-2
- Perl 5.36 rebuild

* Wed Apr 20 2022 Petr Pisar <ppisar@redhat.com> - 1.65-1
- 1.65 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 10 2021 Petr Pisar <ppisar@redhat.com> - 1.63-1
- 1.63 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Petr Pisar <ppisar@redhat.com> - 1.62-1
- 1.62 bump
- Fix a clamp when downsampling bitmaps (bug #1972889)

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.61-2
- Perl 5.34 rebuild

* Fri Apr 23 2021 Petr Pisar <ppisar@redhat.com> - 1.61-1
- 1.61 bump
- Package the tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Petr Pisar <ppisar@redhat.com> - 1.60-1
- 1.60 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.59-2
- Perl 5.32 rebuild

* Fri Jun 05 2020 Petr Pisar <ppisar@redhat.com> - 1.59-1
- 1.59 bump

* Mon Mar 16 2020 Petr Pisar <ppisar@redhat.com> - 1.58-1
- 1.58 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Petr Pisar <ppisar@redhat.com> - 1.57-1
- 1.57 bump
- Fix alpha calculation in ropMultiply
- Fix color resampling on big-endian machines (CPAN RT#131016)
- Fix underscore location in a menu
- Fix text baseline

* Wed Aug 21 2019 Petr Pisar <ppisar@redhat.com> - 1.56-1
- 1.56 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.55-2
- Perl 5.30 rebuild

* Mon Mar 25 2019 Petr Pisar <ppisar@redhat.com> - 1.55-1
- 1.55 bump

* Mon Feb 04 2019 Petr Pisar <ppisar@redhat.com> - 1.54-1
- 1.54 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.53-1
- 1.53 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-6
- Perl 5.28 rebuild

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 1.52-5
- Rebuild (giflib)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Petr Pisar <ppisar@redhat.com> - 1.52-1
- 1.52 bump
- License changed to "BSD and MIT and TCL and ImageMagick and LGPLv2+ and
  AGPLv3+"

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-2
- Perl 5.26 rebuild

* Wed Apr 26 2017 Petr Pisar <ppisar@redhat.com> - 1.51-1
- 1.51 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Petr Pisar <ppisar@redhat.com> - 1.50-1
- 1.50 bump

* Thu Sep 29 2016 Petr Pisar <ppisar@redhat.com> - 1.49-1
- 1.49 bump

* Fri Sep 02 2016 Petr Pisar <ppisar@redhat.com> - 1.48-1
- 1.48 bump

* Mon Jun 06 2016 Petr Pisar <ppisar@redhat.com> - 1.47-1
- 1.47 bump
- License changed to "BSD and MIT and TCL and ImageMagick and LGPLv2+"

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.46-3
- Perl 5.24 rebuild

* Mon Mar 21 2016 Petr Pisar <ppisar@redhat.com> - 1.46-2
- Fix bars on big endian (bug #1318734)

* Thu Mar 17 2016 Petr Pisar <ppisar@redhat.com> - 1.46-1
- 1.46 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Petr Pisar <ppisar@redhat.com> - 1.45-1
- 1.45 bump

* Wed Aug 05 2015 Petr Pisar <ppisar@redhat.com> - 1.44-1
- 1.44 bump

* Tue Jun 23 2015 Petr Pisar <ppisar@redhat.com> - 1.43-4
- Build-require open Perl module (bug #1234731)
- Replace dependency on glibc-headers with gcc (bug #1230488)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-2
- Perl 5.22 rebuild

* Mon Apr 13 2015 Petr Pisar <ppisar@redhat.com> - 1.43-1
- 1.43 bump

* Mon Mar 16 2015 Petr Pisar <ppisar@redhat.com> - 1.42-2
- Provide perl(Prima::noX11)

* Thu Mar 12 2015 Petr Pisar <ppisar@redhat.com> - 1.42-1
- 1.42 bump

* Wed Nov 12 2014 Petr Pisar <ppisar@redhat.com> - 1.41-1
- 1.41 bump

* Fri Sep 19 2014 Petr Pisar <ppisar@redhat.com> - 1.40-1
- 1.40 bump

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.37-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 26 2013 Petr Pisar <ppisar@redhat.com> 1.37-1
- Specfile autogenerated by cpanspec 1.78.
