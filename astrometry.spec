# Bootstrap option, we have to build astrometry before we can generate index
# files, but later package will require them for tests at build time
%global bootstrap 1

# Parallel make flags on break build
%global _smp_build_ncpus 1


Name:           astrometry
Version:        0.94
Release:        6%{?dist}
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
# General license for astrometry code: 3-clause BSD
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
#    2MASS data files index-42xx.fits
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

# 2MASS data files, ./astrometry-get-data.sh
Source2:        astrometry-data-4204.tar.xz
Source3:        astrometry-data-4205.tar.xz
Source4:        astrometry-data-4206.tar.xz
Source5:        astrometry-data-4207.tar.xz
Source6:        astrometry-data-4208-4219.tar.xz
Source7:        astrometry-get-data.sh

Patch:          numpy-distutils-removal.patch

# Patches from Ole Streicher <olebole@debian.org> used on Debian
Patch:          %{name}-0.89_Add-SONAME-to-libastrometry.so.patch
Patch:          %{name}-0.89_Dynamically-link-to-libastrometry.so-when-possible.patch
Patch:          %{name}-0.89_Fix-issues-when-using-Debian-libs-instead-of-convienience.patch
Patch:          %{name}-0.91_Fix-shared-lib-flags-so-that-the-package-can-be-built-on-.patch
Patch:          %{name}-0.89_Don-t-copy-demo-files-to-examples.patch
Patch:          %{name}-0.89_Remove-errornous-generation-of-net-client.py.patch

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

%if ! 0%{?bootstrap}
BuildRequires:  astrometry-tycho2
%endif

Requires:       %{name}-data = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       netpbm-progs
Requires:       python3-%{name} = %{version}-%{release}

# User could use own set of index files or another set from upstream.
# Therefore we suggest and not require astrometry-tycho2 here
Suggests:       astrometry-tycho2

Provides:       bundled(libkd)
Provides:       bundled(qfits)

# FIXME
# Kill s390x build for now, s390x build seems unknown
# "cpio: read failed - Inappropriate ioctl for device" error
# when unpacking srpm
# ExcludeArch:	s390x

%description
The astrometry engine will take any image and return the astrometry
world coordinate system (WCS), a standards-based description of the
transformation between image coordinates and sky coordinates.

Other tools included in the astrometry package can do much more, like
plotting astronomic information over solved images, convertion utilities
or generate statistics from FITS images.


%package data
Summary:        2MASS catalog index files for astrometry (4208-4129, wide-field)
License:        GPLv2+
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-data-4208-4219 = %{version}-%{release}

%description data
2MASS index files 4208-4219 (wide-field, 30-2000 arcminutes) for astrometry.


%package data-4204
Summary:        2MASS catalog index files (4204 series) for astrometry
License:        GPLv2+
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}

%description data-4204
2MASS index files (4204 series) with 8-11 arcminutes skymarks for astrometry.


%package data-4205
Summary:        2MASS catalog index files (4205 series) for astrometry
License:        GPLv2+
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}

%description data-4205
2MASS index files (4205 series) with 11-16 arcminutes skymarks for astrometry.


%package data-4206
Summary:        2MASS catalog index files (4206 series) for astrometry
License:        GPLv2+
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}

%description data-4206
2MASS index files (4206 series) with 16-22 arcminutes skymarks for astrometry.


%package data-4207
Summary:        2MASS catalog index files (4207 series) for astrometry
License:        GPLv2+
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}

%description data-4207
2MASS index files (4207 series) with 22-30 arcminutes skymarks for astrometry.


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
%setup -T -D -a 5 -n %{name}.net-%{version}
%setup -T -D -a 6 -n %{name}.net-%{version}


%build
# Weird symlink required... (also in upstream git)
ln -sf . astrometry

# Astrometry doesn't automatically find netpbm
export NETPBM_INC=-I%{_includedir}/netpbm
export NETPBM_LIB="-L%{_libdir} -lnetpbm"

# Parallel make flags on break build
make SYSTEM_GSL=yes all py extra \
    ARCH_FLAGS="%{optflags}"


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

# Rename generic named executables with known conflict
pushd %{buildroot}%{_bindir}
for exec in tabmerge tablist; do
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

# LICENSE file is managed by %%license scriptlet
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE

# Remove symlink in bin to python script
rm -f %{buildroot}%{_bindir}/plotann.py

# Install data files
install -m0644 astrometry-data*/*.fits %{buildroot}%{_datadir}/%{name}/data

%check
export PYTHON=%{__python3}
make test ARCH_FLAGS="%{optflags}"


%files
%doc CREDITS README.md
%license LICENSE
%{_mandir}/man1/*
%{_bindir}/*
# Exclude python scripts
%exclude %{_bindir}/degtohms
%exclude %{_bindir}/hmstodeg
%exclude %{_bindir}/image2pnm
%exclude %{_bindir}/merge-columns
%exclude %{_bindir}/removelines
%exclude %{_bindir}/text2fits
%exclude %{_bindir}/uniformize
%exclude %{_bindir}/votabletofits
%dir %{_datadir}/astrometry
%dir %{_datadir}/astrometry/data
%{_datadir}/astrometry/examples
%config(noreplace) %{_sysconfdir}/astrometry.cfg

%files data
%license astrometry-data-4208-4219/LICENSE
%{_datadir}/astrometry/data/index-4208.fits
%{_datadir}/astrometry/data/index-4209.fits
%{_datadir}/astrometry/data/index-421*.fits

%files data-4204
%license astrometry-data-4204/LICENSE
%{_datadir}/astrometry/data/index-4204*.fits

%files data-4205
%license astrometry-data-4205/LICENSE
%{_datadir}/astrometry/data/index-4205*.fits

%files data-4206
%license astrometry-data-4206/LICENSE
%{_datadir}/astrometry/data/index-4206*.fits

%files data-4207
%license astrometry-data-4207/LICENSE
%{_datadir}/astrometry/data/index-4207*.fits

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
* Mon Jan 29 2024 Mattia Verga <mattia.verga@protonmail.com> - 0.94-6
- Rebuilt for libwcs soname bump

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Mattia Verga <mattia.verga@protonmail.com> - 0.94-4
- Fix build failure due to removed numpy.distutils and deprecated distutils

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Mattia Verga <mattia.verga@protonmail.com> - 0.94-2
- Rebuilt for libwcs soname bump

* Sun Sep 17 2023 Mattia Verga <mattia.verga@protonmail.com> - 0.94-1
- Update to 0.94 (fedora#2148995)
- Migrate license to SPDX

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.91-4
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 0.91-2
- Rebuild for cfitsio 4.2

* Tue Nov 01 2022 Mattia Verga <mattia.verga@proton.me> - 0.91-1
- Update to 0.91 (fedora#2078037)

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.89-4
- Rebuild for gsl-2.7.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.89-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.89-2
- Rebuilt for Python 3.11

* Sun Feb 06 2022 Mattia Verga <mattia.verga@protonmail.com> - 0.89-1
- Update to 0.89 (fedora#1828169)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.78-11
- Rebuilt for Python 3.10

* Tue Feb 02 2021 Christian Dersch <lupinix@mailbox.org> - 0.78-10
- Rebuilt for libcfitsio.so.7

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.78-7
- Rebuilt for Python 3.9

* Wed Mar 25 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.78-6
- Rebuild for new wcslib

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.78-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.78-4
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.78-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Christian Dersch <lupinix@mailbox.org> - 0.78-1
- new version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.76-1
- new version

* Mon Jul 16 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.75-2
- Dependency fix, require python3-astrometry, not python2-astrometry

* Sat Jul 14 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.75-1
- new version

* Sat Jul 14 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.74-3
- Switch to Python 3
- BuildRequires: gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 0.74-1
- new version

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 0.73-5
- rebuilt for cfitsio 3.450

* Sat Feb 24 2018 Christian Dersch <lupinix@mailbox.org> - 0.73-4
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.73-3
- rebuilt

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Christian Dersch <lupinix@mailbox.org> - 0.73-1
- new version

* Tue Oct 17 2017 Christian Dersch <lupinix@mailbox.org> - 0.72-4
- Added subpackages for 4204-4207 index files

* Mon Oct 16 2017 Christian Dersch <lupinix@mailbox.org> - 0.72-3
- Added data subpackage containing the wide-field 2MASS indices

* Mon Sep 25 2017 Christian Dersch <lupinix@mailbox.org> - 0.72-2
- Move libs to subpackage to be multiarch compatible

* Tue Sep 12 2017 Christian Dersch <lupinix@mailbox.org> - 0.72-1
- Initial SCM import (#1470436)

* Wed Jul 12 2017 Christian Dersch <lupinix@mailbox.org> - 0.72-0.1
- initial spec (using the packaging effort from Mattia Verga, RHBZ  #1299139)

