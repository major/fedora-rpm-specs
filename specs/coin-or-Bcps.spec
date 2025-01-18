%global		module		Bcps

Name:		coin-or-%{module}
Summary:	Part of the COIN High Performance Parallel Search Framework
Version:	0.95.1
Release:	3%{?dist}
License:	EPL-1.0
URL:		https://github.com/coin-or/CHiPPS-BiCePS
Source0:	https://github.com/coin-or/CHiPPS-BiCePS/archive/releases/%{version}/CHiPPS-%{module}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

BuildRequires:	coin-or-Alps-devel
BuildRequires:	coin-or-Alps-doc
BuildRequires:	coin-or-Cgl-devel
BuildRequires:	coin-or-CoinUtils-doc
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	make

%description
BiCePS is one of the libraries that make up the CHiPPS (COIN High Performance
Parallel Search Framework) library hierarchy. It implements the data-handling
functions needed to support development of many types of relaxation-based
branch-and-bound algorithms, especially for solving mathematical programs. It
is intended to capture the implementation of methods common to all such
algorithms without assuming anything about the structure of the mathematical
program or the bounding method used. BLIS, which is another layer built on top
of BiCePS, is a concretization of Bcps for the case of mixed integer linear
programs. DIP is another implementation being developed using BLIS that
implements a decomposition-based bounding procedure.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Alps-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Alps-doc
Requires:	coin-or-CoinUtils-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n CHiPPS-BiCePS-releases-%{version}

%build
%configure

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all
doxygen doxydoc/doxygen.conf

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{_datadir}/doc/coin-or-bcps/LICENSE
cp -a doxydoc/html bcps_doxy.tag %{buildroot}%{_datadir}/doc/coin-or-bcps

%check
make test

%files
%license LICENSE
%dir %{_datadir}/doc/coin-or-bcps/
%{_datadir}/doc/coin-or-bcps/AUTHORS
%{_datadir}/doc/coin-or-bcps/README
%{_datadir}/doc/coin-or-bcps/README.md
%{_libdir}/libBcps.so.1
%{_libdir}/libBcps.so.1.*

%files		devel
%{_includedir}/coin-or/
%{_libdir}/libBcps.so
%{_libdir}/pkgconfig/bcps.pc

%files		doc
%{_datadir}/doc/coin-or-bcps/html/
%{_datadir}/doc/coin-or-bcps/bcps_doxy.tag

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Jerry James <loganjerry@gmail.com> - 0.95.1-1
- Version 0.95.1
- Verify that License is valid SPDX
- Drop all patches
- Stop building for 32-bit x86

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Florian Weimer <fweimer@redhat.com> - 0.94.5-9
- Port configure scripts to C99

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 0.94.5-1
- New upstream version
- Update URLs
- Change License from EPL to EPL-1.0
- Drop -doxygen path since new warnings pop up with every doxygen release
- Eliminate unnecessary BRs and Rs
- Eliminate rpath from the library
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Package doxygen tag file to enable cross-linking

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.94.4-8
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 15 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.94.4-1
- Update to latest upstream release (#1314316)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.94.3-1
- Update to latest upstream release (#1265640)

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.94.2-3
- Full rebuild of coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.94.2-1
- Update to latest upstream release (#1227744)

* Sun Apr 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.94.1-1
- Update to latest upstream release (#1209031)

* Sat Feb 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.94.0-2
- Rebuild to ensure using latest C++ abi changes.

* Sat Feb 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.94.0-1
- Update to latest upstream release (#1191433)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 12 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.93.12-2
- Remove deprecated doxygen option (#894591#c4).

* Sun Mar  9 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.93.12-1
- Update to latest upstream release.

* Sat Mar  8 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.93.11-1
- Update to latest upstream release.

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> -  0.93.6-1
- Update to latest upstream release.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.93.4-4
- Update to run make check (#894610#c4).

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.93.4-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.93.4-1
- Rename package to coin-or-Bcps.
- Do not package Thirdy party data or data without clean license.

* Thu Sep 27 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.93.4-1
- Initial coinor-Bcps spec.
