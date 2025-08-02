%if 0%{?fedora} || 0%{?rhel} >= 9
%bcond_without flexiblas
%endif
%if %{with flexiblas}
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:           ncl
Version:        6.6.2
Release:        %autorelease
Summary:        NCAR Command Language and NCAR Graphics

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.ncl.ucar.edu
Source0:        https://github.com/NCAR/ncl/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        Site.local.ncl
Source2:        ncarg.csh
Source3:        ncarg.sh
# Fails to build on ppc64le with error: detected recursion whilst expanding macro ‘vector’
ExcludeArch:    %{ix86} ppc64le

# ymake uses cpp with some defines on the command line to generate a 
# Makefile which consists in:
#  Template: command line defines
#  Site.conf
#  LINUX
#  Site.conf
#  Template: generic defaults, including default paths
#  Project
#  Rules
#  yMakefile
#  Template: some rules
#
# install paths are set up in Project. Paths used in code are also in 
# Project, in NGENV_DESCRIPT.
Patch0:         ncl-5.1.0-paths.patch
# https://github.com/NCAR/ncl/pull/134
Patch1:         ncarg-4.4.1-deps.patch
Patch2:         ncl-5.1.0-ppc64.patch
# Add needed -lm to ictrans build, remove unneeded -lrx -lidn -ldl from ncl
Patch3:         ncl-libs.patch
# -Werror=format-security
# https://github.com/NCAR/ncl/pull/108
Patch4:         ncl-format.patch
# Fix use of BOZ constans
Patch5:         ncl-boz.patch
# Change link order of g2clib and gdal to work around gdal's modified g2_getfld()
# https://bugzilla.redhat.com/show_bug.cgi?id=1856959
# https://github.com/OSGeo/gdal/issues/2775
Patch6:         ncl-gdal.patch
# Drop unused headers removed from hdf 4.3
# https://github.com/NCAR/ncl/pull/209
Patch7:         ncl-hdf4.3.patch
# Fixes for gcc15
Patch8:         ncl-gcc15.patch
# don't have the installation target depends on the build target since
# for library it implies running ranlib and modifying the library timestamp
Patch10:        ncl-5.0.0-no_install_dep.patch
# put install and build rules before script rules such that the default rule
# is all
# https://github.com/NCAR/ncl/pull/135
Patch11:        ncl-5.0.0-build_n_scripts.patch
Patch12:        ncl-5.1.0-netcdff.patch
# https://github.com/NCAR/ncl/pull/136
Patch13:        ncl-5.1.0-includes.patch
# Add Fedora secondary arches
Patch16:        ncl-5.2.1-secondary.patch
# Fix build with proj8
Patch17:        ncl-proj8.patch

BuildRequires:  /bin/csh
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  netcdf-fortran-devel
BuildRequires:  cairo-devel
BuildRequires:  hdf-static, hdf-devel >= 4.2r2
BuildRequires:  g2clib-static
BuildRequires:  gdal-devel >= 2.2
BuildRequires:  gsl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  proj-devel
# imake needed for makedepend
BuildRequires:  imake, libXt-devel, libXaw-devel, libXext-devel, libXpm-devel
BuildRequires:  byacc, flex
BuildRequires:  flex-static
BuildRequires:  %{blaslib}-devel
BuildRequires:  udunits2-devel
Requires:       %{name}-common = %{version}-%{release}
Requires:       udunits2

Provides:       ncarg = %{version}-%{release}
Obsoletes:      ncarg < %{version}-%{release}


%description
NCAR Command Language (NCL) is an interpreted language designed specifically
for scientific data processing and visualization.  Portable, robust, and free,
NCL supports netCDF3/4, GRIB1/2, HDF-SDS, HDF4-EOS, binary, shapefiles, and
ASCII files.  Numerous analysis functions are built-in.  High quality graphics
are easily created and customized with hundreds of graphic resources.  Many
example scripts and their corresponding graphics are available.


%package common
Summary:        Common files for NCL and NCAR Graphics
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description common
%{summary}.


%package devel
Summary:        Development files for NCL and NCAR Graphics
Requires:       %{name} = %{version}-%{release}
Requires:       cairo-devel
Provides:       ncl-static = %{version}-%{release}
Provides:       ncarg-devel = %{version}-%{release}
Obsoletes:      ncarg-devel < %{version}-%{release}

%description devel
%{summary}.


%package examples
Summary:        Example programs and data using NCL
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description examples
Example programs and data using NCL.


%prep
%setup -q -n ncl-%{version}
%patch -P0 -p1 -b .paths
%patch -P1 -p1 -b .deps
%patch -P2 -p1 -b .ppc64
%patch -P3 -p1 -b .libs
%patch -P4 -p1 -b .format
%patch -P5 -p1 -b .boz
%patch -P6 -p1 -b .gdal
%patch -P7 -p1 -b .hdf
%patch -P8 -p1 -b .gcc15
%patch -P10 -p1 -b .no_install_dep
%patch -P11 -p1 -b .build_n_scripts
%patch -P12 -p1 -b .netcdff
%patch -P13 -p1 -b .includes
%patch -P16 -p1 -b .secondary
%patch -P17 -p1 -b .proj

sed -ri -e 's,-lblas_ncl,-l%{blaslib},' \
        -e 's,-llapack_ncl,-l%{blaslib},' config/Project
#Spurrious exec permissions
find -name '*.[fh]' -exec chmod -x {} +

#Use ppc config if needed
%ifarch ppc ppc64
cp config/LINUX.ppc32.GNU config/LINUX
%endif

#Fixup LINUX config (to expose vsnprintf prototype)
sed -i -e '/StdDefines/s/-DSYSV/-D_ISOC99_SOURCE/' config/LINUX

rm -rf external/blas external/lapack

# fix the install directories, etc.
sed -e 's;@prefix@;%{_prefix};' \
 -e 's;@mandir@;%{_mandir};' \
 -e 's;@datadir@;%{_datadir};' \
 -e 's;@libdir@;%{_libdir};' \
 -e 's;@g2clib@;%{g2clib};' \
 %{SOURCE1} > config/Site.local

#Setup the profile scripts
cp %{SOURCE2} %{SOURCE3} .
sed -i -e s,@LIB@,%{_lib},g ncarg.csh ncarg.sh

sed -i -e 's;load "\$NCARG_ROOT/lib/ncarg/nclex\([^ ;]*\);loadscript(ncargpath("nclex") + "\1);' \
    -e 's;"\$NCARG_ROOT/lib/ncarg/\(data\|database\);ncargpath("\1") + ";' \
    -e 's;\$NCARG_ROOT/lib/ncarg/nclscripts;$NCARG_ROOT/share/ncarg/nclscripts;' \
    `find ni/src -name \*.ncl`


%build
# short-cicuit:
./config/ymkmf

# ./config/ymkmf could be also short circuited, since it does:
# (cd ./config; make -f Makefile.ini clean all)
# ./config/ymake -config ./config -Curdir . -Topdir .

# The package does not build in strict C99 mode.  See bug 2145150.
%global build_type_safety_c 0

FCOPTIONS="$RPM_OPT_FLAGS -fPIC -fno-second-underscore -fno-range-check -fopenmp"
%if 0%{?fedora} || 0%{?rhel} >= 9
FCOPTIONS="$FCOPTIONS -fallow-argument-mismatch -fcommon"
%endif
make Build CCOPTIONS="$RPM_OPT_FLAGS -std=c99 -fPIC -fno-strict-aliasing -fopenmp -fcommon -DH5_USE_110_API" \
 F77=gfortran F77_LD=gfortran CTOFLIBS="-lgfortran" FCOPTIONS="$FCOPTIONS" COPT= FOPT=


%install
export NCARG=`pwd`
%make_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 0644 ncarg.csh ncarg.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
# database, fontcaps, and graphcaps are arch dependent
for x in {database,{font,graph}caps}
do
  mv $RPM_BUILD_ROOT%{_datadir}/ncarg/$x $RPM_BUILD_ROOT%{_libdir}/ncarg/
  ln -s ../../%{_lib}/ncarg/$x $RPM_BUILD_ROOT%{_datadir}/ncarg/
done
# Compat links for what is left
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/ncarg
for x in $RPM_BUILD_ROOT%{_datadir}/ncarg/*
do
  [ ! -e $RPM_BUILD_ROOT%{_prefix}/lib/ncarg/$(basename $x) ] &&
    ln -s ../../share/ncarg/$(basename $x) $RPM_BUILD_ROOT%{_prefix}/lib/ncarg/
done
# Use system udunits
rm -r $RPM_BUILD_ROOT%{_datadir}/ncarg/udunits
ln -s ../udunits $RPM_BUILD_ROOT%{_datadir}/ncarg/
# Don't conflict with allegro-devel (generic API names)
for manpage in $RPM_BUILD_ROOT%{_mandir}/man3/*
do
   manname=`basename $manpage`
   mv $manpage $RPM_BUILD_ROOT%{_mandir}/man3/%{name}_$manname
done



%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/profile.d/ncarg.*sh
%{_bindir}/ConvertMapData
%{_bindir}/WriteLineFile
%{_bindir}/WriteNameFile
%{_bindir}/WritePlotcharData
%{_bindir}/cgm2ncgm
%{_bindir}/ctlib
%{_bindir}/ctrans
%{_bindir}/ezmapdemo
%{_bindir}/fcaps
%{_bindir}/findg
%{_bindir}/fontc
%{_bindir}/gcaps
%{_bindir}/graphc
%{_bindir}/ictrans
%{_bindir}/idt
%{_bindir}/med
%{_bindir}/ncargfile
%{_bindir}/ncargpath
%{_bindir}/ncargrun
%{_bindir}/ncargversion
%{_bindir}/ncargworld
%{_bindir}/ncarlogo2ps
%{_bindir}/ncarvversion
%{_bindir}/ncgm2cgm
%{_bindir}/ncgmstat
%{_bindir}/ncl
%{_bindir}/ncl_convert2nc
%{_bindir}/ncl_filedump
%{_bindir}/ncl_grib2nc
%{_bindir}/ncl_quicklook
%{_bindir}/nnalg
%{_bindir}/pre2ncgm
%{_bindir}/pre2ncgm.prog
%{_bindir}/psblack
%{_bindir}/psplit
%{_bindir}/pswhite
%{_bindir}/pwritxnt
%{_bindir}/ras2ccir601
%{_bindir}/rascat
%{_bindir}/rasgetpal
%{_bindir}/rasls
%{_bindir}/rassplit
%{_bindir}/rasstat
%{_bindir}/rasview
%{_bindir}/tdpackdemo
%{_bindir}/tgks0a
%{_bindir}/tlocal
%{_libdir}/ncarg/database/
%{_libdir}/ncarg/fontcaps/
%{_libdir}/ncarg/graphcaps/
%if "%{_lib}" != "lib"
%{_prefix}/lib/ncarg/database
%{_prefix}/lib/ncarg/fontcaps
%{_prefix}/lib/ncarg/graphcaps
%endif

%files common
%dir %{_datadir}/ncarg
%{_datadir}/ncarg/colormaps/
%{_datadir}/ncarg/data/
%{_datadir}/ncarg/database
%{_datadir}/ncarg/fontcaps
%{_datadir}/ncarg/graphcaps
%{_datadir}/ncarg/grib2_codetables/
%{_datadir}/ncarg/grib2_codetables.previous/
%{_datadir}/ncarg/nclscripts/
%{_datadir}/ncarg/ngwww/
%{_datadir}/ncarg/sysresfile
%{_datadir}/ncarg/udunits
%{_datadir}/ncarg/xapp/
%dir %{_prefix}/lib/ncarg
%{_prefix}/lib/ncarg/colormaps
%{_prefix}/lib/ncarg/data
%{_prefix}/lib/ncarg/grib2_codetables
%{_prefix}/lib/ncarg/grib2_codetables.previous
%{_prefix}/lib/ncarg/nclscripts
%{_prefix}/lib/ncarg/ngwww
%{_prefix}/lib/ncarg/sysresfile
%{_prefix}/lib/ncarg/udunits
%{_prefix}/lib/ncarg/xapp
%{_mandir}/man1/*.gz
%{_mandir}/man5/*.gz
%{_bindir}/scrip_check_input

%files devel
%{_bindir}/MakeNcl
%{_bindir}/WRAPIT
%{_bindir}/ncargcc
%{_bindir}/ncargf77
%{_bindir}/ncargf90
%{_bindir}/nhlcc
%{_bindir}/nhlf77
%{_bindir}/nhlf90
%{_bindir}/wrapit77
%{_includedir}/ncarg/
%dir %{_libdir}/ncarg
%{_libdir}/ncarg/libcgm.a
%{_libdir}/ncarg/libfftpack5_dp.a
%{_libdir}/ncarg/libhlu.a
%{_libdir}/ncarg/libncarg.a
%{_libdir}/ncarg/libncarg_c.a
%{_libdir}/ncarg/libncarg_gks.a
%{_libdir}/ncarg/libncarg_ras.a
%{_libdir}/ncarg/libncl.a
%{_libdir}/ncarg/libnclapi.a
%{_libdir}/ncarg/libngmath.a
%{_libdir}/ncarg/libnfp.a
%{_libdir}/ncarg/libnfpfort.a
%{_libdir}/ncarg/libnio.a
%{_libdir}/ncarg/libsphere3.1_dp.a
%{_libdir}/ncarg/ncarg/
%{_mandir}/man3/*.gz

%files examples
%{_bindir}/ncargex
%{_bindir}/ng4ex
%{_datadir}/ncarg/examples/
%{_datadir}/ncarg/hluex/
%{_datadir}/ncarg/nclex/
%{_datadir}/ncarg/resfiles/
%{_datadir}/ncarg/tests/
%{_datadir}/ncarg/tutorial/
%{_prefix}/lib/ncarg/examples
%{_prefix}/lib/ncarg/hluex
%{_prefix}/lib/ncarg/nclex
%{_prefix}/lib/ncarg/resfiles
%{_prefix}/lib/ncarg/tests
%{_prefix}/lib/ncarg/tutorial


%changelog
%autochangelog
