%bcond_without system_lapack
%bcond_without atlas
%bcond_without blis
%bcond_without openblas

# https://bugzilla.redhat.com/show_bug.cgi?id=2058840
%undefine _ld_as_needed

%if %{with openblas}
%global default_backend openblas-openmp
%else
%global default_backend netlib
%endif
%global default_backend64 %{default_backend}64

%global major_version 3
%global minor_version 3
%global patch_version 1
%global laapi_version 3.11.0

Name:           flexiblas
Version:        %{major_version}.%{minor_version}.%{patch_version}
Release:        2%{?dist}
Summary:        A BLAS/LAPACK wrapper library with runtime exchangeable backends

# GPLv3 with an exception for the BLAS/LAPACK interface
# https://www.gnu.org/licenses/gpl-faq.en.html#LinkingOverControlledInterface
# libcscutils/ is LGPLv2+
# contributed/ and test/ are BSD
License:        GPLv3 with exceptions and LGPLv2+ and BSD
URL:            https://www.mpi-magdeburg.mpg.de/projects/%{name}
Source0:        https://github.com/mpimd-csc/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make, cmake, python
BuildRequires:  gcc-fortran, gcc-c++
BuildRequires:  multilib-rpm-config
%if %{with system_lapack}
BuildRequires:  blas-static, lapack-static
%endif
%if %{with atlas}
BuildRequires:  atlas-devel
%endif
%if %{with blis}
BuildRequires:  blis-devel
%endif
%if %{with openblas}
BuildRequires:  openblas-devel
%endif

%global _description %{expand:
FlexiBLAS is a wrapper library that enables the exchange of the BLAS and
LAPACK implementation used by a program without recompiling or relinking it.
}

%description %_description

%package        netlib
Summary:        FlexiBLAS wrapper library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-%{default_backend}%{?_isa} = %{version}-%{release}

%description    netlib %_description
This package contains the wrapper library with 32-bit integer support.

%package        hook-profile
Summary:        FlexiBLAS profile hook plugin
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    hook-profile %_description
This package contains a plugin that enables profiling support.

%package        devel
Summary:        Development headers and libraries for FlexiBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
%if 0%{?__isa_bits} == 64
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}
%endif

%description    devel %_description
This package contains the development headers and libraries.

%if %{with atlas}
%package        atlas
Summary:        FlexiBLAS wrappers for ATLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    atlas %_description
This package contains FlexiBLAS wrappers for the ATLAS project.
%endif

%if %{with blis}
%package        blis-serial
Summary:        FlexiBLAS wrappers for BLIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    blis-serial %_description
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 32-integer interface.

%package        blis-openmp
Summary:        FlexiBLAS wrappers for BLIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    blis-openmp %_description
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 32-integer interface.

%package        blis-threads
Summary:        FlexiBLAS wrappers for BLIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    blis-threads %_description
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 32-integer interface.
%endif

%if %{with openblas}
%package        openblas-serial
Summary:        FlexiBLAS wrappers for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    openblas-serial %_description
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 32-integer interface.

%package        openblas-openmp
Summary:        FlexiBLAS wrappers for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    openblas-openmp %_description
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 32-integer interface.

%package        openblas-threads
Summary:        FlexiBLAS wrappers for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    openblas-threads %_description
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 32-integer interface.
%endif

%if 0%{?__isa_bits} == 64
%package        netlib64
Summary:        FlexiBLAS wrapper library (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-%{default_backend64}%{?_isa} = %{version}-%{release}

%description    netlib64 %_description
This package contains the wrapper library with 64-bit integer support.

%package        hook-profile64
Summary:        FlexiBLAS profile hook plugin (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    hook-profile64 %_description
This package contains a plugin that enables profiling support.

%if %{with blis}
%package        blis-serial64
Summary:        FlexiBLAS wrappers for BLIS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    blis-serial64 %_description
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 64-integer interface.

%package        blis-openmp64
Summary:        FlexiBLAS wrappers for BLIS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    blis-openmp64 %_description
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 64-integer interface.

%package        blis-threads64
Summary:        FlexiBLAS wrappers for BLIS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    blis-threads64 %_description
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 64-integer interface.
%endif

%if %{with openblas}
%package        openblas-serial64
Summary:        FlexiBLAS wrappers for OpenBLAS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    openblas-serial64 %_description
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 64-integer interface.

%package        openblas-openmp64
Summary:        FlexiBLAS wrappers for OpenBLAS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    openblas-openmp64 %_description
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 64-integer interface.

%package        openblas-threads64
Summary:        FlexiBLAS wrappers for OpenBLAS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    openblas-threads64 %_description
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 64-integer interface.
%endif
%endif

%prep
%autosetup -p1

%build
%if %{with system_lapack}
rm -rf contributed
%endif
%cmake -B build \
%if %{with system_lapack}
    -DLAPACK_API_VERSION=%{laapi_version} \
    -DSYS_BLAS_LIBRARY=$(pkg-config --variable=libdir blas)/libblas.a \
    -DSYS_LAPACK_LIBRARY=$(pkg-config --variable=libdir lapack)/liblapack_pic.a \
%endif
    -DINTEGER8=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DTESTS=ON
%make_build -C build
%if 0%{?__isa_bits} == 64
%cmake -B build64 \
%if %{with system_lapack}
    -DLAPACK_API_VERSION=%{laapi_version} \
    -DSYS_BLAS_LIBRARY=$(pkg-config --variable=libdir blas)/libblas64.a \
    -DSYS_LAPACK_LIBRARY=$(pkg-config --variable=libdir lapack)/liblapack_pic64.a \
%endif
    -DINTEGER8=ON \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DTESTS=ON
%make_build -C build64
%endif

%install
%make_install -C build
echo "default = %{default_backend}" > %{buildroot}%{_sysconfdir}/%{name}rc
%if 0%{?__isa_bits} == 64
%make_install -C build64
echo "default = %{default_backend64}" > %{buildroot}%{_sysconfdir}/%{name}64rc
%endif

# Replace arch-dependent header file with arch-independent stub
%multilib_fix_c_header --file %{_includedir}/%{name}/%{name}_config.h

# remove dummy hook
rm -f %{buildroot}%{_libdir}/%{name}*/lib%{name}_hook_dummy.so

# set Fedora-friendly names
rename -- serial -serial %{buildroot}%{_libdir}/%{name}*/* || true
rename -- openmp -openmp %{buildroot}%{_libdir}/%{name}*/* || true
rename -- pthread -threads %{buildroot}%{_libdir}/%{name}*/* || true
rename NETLIB netlib %{buildroot}%{_sysconfdir}/%{name}*.d/* || true
rename ATLAS atlas %{buildroot}%{_sysconfdir}/%{name}*.d/* || true
rename Blis blis %{buildroot}%{_sysconfdir}/%{name}*.d/* || true
rename OpenBLAS openblas %{buildroot}%{_sysconfdir}/%{name}*.d/* || true
rename -- Serial -serial %{buildroot}%{_sysconfdir}/%{name}*.d/* || true
rename -- OpenMP -openmp %{buildroot}%{_sysconfdir}/%{name}*.d/* || true
rename -- PThread -threads %{buildroot}%{_sysconfdir}/%{name}*.d/* || true
find %{buildroot}%{_sysconfdir}/%{name}*.d/* -type f \
    -exec sed -i 's NETLIB netlib gI' {} \;\
    -exec sed -i 's ATLAS atlas gI' {} \;\
    -exec sed -i 's Blis blis gI' {} \;\
    -exec sed -i 's OpenBLAS openblas gI' {} \;\
    -exec sed -i 's Serial -serial gI' {} \;\
    -exec sed -i 's OpenMP -openmp gI' {} \;\
    -exec sed -i 's PThread -threads gI' {} \;

%check
export FLEXIBLAS_TEST=%{buildroot}%{_libdir}/%{name}/lib%{name}_%{default_backend}.so
make -C build test
%if 0%{?__isa_bits} == 64
export FLEXIBLAS64_TEST=%{buildroot}%{_libdir}/%{name}64/lib%{name}_%{default_backend64}.so
make -C build64 test
%endif

%files
%license COPYING COPYING.NETLIB
%doc ISSUES.md README.md CHANGELOG

%files netlib
%config(noreplace) %{_sysconfdir}/%{name}rc
%dir %{_sysconfdir}/%{name}rc.d
%{_sysconfdir}/%{name}rc.d/netlib.conf
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.%{major_version}
%{_libdir}/lib%{name}.so.%{major_version}.%{minor_version}
%{_libdir}/lib%{name}_api.so.%{major_version}
%{_libdir}/lib%{name}_api.so.%{major_version}.%{minor_version}
%{_libdir}/lib%{name}_mgmt.so.%{major_version}
%{_libdir}/lib%{name}_mgmt.so.%{major_version}.%{minor_version}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}_fallback_lapack.so
%{_libdir}/%{name}/lib%{name}_netlib.so
%{_mandir}/man1/%{name}.1*

%files hook-profile
%{_libdir}/%{name}/lib%{name}_hook_profile.so

%files devel
%{_bindir}/%{name}-config
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_api.so
%{_libdir}/lib%{name}_mgmt.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}_api.pc
%if 0%{?__isa_bits} == 64
%{_bindir}/%{name}64-config
%{_includedir}/%{name}64
%{_libdir}/lib%{name}64.so
%{_libdir}/lib%{name}64_api.so
%{_libdir}/lib%{name}64_mgmt.so
%{_libdir}/pkgconfig/%{name}64.pc
%{_libdir}/pkgconfig/%{name}64_api.pc
%endif
%{_mandir}/man3/%{name}_*
%{_mandir}/man7/%{name}-api.7*

%if %{with atlas}
%files atlas
%{_sysconfdir}/%{name}rc.d/atlas.conf
%{_libdir}/%{name}/lib%{name}_atlas.so
%endif

%if %{with blis}
%files blis-serial
%{_sysconfdir}/%{name}rc.d/blis-serial.conf
%{_libdir}/%{name}/lib%{name}_blis-serial.so

%files blis-openmp
%{_sysconfdir}/%{name}rc.d/blis-openmp.conf
%{_libdir}/%{name}/lib%{name}_blis-openmp.so

%files blis-threads
%{_sysconfdir}/%{name}rc.d/blis-threads.conf
%{_libdir}/%{name}/lib%{name}_blis-threads.so
%endif

%if %{with openblas}
%files openblas-serial
%{_sysconfdir}/%{name}rc.d/openblas-serial.conf
%{_libdir}/%{name}/lib%{name}_openblas-serial.so

%files openblas-openmp
%{_sysconfdir}/%{name}rc.d/openblas-openmp.conf
%{_libdir}/%{name}/lib%{name}_openblas-openmp.so

%files openblas-threads
%{_sysconfdir}/%{name}rc.d/openblas-threads.conf
%{_libdir}/%{name}/lib%{name}_openblas-threads.so
%endif

%if 0%{?__isa_bits} == 64
%files netlib64
%config(noreplace) %{_sysconfdir}/%{name}64rc
%dir %{_sysconfdir}/%{name}64rc.d
%{_sysconfdir}/%{name}64rc.d/netlib.conf
%{_bindir}/%{name}64
%{_libdir}/lib%{name}64.so.%{major_version}
%{_libdir}/lib%{name}64.so.%{major_version}.%{minor_version}
%{_libdir}/lib%{name}64_api.so.%{major_version}
%{_libdir}/lib%{name}64_api.so.%{major_version}.%{minor_version}
%{_libdir}/lib%{name}64_mgmt.so.%{major_version}
%{_libdir}/lib%{name}64_mgmt.so.%{major_version}.%{minor_version}
%dir %{_libdir}/%{name}64
%{_libdir}/%{name}64/lib%{name}_fallback_lapack.so
%{_libdir}/%{name}64/lib%{name}_netlib.so
%{_mandir}/man1/%{name}64.1*

%files hook-profile64
%{_libdir}/%{name}64/lib%{name}_hook_profile.so

%if %{with blis}
%files blis-serial64
%{_sysconfdir}/%{name}64rc.d/blis-serial64.conf
%{_libdir}/%{name}64/lib%{name}_blis-serial64.so

%files blis-openmp64
%{_sysconfdir}/%{name}64rc.d/blis-openmp64.conf
%{_libdir}/%{name}64/lib%{name}_blis-openmp64.so

%files blis-threads64
%{_sysconfdir}/%{name}64rc.d/blis-threads64.conf
%{_libdir}/%{name}64/lib%{name}_blis-threads64.so
%endif

%if %{with openblas}
%files openblas-serial64
%{_sysconfdir}/%{name}64rc.d/openblas-serial64.conf
%{_libdir}/%{name}64/lib%{name}_openblas-serial64.so

%files openblas-openmp64
%{_sysconfdir}/%{name}64rc.d/openblas-openmp64.conf
%{_libdir}/%{name}64/lib%{name}_openblas-openmp64.so

%files openblas-threads64
%{_sysconfdir}/%{name}64rc.d/openblas-threads64.conf
%{_libdir}/%{name}64/lib%{name}_openblas-threads64.so
%endif
%endif

%changelog
* Tue Apr 04 2023 Iñaki Úcar <iucar@fedoraproject.org> - 3.3.1-2
- Fix multilib config header conflict

* Mon Apr 03 2023 Iñaki Úcar <iucar@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Iñaki Úcar <iucar@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0

* Fri Dec 23 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.2.1-3
- Specify LAPACK API compatibility level

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1

* Mon Jun 27 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.2.0-4
- Add depency on netlib subpackage to all backends (RHBZ#2101369)

* Tue May 24 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.2.0-3
- Add explicit requires to devel package to content rpmdeps test

* Tue May 17 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.2.0-2
- Undefine _ld_as_needed to fix underlinking issue (BZ 2058840)

* Tue May 17 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Fri Feb 25 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3

* Mon Jan 17 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.1.2-1
- Update to 3.1.2, adding support for LAPACK up to 3.10.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Nikola Forró <nforro@redhat.com> - 3.0.4-5
- Get rid of RPATH

* Fri Apr 23 2021 Iñaki Úcar <iucar@fedoraproject.org> 3.0.4-4
- Rebuilt for LAPACK 3.9.1 with LAPACK_API_VERSION=3.9.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Iñaki Úcar <iucar@fedoraproject.org> 3.0.4-2
- https://fedoraproject.org/wiki/Changes/Remove_make_from_BuildRoot

* Thu Oct 22 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.4-1
- Update to 3.0.4, fixes #1889069

* Wed Oct 21 2020 Kalev Lember <klember@redhat.com> - 3.0.3-2
- Use pkg-config for getting blas and lapack directories

* Fri Aug 28 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.3-1
- Update to 3.0.3, fixes ScaLAPACK issues

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Tue Jul 21 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1, license updated

* Fri Jul 03 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.0-5
- Change default backend to openblas-openmp

* Wed Jul 01 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.0-4
- Fix a bug setting the default backend

* Wed Jul 01 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.0-3
- Move man3 pages to devel subpackage
- Remove dummy hook (only useful for FlexiBLAS development)
- Move profile hook to a separate package (not needed for standard usage)
- Enable Blis64 on s390x again, #1852549 fixed in rawhide

* Tue Jun 30 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.0-2
- Own provided directories
- More robust file renaming
- Rename wrapper(64) subpackages to netlib(64)
- Conditionalize all external libraries, as well as the default
- Disable Blis64 on s390x, which is currently unavailable

* Mon Jun 29 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.0-1
- Initial packaging for Fedora
