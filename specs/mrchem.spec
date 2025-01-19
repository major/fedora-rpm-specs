Name:           mrchem
Version:        1.1.4
Release:        2%{?dist}
Summary:        A numerical real-space code for molecular electronic structure calculations
License:        LGPL-3.0-or-later
URL:            https://github.com/MRChemSoft/mrchem/
Source0:        https://github.com/MRChemSoft/mrchem/archive/v%{version}/%{name}-%{version}.tar.gz

# Relax Eigen3 version check, https://github.com/MRChemSoft/mrcpp/issues/186
Patch0:         mrchem-1.0.2-eigen3.patch
# The Python module is installed in the system directory in Fedora
Patch1:         mrchem-1.0.2-pythonpath.patch
# Disable use of rpath
Patch2:         mrchem-1.1.0-rpath.patch
# Re-enable creation of shared library
Patch3:         mrchem-1.1.2-object.patch

# mrcpp doesn't build on s390x which is not supported by upstream (BZ#2035671)
ExcludeArch:    s390x
%if 0%{?rhel} == 9
# mrcpp compile fails on ppc64le
ExcludeArch:    ppc64le
%endif

# We need the data files
Requires:       %{name}-data = %{version}-%{release}

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  eigen3-devel
BuildRequires:  python3-devel
BuildRequires:  xcfun-devel
BuildRequires:  mrcpp-devel
BuildRequires:  catch2-devel

# Eigen3 is a header-only library; this is for dependency tracking
BuildRequires:  eigen3-static

%description
MRChem is a numerical real-space code for molecular electronic
structure calculations within the self-consistent field (SCF)
approximations of quantum chemistry (Hartree-Fock and Density
Functional Theory).

%package devel
Summary:        Development headers and libraries for mrchem
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
# For license file
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
MRChem is a numerical real-space code for molecular electronic
structure calculations within the self-consistent field (SCF)
approximations of quantum chemistry (Hartree-Fock and Density
Functional Theory).

This package contains the development headers and libraries.

%package data
Summary:        Data files for MRchem
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
# For license file and to ensure data doesn't linger when main package is erased
Requires:       %{name} = %{version}-%{release}

%description data
MRChem is a numerical real-space code for molecular electronic
structure calculations within the self-consistent field (SCF)
approximations of quantum chemistry (Hartree-Fock and Density
Functional Theory).

This package contains the data files for MRChem.

%prep
%setup -q
# EPEL9 doesn't support the new patch syntax
%patch -P0 -p1 -b .eigen3
%patch -P1 -p1 -b .pythonpath
%patch -P2 -p1 -b .rpath
%patch -P3 -p1 -b .object
# Remove bundled catch
rm -rf external/catch/

%build
export CXXFLAGS="%{optflags} -I/usr/include/catch2"
%cmake -DENABLE_ARCH_FLAGS=OFF -DENABLE_OPENMP=ON
%cmake_build

%install
%cmake_install
# Move the python library to the correct location
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}/usr/lib/python/mrchem %{buildroot}%{python3_sitelib}

%check
# Tests use OpenMP so we only want to run them one at a time
%global _smp_mflags "-j1"
# Where to find the python library
export PYTHONPATH=$PWD/python/
# Generate dummy config module for ctest
cat > $PYTHONPATH/mrchem/config.py <<EOF
MRCHEM_VERSION = "%{version}"
MRCHEM_EXECUTABLE = "$PWD/redhat-linux-build/bin/mrchem.x"
MRCHEM_MODULE = "$PYTHONPATH"
EOF
%ctest

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md VERSION
%{python3_sitelib}/mrchem/
%{_bindir}/mrchem
%{_bindir}/mrchem.x

%files devel
%{_includedir}/MRChem/
%{_libdir}/libmrchem.a

%files data
%{_datadir}/MRChem/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.3-5
- convert license to SPDX

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.3-4
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.2-3
- Rebuilt for Python 3.12

* Mon Mar 13 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.2-2
- Fix FTBFS caused by catch3 in rawhide.

* Fri Jan 20 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1.

* Wed Sep 28 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.11

* Thu Feb 03 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.0.2-3
- Address review comments

* Fri Jan 14 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.0.2-2
- Minor cleanups

* Sat Dec 25 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.0.2-1
- First release
