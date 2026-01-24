%global use_system_admesh 0
%global use_system_expat 1
%global use_system_polyclipping 1
%global use_system_poly2tri 1

Name:           slic3r
Version:        1.3.0
Release:        %autorelease
Summary:        G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
# Automatically converted from old format: AGPLv3 and CC-BY - review is highly recommended.
License:        AGPL-3.0-only AND LicenseRef-Callaway-CC-BY
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

# Fix build with Boost 1.88, from Debian
# https://github.com/slic3r/Slic3r/issues/5197
Patch12:        https://salsa.debian.org/3dprinting-team/slic3r/-/raw/boost1.88/debian/patches/Fix-FTBFS-with-boost-1.88.patch

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

%patch -p1 -P0
%patch -p1 -P1
%patch -p1 -P2
%patch -p1 -P3 -b .linker
%if %{use_system_polyclipping}
%patch -p1 -P4
%endif
%patch -p1 -P5 -b .fixtest
%patch -p1 -P6
%patch -p1 -P7
%patch -p1 -P8
%patch -p1 -P9
%patch -p1 -P10
%patch -p1 -P11
%patch -p1 -P12

# To avoid "error: exponent has no digits" on GCC 14+
# https://bugzilla.redhat.com/2259542
# https://bugzilla.redhat.com/1321986
# Simplified from https://github.com/slic3r/Slic3r/commit/c8ccc1a38eded78256dd89faee1f82bc9c0888a8
sed -i 's/-std=c++11/-std=gnu++11/' xs/Build.PL

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
%autochangelog
