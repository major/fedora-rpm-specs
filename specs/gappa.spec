%global _docdir_fmt %{name}

Name:		gappa
Version:	1.4.2
Release:	4%{?dist}
Summary:	Prove programs with floating-point or fixed-point arithmetic

License:	GPL-3.0-only OR CECILL-2.1
URL:		https://gappa.gitlabpages.inria.fr/
VCS:		git:https://gitlab.inria.fr/gappa/gappa.git
Source:		%{url}/releases/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:	bison
BuildRequires:	boost-devel
BuildRequires:	flex
BuildRequires:	gcc-c++
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel
BuildRequires:	%{py3_dist sphinx}
BuildRequires:	remake

%description
Gappa is a tool intended to help verifying and formally prove
properties on numerical programs and circuits handling floating-point
or fixed-point arithmetic.  This tool manipulates logical formulas
stating the enclosures of expressions in some intervals.  Through the
use of rounding operators as part of the expressions, Gappa is specially
designed to deal with formulas that could appear when certifying numerical
codes. In particular, Gappa makes it simple to bound computational errors
due to floating-point arithmetic.  The tool and its documentation were
written by Guillaume Melquiond.

%package doc
Summary:	Documentation for gappa
BuildArch:	noarch
# In addition to the project license, the Javascript and CSS bundled with the
# documentation has the following licenses:
# - searchindex.js: BSD-2-Clause
# - _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# - _static/alabaster.css: BSD-3-Clause
# - _static/basic.css: BSD-2-Clause
# - _static/custom.css: BSD-3-Clause
# - _static/doctools.js: BSD-2-Clause
# - _static/documentation_options.js: BSD-2-Clause
# - _static/file.png: BSD-2-Clause
# - _static/jquery*.js: MIT
# - _static/language_data.js: BSD-2-Clause
# - _static/minus.png: BSD-2-Clause
# - _static/plus.png: BSD-2-Clause
# - _static/searchtools.js: BSD-2-Clause
# - _static/underscore*.js: MIT
License:	(GPL-3.0-only OR CECILL-2.1) AND MIT AND BSD-2-Clause AND BSD-3-Clause

%description doc
Documentation for gappa.

%prep
%autosetup

%conf
# Increase the test timeout for ARM
sed -i 's/timeout 5/&0/' Remakefile.in

%build
%configure
# Use the system remake
rm -f remake
ln -s %{_bindir}/remake remake
remake -d %{?_smp_mflags}
remake -d doc/html/index.html
rm doc/html/.buildinfo

%install
DESTDIR=%{buildroot} remake install

%check
remake check

%files
%{_bindir}/gappa
%doc README.md NEWS.md
%license COPYING COPYING.GPL

%files doc
%doc AUTHORS doc/html

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Jerry James <loganjerry@gmail.com> - 1.4.2-1
- Version 1.4.2
- New URLs

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- Version 1.4.1
- Use SPDX license names
- Add a doc subpackage

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 19 2021 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- Version 1.4.0
- Drop upstreamed -gcc11 patch

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Jeff Law <law@redhat.com> - 1.3.5-7
- Make comparison object invocable as const

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Petr Viktorin <pviktori@redhat.com> - 1.3.5-5
- Remove BuildRequires on python2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 1.3.5-3
- Rebuild for mpfr 4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 1.3.5-1
- New upstream version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 1.3.3-1
- New upstream version
- Drop upstreamed -vec patch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul  6 2018 Jerry James <loganjerry@gmail.com> - 1.3.2-2
- Fix out of bounds vector accesses

* Mon Feb 12 2018 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-3
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- New upstream version

* Fri Jul 22 2016 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- New upstream version

* Fri Jun 24 2016 Jerry James <loganjerry@gmail.com> - 1.2.2-1
- New upstream version

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- New upstream version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-6
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.2.0-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Jerry James <loganjerry@gmail.com> - 1.2.0-1
- New upstream version

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.1.2-2
- Rebuild for boost 1.57.0

* Tue Oct 21 2014 Jerry James <loganjerry@gmail.com> - 1.1.2-1
- New upstream version
- Fix license handling

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.1.1-2
- Rebuild for boost 1.55.0

* Mon Mar 31 2014 Jerry James <loganjerry@gmail.com> - 1.1.1-1
- New upstream version

* Mon Jan 27 2014 Jerry James <loganjerry@gmail.com> - 1.1.0-1
- New upstream version
- Drop upstreamed patch and NEWS typo workaround

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.0.0-2
- Rebuild for boost 1.54.0

* Mon Jul 29 2013 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- New upstream version
- Drop version-specific short test; we rely on the upstream test suite

* Wed Jul  3 2013 Jerry James <loganjerry@gmail.com> - 0.18.0-1
- New upstream version

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 0.17.1-1
- New upstream version

* Mon Feb 25 2013 Jerry James <loganjerry@gmail.com> - 0.16.6-1
- New upstream version

* Tue Feb 19 2013 Jerry James <loganjerry@gmail.com> - 0.16.5-1
- New upstream version
- Trim BRs now that tex(latex) Requires more packages

* Thu Feb 14 2013 Jerry James <loganjerry@gmail.com> - 0.16.3-2
- Add -dblatex patch to fix FTBFS

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 0.16.3-1
- New upstream version

* Wed Dec 26 2012 Jerry James <loganjerry@gmail.com> - 0.16.2-1
- New upstream version
- New BRs due to TeXLive 2012

* Mon Aug  6 2012 Jerry James <loganjerry@gmail.com> - 0.16.1-2
- Rebuild for boost 1.50

* Sat Jul 28 2012 Jerry James <loganjerry@gmail.com> - 0.16.1-1
- New upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 0.16.0-1
- New upstream version

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 0.15.1-2
- Rebuild for GCC 4.7

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15.1-1.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 0.15.1-1.1
- rebuild with new gmp

* Mon Sep 19 2011 Jerry James <loganjerry@gmail.com> - 0.15.1-1
- New upstream version

* Mon Jun  6 2011 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- New upstream version
- Drop defattr

* Tue Apr 19 2011 Jerry James <loganjerry@gmail.com> - 0.14.1-1
- New upstream version
- Drop %%clean section
- Drop upstreamed patches
- Build the PDF file instead of downloading it

* Tue Mar 15 2011 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- New upstream version
- Remove BuildRoot tag
- Use flex and bison to regenerate the lexer and parser

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.13.0-5
- Rebuilt for gcc bug 634757

* Tue Sep 21 2010 David A. Wheeler <dwheeler@dwheeler.com> - 0.13.0-4
- Removed now-incorrect comment.

* Sat Sep 11 2010 David A. Wheeler <dwheeler@dwheeler.com> - 0.13.0-3
- Removed documentation source code from package
- Greatly simplified spec file.

* Fri Sep 10 2010 David A. Wheeler <dwheeler@dwheeler.com> - 0.13.0-2
- Respond to comments 1-2 in https://bugzilla.redhat.com/show_bug.cgi?id=622173
- Simplify (drop variable definitions in configure, drop INSTALL file)
- Preserve the timestamp of file COPYING
- More macro use
- Modified to use bundled testsuite as well
- PDF manual added

* Sat Aug  7 2010 David A. Wheeler <dwheeler@dwheeler.com> - 0.13.0-1
- Initial packaging
