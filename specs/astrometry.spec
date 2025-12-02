# Parallel make flags on break build
%global _smp_build_ncpus 1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# astropy is not available anymore on i686
ExcludeArch:    %{ix86}


Name:           astrometry
Version:        0.98
Release:        %autorelease
Summary:        Blind astrometric calibration of arbitrary astronomical images

# Software is BSD with some GPL code
# https://groups.google.com/forum/#!topic/astrometry/9GgP7rj4Y-g
# Here we asked to fix source headers:
# https://groups.google.com/forum/#!topic/astrometry/mCuyze3TOeM
# 
# Licensing breakdown
# ===================
#
# See also: file CREDITS in source folder
#
# General license for astrometry and libkd code: 3-clause BSD
#
# GPLv2+:
#    qfits-an/*
#    include/astrometry/qfits*
#    catalogs/ucac4-fits.h
#    util/makefile.jpeg
#    util/md5.c
#    Makefile
#    doc/UCAC3_guide/* (not used for build and not shipped)
#    doc/UCAC4_guide/* (not used for build and not shipped)
#    
#    .fits data files
#
# GPLv3+:
#    blind/an_mm_malloc.h
#    util/ctmf.c
#
License:        BSD-3-Clause and GPL-2.0-or-later and GPL-3.0-or-later
URL:            http://www.astrometry.net

# Upstream sources contains nonfree stuff so we must clean them
# Download original sources from:
# Source0:        https://github.com/dstndstn/%%{name}.net/releases/download/%%{version}/%%{name}.net-%%{version}.tar.gz
# Then use the provided script to clean them with
# ./astrometry-generate-tarball %%{version}
Source0:        %{name}.net-%{version}-clean.tar.xz
Source1:        %{name}-generate-tarball.sh

# data files, ./astrometry-get-data.sh
Source2:        astrometry-data-4107-4119.tar.zst
Source3:        astrometry-data-5206.tar.zst
Source4:        astrometry-data-5205.tar.zst
Source5:        astrometry-get-data.sh

# Patches from Ole Streicher <olebole@debian.org> used on Debian
Patch:          Add-SONAME-to-libastrometry.so.patch
Patch:          Dynamically-link-to-libastrometry.so-when-possible.patch
Patch:          Fix-issues-when-using-Debian-libs-instead-of-convienience.patch
Patch:          Fix-shared-lib-flags-so-that-the-package-can-be-built-on-s390x.patch
Patch:          Don-t-copy-demo-files-to-examples.patch
Patch:          Remove-errornous-generation-of-net-client.py.patch
Patch:          Remove-horizons.py-from-Python-package.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  netpbm-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-astropy
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig
BuildRequires:  xorg-x11-proto-devel

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(wcslib)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       netpbm-progs
Requires:       python3-%{name} = %{version}-%{release}

Recommends:     cfitsio-utils
# User could use own set of index files or another set from upstream.
# Therefore we recommend and not require index-files from Fedora repos.
Recommends:     %{name}-data-4107-4119 = %{version}-%{release}

Provides:       bundled(libkd)
Provides:       bundled(qfits)


%description
The astrometry engine will take any image and return the astrometry
world coordinate system (WCS), a standards-based description of the
transformation between image coordinates and sky coordinates.

Other tools included in the astrometry package can do much more, like
plotting astronomic information over solved images, conversion utilities
or generate statistics from FITS images.


%package data-4107-4119
Summary:        Index files for astrometry (scale 7-19, wide-field)
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}
Obsoletes:      %{name}-data <= %{version}-%{release}
Provides:       %{name}-data = %{version}-%{release}
Obsoletes:      %{name}-data-4207 <= %{version}-%{release}
Provides:       %{name}-data-4207 = %{version}-%{release}
Obsoletes:      %{name}-tycho2 <= 2.0-18
Provides:       %{name}-tycho2 = 2.0-18

%description data-4107-4119
Index files for astrometry built from the Tycho-2 catalog
(scales 7-19, wide-field, from 22 to 2000 arcminutes).


%package data-5206
Summary:        Index files for astrometry (scale 6, 16 to 22 arcmin)
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}
Obsoletes:      %{name}-data-4206 <= %{version}-%{release}
Provides:       %{name}-data-4206 = %{version}-%{release}

%description data-5206
Index files for astrometry built from Tycho-2 + Gaia-DR2 catalogs, light
version (no additional Gaia-DR2 information tagged along).
These indexes are suitable for images from 16 to 22 arcminutes.


%package data-5205
Summary:        Index files for astrometry (scale 5, 11 to 16 arcmin)
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}
Obsoletes:      %{name}-data-4205 <= %{version}-%{release}
Provides:       %{name}-data-4205 = %{version}-%{release}

%description data-5205
Index files for astrometry built from Tycho-2 + Gaia-DR2 catalogs, light
version (no additional Gaia-DR2 information tagged along).
These indexes are suitable for images from 11 to 16 arcminutes.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
%{summary}


%package libs
Summary:        Libraries for %{name}

%description libs
Libraries for %{name}


%package -n python3-%{name}
Summary:        Python modules from %{name}
Requires:       python3-astropy

%description -n python3-%{name}
%{summary}


%prep
%autosetup -p1 -n %{name}.net-%{version}
%setup -T -D -a 2 -n %{name}.net-%{version}
%setup -T -D -a 3 -n %{name}.net-%{version}
%setup -T -D -a 4 -n %{name}.net-%{version}


%build
# Weird symlink required... (also in upstream git)
ln -sf . astrometry

# Parallel make flags on break build
%make_build \
    SYSTEM_GSL=yes \
    NETPBM_INC=-I%{_includedir}/netpbm \
    NETPBM_LIB="-L%{_libdir} -lnetpbm" \
    all py extra


%install
%make_install SYSTEM_GSL=yes \
              INSTALL_DIR=%{buildroot}%{_prefix} \
              PY_BASE_INSTALL_DIR=%{buildroot}%{python3_sitearch}/%{name} \
              INCLUDE_INSTALL_DIR=%{buildroot}%{_includedir}/%{name} \
              LIB_INSTALL_DIR=%{buildroot}%{_libdir} \
              BIN_INSTALL_DIR=%{buildroot}%{_bindir} \
              DATA_INSTALL_DIR=%{buildroot}%{_datadir}/%{name}/data \
              PY_BASE_LINK_DIR=%{python3_sitearch}/%{name} \
              ETC_INSTALL_DIR=%{buildroot}%{_sysconfdir} \
              MAN1_INSTALL_DIR=%{buildroot}%{_mandir}/man1 \
              DOC_INSTALL_DIR=%{buildroot}%{_docdir}/%{name} \
              EXAMPLE_INSTALL_DIR=%{buildroot}%{_datadir}/%{name}/examples

# We need to correct the data dir link in config file
sed -i \
    "s:%{buildroot}%{_prefix}/data:%{_datadir}/%{name}/data:" \
    %{buildroot}/etc/astrometry.cfg

# Rename executables taken from cfitsio code
pushd %{buildroot}%{_bindir}
for exec in imarith imstat listhead liststruc modhead tabmerge tablist; do
        mv $exec astrometry-$exec
done
popd

# Fix python shebangs
%py3_shebang_fix %{buildroot}%{_bindir}/degtohms \
                 %{buildroot}%{_bindir}/hmstodeg \
                 %{buildroot}%{_bindir}/image2pnm \
                 %{buildroot}%{_bindir}/merge-columns \
                 %{buildroot}%{_bindir}/removelines \
                 %{buildroot}%{_bindir}/text2fits \
                 %{buildroot}%{_bindir}/uniformize \
                 %{buildroot}%{_bindir}/votabletofits

# Remove unuseful file
rm -f %{buildroot}%{_docdir}/%{name}/report.txt

# We don't ship static libraries so we remove them
rm -f %{buildroot}%{_libdir}/*.a

# Remove symlink in bin to python script
rm -f %{buildroot}%{_bindir}/plotann.py

# Install data files
install -m0644 astrometry-data*/*.fits %{buildroot}%{_datadir}/%{name}/data


%check
export PYTHON=%{__python3}
make test ARCH_FLAGS="%{optflags}"


%files
%doc CREDITS README.md
%license %{_docdir}/%{name}/LICENSE
%{_mandir}/man1/*
%{_bindir}/an-fitstopnm
%{_bindir}/an-pnmtofits
%{_bindir}/astrometry-engine
%{_bindir}/astrometry-imarith
%{_bindir}/astrometry-imstat
%{_bindir}/astrometry-listhead
%{_bindir}/astrometry-liststruc
%{_bindir}/astrometry-modhead
%{_bindir}/astrometry-tabmerge
%{_bindir}/astrometry-tablist
%{_bindir}/augment-xylist
%{_bindir}/build-astrometry-index
%{_bindir}/downsample-fits
%{_bindir}/fit-wcs
%{_bindir}/fits-column-merge
%{_bindir}/fits-flip-endian
%{_bindir}/fits-guess-scale
%{_bindir}/fitsgetext
%{_bindir}/get-healpix
%{_bindir}/get-wcs
%{_bindir}/hpsplit
%{_bindir}/image2xy
%{_bindir}/new-wcs
%{_bindir}/pad-file
%{_bindir}/plot-constellations
%{_bindir}/plotquad
%{_bindir}/plotxy
%{_bindir}/query-starkd
%{_bindir}/solve-field
%{_bindir}/startree
%{_bindir}/subtable
%{_bindir}/tabsort
%{_bindir}/wcs-grab
%{_bindir}/wcs-match
%{_bindir}/wcs-pv2sip
%{_bindir}/wcs-rd2xy
%{_bindir}/wcs-resample
%{_bindir}/wcs-to-tan
%{_bindir}/wcs-xy2rd
%{_bindir}/wcsinfo
%dir %{_datadir}/astrometry
%dir %{_datadir}/astrometry/data
%{_datadir}/astrometry/examples
%config(noreplace) %{_sysconfdir}/astrometry.cfg

%files data-4107-4119
%{_datadir}/astrometry/data/index-41*.fits

%files data-5206
%{_datadir}/astrometry/data/index-5206*.fits

%files data-5205
%{_datadir}/astrometry/data/index-5205*.fits

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files libs
%license LICENSE
%{_libdir}/*.so.0*

%files -n python3-%{name}
%{python3_sitearch}/%{name}
%{_bindir}/degtohms
%{_bindir}/hmstodeg
%{_bindir}/image2pnm
%{_bindir}/merge-columns
%{_bindir}/removelines
%{_bindir}/text2fits
%{_bindir}/uniformize
%{_bindir}/votabletofits

%changelog
%autochangelog
