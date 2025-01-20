%global soversion 6

Name:           qcint
Version:        6.1.2
Release:        4%{?dist}
Summary:        An optimized libcint branch for X86 platform with SSE3 intrinsics
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/sunqm/qcint
Source0:        https://github.com/sunqm/qcint/archive/v%{version}/qcint-%{version}.tar.gz

# This package uses AVX/AVX2/AVX-512 extensions
ExclusiveArch:  x86_64
# qcint is a drop-in replacement of libcint with architecture
# dependent optimizations. The libraries are API compatible, but ABI
# incompatible.
Provides:       libcint = %{version}-%{release}
Obsoletes:      libcint < %{version}-%{release}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake 

%description    
Qcint is a branch of the libcint library.  It provides exactly the
same APIs as libcint. However, the code is optimized using AVX
instructions. On x86_64 platform, qcint can be 5 ~ 50% faster than
libcint. Please refer to libcint for more details of the features.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libcint-devel = %{version}-%{release}
Obsoletes:      libcint-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -msse3 -Wl,--as-needed"
%cmake -DENABLE_EXAMPLE=1 -DWITH_F12=1 -DWITH_COULOMB_ERF=1 -DWITH_RANGE_COULOMB=1 -DQUICK_TEST=1 -DBUILD_MARCH_NATIVE=OFF -S . -B %{_host}
%make_build -C %{_host}

%install
%make_install -C %{_host}

%ldconfig_scriptlets

%files
%doc README.md ChangeLog
%license LICENSE
%{_libdir}/libcint.so.%{soversion}*

%files devel
%{_includedir}/cint.h
%{_includedir}/cint_funcs.h
%{_libdir}/libcint.so

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 6.1.2-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 18 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.1.2-1
- qcint is API compatible but ABI incompatible with libcint; qcint is
  now the only library built on x86_64 and replaces libcint.
- Update to 6.1.2.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 18 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 05 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0.

* Wed Mar 29 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0.

* Thu Mar 23 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.2.2-1
- Update to 5.2.2.

* Wed Mar 15 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.8-1
- Update to 5.1.8.

* Wed Dec 07 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.7-1
- Update to 5.1.7.

* Fri Sep 02 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.6-1
- Update to 5.1.6.

* Thu Aug 25 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.5-1
- Update to 5.1.5.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.2-1
- Update to 5.1.2.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.1-1
- Update to 5.1.1.

* Sat Dec 25 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0 for PySCF compatibility.

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

* Tue Jul 13 2021 Björn Esser <besser82@fedoraproject.org> - 4.4.2-2
- Properly set BLA_VENDOR to FlexiBLAS for cmake >= 3.19

* Mon Jul 12 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.4.2-1
- Update to 4.4.2.

* Sat Jun 05 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.4.1-1
- Update to 4.4.1.

* Tue May 18 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.4.0-2
- Fix issue with illegal instructions caused by silent change of
  behavior in the upstream project.

* Thu May 06 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0.

* Wed Apr 14 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.1.3-1
- Update to 4.1.3.

* Sun Apr 11 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.1.2-1
- Update to 4.1.2.

* Tue Apr 06 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.1.1-1
- Update to 4.1.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.6-1
- Update to 4.0.6.

* Sat Nov 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.5-1
- Update to 4.0.5.

* Thu Oct 08 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.3-1
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

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.20-6
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.20-5
- Adapt to new CMake macros.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Petr Viktorin <pviktori@redhat.com> - 3.0.20-3
- Remove BuildRequires on python2

* Sat May 23 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.20-2
- Add conflicts with libcint-devel to qcint-devel package.

* Thu May 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.20-1
- Update to 3.0.20, no changes from 3.0.19.

* Sun Feb 02 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-3
- Use OpenBLAS instead of ATLAS.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-1
- Update to 3.0.19.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.2-1
- Update to version 3.0.2.

* Tue Sep 26 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.1-1
- Update to version 3.0.1.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Matt Chan <talcite@gmail.com> - 1.8.6-1
- Initial build
