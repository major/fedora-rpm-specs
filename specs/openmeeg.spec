# rhbz#2104109
%bcond_with vtk
#

%bcond_without python
%bcond_without hdf5
%bcond_without matio
%bcond_with cgal
%bcond_without doc
%bcond_without check

%bcond_with debug

# This package fails its testsuite with LTO.  Disable LTO for now
%define _lto_cflags %{nil}

## https://github.com/openmeeg/openmeeg/issues/346
ExcludeArch: s390x

#%%global relsuf rc4

Name:    openmeeg
Version: 2.5.8
Release: 7%{?dist}
Summary: Low-frequency bio-electromagnetism solving forward problems in the field of EEG and MEG
License: CeCILL-B
URL:     http://openmeeg.github.io/
Source0: https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:  %{name}-use_builtin_find_blas_lapack.patch
Patch1:  types.patch

BuildRequires: make
BuildRequires: cmake3
BuildRequires: gcc-c++, git, chrpath
BuildRequires: gnuplot, wget, graphviz
BuildRequires: expat-devel
BuildRequires: flexiblas-devel
%{?fedora:BuildRequires: gifticlib-devel}
%{?fedora:BuildRequires: nifticlib-devel}
BuildRequires: zlib-devel
%if %{with hdf5}
BuildRequires: hdf5-devel
%endif
%if %{with matio}
BuildRequires: matio-devel
%endif
%if %{with vtk}
BuildRequires: vtk-devel
%endif
%if %{with cgal}
BuildRequires: CGAL-devel
%endif

# CGAL causes 'memory exhausted' error
%global openmeeg_cmake_options \\\
%if %{with debug} \
        -DCMAKE_BUILD_TYPE=Debug \\\
        -DCMAKE_CXX_FLAGS_DEBUG:STRING="-O0 -g -fPIC" \\\
%else \
        -DCMAKE_BUILD_TYPE=Release \\\
        -DCMAKE_CXX_FLAGS_DEBUG:STRING="%{build_cxxflags}" \\\
%endif \
        -DUSE_PROGRESSBAR=ON \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_OpenMEEG:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_matio:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_zlib:BOOL=ON \\\
        -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \\\
        -DCMAKE_SKIP_RPATH:BOOL=YES \\\
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \\\
        -DCMAKE_INSTALL_INCLUDEDIR:PATH=include/%{name} \\\
        -DUSE_OMP:BOOL=ON \\\
%if %{with python} \
        -DENABLE_PYTHON:BOOL=ON \\\
        -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \\\
        -DPYTHON_VERSION:STRING=%{python3_version} \\\
%endif \
%if %{with doc} \
        -DBUILD_DOCUMENTATION:BOOL=ON \\\
%endif \
%if %{with check} \
        -DBUILD_TESTING:BOOL=ON \\\
        -DTEST_HEAD3:BOOL=OFF \\\
%endif \
        -DBUILD_TOOLS:BOOL=ON \\\
        -DENABLE_PACKAGING:BOOL=OFF \\\
        -DSKIP_GITHUB_TESTS:BOOL=ON \\\
%if %{with cgal} \
        -DUSE_CGAL:BOOL=ON \\\
%endif \
        %{?fedora:-DUSE_GIFTI:BOOL=ON} \\\
%if %{with hdf5} \
        -DUSE_SYSTEM_hdf5:BOOL=ON \\\
%endif \
%if %{with matio} \
        -DUSE_SYSTEM_matio:BOOL=ON \\\
%endif \
%if %{with vtk} \
        -DUSE_VTK:BOOL=ON \\\
%endif \
        -DUSE_SYSTEM_zlib:BOOL=ON \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -Wno-dev

%description
The OpenMEEG software is a C++ package for solving the forward
problems of electroencephalography (EEG) and magnetoencephalography (MEG).


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use OpenMEEG.

%if %{with python}
%package        -n python%{python3_pkgversion}-openmeeg
Summary:        OpenMEEG binding for Python%{python3_pkgversion}
%py_provides    python3-%{name}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  swig
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       swig
%description    -n python%{python3_pkgversion}-openmeeg
OpenMEEG binding for Python%{python3_pkgversion}.
%endif

%if %{with doc}
%package        doc
Summary:        Documentation files for OpenMEEG
BuildRequires:  doxygen
BuildArch:      noarch
%description    doc
%{summary}.
%endif

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%if %{with debug}
export CXXFLAGS="-O0 -g -fPIC"
export CFLAGS="-O0 -g -fPIC"
%endif
%cmake %{openmeeg_cmake_options}
%cmake_build

%install
%cmake_install

%if %{with check}
%check
export FLEXIBLAS=netlib
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%if %{with debug}
export OPENMEEG_DATA_PATH=%{_builddir}/%{name}-%{version}/data
%ctest -- -VV --force-new-ctest-process -j1 --output-on-failure --debug -E 'openmeeg_python_test_python2.py'
%else
export OPENMEEG_DATA_PATH=%{_builddir}/%{name}-%{version}/data
%ctest -- -E 'openmeeg_python_test_python2.py'
%endif
%endif

%files
%license LICENSE.txt
%{_bindir}/om*
%{_libdir}/lib*.so.1
%{_libdir}/lib*.so.1.1.0

%files devel
%doc coding_guidelines.txt
#%%{_libdir}/cmake/%%{name}/
%{_libdir}/lib*.so
%{_includedir}/%{name}/

%if %{with python}
%files -n python%{python3_pkgversion}-openmeeg
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}.dist-info/
%endif

%if %{with doc}
%files doc
%license LICENSE.txt
%{_docdir}/OpenMEEG/
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 22 2024 Sandro <devel@penguinpee.nl> - 2.5.8-6
- Rebuild for NumPy 2.x

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 2.5.8-5
- Rebuild for hdf5 1.14.5

* Tue Aug 20 2024 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.5.8-4
- Rebuild for nifticlib 3.x

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.5.8-2
- Rebuilt for Python 3.13

* Mon Apr 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.5.8-1
- 2.5.8

* Mon Apr 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.5.7-4
- matio rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 19 2023 Antonio Trande <sagitter@fedoraproject.org> - 2.5.7-1
- Release 2.5.7

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.5.5-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 28 2022 Iñaki Úcar <iucar@fedoraproject.org> - 2.5.5-1
- Release 2.5.5
- Switch back to flexiblas rhbz#2121388

* Tue Jul 26 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.4.7-1
- Release 2.4.7
- Disable vtk for rhbz#2104109

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.4.2-1
- Release 2.4.2
- Disable tests (upstream bug #456)

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.4.2-0.20
- Rebuilt for Python 3.11

* Sat Mar 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.4.2-0.19
- Fix rhbz#2060866

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-0.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Orion Poplawski <orion@nwra.com> - 2.4.2-0.17
- Rebuild for vtk 9.1.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.2-0.15
- Rebuilt for Python 3.10

* Mon Apr 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.2-0.14
- matio rebuild.

* Tue Mar 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.4.2-0.13
- Add vtk-java BR (rhbz#1944534)

* Sun Jan 31 2021 Orion Poplawski <orion@nwra.com> - 2.4.2-0.12
- Rebuild for VTK 9

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.4.2-0.10
- Patched for CMake-3.19.* (rhbz#1917435)

* Mon Sep 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.4.2-0.9
- Rebuilt and patched for matio-1.5.18 (rhbz#1880819)

* Fri Aug 14 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.2-0.8
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Aug 10 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.4.2-0.7
- Disable debug builds

* Mon Aug 10 2020 Jeff Law <law@redhat.com> - 2.4.2-0.6
- Disable LTO

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-0.3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.4.2-0.1
- Pre-release 2.4.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 2.4.1-4
- Rebuild for vtk 8.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Orion Poplawski <orion@cora.nwra.com> - 2.4.1-2
- Rebuild for VTK 8.1

* Sun Sep 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.1-1
- Release 2.4.1
- Exclude s390x build

* Sat Sep 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-0.5.rc4
- Switch to python3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.4.rc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-0.3.rc4
- Update to 2.4-rc4

* Fri Apr 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-0.2.rc1
- Update to 2.4-rc1
- Modified for epel7

* Fri Mar 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-0.1.20180323gitee565c4
- Initial rpm
