# git commit appears in the directory name of the tarball...
%global commit f643684aa4a440f47f7853e4148f2ea03f951426

Name:           OpenMolcas
Version:        24.10
Release:        3%{?dist}
Summary:        A multiconfigurational quantum chemistry software package
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://gitlab.com/Molcas/OpenMolcas
Source0:        https://gitlab.com/Molcas/OpenMolcas/-/archive/v%{version}/%{name}-%{version}.tar.bz2

# Fedora patches
Patch0:         OpenMolcas-23.06-fedora.patch
# Read python modules from system directory
Patch1:         OpenMolcas-19.11-pymodule.patch
# Patch for libxc 7
Patch2:         https://gitlab.com/Molcas/OpenMolcas/-/merge_requests/728.patch

# OpenMolcas is only supported on 64-bit architectures
ExclusiveArch:  x86_64 aarch64 ppc64le s390x

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-gfortran
%if 0%{?fedora} >= 33
BuildRequires:  pkgconfig(flexiblas)
%else
BuildRequires:  openblas-devel
%endif
BuildRequires:  libxc-devel
BuildRequires:  hdf5-devel
BuildRequires:  CheMPS2-devel

# Required by runtime
%if 0%{?rhel} == 7
BuildRequires:  python2-devel
Requires:       pyparsing
%else
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pyparsing
Requires:       python3-pyparsing
Requires:       python3-setuptools
%endif

# CheMPS2 support at runtime (not linked, calls binary)
Requires:       CheMPS2

%description
OpenMolcas is a quantum chemistry software package developed by
scientists and intended to be used by scientists. It includes programs
to apply many different electronic structure methods to chemical
systems, but its key feature is the multiconfigurational approach,
with methods like CASSCF and CASPT2.

OpenMolcas is not a fork or reimplementation of Molcas, it is a large
part of the Molcas codebase that has been released as free and
open-source software (FOSS) under the Lesser GNU Public License
(LGPL). Some parts of Molcas remain under a different license by
decision of their authors (or impossibility to reach them), and are
therefore not included in OpenMolcas.

%prep
%setup -q -n %{name}-v%{version}-%{commit}
%patch -P0 -p1 -b .fedora
%patch -P1 -p1 -b .pymodule
%patch -P2 -p1 -b .libxc7

# Name of OpenBLAS library to use is
%if 0%{?fedora} >= 33
%if 0%{?__isa_bits} == 64
sed -i 's|@OPENBLAS_LIBRARY@|flexiblas64|g' CMakeLists.txt
%else
sed -i 's|@OPENBLAS_LIBRARY@|flexiblas|g' CMakeLists.txt
%endif
%else
%if 0%{?__isa_bits} == 64
sed -i 's|@OPENBLAS_LIBRARY@|openblaso64|g' CMakeLists.txt
%else
sed -i 's|@OPENBLAS_LIBRARY@|openblaso|g' CMakeLists.txt
%endif
%endif

# Location python modules are installed
sed -i 's|@MOLCAS_PYTHON@|%{_libdir}/%{name}/python|g' Tools/pymolcas/pymolcas.py
# Fix shebangs
%if 0%{?rhel} == 7
for f in Tools/pymolcas/*.py; do
    sed -i 's|#!/usr/bin/env python|#!/usr/bin/python2|g' $f
done
%else
for f in Tools/pymolcas/*.py; do
    sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|g' $f
done
%endif

%build
export CC=gcc
export FC=gfortran

export CFLAGS="%{optflags} -fopenmp -std=gnu99 -fPIC"
export FFLAGS="%{optflags} -cpp -fopenmp -fdefault-integer-8 -fPIC -I%{_libdir}/gfortran/modules"

# GCC10 compatibility
%if 0%{?fedora} > 31
export FFLAGS="$FFLAGS -fallow-argument-mismatch"
%endif

%cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_libdir}/%{name}/ \
       -DLINALG=OpenBLAS -DOPENMP=ON -DHDF5=ON -DCHEMPS2=ON \
       -DEXTERNAL_LIBXC=%{_usr} -S . -B %{_host}
%make_build -C %{_host}

%install
%{make_install} -C %{_host}

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh <<EOF
# OpenMolcas root is
export MOLCAS=%{_libdir}/%{name}
export PATH=\${PATH}:\${MOLCAS}/bin:\${MOLCAS}/sbin
EOF
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh <<EOF
# OpenMolcas root is
setenv MOLCAS %{_libdir}/%{name}
export PATH \${PATH}:\${MOLCAS}/bin:\${MOLCAS}/sbin
EOF

# Install the wrapper and its requirements
mkdir -p %{buildroot}%{_libdir}/%{name}/python

for f in $(cd Tools/pymolcas; ls *.py|grep -v pymolcas.py); do
    cp -p Tools/pymolcas/${f} %{buildroot}%{_libdir}/%{name}/python
done
mkdir -p %{buildroot}%{_bindir} 
cp -p Tools/pymolcas/pymolcas.py %{buildroot}%{_bindir}/pymolcas

%files
%license LICENSE
%doc CONTRIBUTORS.md
%{_sysconfdir}/profile.d/%{name}.*
%{_libdir}/%{name}
%{_bindir}/pymolcas

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 24.10-2
- Rebuild for hdf5 1.14.5

* Tue Oct 15 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 24.10-1
- Update to 24.10.

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 24.06-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 24.06-1
- Update to 24.06.

* Thu Feb 15 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 24.02-1
- Update to 24.02.

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 16 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 23.10-1
- Update to release 23.10.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 23.06-1
- Update to release 23.06.

* Wed Mar 15 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 23.02-1
- Update to release 23.02.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.10-2
- Bump for libxc rebuild.

* Sat Oct 15 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.10-1
- Update to release 22.10.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 22.06-2
- Rebuilt for pyparsing-3.0.9

* Wed Jun 15 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.06-1
- Update to release 22.06.

* Tue Feb 15 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 22.02-1
- Update to release 22.02, including libxc support.
- Also enabled HDF5 and CheMPS2 support.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 21.10-1
- Update to release 21.10.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 21.06-1
- Update to release 21.06.

* Thu May 06 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 21.02-1
- Disable builds on 32-bit architectures by request of upstream.
- Update to release 21.02.

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 07 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 20.10-1
- Update to release 20.10.

* Sat Nov 07 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 19.11-8
- Some files necessary for pymolcas were missing.

* Fri Aug 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 19.11-7
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 19.11-6
- Adapt to new CMake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.11-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 19.11-3
- Explicit buildrequire python3-setuptools.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 19.11-1
- Update to 19.11.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.09-2
- Fix python shebang.

* Wed Jan 02 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.09-1
- Update to 18.09 stable release.

* Tue Sep 25 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-7.o180813.1752
- Remove HDF5 support because upstream code is non-portable and too hard to fix.

* Tue Sep 18 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-6.o180813.1752
- Fix pyparsing requirement on EPEL7.

* Wed Sep 12 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-5.o180813.1752
- Add missing python modules and wrapper.

* Fri Aug 31 2018 Dave Love <loveshack@fedoraproject.org> - 18.0-4.o180813.1752
- Fix build on EPEL

* Fri Aug 24 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-3.o180813.1752
- Fix build on non-64-bit architectures.

* Fri Aug 24 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-2.o180813.1752
- Review fixes.

* Thu Aug 16 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-1.o180813.1752
- Initial release.
