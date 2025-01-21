%define soname 6

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif

Name:           xtb
Version:        6.7.1
Release:        2%{?dist}
Summary:        Semiempirical Extended Tight-Binding Program Package
License:        LGPL-3.0-or-later
URL:            https://github.com/grimme-lab/xtb/
Source0:        https://github.com/grimme-lab/xtb/archive/v%{version}/xtb-%{version}.tar.gz

# Fedora versioning
Patch0:         xtb-6.5.1-fedora.patch
# Add sanity checks to environment variables, https://github.com/grimme-lab/xtb/pull/317
Patch4:         xtb-6.3.2-environment.patch

BuildRequires:  gcc-gfortran
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  %{blaslib}-devel
# To generate man pages
BuildRequires:  rubygem-asciidoctor
# The program queries $HOSTNAME at runtime and so fails to run in mock without this
BuildRequires:  hostname
BuildRequires:  mctc-lib-devel
BuildRequires:  test-drive-devel
BuildRequires:  multicharge-devel
BuildRequires:  dftd4-devel

# Tests fail on s390x for some reason
ExcludeArch:    s390x

# Need data files to run
Requires:       %{name}-data = %{version}-%{release}

%description
The xtb program package developed by the Grimme group in Bonn.

%package data
Summary:   Data files for xtb
BuildArch: noarch

%description data
This package contains the data files for xtb.

%package libs
Summary:   Shared libraries for xtb
# The program queries $HOSTNAME at runtime and so fails to run in mock without this
Requires: hostname
# Need data files to run
Requires:       %{name}-data = %{version}-%{release}

%description libs
This package contains the shared libraries for xtb.

%package devel
Summary:   Development headers for xtb
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains development headers for xtb.

%prep
%setup -q
%patch 0 -p1 -b .fedoraver
%patch 4 -p1 -b .env

%build
export FFLAGS="%{optflags} -I%{_fmoddir} -fPIC"
export FCLAGS="%{optflags} -I%{_fmoddir} -fPIC"
# TODO: tblite and cpcm-x support should ideally be turned on, but the packages are not yet in Fedora
%meson -Dlapack=custom -Dcustom_libraries=%{blaslib}%{blasvar} -Dtblite=disabled -Dcpcmx=disabled
date=$(date)
# Create customized Fedora versioning
cat > %{_vpath_builddir}/xtb_version.fh <<EOF
character(len=*),parameter :: version = "%{version}-%{release}%{dist}"
character(len=*),parameter :: date = "$date"
character(len=*),parameter :: author = "Fedora project"
EOF
%meson_build

%install
%meson_install
# Remove static library
rm %{buildroot}%{_libdir}/libxtb.a
# Remove environment module files
rm -rf %{buildroot}%{_datadir}/modules

# Create profile files
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/xtb.sh <<EOF
XTBPATH=%{_datadir}/xtb
export XTBPATH
EOF
cat > %{buildroot}%{_sysconfdir}/profile.d/xtb.csh <<EOF
setenv XTBPATH %{_datadir}/xtb
EOF

%check
# Set missing environment variable
export HOSTNAME=$(hostname)
# Turn off use of OpenMP parallelism since tests are already run in parallel
export OMP_NUM_THREADS=1
# Tests time out
%meson_test --timeout-multiplier=10

%files
# LGPLv3+ license is stated at bottom of README.md
%doc README.md CONTRIBUTING.md
%license COPYING COPYING.LESSER README.md
%{_mandir}/man1/xtb.1*
%{_mandir}/man7/xcontrol.7*
%{_bindir}/xtb

%files data
%{_sysconfdir}/profile.d/xtb.sh
%{_sysconfdir}/profile.d/xtb.csh
%{_datadir}/xtb/

%files libs
%license COPYING COPYING.LESSER README.md
%{_libdir}/libxtb.so.%{soname}*

%files devel
%{_includedir}/xtb.h
%{_libdir}/libxtb.so
%{_libdir}/pkgconfig/xtb.pc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 13 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.7.1-1
- Update to 6.7.1.

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 6.6.1-4
- convert license to SPDX

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 14 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.6.1-1
- Update to 6.6.1.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.6.0-1
- Update to 6.6.0.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 02 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.5.1-1
- Update to 6.5.1.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 16 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.5.0-1
- Update to 6.5.0.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.4.1-2
- Split data files into separate package.

* Fri Jun 11 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.4.1-1
- Update to 6.4.1.

* Mon Feb 01 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.4.0-1
- Update to 6.4.0.

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 17 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.3-1
- Update to 6.3.3.

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 6.3.2-2
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.2-1
- Update to 6.3.2.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.1-5
- Review fixes.

* Sun Jun 21 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.1-4
- Drop Python requirements since the python stuff is now in another project.

* Thu Jun 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.1-3
- Fix crashes on several architectures.

* Thu Jun 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.1-2
- Add dependency on rubygem-asciidoc to get man pages.
- Increase test timeouts to avoid build failures.
- Disable architectures that fail to work.
- Use external BLAS library for matmul.

* Wed Jun 17 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.1-1
- First release.
