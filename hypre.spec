# Copyright (c) 2014  Dave Love, University of Liverpool
# Copyright (c) 2018  Dave Love, University of Manchester
# MIT licence, per Fedora policy

%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif

%bcond_without mpich
%bcond_with check
%bcond_without flexiblas

%if %{with flexiblas}
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

%global somajor 2
%global soversion %{somajor}.1

# No sphinx in el8 as of 2019-09, and missing latex packages
%{!?el8:%global docs 1}

Name:           hypre
Version:        2.24.0
Release:        12%{?dist}
Summary:        High performance matrix preconditioners
License:        Apache-2.0 OR MIT
URL:            http://www.llnl.gov/casc/hypre/
Source:         https://github.com/hypre-space/hypre/archive/v%version/%{name}-%{version}.tar.gz
# Don't use hostname for tests and use two MPI processes
Patch2:         hypre-test.patch

BuildRequires:  gcc-c++ gcc-gfortran automake libtool libtool-ltdl-devel make
BuildRequires:  SuperLU-devel
BuildRequires:  %{blaslib}-devel
%if 0%{?docs}
BuildRequires:  doxygen-latex python-sphinx python-sphinx-theme-alabaster
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx-latex /usr/bin/latexmk
BuildRequires:  tex(threeparttable.sty) tex(hanging.sty) tex(adjustbox.sty)
BuildRequires:  tex(fncychap.sty) tex(tabulary.sty) tex(capt-of.sty)
BuildRequires:  tex(needspace.sty) tex(stackengine.sty) tex(listofitems.sty)
BuildRequires:  tex(ulem.sty) tex(etoc.sty)
%endif

%global __requires_exclude libHYPRE.*
%{?filter_setup:
%filter_from_requires /libHYPRE/d
%filter_setup
}

%global desc \
Hypre is a set of matrix preconditioning libraries to aid in the\
solution of large systems of linear equations.

%description
%desc

%package devel
Summary:        Development files for %name
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       SuperLU-devel%{?_isa} 
Requires:       %{blaslib}-devel%{?_isa}

%description devel
Development files for %name

%if %{with openmpi}
%package openmpi
Summary:        High performance matrix preconditioners - openmpi
Requires:       openmpi%{?_isa}
BuildRequires:  superlu_dist-openmpi-devel ptscotch-openmpi-devel

%description openmpi
%desc

This is the openmpi version.

%package openmpi-devel
Summary:        Development files for %name-openmpi
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:       openmpi-devel%{?_isa} superlu_dist-openmpi-devel%{?_isa}
Requires:       ptscotch-openmpi-devel%{?_isa}
Requires:       %{blaslib}-devel%{?_isa}

%description openmpi-devel
Development files for %name-openmpi
%endif

%if %{with mpich}
%package mpich
Summary:        High performance matrix preconditioners - mpich
Requires:       mpich%{?_isa}
BuildRequires:  superlu_dist-mpich-devel ptscotch-mpich-devel

%description mpich
%desc

This is the mpich version.

%package mpich-devel
Summary:        Development files for %name-mpich
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
Requires:       mpich-devel%{?_isa}
Requires:       superlu_dist-mpich-devel%{?_isa} ptscotch-mpich-devel%{?_isa}
Requires:       %{blaslib}-devel%{?_isa}

%description mpich-devel
Development files for %name-mpich
%endif

%if 0%{?docs}
%package doc
Summary:        Documentation for hypre
BuildArch:      noarch

%description doc
Documentation for hypre
%endif


%prep
%setup -q -n %name-%version
%patch -P 2 -p1 -b .test

find \( -name \*.[ch] -o -name \*.cxx \) -perm /=x -exec chmod 0644 {} \;

%if %{with openmpi}
cp -a src openmpi
%endif
%if %{with mpich}
cp -a src mpich
%endif

%build
%global lalibs --with-blas-libs=%{blaslib} --with-lapack-libs=%{blaslib} \\\
           --with-blas-lib-dirs=%_libdir --with-lapack-lib-dirs=%_libdir

pushd src
# -O3 seems like a good idea for vectorization, at least.  We need LIBS to
# link the shared lib correctly.
export LIBS='-lsuperlu -fopenmp'
%configure --without-MPI --with-timing --with-openmp --enable-shared=yes \
           %lalibs \
           --with-superlu --with-superlu-include=%_includedir/SuperLU \
           --with-superlu-libs=superlu --with-mli \
           CFLAGS="$CFLAGS -O3"
%make_build SONAME=libHYPRE.so.%soversion
%{?docs:make -C docs                    # not smp-safe
rm docs/usr-manual-html/.buildinfo}
popd

# Specifying CC is necessary on f33 as MPI_LIB isn't being passed on
# for some reason; it was OK previously
%global do_mpi_build \
%configure --prefix=$MPI_HOME --with-MPI --with-MPI-include=$MPI_INCLUDE \\\
           --with-MPI-lib-dirs=$MPI_LIB --with-timing --without-openmp \\\
           %lalibs \\\
           --enable-shared=yes --with-fei --with-mli \\\
           --with-dsuperlu --with-dsuperlu-include=$MPI_INCLUDE/superlu_dist \\\
           --with-dsuperlu-libs='superlu_dist ptscotch' \\\
           CFLAGS="$CFLAGS -O3" CC=mpicc \
  %make_build SONAME=libHYPRE.so.%soversion

export LIBS='-lsuperlu_dist -lptscotch'
%if %{with openmpi}
pushd openmpi
%_openmpi_load
%do_mpi_build
%_openmpi_unload
popd
%endif

%if %{with mpich}
pushd mpich
%_mpich_load
%do_mpi_build
%_mpich_unload
popd
%endif


%check
# Currently seeing inconsistent hangs on koji (as for superlu_dist).
# Assume it doesn't deadlock in realistic situations.
%if %{with check}
%if %{with openmpi}
export LD_LIBRARY_PATH=$(pwd)/openmpi/hypre/lib
export OMPI_MCA_orte_allocation_required=0
%_openmpi_load
pushd openmpi/test
%make_build SONAME=libHYPRE.so.%soversion
# A random selection to check, rather than all possibilities.  (The
# relevant binaries aren't built for all the TEST_...s.)
./runtest.sh TEST_ij/*sh
popd
%endif
%endif


%install
make -C src install HYPRE_INSTALL_DIR=%{buildroot}%{_prefix} \
     HYPRE_LIB_INSTALL=%{buildroot}%{_libdir} \
     HYPRE_INC_INSTALL=%{buildroot}%{_includedir}/%{name} SONAME=libHYPRE.so.%soversion

ln -s libHYPRE.so.%soversion %{buildroot}%{_libdir}/libHYPRE.so.%somajor

%if %{with openmpi}
%_openmpi_load
make -C openmpi install HYPRE_INSTALL_DIR=%{buildroot}$MPI_HOME \
     HYPRE_LIB_INSTALL=%{buildroot}$MPI_LIB \
     HYPRE_INC_INSTALL=%{buildroot}$MPI_INCLUDE/%{name} SONAME=libHYPRE.so.%soversion

for l in openmpi/lib; do
  ln -s libHYPRE.so.%soversion %{buildroot}%{_libdir}/$l/libHYPRE.so.%somajor
done
%_openmpi_unload
%endif

%if %{with mpich}
%_mpich_load
make -C mpich install HYPRE_INSTALL_DIR=%{buildroot}$MPI_HOME \
     HYPRE_LIB_INSTALL=%{buildroot}$MPI_LIB \
     HYPRE_INC_INSTALL=%{buildroot}$MPI_INCLUDE/%{name} SONAME=libHYPRE.so.%soversion
     
for l in mpich/lib; do
  ln -s libHYPRE.so.%soversion %{buildroot}%{_libdir}/$l/libHYPRE.so.%somajor
done
%_mpich_unload
%endif

%files
%doc CHANGELOG README.md
%license COPYRIGHT LICENSE-*
%{_libdir}/libHYPRE.so.%{somajor}*

%files devel
%{_libdir}/libHYPRE.so
%{_includedir}/%{name}

%if %{with openmpi}
%files openmpi
%doc CHANGELOG README.md
%license COPYRIGHT LICENSE-*
%{_libdir}/openmpi/lib/libHYPRE.so.%{somajor}*

%files openmpi-devel
%{_libdir}/openmpi/lib/libHYPRE.so
%{_includedir}/openmpi-%_arch/%{name}
%endif

%if %{with mpich}
%files mpich
%doc CHANGELOG README.md
%license COPYRIGHT LICENSE-*
%{_libdir}/mpich/lib/libHYPRE.so.%{somajor}*

%files mpich-devel
%{_libdir}/mpich/lib/libHYPRE.so
%{_includedir}/mpich-%_arch/%{name}
%endif

%if 0%{?docs}
%files doc
%doc CHANGELOG README.md src/examples
%license COPYRIGHT LICENSE-*
%doc src/docs/*.pdf src/docs/*-manual-html
%endif

%changelog
* Sat Mar 16 2024 Dave Love <loveshack@fedoraproject.org> - 2.24.0-12
- Fix licence (changed from LGPL to Apache 2 or MIT)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 15 2023 Antonio Trande <sagitter@fedoraproject.org> - 2.24.0-9
- Rebuild for superlu_dist-8.2.0

* Thu Aug 17 2023 Antonio Trande <sagitter@fedoraproject.org> - 2.24.0-8
- Rebuild for Scotch-7.0.4

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Antonio Trande <sagitter@fedoraproject.org> - 2.24.0-6
- Rebuild for SuperLU-6.0.0

* Thu Apr 13 2023 Antonio Trande <sagitter@fedoraproject.org> - 2.24.0-5
- Rebuild for Scotch-7

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.24.0-2
- Rebuild for superlu_dist-8.0.0

* Sat Apr 02 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.24.0-1
- Release 2.24.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.18.2-5
- Rebuild for SuperLU-5.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2.18.2-2
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Fri Aug  7 2020  <vagrant@rawhide.localdomain> - 2.18.2-1
- Configure with CC=mpicc to fix FTBFS (#1863655)
- Update to 2.18.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Dave love <loveshack@fedoraproject.org> - 2.18.1-1
- New version

* Tue Oct  8 2019 Dave love <loveshack@fedoraproject.org> - 2.18.0-2
- Make libHYPRE.so.%%somajor links

* Tue Oct  1 2019 Dave love <loveshack@fedoraproject.org> - 2.18.0-1
- New version
- Add minor version to soname

* Wed Sep 18 2019 Dave love <loveshack@fedoraproject.org> - 2.17.0-2
- Don't try to build docs on el8

* Mon Sep 16 2019 Dave love <loveshack@fedoraproject.org> - 2.17.0-1
- New version, with soname bump and licence change

* Sat Sep 14 2019 Dave love <loveshack@fedoraproject.org> - 2.16.0-1
- New version from updated origin
- Build docs; add BRs
- Drop soname patch

* Wed Sep 11 2019 Orion Poplawski <orion@nwra.com> - 2.15.1-7
- Drop el6 conditionals, build openmpi for EL8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 2.15.1-5
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec  3 2018 Dave Love <loveshack@fedoraproject.org> - 2.15.1-3
- Revert omitting builtin BLAS, which is namedspaced

* Mon Dec  3 2018 Dave Love <loveshack@fedoraproject.org> - 2.15.1-2
- Fix FTBFS with current superlu_dist [#1654932]
- Clean up configuration and avoid builtin BLAS

* Wed Nov 21 2018 Dave Love <loveshack@fedoraproject.org> - 2.15.1-1
- New version, removing hypre_PFMGSetupInterpOp_CC0, hypre_finalize,
  hypre_init, which appear actually to be internal, so soname unchanged
- Avoid tests

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 2.14.0-4
- Rebuild (scotch)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.14.0-2
- Build hypre-openmpi on s390x (#1571450)

* Fri Mar 23 2018 Dave Love <loveshack@fedoraproject.org> - 2.14.0-1
- Update to 2.14.0 (#1557645)
- Reinstate superlu and use superlu_dist

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.13.0-6
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 16 2018 Dave Love <loveshack@fedoraproject.org> - 2.13.0-5
- Fix openblas BR (#1545197)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov  6 2017 Dave Love <loveshack@fedoraproject.org> - 2.13.0-3
- Disable tests on ix86 temporarily

* Sat Nov  4 2017 Dave Love <loveshack@fedoraproject.org> - 2.13.0-3
- Revert last change in favour of updated superlu_dist

* Fri Nov  3 2017 Dave Love <loveshack@fedoraproject.org> - 2.13.0-2
- Fix link failure against parmetis

* Mon Oct 30 2017 Dave Love <loveshack@fedoraproject.org> - 2.13.0-1
- New version
- Configure --with-mli for compatibility
- Configure with superlu
- Remove -Dhypre_dgesvd=dgesvd_ bodge
- Bump soname major version (due to added elements in structs)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.11.2-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Thu May  4 2017 Dave Love <loveshack@fedoraproject.org> - 2.11.2-1
- New version

* Wed Mar 15 2017 Orion Poplawski <orion@cora.nwra.com> - 2.11.1-8
- Build with openblas on all available architectures

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec  1 2016 Dave Love <loveshack@fedoraproject.org> - 2.11.1-6
- Conditionalize mpich-devel%%{?_isa}

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.11.1-5
- Rebuild for openmpi 2.0

* Fri Jul 22 2016 Dave Love <loveshack@fedoraproject.org> - 2.11.1-4
- Ship manuals correctly

* Wed Jul 20 2016 Dave Love <loveshack@fedoraproject.org> - 2.11.1-3
- Avoid openmpi on s390
- Patch to not call hostname in test.sh and use two procs

* Mon Jul 11 2016 Dave Love <loveshack@fedoraproject.org> - 2.11.1-2
- Fix openblas conditionals

* Mon Jul 11 2016 Dave Love <loveshack@fedoraproject.org> - 2.11.1-1
- New version
- Update URL
- Drop previous patches -- make single library with new soversion
- Adjust configure/build
- Run tests
- Compile with -O3

* Fri Apr  1 2016 Dave Love <loveshack@fedoraproject.org> - 2.11.0-1
- New version
- Adjust hypre-shlibs-interlink.patch and %%lalibs

* Mon Dec 14 2015 Dave Love <loveshack@fedoraproject.org> - 2.10.1-2
- Fix use of %%license for -mpich package

* Tue Dec  1 2015 Dave Love <loveshack@fedoraproject.org> - 2.10.1-1
- New version
- Remove -Wl,-z,defs from configure to avoid link error (patch5)
- Fix use of atlas on non-x86
- Fix %%license conditional

* Sun Jul  5 2015 Dave Love <d.love@liverpool.ac.uk> - 2.9.1a-1
- New version, without babel stuff
- Modify patches
- Use %%license

* Fri Feb 20 2015 Dave Love <d.love@liverpool.ac.uk> - 2.8.0b-16
- Conditionalize out mpich on ppc64 el6
- Use -f with libtoolize (for f22)
- Fix some missing _isa in requires
- Drop unnecessary configure patch
- Run tests
- Small simplifications

* Wed Feb  4 2015 Dave Love <d.love@liverpool.ac.uk> - 2.8.0b-15
- Fix requires

* Mon Dec 29 2014 Dave Love <d.love@liverpool.ac.uk> - 2.8.0b-15
- Build without internal superlu

* Thu Dec 11 2014 Dave Love <d.love@liverpool.ac.uk> - 2.8.0b-14
- mpich version

* Fri Nov 28 2014 Dave Love <d.love@liverpool.ac.uk> - 2.8.0b-13
- Initial packaging, following Debian, including patches
  High release number to avoid clash with old SuSE-based version
