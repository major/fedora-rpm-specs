# Omit internal libraries from dependency generation. We can omit all
# the provides
%global __provides_exclude_from ^%{python3_sitearch}/pyscf/lib/.*\\.so$
# but since we still need to pick up the dependencies for libcint,
# libxc, etc, we just have to filter out the internal libraries
%global __requires_exclude ^(libao2mo\\.so|libcgto\\.so|libcvhf\\.so|libfci\\.so|libnp_helper\\.so|libpbc\\.so).*$

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global cmake_blas_flags -DBLA_VENDOR=FlexiBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif

Name:           python-pyscf
Version:        2.8.0
Release:        1%{?dist}
Summary:        Python module for quantum chemistry
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/pyscf/pyscf/
Source0:        https://github.com/pyscf/pyscf/archive/v%{version}/pyscf-%{version}.tar.gz

# Disable rpath
Patch1:         pyscf-2.6.0-rpath.patch
# Need to load libpbc before libdft, https://github.com/pyscf/pyscf/pull/2273
Patch2:         2273.patch

# ppc64 doesn't appear to have floats beyond 64 bits, so ppc64 is
# disabled as per upstream's request as for the libcint package.
ExcludeArch:    %{power64}

BuildRequires:  %{blaslib}-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-h5py
BuildRequires:  libxc-devel
# make sure we are using the newer version
BuildRequires:  libcint-devel >= 5.0.0
BuildRequires:  xcfun-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++

# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov

%description
Python‐based simulations of chemistry framework (PySCF) is a
general‐purpose electronic structure platform designed from the ground
up to emphasize code simplicity, so as to facilitate new method
development and enable flexible computational workflows. The package
provides a wide range of tools to support simulations of finite‐size
systems, extended systems with periodic boundary conditions,
low‐dimensional periodic systems, and custom Hamiltonians, using
mean‐field and post‐mean‐field methods with standard Gaussian basis
functions. To ensure ease of extensibility, PySCF uses the Python
language to implement almost all of its features, while
computationally critical paths are implemented with heavily optimized
C routines. Using this combined Python/C implementation, the package
is as efficient as the best existing C or Fortran‐based quantum
chemistry programs.

%package -n python3-pyscf
Summary:        Python 3 module for quantum chemistry
# These are needed at runtime
Requires:  python3-numpy
Requires:  python3-scipy
Requires:  python3-h5py

%description -n python3-pyscf
Python‐based simulations of chemistry framework (PySCF) is a
general‐purpose electronic structure platform designed from the ground
up to emphasize code simplicity, so as to facilitate new method
development and enable flexible computational workflows. The package
provides a wide range of tools to support simulations of finite‐size
systems, extended systems with periodic boundary conditions,
low‐dimensional periodic systems, and custom Hamiltonians, using
mean‐field and post‐mean‐field methods with standard Gaussian basis
functions. To ensure ease of extensibility, PySCF uses the Python
language to implement almost all of its features, while
computationally critical paths are implemented with heavily optimized
C routines. Using this combined Python/C implementation, the package
is as efficient as the best existing C or Fortran‐based quantum
chemistry programs.

%prep
%setup -q -n pyscf-%{version}
%patch 1 -p1 -b .rpath
%patch 2 -p1 -b .2273

# Remove shebangs
find pyscf -name \*.py -exec sed -i '/#!\/usr\/bin\/env /d' '{}' \;
find pyscf -name \*.py -exec sed -i '/#!\/usr\/bin\/python/d' '{}' \;

%build
cd pyscf/lib
%cmake -DENABLE_LIBXC=ON -DBUILD_LIBXC=OFF -DENABLE_XCFUN=ON -DBUILD_XCFUN=OFF -DBUILD_LIBCINT=OFF %{cmake_blas_flags} -DCMAKE_SKIP_BUILD_RPATH=1
%cmake_build

%install
# Package doesn't have an install command, so we do this by hand.
# Install all python sources
for f in $(find pyscf -name \*.py); do
    install -D -p -m 644 $f %{buildroot}%{python3_sitearch}/$f
done
# Install data files (mostly basis sets)
for f in $(find pyscf -name \*.dat); do
    install -D -p -m 644 $f %{buildroot}%{python3_sitearch}/$f
done
# Install compiled libraries
for f in $(find pyscf -name \*.so); do
    install -D -p -m 755 $f %{buildroot}%{python3_sitearch}/$f
done

%check
export PYTHONPATH=$PWD
## While the program has tests, they take forever and won't ever finish
##on the build system.
#pytest

%files -n python3-pyscf
%license LICENSE
%doc CHANGELOG CONTRIBUTING.md FEATURES NOTICE README.md
%{python3_sitearch}/pyscf/

%changelog
* Tue Jan 14 2025 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0.

* Wed Oct 16 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.7.0-3
- Bump release

* Sat Oct 12 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.7.0-2
- Bump release to rebuild against libxc 7 in rawhide (f42).

* Thu Sep 26 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0.

* Wed Sep 04 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2.

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.0-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.0-4
- Patch to load in new library where it is needed.

* Fri Jun 14 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.0-3
- Filter out a new internal dependency from rpm tracking.

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.6.0-2
- Rebuilt for Python 3.13

* Wed Jun 05 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0.

* Sat May 18 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 20 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 2.3.0-2
- Rebuilt for Python 3.12

* Sat Jul 08 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0.

* Mon Apr 03 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1.

* Thu Mar 16 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.1-2
- Rebuild with libxc 6.0.0 in rawhide.

* Mon Sep 26 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1.

* Sun Sep 04 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.0.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-3
- Patch for libcint 5.1.x compatibility.

* Wed Dec 08 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-2
- Build against xcfun.

* Fri Nov 26 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Björn Esser <besser82@fedoraproject.org> - 1.7.6-3
- Properly set BLA_VENDOR to FlexiBLAS for cmake >= 3.19

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.6-2
- Rebuilt for Python 3.10

* Mon Mar 29 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.6-1
- Update to 1.7.6.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.5-1
- Update to 1.7.5.

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.7.4-2
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Aug 03 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.4-1
- Adapt to updated CMake scripts.
- Update to 1.7.4.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 11 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.3-1
- Update to 1.7.3.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-2
- Rebuilt for Python 3.9

* Thu May 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2.

* Mon Apr 20 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.1-2
- Patch for libxc 5.

* Tue Mar 24 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1.

* Sun Feb 02 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.0-6
- Build against libopenblaso not libopenblas as the latter yields incorrect results.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.0-4
- Switch buildrequire to libcint and disable build on ppc64.

* Thu Jan 23 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.0-3
- Filter provides and requires.

* Wed Jan 22 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.0-2
- Remove shebangs and rpath.

* Tue Jan 07 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.0-1
- First release.
