Name:           CheMPS2
Version:        1.8.9
Release:        26%{?dist}
Summary:        A spin-adapted implementation of DMRG for ab initio quantum chemistry

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/SebWouters/CheMPS2
Source0:        https://github.com/SebWouters/CheMPS2/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  cmake
BuildRequires:  hdf5-devel
BuildRequires:  zlib-devel

%description    
The CheMPS2 library provides a free open-source spin-adapted 
implementation of the density matrix renormalization group (DMRG) for ab initio 
quantum chemistry. This method allows to obtain numerical accuracy in active 
spaces beyond the capabilities of full configuration interaction. For the 
input Hamiltonian and targeted symmetry sector, the library performs successive 
DMRG sweeps according to a user-defined convergence scheme. As output, the 
library returns the minimal encountered energy as well as the 2-RDM of the 
active space. The latter allows to calculate various properties, as well as 
the gradient and Hessian for orbital rotations or nuclear displacements.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# For directory ownership
Requires:       cmake

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake -DMKL=OFF -DLAPACK_LIBRARIES="-lflexiblas" -DENABLE_XHOST=OFF -DSHARED_ONLY=ON
%cmake_build

%install
%cmake_install
install -D -p -m 644 chemps2.1 %{buildroot}%{_mandir}/man1/chemps2.1
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc README.md CHANGELOG.md FILES.md
%license LICENSE
%{_libdir}/libchemps2.so.*
%{_bindir}/chemps2
%{_mandir}/man1/chemps2.1.*

%files devel
%{_datadir}/cmake/CheMPS2/
%{_includedir}/chemps2/
%{_libdir}/libchemps2.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 1.8.9-25
- Rebuild for hdf5 1.14.5

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.9-24
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.8.9-17
- Rebuild due to erroneous package retirement.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 1.8.9-14
- Rebuild for hdf5 1.12.1

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 1.8.9-13
- Rebuild for hdf5 1.10.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.8.9-10
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 1.8.9-7
- Rebuild for hdf5 1.10.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.8.9-4
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.9-2
- Subpackage python2-chemps2 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Nov 11 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.8.9-1
- Switch to using OpenBLAS instead of ATLAS.
- Update to 1.8.9.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8.3-6
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8.3-5
- Python 2 binary package renamed to python2-chemps2
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 05 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.8.3-1
- Update to 1.8.3.

* Mon Aug 29 2016 Matt Chan <talcite@gmail.com> - 1.8-1
- Updated to 1.8, Updated patches, build shared only
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Thu Jul 14 2016 Matt Chan <talcite@gmail.com> - 1.7.3-1
- Updated to 1.7.3
* Wed Jun 15 2016 Matt Chan <talcite@gmail.com> - 1.7.2-1
- Updated to 1.7.2
* Wed Jun 15 2016 Matt Chan <talcite@gmail.com> - 1.7-4
- Added patch, cleaned up specfile 
* Wed Jun 15 2016 Matt Chan <talcite@gmail.com> - 1.7-3
- Changed CXX flags, changed BR
* Tue Jun 14 2016 Matt Chan <talcite@gmail.com> - 1.7-2
- Changed to follow packaging guidelines
- Added zlib for RHEL6 compatibility
* Sat Jun 11 2016 Matt Chan <talcite@gmail.com> - 1.7-1
- Initial build
