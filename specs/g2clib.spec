%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:           g2clib
Version:        1.6.3
Release:        %autorelease
Summary:        GRIB2 encoder/decoder and search/indexing routines in C

License:        LicenseRef-Fedora-Public-Domain
URL:            http://www.nco.ncep.noaa.gov/pmb/codes/GRIB2/
Source0:        http://www.nco.ncep.noaa.gov/pmb/codes/GRIB2/g2clib-%{version}.tar
Source1:        g2clib-msg.txt
# Patch to fix up type detection and printf arguments on 64-bit machines
Patch0:         g2clib-64bit.patch
# Patch to remove multiple definitions of templates
Patch1:         g2clib-templates.patch
# Patch from Wesley Ebisuzaki <wesley.ebisuzaki@noaa.gov> to fix sigfault
# if simunpack() is called with 0 values to unpack
Patch2:         g2clib-simunpack.patch
# Patch from degrib - appears to fix projection issues
Patch3:         g2clib-degrib.patch
# Fix build with Jasper 2
Patch4:         g2clib-jasper2.patch
# jasper3 now hides internal encoder / decoder. Use wrapper entry point
# c.f. https://github.com/jasper-software/jasper/commit/5fe57ac5829ec31396e7eaab59a688da014660af
Patch5:         g2clib-1.6.3-jasper3-use-wrapper-entry-point.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libpng-devel jasper-devel
ExcludeArch:    %{ix86}

# static only library - no debuginfo
%global debug_package %{nil}

%if %{lua: print(rpm.vercmp(rpm.expand("%version"),"1.6.0"))} >= 0
%global g2clib g2c_v%{version}
%else
%global g2clib grib2c
%endif

%description
This library contains "C" decoder/encoder
routines for GRIB edition 2.  The user API for the GRIB2 routines
is described in ASCII file "grib2c.doc".


%package        devel
Summary:        Development files for %{name}
#Requires:       %%{name} = %%{version}-%%{release}
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
Requires:       jasper-devel%{?_isa}
Requires:       libpng-devel%{?_isa}

%description    devel
This library contains "C" decoder/encoder
routines for GRIB edition 2.  The user API for the GRIB2 routines
is described in file "grib2c.doc".

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch -P0 -p1 -b .64bit
%patch -P1 -p1 -b .templates
%patch -P2 -p1 -b .simunpack
%patch -P3 -p1 -b .degrib
%patch -P4 -p1 -b .jasper2
%patch -P5 -p1 -b .jasper3_internal
chmod a-x *.h *.c README CHANGES grib2c.doc makefile
cp -p %{SOURCE1} .


%build
CFLAGS="$RPM_OPT_FLAGS -DUSE_PNG -DUSE_JPEG2000"

%ifarch sparc64 s390x %{mips64}
CFLAGS="$CFLAGS -D__64BIT__ -fPIC"
%endif
%ifarch x86_64 ia64 %{power64} aarch64
CFLAGS="$CFLAGS -D__64BIT__ -fpic"
%endif
%ifarch %{ix86} %{arm} %{mips32}
CFLAGS="$CFLAGS -fpic"
%endif

make CFLAGS="$CFLAGS" CC="%{__cc}" ARFLAGS=


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 lib%{g2clib}.a $RPM_BUILD_ROOT%{_libdir}
install -p -m0644 grib2.h $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 drstemplates.h $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 gridtemplates.h $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 pdstemplates.h $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{macrosdir}
echo %%g2clib %g2clib > $RPM_BUILD_ROOT%{macrosdir}/macros.g2clib


%files devel
%doc README CHANGES grib2c.doc g2clib-msg.txt
#%%{_libdir}/libgrib2c.a
%{_libdir}/lib%{g2clib}.a
%{_includedir}/grib2.h
%{_includedir}/drstemplates.h
%{_includedir}/gridtemplates.h
%{_includedir}/pdstemplates.h
%{macrosdir}/macros.g2clib


%changelog
%autochangelog
