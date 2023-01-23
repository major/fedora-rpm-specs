%global use_system_admesh 0
%global use_system_expat 1
%global use_system_polyclipping 1
%global use_system_poly2tri 1

Name:           slic3r
Version:        1.3.0
Release:        28%{?dist}
Summary:        G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
License:        AGPLv3 and CC-BY
# Images are CC-BY, code is AGPLv3
URL:            http://slic3r.org/
Source0:        https://github.com/alexrj/Slic3r/archive/%{version}.tar.gz

# Modify Build.PL so we are able to build this on Fedora
Patch0:         %{name}-buildpl.patch

# Use /usr/share/slic3r as datadir
Patch1:         %{name}-datadir.patch
Patch2:         %{name}-english-locale.patch
Patch3:         %{name}-linker.patch
Patch4:         %{name}-clipper.patch
Patch5:         %{name}-1.3.0-fixtest.patch
Patch6:         %{name}-wayland.patch
Patch7:         %{name}-boost169.patch

# Use GCC predefined macros instead of deprecated Boost header
# Upstream already dropped this code in PR#781
Patch8:         %{name}-endian.patch
# Make boost::Placeholders::_1 visible (PR#4976)
Patch9:         %{name}-bind-placeholders.patch
# Use boost/nowide/cstdlib.hpp instead of boost/nowide/cenv.hpp (PR#4976)
Patch10:        %{name}-boost-nowide.patch

# Security fix for CVE-2020-28591
# https://github.com/slic3r/Slic3r/pull/5063
Patch11:        %{name}-CVE-2020-28591.patch

Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode::Locale) >= 1.05
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.80
BuildRequires:  perl(ExtUtils::Typemaps::Default) >= 1.05
BuildRequires:  perl(ExtUtils::Typemaps) >= 1.00
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(local::lib)
BuildRequires:  perl(Module::Build::WithXSpp) >= 0.14
BuildRequires:  perl(Moo) >= 1.003001
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SVG)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(threads) >= 1.96
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(Wx)

%if %{use_system_admesh}
BuildRequires:  admesh-devel >= 0.98.1
Requires:       admesh-libs >= 0.98.1

%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif
%else
Provides:       bundled(admesh) = 0.98

# Bundled admesh FTBFS with:
# error "admesh works correctly on little endian machines only!"
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    ppc ppc64 s390 s390x %{ix86}
%else
ExcludeArch:    ppc ppc64 s390 s390x
%endif
%endif

%if %{use_system_expat}
BuildRequires:  expat-devel >= 2.2.0
%else
Provides:       bundled(expat) = 2.2.0
%endif

%if %{use_system_polyclipping}
BuildRequires:  polyclipping-devel >= 6.4.2
%else
Provides:       bundled(polyclipping) = 6.4.2
%endif

%if %{use_system_poly2tri}
BuildRequires:  poly2tri-devel
%else
Provides:       bundled(poly2tri) = 0.0
%endif

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
Requires:       perl(Growl::GNTP) >= 0.15
Requires:       perl(XML::SAX)

# Optional dependency. Not packaged in Fedora yet, hence we cannot list it.
# It's only used for magically finding octoprint servers.
#Recommends:    perl(Net::Bonjour)

# Optional dependencies to allow background processing.
Recommends:     perl(Thread::Queue)
Recommends:     perl(threads::shared)

%description
Slic3r is a G-code generator for 3D printers. It's compatible with RepRaps,
Makerbots, Ultimakers and many more machines.
See the project homepage at slic3r.org and the documentation on the Slic3r wiki
for more information.

%prep
%setup -qn Slic3r-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .linker
%if %{use_system_polyclipping}
%patch4 -p1
%endif
%patch5 -p1 -b .fixtest
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

# Optional removals
%if %{use_system_admesh}
rm -rf xs/src/admesh
sed -i '/src\/admesh/d' xs/MANIFEST
%endif

%if %{use_system_expat}
rm -rf xs/src/expat
sed -i '/src\/expat/d' xs/MANIFEST
# These are the files with hardcoded expat/expat.h includes
sed -i 's|expat/expat.h|expat.h|g' xs/src/libslic3r/IO/AMF.cpp
sed -i 's|expat/expat.h|expat.h|g' xs/src/libslic3r/IO/TMF.hpp
%endif

%if %{use_system_polyclipping}
#rm xs/src/clipper.*pp
export SYSTEM_LIBS="${SYSTEM_LIBS} -lpolyclipping"
%endif

%if %{use_system_poly2tri}
rm -rf xs/src/poly2tri
sed -i '/src\/poly2tri/d' xs/MANIFEST
%endif

# We always do boost.
rm -rf xs/src/boost
sed -i '/src\/boost\/nowide/d' xs/MANIFEST

%build
%if %{use_system_admesh}
export SYSTEM_LIBS="${SYSTEM_LIBS} -ladmesh"
%endif

%if %{use_system_expat}
export SYSTEM_LIBS="${SYSTEM_LIBS} -lexpat"
%endif

%if %{use_system_poly2tri}
export SYSTEM_LIBS="${SYSTEM_LIBS} -lpoly2tri"
%endif

cd xs
[[ ! -z "${SYSTEM_LIBS}" ]] && echo "SYSTEM_LIBS is ${SYSTEM_LIBS}"
perl ./Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build
cd -
# Building non XS part only runs test, so skip it and run it in tests

# prepare pngs in mutliple sizes
for res in 16 32 48 128 256; do
  mkdir -p hicolor/${res}x${res}/apps
done
cd hicolor
convert ../var/Slic3r.ico %{name}.png
cp %{name}-0.png 256x256/apps/%{name}.png
cp %{name}-1.png 128x128/apps/%{name}.png
cp %{name}-2.png 48x48/apps/%{name}.png
cp %{name}-3.png 32x32/apps/%{name}.png
cp %{name}-4.png 16x16/apps/%{name}.png
rm %{name}-*.png
cd -

# To avoid "iCCP: Not recognized known sRGB profile that has been edited"
cd var
find . -type f -name "*.png" -exec convert {} -strip {} \;
cd -

%install
cd xs
./Build install destdir=%{buildroot} create_packlist=0
cd -
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# I see no way of installing slic3r with it's build script
# So I copy the files around manually
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{perl_vendorlib}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/icons
mkdir -p %{buildroot}%{_datadir}/appdata

cp -a %{name}.pl %{buildroot}%{_bindir}/%{name}
cp -ar lib/* %{buildroot}%{perl_vendorlib}

cp -a var/* %{buildroot}%{_datadir}/%{name}
cp -r hicolor %{buildroot}%{_datadir}/icons
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

cp %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%{_fixperms} %{buildroot}*

%check
cd xs
./Build test verbose=1
cd -
SLIC3R_NO_AUTO=1 perl Build.PL installdirs=vendor
# the --gui runs no tests, it only checks requires

%files
%doc README.md
%{_bindir}/%{name}
%{perl_vendorlib}/Slic3r*
%{perl_vendorarch}/Slic3r*
%{perl_vendorarch}/auto/Slic3r*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/%{name}

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-26
- Do not BuildRequire non-existing boost-nowide-devel

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-25
- Perl 5.36 rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.3.0-24
- Rebuilt for Boost 1.78

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 1.3.0-22
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-20
- Perl 5.34 rebuild

* Thu Mar 18 2021 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-19
- Security fix for CVE-2020-28591
- Resolves: rhbz#1934823
- Resolves: rhbz#1934824

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.3.0-17
- Rebuilt for Boost 1.75

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-15
- Perl 5.32 rebuild

* Tue Jun 02 2020 Jonathan Wakely <jwakely@redhat.com> - 1.3.0-14
- Rebuilt and patched for Boost 1.73

* Wed May 13 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-13
- Recommend optional dependencies to have background processing by default

* Mon Mar 16 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-12
- Add BR: perl(Thread::Semaphore)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-10
- Drop weak dependencies on packages not available in Fedora

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jonathan Wakely <jwakely@redhat.com> - 1.3.0-6
- Add patch for Boost 1.69 header changes

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.3.0-6
- Rebuilt for Boost 1.69

* Sat Dec 22 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-5
- Set GDK_BACKEND=x11 to prevent crashes on Wayland (#1661324)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-3
- Perl 5.28 rebuild

* Mon Jun 25 2018 Tom Callaway <spot@fedoraproject.org> - 1.3.0-2
- conditionalize bundled bits
- fix t/gcode.t (needed to define config->layer_height before trying to use it)
- exclude big endian architectures

* Thu May 31 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Tue Mar 06 2018 Petr Pisar <ppisar@redhat.com> - 1.2.9-18
- Adapt to removing GCC from a build root (bug #1547165)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.9-16
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.9-13
- Perl 5.26 re-rebuild of bootstrapped packages

* Fri Jun 02 2017 Miro Hrončok <mhroncok@redhat.com> - 1.2.9-12
- Fix rendering issues with perl-OpenGL 0.70

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.2.9-9
- Rebuilt for Boost 1.63

* Wed Aug 31 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.9-8
- Fix bug that crashes slic3r when about dialog is opened (#1285807)

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.9-7
- Perl 5.24 rebuild

* Tue Feb 23 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.9-6
- Add patch to fix FTBFS with Boost 1.60 (#1306668)
- Add patch to manually cast too bool, fix other FTBFS

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2.9-4
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.2.9-2
- rebuild for Boost 1.58

* Mon Jun 29 2015 Miro Hrončok <mhroncok@redhat.com> - 1.2.9-1
- New version 1.2.9
- Removed already merged patches
- Removed unused BRs

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.7-4
- Perl 5.22 rebuild

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.1.7-3
- Rebuild for boost 1.57.0

* Mon Oct 20 2014 Miro Hrončok <mhroncok@redhat.com> - 1.1.7-2
- Unbundle polyclipping 6.2.0

* Tue Sep 23 2014 Miro Hrončok <mhroncok@redhat.com> - 1.1.7-1
- Update to 1.1.7
- Add patch from Debian to fix debian#757798

* Tue Sep 23 2014 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-4
- Admesh 0.98.1 compatibility patch

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.6-3
- Perl 5.20 rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-1
- Update to 1.1.6

* Sun Jun 29 2014 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-1
- Update to 1.1.5
- Unbundle stuff

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 03 2014 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Sun Apr 06 2014 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-1
- 1.0.0 stable

* Wed Mar 19 2014 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.5.RC3
- Instead of single ico file, ship multiple pngs

* Wed Mar 05 2014 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.4.RC3
- New RC version
- Include appdata file

* Thu Jan 02 2014 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.3.RC2
- New RC version
- Remove already merged patches
- Only require Module::Build::WithXSpp 0.13 in Build.PL

* Fri Dec 13 2013 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.2.RC1
- Backported several bugfixes

* Wed Nov 20 2013 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.1.RC1
- 1.0.0RC1 version
- refactor build and install
- become arched
- bundle admesh

* Fri Oct 18 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.10b-5
- For F20+, require Moo >= 1.003001

* Fri Oct 18 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.10b-4
- Remove all filtering from provides, it is not needed anymore
- Don't add MANIFEST to %%doc
- Fix crash when loading config (#1020802)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.10b-2
- Filter perl(Wx::GLCanvas) from requires, it's optional and not yet in Fedora

* Mon Jun 24 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.10b-1
- New upstream release
- Removed some already merged patches

* Tue Apr 23 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-5
- Added BR perl(Encode::Locale)

* Tue Apr 23 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-4
- Removed (optional) Net::DBus usage, that causes crashes

* Tue Apr 23 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-3
- Added second patch to fix upstream issue 1077

* Tue Apr 23 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-2
- Added patch to fix upstream issue 1077

* Wed Apr 03 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-1
- New upstream release
- Added version to perl(Boost::Geometry::Utils) BR
- Sort (B)Rs alphabetically   
- Added (B)R perl(Class::XSAccessor)

* Wed Mar 20 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-4
- Comments added about patches

* Mon Mar 11 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-3
- In-file justification provided for patches

* Mon Jan 21 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-2
- Added patch to grab icons from %%{datadir}/%%{name}
- Added patch to avoid bad locales behavior
- Removed no longer needed filtering perl(Wx::Dialog) from Requires
- Filter perl(XML::SAX::PurePerl) only in F17
- Removed Perl default filter
- Removed bash launcher
- Renamed slic3r.pl to slic3r

* Thu Jan 17 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-1
- New version
- (Build)Requires Math::Clipper 1.17

* Thu Jan 17 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-3
- Updated source to respect GitHub rule
- Dropped mkdir, ln -s, cp, mv, perl macros
- Reorganized %%install section a bit
- Added version to Require perl(Math::Clipper)

* Sat Jan 05 2013 Miro Hrončok <miro@hroncok.cz> - 0.9.7-2
- Added Require perl(Math::Clipper)

* Sun Dec 30 2012 Miro Hrončok <miro@hroncok.cz> - 0.9.7-1
- New version
- Do not download additional sources from GitHub
- Removed deleting empty directories

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 0.9.5-2
- Removed BRs provided by perl package

* Wed Nov 14 2012 Miro Hrončok <miro@hroncok.cz> 0.9.5-1
- New version
- Requires perl(Math::Clipper) >= 1.14
- Requires perl(Math::ConvexHull::MonotoneChain)
- Requires perl(XML::SAX::ExpatXS)

* Thu Oct 04 2012 Miro Hrončok <miro@hroncok.cz> 0.9.3-1
- New package
