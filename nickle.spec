%if 0%{?fedora}
%bcond_without docs
%else
# rubygem dependencies not in EPEL yet
# F34: prawn-svg not Ruby 3.0 compatible
# https://bugzilla.redhat.com/show_bug.cgi?id=1923630
%bcond_with docs
%endif

Name:           nickle
Version:        2.90
Release:        7%{?dist}
Summary:        A programming language-based prototyping environment

License:        MIT
URL:            https://nickle.org
Source0:        https://nickle.org/release/nickle-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
%if %{with docs}
# for documentation
BuildRequires:  rubygem(asciidoctor-pdf)
BuildRequires:  rubygem(prawn-icon)
BuildRequires:  rubygem(prawn-svg)
%endif

%description
Nickle is a programming language based prototyping environment with
powerful programming and scripting capabilities. Nickle supports a
variety of datatypes, especially arbitrary precision numbers. The
programming language vaguely resembles C. Some things in C which do
not translate easily are different, some design choices have been made
differently, and a very few features are simply missing.

Nickle provides the functionality of UNIX bc, dc and expr in
much-improved form. It is also an ideal environment for prototyping
complex algorithms. Nickle's scripting capabilities make it a nice
replacement for spreadsheets in some applications, and its numeric
features nicely complement the limited numeric functionality of
text-oriented languages such as AWK and PERL.

%package devel
Summary:  Include files for Nickle
Requires: %{name} = %{version}-%{release}

%description devel
Include files for Nickle, used for building external FFI (foreign
function interface) libraries (e.g. the Cairo interface for Nickle).


%prep
%autosetup -p1


%build
# we will install documentation ourselves,
# but this saves having to delete the ones installed by 'make install'
%configure --docdir=%{_pkgdocdir}
%make_build


%check
cd test
make check


%install
%make_install DESTDIR=$RPM_BUILD_ROOT
rm `find examples -name 'Makefile*'`
rm examples/COPYING

# Fix permissions on example files
chmod a-x examples/menace2.5c
chmod a-x examples/turtle/snowflake.5c


%files
%license COPYING
%doc README README.name AUTHORS ChangeLog TODO
%doc examples
%if %{with docs}
%doc doc/tutorial/nickle-tutorial.pdf
%endif
%{_bindir}/nickle
%{_datadir}/nickle/
%exclude %{_datadir}/nickle/COPYING
%exclude %{_datadir}/nickle/examples
%{_mandir}/man1/nickle.1*

%files devel
%{_includedir}/nickle

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.90-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 16 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.90-4
- Reenable docs on Fedora > 34

* Sun Mar 14 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.90-3
- Temporarily disable docs generation on F34+

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.90-1
- Update to 2.90

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 17 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.86-1
- Update to 2.86

* Sun Feb  2 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.85-1
- Update to 2.85

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun  2 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.84-1
- Update to 2.84

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.77-17
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.77-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.77-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.77-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.77-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.77-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.77-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.77-10
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.77-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.77-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.77-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.77-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.77-5
- Install docs into %% _pkgdocdir (Fix FTBFS RHBZ#992357).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar  9 2013 Michel Salim <salimma@fedoraproject.org> - 2.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
- Fix mismatch between date and day-of-week of first changelog timestamp
- Also depend on texlive-collection-latexrecommended on F-19+

* Sat Nov 10 2012 Michel Salim <salimma@fedoraproject.org> - 2.77-2
- Build and package tutorial PDF

* Fri Nov  9 2012 Michel Salim <salimma@fedoraproject.org> - 2.77-1
- Update to 2.77

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Michel Salim <salimma@fedoraproject.org> - 2.76-1
- Update to 2.76

* Thu May  3 2012 Michel Salim <salimma@fedoraproject.org> - 2.75-1
- Update to 2.75

* Sat Mar  3 2012 Michel Salim <salimma@fedoraproject.org> - 2.73-1
- Update to 2.73

* Sat Feb  4 2012 Michel Salim <salimma@fedoraproject.org> - 2.72-1
- Update to 2.72

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Mar 12 2011 Michel Salim <salimma@fedoraproject.org> - 2.70-1
- Update to 2.70

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.69-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 23 2009 Michel Salim <salimma@fedoraproject.org> - 2.69-2
- Lower FORTIFY setting; level 2 does not work with gcc 4.4.2

* Fri Sep 18 2009 Michel Salim <salimma@fedoraproject.org> - 2.69-1
- Update to 2.69

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 11 2009 Michel Salim <salimma@fedoraproject.org> - 2.68-1
- Update to 2.68
- Enable checks

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun  6 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.67-1
- Update to 2.67

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.62-2
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.62-1
- Update to 2.62

* Sun Sep 23 2007 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.58-1
- Update to 2.58

* Sat Nov  4 2006 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.54-2
- Only package example files once, remove leftover Makefiles

* Thu Nov  2 2006 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.54-1
- Update to 2.54
- Use exclude macro instead of ghost

* Sun Mar 19 2006 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.53-3
- Moved examples to doc
- Removed redundant COPYING files from examples

* Sun Mar  5 2006 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.53-2
- Removed INSTALL from installed documentation
- Added description for devel package

* Sat Feb 18 2006 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.53-1
- Initial Fedora package

* Thu Mar 11 2004 Mike A. Harris <mharris@www.linux.org.uk> - 2.29-2
- Initial rpm spec file

