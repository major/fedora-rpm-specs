%global		module		FlopC++

Name:		coin-or-%{module}
Summary:	Algebraic modeling language
Version:	1.2.5
Release:	16%{?dist}
License:	EPL-1.0
URL:		https://projects.coin-or.org/FlopCpp
Source0:	http://www.coin-or.org/download/pkgsource/%{module}/%{module}-%{version}.tgz
BuildRequires:	coin-or-Cbc-devel
BuildRequires:	coin-or-Cbc-doc
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	make

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Catch polymorphic exceptions by reference, not by value
Patch1:		%{name}-catch.patch

Patch2:		coin-or-FlopC++-configure-c99.patch

%description
An open source algebraic modeling language implemented as a C++ class
library.

Using FLOPC++, linear optimization models can be specified in a declarative
style, similar to algebraic modeling languages such as GAMS and AMPL,
within a C++ program. As a result the traditional strengths of algebraic
modeling languages are preserved, while embedding linear optimization
models in software applications is facilitated.

FLOPC++ can be used as a substitute for traditional modeling languages,
when modeling linear optimization problems, but its principal strength
lies in the fact that the modeling facilities are combined with a
powerful general purpose programming language. This combination is
essential for implementing efficient algorithms (using linear optimization
for subproblems), integrating optimization models in user applications, etc.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-CoinUtils-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Cbc-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n %{module}-%{version}
sed -i 's/\r//' README

%build
%configure

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all doxydoc

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,flopcpp_addlibs.txt}
cp -a doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%files
%license LICENSE
%{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/flopcpp_doxy.tag
%{_libdir}/libFlopCpp.so.0
%{_libdir}/libFlopCpp.so.0.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libFlopCpp.so
%{_libdir}/pkgconfig/flopcpp.pc

%files		doc
%{_docdir}/%{name}/html
%{_docdir}/%{name}/flopcpp_doxy.tag

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Jerry James <loganjerry@gmail.com> - 1.2.5-14
- Stop building for 32-bit x86
- Verify the License field is valid SPDX
- Correct the project URL

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 05 2023 Florian Weimer <fweimer@redhat.com> - 1.2.5-10
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 1.2.5-1
- Update to latest upstream release, fixes FTBFS (bz 1555673, 1603681, 1674750)
- Update project URL
- Change License from EPL to EPL-1.0
- Eliminate unnecessary BRs and Rs
- Add -doc subpackage
- Eliminate rpath from the library
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 15 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.4-1
- Update to latest upstream release
- Correct FTBFS in rawhide (#1307389)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.7-6
- Full rebuild of coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.7-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar  1 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.7-4
- Correct package URL (#894603#c5)
- Correct line endings of the README file (#894603#c5)

* Sat Feb 28 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.7-3
- Correct package build
- Use license macro

* Sat Oct 11 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.7-2
- Update to upstream repackaged tarball.

* Sat Sep 20 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.7-1
- Update to latest upstream release
- Add bzip2 and zlib devel to build requires (#894603#c3)
- Create doc subpackage

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.2-4
- Update to run make check (#894610#c4).

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.2-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.2-2
- Rename package to coin-or-FlopC++.
- Do not package Thirdy party data or data without clean license.

* Thu Sep 27 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.2-1
- Initial coinor-FlopC++ spec.
