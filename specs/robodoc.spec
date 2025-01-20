#	Perl files are only documentation examples.

%global __perl_provides		%{nil}
%global __perl_requires		%{nil}


Name:		robodoc
Version:	4.99.44
Release:	11%{?dist}
Summary:	Extract documentation from source code
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
Source0:	http://rfsber.home.xs4all.nl/Robo/archives/%{name}-%{version}.tar.gz
Patch1:		robodoc-4.99.43-silentwarnings.patch
URL:		http://rfsber.home.xs4all.nl/Robo/
BuildRequires: make
BuildRequires:	gcc
BuildRequires:	perl-generators


%description
  ROBODoc is a documentation tool (based on the AutoDocs program written
a long time ago by Commodore). It extracts specially formatted comment
headers from the source file and puts them in a separate file. ROBODoc
thus allows you to include the program documentation in the source
code and avoid having to maintain two separate documents.

  ROBODoc can format the documentation in HTML, ASCII, AmigaGuide,
LaTeX, or RTF format. It is even possible to include parts of the
source code with function names that point their the documentation. It
also can create index tables for all your variables, classes,
functions, etc.

  The best feature of ROBODoc is that it works with many languages:
Assembler, C, Perl, LISP, Occam, Tcl/Tk, Pascal, Fortran, shell
scripts, and COBOL, basically any language that supports
comments/remarks.


#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------

%setup -q

%patch -P1 -p 1 -b .silentwarnings


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

%configure docdir="%{_docdir}/robodoc"
make CFLAGS="${RPM_OPT_FLAGS}" %{?_smp_mflags}

#	Changelog is ISO8859. Convert it to UTF-8.

iconv -f ISO8859-1 -t UTF-8 -o ChangeLog.utf8 ChangeLog
touch -r ChangeLog ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

make DESTDIR="${RPM_BUILD_ROOT}" INSTALL="install -p" install

#	Get rid of the installed documentation

rm -rf "${RPM_BUILD_ROOT}%{_docdir}/robodoc"

#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------

%doc AUTHORS Change* COPYING README Docs/manual.css Docs/manual.html
%doc Examples
%{_bindir}/*
%{_mandir}/man1/*


#-------------------------------------------------------------------------------
%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.44-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.99.44-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.44-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.44-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.44-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 4.99.44-1
- New upstream release (#1976669)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.43-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.43-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.43-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

#-------------------------------------------------------------------------------

* Wed Mar  7 2018 Patrick Monnerat <patrick@monnerat.net> 4.99.43-1
- New upstream release.
- Patch "silentwarnings" replaces patch "f21".

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.41-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.41-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.41-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.41-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.99.41-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.41-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Patrick Monnerat <pm@datasphere.ch> 4.99.41-7
- Patch "f21" to satisfy compilation requirements in Fedora 21.
- Rename configure.in to configure.ac to satisfy new autoconf requirement.
  https://bugzilla.redhat.com/show_bug.cgi?id=1107030

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 4.99.41-4
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Patrick Monnerat <pm@datasphere.ch> 4.99.41-1
- New upstream release.
- Patch "doubleman" to avoid double install of man pages.
  https://sourceforge.net/tracker/?func=detail&aid=3512312&group_id=7245&atid=307245

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  5 2010 Patrick Monnerat <pm@datasphere.ch> 4.99.38-1
- New upstream version.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec  2 2008 Patrick Monnerat <pm@datasphere.ch> 4.99.36-2
- Preserve ChangeLog timestamp.

* Wed Oct 22 2008 Patrick Monnerat <pm@datasphere.ch> 4.99.36-1
- New package.
