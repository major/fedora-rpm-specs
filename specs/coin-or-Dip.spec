%global		module		Dip

%if 0%{?fedora}
%global		with_asl	1
%else
%global		with_asl	0
%endif
%global		with_mpi	0

Name:		coin-or-%{module}
Summary:	Decomposition for Integer Programming
Version:	0.95.0
Release:	15%{?dist}
License:	EPL-1.0
URL:		https://github.com/coin-or/%{module}/wiki
Source0:	https://github.com/coin-or/%{module}/archive/releases/%{version}/%{module}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

BuildRequires:	coin-or-Alps-doc
BuildRequires:	coin-or-Cbc-doc
%if %{with_mpi}
BuildRequires:	coin-or-Ipopt-openmpi-devel
%else
BuildRequires:	pkgconfig(ipopt)
%endif
BuildRequires:	doxygen-latex
BuildRequires:	gcc-c++
BuildRequires:	make
%if %{with_asl}
BuildRequires:	asl-devel
%endif
%if %{with_mpi}
BuildRequires:	pkgconfig(ompi)
BuildRequires:	scalapack-openmpi-devel
BuildRequires:	openssh-clients
%endif
BuildRequires:	pkgconfig(alps)
BuildRequires:	pkgconfig(cbc)
BuildRequires:	pkgconfig(symphony)
BuildRequires:	tex(arydshln.sty)
BuildRequires:	tex(comment.sty)
BuildRequires:	tex(subfigure.sty)
BuildRequires:	tex(textpos.sty)
BuildRequires:	tex(vmargin.sty)

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Bad #define generated if svnversion is available
Patch1:		%{name}-svnversion.patch

# Fix a BibTeX commenting issue in the guide
Patch2:		%{name}-bib.patch

# Fix Modern C issues in the configure script
Patch3:		%{name}-configure-c99.patch

%description
DIP (Decomposition for Integer Programming) is an open-source extensible
software framework for implementing decomposition-based bounding algorithms
for use in solving large-scale discrete optimization problems. The framework
provides a simple API for experimenting with various decomposition-based
algorithms, such as Dantzig-Wolfe decomposition, Lagrangian relaxation,
and various cutting plane methods. Given a compact formulation and a
relaxation, the framework takes care of all algorithmic details associated
with implementing any of a wide range of decomposition-based algorithms,
such as branch and cut, branch and price, branch and cut and price,
subgradient-based Lagrangian relaxation, branch and relax and cut, and
decompose and cut. The user can specify customizations, such as methods
for generating valid inequalities and branching, in terms of the variables
of the compact formulation, without having to worry about the details of
any required reformulations.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Alps-devel%{?_isa}
Requires:	coin-or-Cgl-devel%{?_isa}
Requires:	coin-or-SYMPHONY-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Alps-doc
Requires:	coin-or-Cbc-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n %{module}-releases-%{version}

# Fix paths to the examples
sed -i 's,examples/Dippy,src/dippy/examples,g' Dip/doc/guide/*.tex

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ @DIPLIB_PCLIBS@/\nLibs.private:&/' Dip/dip.pc.in

%build
%if %{with_mpi}
%_openmpi_load
%endif
%configure --enable-openmp	\
%if %{with_asl}
	--with-asl-lib="-lasl -lipoptamplinterface -lbonminampl" \
	--with-asl-incdir="%{_includedir}/asl"
%endif

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all
%make_build -C Dip doxydoc
cd Dip/doc/guide
pdflatex dippy
bibtex dippy
pdflatex dippy
pdflatex dippy
cd -

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_pkgdocdir}/{LICENSE,dip_addlibs.txt}
install -m 644 AUTHORS README* %{buildroot}%{_pkgdocdir}
install -m 644 Dip/doc/guide/dippy.pdf %{buildroot}%{_pkgdocdir}
cp -a Dip/doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

%check
%if %{with_mpi}
%_openmpi_load
%endif
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%files
%license LICENSE
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/README*
%{_bindir}/dip
%{_libdir}/libDecomp.so.0
%{_libdir}/libDecomp.so.0.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libDecomp.so
%{_libdir}/pkgconfig/dip.pc

%files		doc
%{_pkgdocdir}/html/
%{_pkgdocdir}/dip_doxy.tag
%{_pkgdocdir}/dippy.pdf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Jerry James <loganjerry@gmail.com> - 0.95.0-13
- Build with asl instead of mp
- Verify that License is valid SPDX
- Stop building for 32-bit x86

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Florian Weimer <fweimer@redhat.com> - 0.95.0-9
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Antonio Trande <sagitter@fedoraproject.org> - 0.95.0-5
- Rebuilt for Ipopt-3.14.4

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 21 2020 Jerry James <loganjerry@gmail.com> - 0.95.0-1
- Version 0.95.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 0.92.4-1
- Update to latest upstream release
- Change URLs to github
- Change License from EPL to EPL-1.0
- Add -doc subpackage
- Eliminate unnecessary BRs and Rs
- Add -bib patch to fix guide build
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Filter out unnecessary Libs values from pkgconfig files

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.92.2-8
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.92.2-1
- Update to latest upstream release

* Sun Mar 13 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.91.2-6
- Install docs directly into %%{_pkgdocdir} (F24FTBFS, RHBZ#1307388).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.91.2-4
- Full rebuild of coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.91.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 23 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.91.2-1
- Update to latest upstream release.
- Rediff patches (#894602#c10)
- Use license macro (#894602#c10)

* Sat Feb 28 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.91.1-1
- Update to latest upstream release.

* Mon Apr 21 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.9.9-2
- Disable python subpackage, it should be packaged separately (#894602#c4).

* Sat Apr 19 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.9.9-1
- Update to latest upstream release.
- Create new python subpackage.

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.9.4-1
- Update to latest upstream release.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.83.2-4
- Update to run make check (#894610#c4).

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.83.2-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.83.2-2
- Rename package to coin-or-Dip.
- Do not package Thirdy party data or data without clean license.

* Sat Sep 29 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.83.2-1
- Initial coinor-Dip spec.
