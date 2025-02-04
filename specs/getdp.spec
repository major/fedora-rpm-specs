Name:           getdp
# TODO: Enablee building with gmsh support as soon as getdp does not require private gmsh api anymore
Version:        3.6.0
Release:        8%{?dist}
Summary:        General Environment for the Treatment of Discrete Problems

License:        GPL-2.0-or-later
URL:            http://www.geuz.org/getdp/
Source0:        http://www.geuz.org/getdp/src/%{name}-%{version}-source.tgz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++ gcc-gfortran
BuildRequires:  arpack-devel
BuildRequires:  gsl-devel
BuildRequires:  flexiblas-devel
BuildRequires:  python3-devel
BuildRequires:  petsc-devel
BuildRequires:  SuperLU-devel
BuildRequires:  libX11-devel
BuildRequires:  metis-devel
BuildRequires:  hdf5-devel
BuildRequires:  cgnslib-devel

# GPLv3+, some fortran files in contrib/pewe, some git version
Provides:       bundled(pewe)

%description
GetDP is an open source finite element solver using mixed elements to
discretize de Rham-type complexes in one, two and three dimensions. The main
feature of GetDP is the closeness between the input data defining discrete
problems (written by the user in ASCII data files) and the symbolic mathematical
expressions of these problems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}-source

# remove bundled libs
find contrib/ -mindepth 1 -maxdepth 1 -type d -not \( -name pewe \) -prune -exec rm -vrf {} ';'

# fix lib -> lib64 for petsc detection
sed -i 's|${ENV_PETSC_ARCH}/lib|${ENV_PETSC_ARCH}/%_lib|g' CMakeLists.txt

# set blas in bundled lib
sed -i 's|-llapack -lblas|-lflexiblas|' contrib/pewe/fortran/Makefile


%build
%cmake \
    -DBLAS_LAPACK_LIBRARIES="-lflexiblas" \
    -DENABLE_MULTIHARMONIC=ON \
    -DENABLE_NX=OFF           \
    -DENABLE_OPENMP=ON        \
    -DENABLE_SLEPC=OFF        \
    -DENABLE_SPARSKIT=OFF     \
    -DENABLE_BUILD_SHARED=ON  \
    -DENABLE_BUILD_DYNAMIC=ON
%cmake_build


%install
%cmake_install

# remove auto-installed docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}


%check
%ctest


%files
%license LICENSE.txt CREDITS.txt
%{_bindir}/%{name}
%{_libdir}/libgetdp.so.3.6
%{_libdir}/libgetdp.so.3.6.0
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/libgetdp.so

%changelog
* Sun Feb 02 2025 Orion Poplawski <orion@nwra.com> - 3.6.0-8
- Rebuild with gsl 2.8

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 01 2025 Sandro Mani <manisandro@gmail.com> - 3.6.0-6
- Rebuild (petsc)

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 3.6.0-5
- Rebuild for hdf5 1.14.5

* Mon Aug 19 2024 Sandro Mani <manisandro@gmail.com> - 3.6.0-4
- Drop BR: gmsh (#2304315)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 3.6.0-2
- Rebuilt for Python 3.13

* Sun Mar 03 2024 Sandro Mani <manisandro@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 20 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 3.5.0-10
- Rebuild for PETSc-3.20.0 (close RHBZ#2245240)

* Sun Aug 13 2023 Antonio Trande <sagitter@fedorapoject.org> - 3.5.0-9
- Rebuild for petsc-3.19.4

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 17 2023 Python Maint <python-maint@redhat.com> - 3.5.0-7
- Rebuilt for Python 3.12

* Wed Apr 26 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 3.5.0-6
- Drop conditionals for end-of-life Fedora releases
- Drop obsolete ldconfig_scriptlets macro
- Rebuild for PETSc-3.18.5 (fix RHBZ#2189695)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.0-4
- Rebuild for gsl-2.7.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.5.0-2
- Rebuilt for Python 3.11

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Sat Apr 23 2022 Antonio Trande <sagitter@fedorapoject.org> - 3.4.0-4
- Rebuild for PETSc-3.17.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Antonio Trande <sagitter@fedorapoject.org> - 3.4.0-2
- Rebuild for PETSc-3.16.0

* Thu Sep 23 2021 Sandro Mani <manisandro@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.0-11
- Rebuilt for Python 3.10

* Wed May 05 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.3.0-10
- Rebuild for petsc 3.15

* Wed May 05 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-9
- Rebuild (petsc)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 22 2020 Orion Poplawski <orion@nwra.com> - 3.3.0-7
- Rebuild for petsc 3.14

* Fri Aug 14 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.3.0-6
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-4
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Sandro Mani <manisandro@gmail.com> - 3.3.0-3
- Rebuild (petsc), add missing BRs

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 Sandro Mani <manisandro@gmail.com> - 3.3.0-1
- Update to 3.3.0

* Mon Nov 11 2019 Sandro Mani <manisandro@gmail.com> - 3.2.0-6
- Rebuild (petsc)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-5
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.2.0-4
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Sandro Mani <manisandro@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Sat Apr 20 2019 Sandro Mani <manisandro@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Sandro Mani <manisandro@gmail.com> - 2.11.3-8
- Rebuild (gmsh)

* Tue Jan 22 2019 Sandro Mani <manisandro@gmail.com> - 2.11.3-7
- Rebuild (gmsh)

* Mon Jan 21 2019 Richard Shaw <hobbes1069@gmail.com> - 2.11.3-6
- Rebuild for gmsh 4.1.1.

* Sun Sep 02 2018 Sandro Mani <manisandro@gmail.com> - 2.11.3-5
- Rebuild (gmsh)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.11.3-2
- Switch to %%ldconfig_scriptlets

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.11.3-1
- Update to 2.11.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.11.2-1
- Update to 2.11.2

* Thu Jun 15 2017 Sandro Mani <manisandro@gmail.com> - 2.11.1-2
- Rebuild (gmsh)

* Mon May 29 2017 Sandro Mani <manisandro@gmail.com> - 2.11.1-1
- Update to 2.11.1 (RHBZ #1450617)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu May 11 2017 Sandro Mani <manisandro@gmail.com> - 2.11.0-3
- Rebuild (gmsh)

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 2.11.0-2
- Rebuilt for libgfortran soname bump

* Wed Jan 04 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.11.0-1
- Update to 2.11.0 (RHBZ #1409937)

* Sun Dec 11 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.10.0-3
- Rebuild for gmsh 2.15

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.10.0-2
- Rebuild (gmsh)

* Mon Oct 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.10.0-1
- Update to 2.10.0 (RHBZ #1383102)

* Sun Aug 28 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.9.2-1
- Update to 2.9.2

* Tue Jul 12 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.9.0-1
- Update to 2.9.0 (RHBZ #1354698)

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.8.0-1
- Update to 2.8.0 (RHBZ #1315030)

* Tue Feb 23 2016 Orion Poplawski <orion@cora.nwra.com> - 2.7.0-3
- Rebuild for gsl 2.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.7.0-1
- Initial package
