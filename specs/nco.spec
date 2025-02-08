%global builddocs 1

Name:           nco
Version:        5.3.2
Release:        %autorelease
Summary:        Suite of programs for manipulating NetCDF/HDF4 files
License:        BSD-3-Clause
URL:            http://nco.sourceforge.net/

Source0:        https://github.com/nco/nco/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         nco-install_C_headers.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  bison, flex, gawk
BuildRequires:  netcdf-devel
%ifarch %java_arches
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  antlr-C++
%else
BuildRequires:  antlr
%endif
%endif
BuildRequires:  chrpath
BuildRequires:  gsl-devel
BuildRequires:  texinfo
BuildRequires:  udunits2-devel
%if 0%{?builddocs}
BuildRequires:  texinfo-tex
%endif

%package devel
Summary:        Development files for NCO
Requires:       %{name} = %{version}-%{release}

%package static
Summary:        Static libraries for NCO
Requires:       %{name}-devel = %{version}-%{release}

%description
The netCDF Operators, NCO, are a suite of command line programs known
as operators.  The operators facilitate manipulation and analysis of
self-describing data stored in the freely available netCDF and HDF
formats (http://www.unidata.ucar.edu/packages/netcdf and
http://hdf.ncsa.uiuc.edu, respectively).  Each NCO operator (e.g.,
ncks) takes netCDF or HDF input file(s), performs an operation (e.g.,
averaging, hyperslabbing, or renaming), and outputs a processed netCDF
file.  Although most users of netCDF and HDF data are involved in
scientific research, these data formats, and thus NCO, are generic and
are equally useful in fields from agriculture to zoology.  The NCO
User's Guide illustrates NCO use with examples from the field of
climate modeling and analysis.  The NCO homepage is
http://nco.sourceforge.net/.

%description devel
This package contains the NCO header and development files.

%description static
This package contains the NCO static libs.

%prep
%setup -q
%patch -P0 -p1 -b .install_C_headers


%build
export CPPFLAGS=-I%{_includedir}/udunits2
%configure \
%ifarch %java_arches
  HAVE_ANTLR=yes \
%endif
  --disable-dependency-tracking --includedir=%{_includedir}/nco
%make_build
%if 0%{?builddocs}
make -C doc html pdf
%endif


%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
# Ignore non-ELF files
chrpath -d -k $RPM_BUILD_ROOT%{_bindir}/* || :


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license doc/LICENSE
%doc README* doc/rtfm.txt doc/nco.html doc/nco.pdf doc/nco.css
%doc doc/index.shtml doc/TODO doc/ChangeLog doc/nco.png doc/nco_news.shtml
%doc doc/nsf.png
%ifarch %java_arches
%{_bindir}/ncap2
%endif
%{_bindir}/ncatted
%{_bindir}/ncbo
%{_bindir}/ncchecker
%{_bindir}/ncclimo
%{_bindir}/ncdiff
%{_bindir}/ncea
%{_bindir}/ncecat
%{_bindir}/nces
%{_bindir}/ncflint
%{_bindir}/ncks
%{_bindir}/ncpdq
%{_bindir}/ncra
%{_bindir}/ncrcat
%{_bindir}/ncremap
%{_bindir}/ncrename
%{_bindir}/ncwa
%{_bindir}/ncz2psx
%{_mandir}/man1/ncap2.1*
%{_mandir}/man1/ncatted.1*
%{_mandir}/man1/ncbo.1*
%{_mandir}/man1/ncchecker.1*
%{_mandir}/man1/ncclimo.1*
%{_mandir}/man1/ncecat.1*
%{_mandir}/man1/nces.1*
%{_mandir}/man1/ncflint.1*
%{_mandir}/man1/ncks.1*
%{_mandir}/man1/nco.1*
%{_mandir}/man1/ncpdq.1*
%{_mandir}/man1/ncra.1*
%{_mandir}/man1/ncrcat.1*
%{_mandir}/man1/ncremap.1*
%{_mandir}/man1/ncrename.1*
%{_mandir}/man1/ncwa.1*
%{_mandir}/man1/ncz2psx.1*
%{_infodir}/*
%{_libdir}/libnco*[0-9]*.so

%files devel
%{_libdir}/libnco.so

%files static
%{_libdir}/libnco*.a


%changelog
%autochangelog
