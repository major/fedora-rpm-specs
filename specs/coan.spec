Name:		coan
Version:	6.0.1
Release:	36%{?dist}
Summary:	A command line tool for simplifying the pre-processor conditionals in source code
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://coan2.sourceforge.net/
Source0:	http://downloads.sourceforge.net/coan2/%{name}-%{version}.tar.gz
# https://sourceforge.net/p/coan2/bugs/92/
Patch0:         expression_parser.patch
# https://sourceforge.net/p/coan2/bugs/95/
Patch1:         coan-autoconf-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  perl-Pod-Html
BuildRequires:  autoconf automake

# removed python2 dependencies and asked upstream to port tests to python3
# https://sourceforge.net/p/coan2/bugs/93/

# Regression on other arches with F26 mass rebuild (big endian systems)
# Temporarily exclude them
# https://bugzilla.redhat.com/show_bug.cgi?id=1423293
# checking for big-endian host... yes
# RPM build errors:
# configure: error: Sorry. Coan is buggy on big-endian systems
ExcludeArch:	ppc64 s390x


%description
%{name} (formerly sunifdef) is a software engineering tool for analyzing
pre-processor-based configurations of C or C++ source code. Its principal use
is to simplify a body of source code by eliminating any parts that are
redundant with respect to a specified configuration.

%{name} is most useful to developers of constantly evolving products
with large code bases, where pre-processor conditionals are used to
configure the feature sets, APIs or implementations of different
releases. In these environments the code base steadily
accumulates #ifdef-pollution as transient configuration options become
obsolete. %{name} can largely automate the recurrent task of purging
redundant #if-logic from the code.

%prep
%autosetup -p0

for i in AUTHORS LICENSE.BSD README ChangeLog ; do
    sed -i -e 's/\r$//' $i
done

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
autoreconf -vi
%configure
%make_build

# disabling all checks it's broken again on rawhide :(
# some tests are broken in armv7hl and ppc64le - disable until upstream
# fixes the issue upstream bug report:
#     https://sourceforge.net/p/coan2/bugs/83/
# so for now we'll just allow the tests to fail
#
# %ifnarch %{arm} ppc64le
# make check || (for f in test_coan/*.log ; do cat ${f} ; done ; false)
# %else
# make check || (for f in test_coan/*.log ; do cat ${f} ; done ; true)
# %endif


%install
%make_install

%files
%doc AUTHORS README ChangeLog
%license LICENSE.BSD
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 6.0.1-35
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Peter Fordham <peter.fordham@gmail.com> - 6.0.1-29
- Fix c99 complaince isses in configure.ac and add autoreconf to build.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Filipe Rosset <rosset.filipe@gmail.com> - 6.0.1-25
- Remove python2 dependencies (required only for tests) fix rhbz#1805173

* Thu Jan 28 2021 Filipe Rosset <rosset.filipe@gmail.com> - 6.0.1-24
- Fix FTBFS

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 6.0.1-23
- Force C++14 as the code is not ready for C++17

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Filipe Rosset <rosset.filipe@gmail.com> - 6.0.1-20
- Disable (again) all tests to fix FTBFS F31+

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 6.0.1-17
- Add patch to fix crash on Fedora 28 and later (BZ 1626440)
- Fix missing python on Fedora >=29
- Re-enable test failures on x86_64 and i686 only

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 6.0.1-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 17 2017 Filipe Rosset <rosset.filipe@gmail.com> - 6.0.1-11
- ExcludeArch ppc64 and s390x due FTBFS, fixes rhbz #1423293

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 25 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 6.0.1-8
- Re-enable tests

* Thu Feb 25 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 6.0.1-7
- Add BuildRequires:  gcc-c++
- BuildRequire perl-Pod-Html for Fedora 24 and later (for pod2html)

* Thu Feb 25 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 6.0.1-6
- Add BuildRequires: perl-podlators to fix FTBFS (BZ 1307386)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 08 2015 Filipe Rosset <rosset.filipe@gmail.com> - 6.0.1-3
- Disable tests until upstream fixes armv7hl

* Fri May 08 2015 Filipe Rosset <rosset.filipe@gmail.com> - 6.0.1-2
- Fixes a broken build plus spec cleanup, added python as BR to run tests

* Thu May 07 2015 Filipe Rosset <rosset.filipe@gmail.com> - 6.0.1-1
- Rebuilt for new upstream version 6.0.1, fixes rhbz #1135805

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.2-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Filipe Rosset <rosset.filipe@gmail.com> - 5.2-1
- Rebuilt for new upstream version, fixes rhbz #925162, #992071 and #902927

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 5.1.2-1
- Update to version 5.1.2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-2
- Rebuilt for c++ ABI breakage

* Wed Feb  8 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 5.1-1
- Update to version 5.1

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 12 2010 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 4.1-2
- Use wild card for manpage extension to allow future compression changes
- Replace occurences of Sunifdef in package description with %%{name}
- Use INSTALL="install -p" to preserve file time stamps
- Beautify top of spec file
- No longer need to remove executable bit on source files
- Fix up spelling mistakes

* Sat Jun 12 2010 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 4.1-1
- Rename package to coan (from sunifdef)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Mar  9 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 3.1.3-2
- Fix Source0 URL

* Wed Feb  6 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 3.1.3-1
- Update to version 3.1.3

* Sun Nov 25 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 3.1.2-1
- Update to version 3.1.2
- Fix typo in changelog
- Fix line endings in AUTHORS LICENSE.BSD README ChangeLog

* Fri Aug 31 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 3.1-4
- Fix source URL
- Fix email addresses in changelog entries

* Tue Aug 28 2007 Stepan Kasal <skasal@redhat.com> - 3.1-3
- Fix typos, do not try to use '\#' to avoid interpretation of #
  as a comment; it seems the only way is to take care that it does
  not appear at the beginning of a line.

* Tue Aug 21 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 3.1-2
- Bump release and rebuild

* Mon May 21 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 3.1-1
- Update to version 3.1 (bug fix release)

* Wed Jan 24 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 3.0-1
- Update to version 3.0

* Tue Jul 25 2006 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.1.2-1
- Update to version 2.1.2

* Tue Jul 11 2006 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.1.1-1
- Update to version 2.1.1

* Mon Jun  5 2006 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.0.1-4
- Update to version 1.0.1
- No need to remove build-bin and autom4te.cache with this release

* Sat Jun  3 2006 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.0-3
- Move make check to a check section

* Fri Jun  2 2006 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.0-2
- Clean up permissions on source files
- Remove prebuilt binary directory and automa4te.cache that are included in
  tarball 
- Add make check to build
- Wrap description at 70 columns rather than 80

* Mon May 29 2006 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.0-1
- Initial package

