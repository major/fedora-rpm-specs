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
Release:        48%{?dist}
Summary:        NCAR Command Language and NCAR Graphics

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.ncl.ucar.edu
Source0:        https://github.com/NCAR/ncl/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        Site.local.ncl
Source2:        ncarg.csh
Source3:        ncarg.sh
ExcludeArch:    %{ix86}

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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 08 2024 Sandro Mani <manisandro@gmail.com> - 6.6.2-47
- Rebuild (gdal)

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 6.6.2-46
- Rebuild for hdf5 1.14.5

* Wed Oct 02 2024 Orion Poplawski <orion@nwra.com> - 6.6.2-45
- Add patch to fix build with hdf 4.3

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 6.6.2-44
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 13 2024 Sandro Mani <manisandro@gmail.com> - 6.6.2-42
- Rebuild (gdal)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Orion Poplawski <orion@nwra.com> - 6.6.2-39
- Rebuild for jasper 4.1

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 6.6.2-38
- Rebuild (gdal)

* Tue Aug 29 2023 Florian Weimer <fweimer@redhat.com> - 6.6.2-37
- Set build_type_safety_c to 0 (#2145150)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 6.6.2-35
- Rebuild (gdal)

* Thu Mar 30 2023 Orion Poplawski <orion@nwra.com> - 6.6.2-34
- Drop i686 builds

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 6.6.2-32
- Rebuild (gdal)

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 6.6.2-31
- Rebuild (gdal)

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.6.2-30
- Rebuild for gsl-2.7.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 6.6.2-28
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 6.6.2-27
- Rebuild for proj-9.0.0

* Sun Feb 13 2022 Josef Ridky <jridky@redhat.com> - 6.6.2-26
- Rebuilt for libjasper.so.6

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Orion Poplawski <orion@nwra.com> - 6.6.2-24
- Rebuild for hdf5 1.12.1

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 6.6.2-23
- Rebuild (gdal)

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 6.6.2-22
- Rebuild for hdf5 1.10.7/netcdf 4.8.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 6.6.2-20
- Rebuild (gdal)

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 6.6.2-19
- Rebuild (proj)

* Mon Feb  1 2021 Orion Poplawski <orion@nwra.com> - 6.6.2-18
- Use flexiblas and "-fallow-argument-mismatch -fcommon" on EL9+

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 12:49:29 CET 2020 Sandro Mani <manisandro@gmail.com> - 6.6.2-16
- Rebuild (proj, gdal)

* Thu Sep 17 2020 Orion Poplawski <orion@nwra.com> - 6.6.2-15
- Use %%make_install

* Fri Aug 14 2020 Iñaki Úcar <iucar@fedoraproject.org> - 6.6.2-14
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Orion Poplawski <orion@nwra.com> - 6.6.2-12
- Change link order to fix issue with gdal and g2clib (bz#1856959)

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 6.6.2-11
- Rebuild for hdf5 1.10.6

* Fri Jun  5 2020 Orion Poplawski <orion@nwra.com> - 6.6.2-10
- Add extra needed symlinks to /usr/lib/ncarg (bz#1288083)

* Thu Jun  4 2020 Orion Poplawski <orion@nwra.com> - 6.6.2-9
- Fix format patch

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 6.6.2-8
- Rebuild (gdal)

* Thu Apr 30 2020 Orion Poplawski <orion@nwra.com> - 6.6.2-7
- Rebuild for gdal 3

* Tue Mar 17 2020 Orion Poplawski <orion@nwra.com> - 6.6.2-6
- Use work arounds and patch to fix FTBFS with gcc 10 (bz#1799675)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 6.6.2-5
- Rebuild (gdal)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Orion Poplawski <orion@nwra.com> - 6.6.2-3
- Rebuild for proj 6.2.0

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.6.2-2
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Orion Poplawski <orion@nwra.com> - 6.6.2-1
- Update to 6.6.2
- Build with openblas (bugz#1619049)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 6.5.0-4
- Rebuild for netcdf 4.6.3

* Thu Feb 07 2019 Orion Poplawski <orion@cora.nwra.com> - 6.5.0-3
- Rebuild for proj 5.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 29 2018 Orion Poplawski <orion@cora.nwra.com> - 6.5.0-1
- Update to 6.5.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 2 2018 Orion Poplawski <orion@nwra.com> - 6.4.0-5
- Handle different g2clib names

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 7 2017 Orion Poplawski <orion@cora.nwra.com> - 6.4.0-1
- Update to 6.4.0

* Mon Feb 06 2017 Orion Poplawski <orion@cora.nwra.com> - 6.3.0-11
- Rebuild for gcc 7

* Sun Dec 04 2016 Orion Poplawski <orion@cora.nwra.com> - 6.3.0-10
- Rebuild for jasper 2.0

* Thu Sep 29 2016 Orion Poplawski <orion@cora.nwra.com> - 6.3.0-9
- Make ncl-devel require cairo-devel

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 6.3.0-7
- Rebuild for netcdf 4.4.0

* Sun Sep 13 2015 Peter Robinson <pbrobinson@fedoraproject.org> 6.3.0-6
- Fix FTBFS on aarch64

* Mon Jul 27 2015 Orion Poplawski <orion@cora.nwra.com> - 6.3.0-5
- Rebuild for gdal 2.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 6.3.0-3
- Rebuild for hdf5 1.8.15

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.3.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 19 2015 Orion Poplawski - 6.3.0-1
- Update to 6.3.0

* Thu Jan 08 2015 Orion Poplawski <orion@cora.nwra.com> - 6.2.1-2
- Rebuild for hdf5 1.8.14

* Fri Sep 5 2014 Orion Poplawski - 6.2.1-1
- Update to 6.2.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 4 2014 Orion Poplawski - 6.2.0-1
- Update to 6.2.0
- Compile with -fopenmp

* Fri Jan 31 2014 Orion Poplawski - 6.1.2-6
- Fix build with -Werror=format-security (bug #1037211)

* Sun Sep 22 2013 Orion Poplawski - 6.1.2-5
- Rebuild for atlas 3.10

* Tue Aug 27 2013 Orion Poplawski - 6.1.2-4
- Rebuild for gdal 1.10.0

* Wed Jul 31 2013 Orion Poplawski <orion@cora.nwra.com> - 6.1.2-3
- Build for arm

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 6.1.2-2
- Rebuild for hdf5 1.8.11

* Thu Feb 7 2013 Orion Poplawski <orion@cora.nwra.com> - 6.1.2-1
- Update to 6.1.2

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 6.1.0-2
- rebuild due to "jpeg8-ABI" feature drop

* Wed Oct 31 2012 Orion Poplawski <orion@cora.nwra.com> - 6.1.0-1
- Update to 6.1.0
- Drop xwd patch applied upstream

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Orion Poplawski <orion@cora.nwra.com> - 6.0.0-6
- Don't link against librx, was causing memory corruption
- Compile with -fno-strict-aliasing for now

* Fri Jul 13 2012 Orion Poplawski <orion@cora.nwra.com> - 6.0.0-5
- Add patch to fix xwd driver on 64-bit (bug 839707)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 6.0.0-3
- Rebuild for new libpng

* Thu Sep 29 2011 - Orion Poplawski <orion@cora.nwra.com> - 6.0.0-2
- Use system udunits by linking it into where ncl expects it, drop
  udunits patch.  Fixes bug 742307.

* Thu Sep 1 2011 - Orion Poplawski <orion@cora.nwra.com> - 6.0.0-1
- Update to 6.0.0 final

* Wed May 18 2011 - Orion Poplawski <orion@cora.nwra.com> - 6.0.0-0.2.beta
- Rebuild for hdf5 1.8.7

* Thu Mar 31 2011 - Orion Poplawski <orion@cora.nwra.com> - 6.0.0-0.1.beta
- Update to 6.0.0-beta
- Enable cairo and gdal support

* Fri Feb 18 2011 - Orion Poplawski <orion@cora.nwra.com> - 5.2.1-6
- Rebuild for new g2clib - fix grib handling on 64-bit machines

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 - Orion Poplawski <orion@cora.nwra.com> - 5.2.1-5
- No flex-static in EL

* Mon Nov 22 2010 - Orion Poplawski <orion@cora.nwra.com> - 5.2.1-4
- Add BR flex-static

* Mon Nov 22 2010 - Orion Poplawski <orion@cora.nwra.com> - 5.2.1-3
- Add compatibility links to /usr/lib/ncarg

* Mon Sep 6 2010 - Dan Horák <dan[at]danny.cz> - 5.2.1-2
- Recognize Fedora secondary architectures

* Tue Aug 10 2010 - Orion Poplawski <orion@cora.nwra.com> - 5.2.1-1
- Update to 5.2.1
- Update udunits patch

* Thu Jul 1 2010 - Orion Poplawski <orion@cora.nwra.com> - 5.2.0-2
- Drop BR libnc-dap and update lib patch to remove unneeded libraries

* Wed Apr 28 2010 - Orion Poplawski <orion@cora.nwra.com> - 5.2.0-1
- Update to 5.2.0
- Update libs patch
- Fixup profile script packaging

* Tue Feb 16 2010 - Orion Poplawski <orion@cora.nwra.com> - 5.1.1-6
- Add patch to fix FTBFS bug #564856

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 5.1.1-5
- Same as below with hdf-static
- Explicitly BR g2clib-static in accordance with the Packaging
  Guidelines (g2clib-devel is still static-only).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.1.1-2
- Rebuild for libdap 3.9.3

* Mon Jul 13 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.1.1-1
- Update to 5.1.1

* Tue Jul 7 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.1.0-4
- Fixup more paths in shipped ncl scripts (bug #505240)

* Tue May 26 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.1.0-3
- Move database back to main arch dependent package
 
* Tue May 19 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.1.0-2
- Set NCARG_NCARG to /usr/share/ncarg
- Move fontcaps and graphcaps back to main arch dependent package

* Thu Mar 5 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.1.0-1
- Update to 5.1.0
- Rebase ppc64, netcdff patch
- Drop triangle, flex, hdf, png, wrapit, uint32 patch upstreamed

* Tue Feb 24 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-19
- Rebuild for gcc 4.4.0 and other changes
- Move data files into noarch sub-package
- Make examples sub-package noarch

* Mon Feb 2 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-18
- Fix unowned directory (bug #483468)

* Mon Dec 15 2008 Deji Akingunola <dakingun@gmail.com> - 5.0.0-17
- Rebuild for atlas-3.8.2

* Fri Dec 12 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-16
- Re-add profile.d startup scripts to set NCARG env variables

* Mon Dec 8 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-15
- Try changing the udunits path in config/Project

* Thu Dec 4 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-14
- Actually apply udunits patch

* Thu Nov 27 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-13
- Enable udunits support add use system udunits.dat

* Thu Sep 11 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-12
- Rebuild for new libdap
- Fix netcdf include location

* Fri Apr 11 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-11
- Add patch to fix raster image problems on non 32-bit platforms
- Add more includes to includes patch

* Thu Mar 27 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-10
- Add patch to fixup some missing includes
- Define _ISOC99_SOURCE to expose vsnprintf prototype
- Update hdf patch to remove hdf/netcdf.h include

* Mon Feb 18 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-9
- Rename Site.local to Site.local.ncl
- Add comment for imake BR

* Wed Feb  6 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-8
- Move examples into separate sub-package

* Fri Feb  1 2008 - Patrice Dumas <pertusus@free.fr> - 5.0.0-7
- put noarch files in datadir
- avoid compilation in %%install

* Mon Jan 14 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-6
- Make BR hdf-devel >= 4.2r2.

* Fri Dec 14 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-5
- Fixup wrapit flex compilation

* Fri Dec 14 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-4
- Actually get ncl to build

* Sun Nov 18 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-3
- Move robj to -devel
- Provide ncl-static in ncl-devel
- Turn on BuildUdunits.  Turn off BuildV5D.
- Drop config/LINUX patch, use sed

* Wed Nov 14 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-2
- Fixup profile.d script permissions, Group, move aed.a to devel

* Tue Nov  6 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.0.0-1
- Initial ncl package, based on ncarg
