%global soversion 6

Name:           libcint
Version:        6.1.2
Release:        4%{?dist}
Summary:        General Gaussian-type orbitals integrals for quantum chemistry
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sunqm/libcint
Source0:        https://github.com/sunqm/libcint/archive/v%{version}/libcint-%{version}.tar.gz

BuildRequires:  gcc-gfortran
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  python3-numpy

# For documentation
BuildRequires:  pandoc
BuildRequires:  tex(latex)
BuildRequires:  make

# ppc64 doesn't appear to have floats beyond 64 bits, so ppc64 is
# disabled as per upstream's request
ExcludeArch:    %{power64}
# Exclude x86_64 since that platform has an API compatible library
# qcint, which however is ABI incompatible with libcint. We prefer to
# use the faster implementation.
ExcludeArch:    x86_64


%description
libcint is an open source library for analytical Gaussian integrals.
It provides C/Fortran API to evaluate one-electron / two-electron
integrals for Cartesian / real-spherical / spinor Gaussian type functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
# Replace name of build directory in test suite
for f in testsuite/*.py; do
    sed -i 's|../../build/libcint.so|../../%{_build}/libcint.so|g' $f
done

%build
export CFLAGS="%{optflags} -Wl,--as-needed"
%cmake -DENABLE_EXAMPLE=1 -DWITH_F12=1 -DWITH_COULOMB_ERF=1 -DWITH_RANGE_COULOMB=1 -DENABLE_TEST=1 -DQUICK_TEST=1 -S . -B %{_host}
%make_build -C %{_host}

# Build documentation
cd doc
bash compile.sh

%install
%make_install -C %{_host}

%check
make -C %{_host} test ARGS=-V

%files
%doc README.rst ChangeLog
%license LICENSE
%{_libdir}/libcint.so.%{soversion}*

%files devel
%doc doc/program_ref.pdf
%{_includedir}/cint.h
%{_includedir}/cint_funcs.h
%{_libdir}/libcint.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 6.1.2-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 18 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.1.2-1
- Disable build on x86_64; libcint is ABI incompatible with qcint
  which should be used instead on that platform.
- Update to 6.1.2.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 18 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 05 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0.

* Wed Mar 29 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0.

* Thu Mar 23 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.2.2-1
- Update to 5.2.2.

* Wed Mar 15 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1.

* Thu Feb 02 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.8-1
- Update to 5.1.8.

* Wed Dec 07 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.7-1
- Update to 5.1.7.

* Thu Sep 01 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.6-1
- Update to 5.1.6.

* Thu Aug 25 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.5-1
- Update to 5.1.5.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.2-1
- Update to 5.1.2.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.1-1
- Update to 5.1.1.

* Sat Dec 25 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0 for compatibility with PySCF.

* Mon Nov 08 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0, which drops BLAS dependency.

* Wed Sep 29 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.4.6-1
- Update to 4.4.6.

* Sat Aug 28 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.4.5-1
- Update to 4.4.5.

* Thu Aug 12 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.4.4-1
- Update to 4.4.4.

* Thu Jul 22 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.4.3-1
- Update to 4.4.3.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Björn Esser <besser82@fedoraproject.org> - 4.4.2-2
- Properly set BLA_VENDOR to FlexiBLAS for cmake >= 3.19

* Mon Jul 12 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.4.2-1
- Update to 4.4.2.

* Sat Jun 05 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.4.1-1
- Update to 4.4.1.

* Thu May 06 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0.

* Wed Apr 14 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.1.3-1
- Update to 4.1.3.

* Sun Apr 11 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.1.2-1
- Update to 4.1.2

* Mon Mar 22 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.1.1-1
- Update to 4.1.1.

* Wed Feb 17 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.7-1
- Update to 4.0.7.

* Sat Nov 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.6-1
- Update to 4.0.6.

* Sun Nov 01 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.5-1
- Update to 4.0.5.

* Thu Oct 08 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.2-1
- Update to 4.0.3.

* Mon Oct 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2.
- Make CMake build work also on released branches.

* Sat Oct 03 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1.

* Sun Sep 27 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0.

* Wed Aug 26 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1.

* Thu Aug 13 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.20-6
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.20-5
- Adapt to new CMake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.20-2
- Add missing conflicts: qcint-devel to libcint-devel.

* Thu May 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.20-1
- Update to 3.0.20, fixing a bug in magnetizabilities.

* Sun Feb 02 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-6
- Use OpenBLAS instead of ATLAS.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-4
- Include documentation.

* Sat Jan 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-3
- Use %%make_build and %%make_install, remove %%ldconfig_scriptlets.

* Sat Jan 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-2
- Fix typo in buildrequirements; python2 instead of python3.

* Tue Jan 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-1
- Update to 3.0.19.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 09 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.4-2
- Disable build on ppc64.

* Mon Oct 09 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.4-1
- Update to 3.0.4.

* Thu Oct 05 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.3-1
- Update to 3.0.3.

* Wed Oct 04 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2.

* Wed Sep 27 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1.

* Tue Sep 26 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.0-1
- Update to libcint version 3, based on patch sent by Qiming Sun.
- Enabled F12 integrals.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Matt Chan <talcite@gmail.com> - 2.8.7-3
- Disable aarch64 builds because of missing dependency
* Mon Sep 19 2016 Matt Chan <talcite@gmail.com> - 2.8.7
- Disable ppc64(LE) builds because of missing dependency
* Tue Jul 19 2016 Matt Chan <talcite@gmail.com> - 2.8.6
- Initial build
