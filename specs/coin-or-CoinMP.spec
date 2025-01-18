%global		module		CoinMP

Name:		coin-or-%{module}
Summary:	C-API interface to CLP, CBC and CGL
Version:	1.8.4
Release:	16%{?dist}
License:	CPL-1.0
URL:		https://projects.coin-or.org/%{module}
Source0:	http://www.coin-or.org/download/pkgsource/%{module}/%{module}-%{version}.tgz
BuildRequires:	coin-or-Cbc-devel
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	make

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Fix Modern C issues in the configure script
Patch1:		%{name}-configure-c99.patch

%description
CoinMP is a C-API library that supports most of the functionality of CLP
(Coin LP), CBC (Coin Branch-and-Cut), and CGL (Cut Generation Library)
projects.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{module}-%{version}
# Use unix style line endings
for file in README AUTHORS examples/example.c LICENSE; do
    sed -i.orig 's|\r||' $file
    touch -r $file.orig $file
    rm $file.orig
done

%build
export CPPFLAGS='-DNDEBUG'
%configure

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
# Some install rule install 2 sample doc files under buildroot/buildroot
for file in `find %{buildroot}%{buildroot} -type f`; do
    mv $file `echo $file | sed -e 's|%{buildroot}||'`
done
rm %{buildroot}%{_docdir}/%{name}/{LICENSE,Makefile,coinmp_addlibs.txt}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%files
%license LICENSE
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/example.c
%{_libdir}/libCoinMP.so.1
%{_libdir}/libCoinMP.so.1.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libCoinMP.so
%{_libdir}/pkgconfig/coinmp.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Jerry James <loganjerry@gmail.com> - 1.8.4-14
- Stop building for 32-bit x86
- Convert License tag to SPDX
- Build with NDEBUG

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Florian Weimer <fweimer@redhat.com> - 1.8.4-9
- Port configure script to C99

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 1.8.4-1
- Update to latest upstream release
- Eliminate unnecessary BRs and Rs
- Eliminate rpath from the library
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.8.3-7
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8.3-1
- Update to latest upstream release
- Remove no longer needed patch

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.7.6-7
- Full rebuild of coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.6-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.7.6-4
- Rebuild to ensure using latest C++ abi changes.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.7.6-1
- Update to latest upstream release.

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.7.1-1
- Update to latest upstream release.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6.0-4
- Update to run make check (#894610#c4).

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6.0-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6.0-2
- Rename package to coin-or-CoinMP.
- Do not package Thirdy party data or data without clean license.

* Sat Sep 29 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6.0-1
- Initial coinor-CoinMP spec.
