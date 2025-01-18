Name:           ftnchek
Version:        3.3.1
Release:        43%{?dist}
Summary:        Static analyzer for Fortran 77 programs

License:        MIT
URL:            http://www.dsm.fordham.edu/~ftnchek/
Source0:        http://www.dsm.fordham.edu/~ftnchek/download/ftnchek-3.3.1.tar.gz
Patch0:         ftnchek-3.3.1-datadir.patch
Patch1:         http://www.dsm.fordham.edu/~ftnchek/download/ftnchek-3.3.1-varfmt.patch
# Patch to support bison 2.6
Patch2:         ftnchek-3.3.1-bison26.patch
Patch3: ftnchek-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  groff, emacs
BuildRequires:  perl
BuildRequires: make
Requires:       emacs-filesystem
Obsoletes:      emacs-ftnchek < 3.3.1-21
Provides:       emacs-ftnchek = %{version}-%{release}
Obsoletes:      emacs-ftnchek-el < 3.3.1-21
Provides:       emacs-ftnchek-el = %{version}-%{release}

%description
ftnchek is a static analyzer for Fortran 77 programs. It is designed to
detect certain errors in a Fortran program that a compiler usually does
not. ftnchek is not primarily intended to detect syntax errors. Its
purpose is to assist the user in finding semantic errors. Semantic
errors are legal in the Fortran language but are wasteful or may cause
incorrect operation. For example, variables which are never used may
indicate some omission in the program; uninitialized variables contain
garbage which may cause incorrect results to be calculated; and variables
which are not declared may not have the intended type. ftnchek is
intended to assist users in the debugging of their Fortran program. It is
not intended to catch all syntax errors. This is the function of the
compiler. Prior to using ftnchek, the user should verify that the program
compiles correctly.


%prep
%setup -q
%patch -P0 -p1 -b .datadir
%patch -P1 -p1 -b .varfmt
%patch -P2 -p1 -b .bison26
%patch -P3 -p1
#Stop configure from overriding CFLAGS
sed -i -e 's/CFLAGS="-DUNIX.*"//' configure


%build
export CFLAGS="$RPM_OPT_FLAGS -DUNIX"
%configure
make || :
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/ftnchek
%makeinstall STRIP=/bin/true datadir=$RPM_BUILD_ROOT%{_datadir}/ftnchek \
             lispdir=$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/ftnchek



%files
%doc LICENSE README FAQ PATCHES
%{_bindir}/dcl2inc
%{_bindir}/ftnchek
%{_datadir}/ftnchek/
%{_mandir}/man1/dcl2inc.1*
%{_mandir}/man1/ftnchek.1*
%{_emacs_sitelispdir}/ftnchek/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Florian Weimer <fweimer@redhat.com> - 3.3.1-38
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Orion Poplawski <orion@nwra.com> - 3.3.1-28
- Add BR perl (FTBFS bug #1604014)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-21
- Update emacs packaging (bug #1234565)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 2 2012 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-15
- Add patch to stop modifying bison output - breaks builds with bison 2.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov  9 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 3.3.1-11
- Update spec file and packaging to comply with Emacs add-on packaging guidelines

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 13 2009 Orion Poplawski <orion@cora.nwra.com> 3.3.1-9
- Add upstream varfmt patch
- Add BR bison to handle change to yacc file

* Thu Aug 28 2008 Orion Poplawski <orion@cora.nwra.com> 3.3.1-8
- Change %%patch -> %%patch0

* Sat Feb  9 2008 Orion Poplawski <orion@cora.nwra.com> 3.3.1-7
- Rebuild for gcc 3.4

* Tue Aug 21 2007 Orion Poplawski <orion@cora.nwra.com> 3.3.1-6
- Rebuild for BuildID

* Tue Aug 29 2006 Orion Poplawski <orion@cora.nwra.com> 3.3.1-5
- Rebuild for FC6

* Fri Mar 24 2006 Orion Poplawski <orion@cora.nwra.com> 3.3.1-4
- Don't strip binaries so we get a good debuginfo

* Wed Mar 08 2006 Orion Poplawski <orion@cora.nwra.com> 3.3.1-3
- Own %%{_datadir}/ftnchek/
- Add period to end of emacs package description

* Wed Mar 08 2006 Orion Poplawski <orion@cora.nwra.com> 3.3.1-2
- Add emacs sub-package for emacs support
- Fix up CFLAGS to use RPM CFLAGS
- Add FAQ and PATCHES to %%doc

* Tue Mar 07 2006 Orion Poplawski <orion@cora.nwra.com> 3.3.1-1
- Initial Fedora Extras submission
