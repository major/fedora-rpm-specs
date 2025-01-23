Name:           apr-api-docs
Version:        1.7.5
Release:        1%{?dist}
Summary:        Apache Portable Runtime API documentation

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://apr.apache.org/
Source0:        http://svn.apache.org/repos/asf/apr/apr/tags/%{version}/docs/doxygen.conf
Source1:        http://svn.apache.org/repos/asf/apr/apr/tags/%{version}/LICENSE.APR
Source2:        http://svn.apache.org/repos/asf/apr/apr-util/tags/%{version}/LICENSE.APU
Patch0:         apr-api-docs-doxygen.patch
BuildRequires:  apr-devel = %{version}, apr-util-devel, doxygen
BuildArch:      noarch

%description
The mission of the Apache Portable Runtime (APR) is to provide a free library
of C data structures and routines, forming a system portability layer to as
many operating systems as possible, including Unices, MS Win32, BeOS and OS/2.
This package provides APR and APR-util API documentation for developers.

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
cd %{name}-%{version}
cp %{SOURCE0} doxygen.conf
%patch -P 0 -p0 -b .doxygen-apu

%build
cd %{name}-%{version}
sed -e 's,\(INPUT *= *\).*$,\1%{_includedir}/apr-1,' \
    -e 's,\(OUTPUT_DIRECTORY *= *\).*$,\1docs,' \
    -e 's,\(GENERATE_TAGFILE *= *\).*$,\1docs/apr.tag,' \
doxygen.conf | doxygen -
sed -i -e 's,^\[<a class="el" href="group___a_p_r.html">Apache Portability Runtime library</a>\],&'\
'<br><strong><font color="red">'\
'WARNING: The actual values of macros and typedefs<br>'\
'are platform specific and should NOT be relied upon!'\
'</font></strong>,' docs/html/group__apr__platform.html

%install
cd %{name}-%{version}
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/apr/api-docs/search
install -m 644 docs/apr.tag $RPM_BUILD_ROOT%{_docdir}/apr/api-docs
install -m 644 docs/html/search/* $RPM_BUILD_ROOT%{_docdir}/apr/api-docs/search
install -m 644 `find docs/html -type f -maxdepth 1` $RPM_BUILD_ROOT%{_docdir}/apr/api-docs
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/apr/api-docs
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/apr/api-docs

%files
%doc %dir %{_docdir}/apr
%doc %dir %{_docdir}/apr/api-docs
%doc %{_docdir}/apr/api-docs/*

%changelog
* Wed Jan 22 2025 Bojan Smojver <bojan@rexursive.com> 1.7.5-1
- bump up to 1.7.5

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.3-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Bojan Smojver <bojan@rexursive.com> 1.7.3-1
- bump up to 1.7.3

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Bojan Smojver <bojan@rexursive.com> 1.7.0-1
- bump up to 1.7.0

* Tue Feb 12 2019 Bojan Smojver <bojan@rexursive.com> 1.6.5-1
- bump up to 1.6.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Bojan Smojver <bojan@rexursive.com> 1.6.3-1
- bump up to 1.6.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul  6 2015 Bojan Smojver <bojan@rexursive.com> 1.5.2-1
- bump up to 1.5.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  9 2014 Bojan Smojver <bojan@rexursive.com> 1.5.1-1
- bump up to 1.5.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan  1 2014 Bojan Smojver <bojan@rexursive.com> 1.5.0-1
- bump up to 1.5.0

* Thu Aug  8 2013 Bojan Smojver <bojan@rexursive.com> 1.4.8-1
- bump up to 1.4.8
- switch to unversioned documentation directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar  4 2012 Bojan Smojver <bojan@rexursive.com> 1.4.6-1
- Bump up to 1.4.6

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat May 21 2011 Bojan Smojver <bojan@rexursive.com> 1.4.5-1
- Bump up to 1.4.5

* Thu May 12 2011 Bojan Smojver <bojan@rexursive.com> 1.4.4-2
- force APR_HAS_LDAP

* Thu May 12 2011 Bojan Smojver <bojan@rexursive.com> 1.4.4-1
- Bump up to 1.4.4

* Tue Feb  8 2011 Bojan Smojver <bojan@rexursive.com> 1.4.2-1
- Bump up to 1.4.2

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 28 2009 Bojan Smojver <bojan@rexursive.com> 1.3.9-1
- Bump up to 1.3.9

* Thu Sep  3 2009 Bojan Smojver <bojan@rexursive.com> 1.3.8-1
- Bump up to 1.3.8
- Add search

* Tue Jul 28 2009 Bojan Smojver <bojan@rexursive.com> 1.3.7-1
- Bump up to 1.3.7

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Bojan Smojver <bojan@rexursive.com> 1.3.6-1
- Bump up to 1.3.6

* Tue Jun 16 2009 Bojan Smojver <bojan@rexursive.com> 1.3.5-2
- Bump up to 1.3.5

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep  5 2008 Bojan Smojver <bojan@rexursive.com> 1.3.3-1
- Bump up to 1.3.3

* Fri Jul 04 2008 Bojan Smojver <bojan@rexursive.com> 1.3.2-2
- %%{_arch} is set to noarch, cannot use that, include all headers

* Wed Jul 02 2008 Bojan Smojver <bojan@rexursive.com> 1.3.2-1
- Bump up to 1.3.2

* Wed Jun 11 2008 Bojan Smojver <bojan@rexursive.com> 1.3.0-1
- Align with latest apr/apr-util

* Wed Nov 28 2007 Bojan Smojver <bojan@rexursive.com> 1.2.12-1
- Align with latest apr/apr-util

* Tue Sep 11 2007 Bojan Smojver <bojan@rexursive.com> 1.2.11-1
- Align with latest apr/apr-util

* Wed Aug 22 2007 Bojan Smojver <bojan@rexursive.com> 1.2.9-3
- Fix license

* Mon Aug 20 2007 Bojan Smojver <bojan@rexursive.com> 1.2.9-2
- add APU macros to PREDEFINED list

* Fri Jul 20 2007 Bojan Smojver <bojan@rexursive.com> 1.2.9-1
- bump up to 1.2.9

* Thu Jul 19 2007 Bojan Smojver <bojan@rexursive.com> 1.2.8-4
- introduce warning about platform specific macros and typedefs
- pick up APU docs too

* Tue Jun 26 2007 Bojan Smojver <bojan@rexursive.com> 1.2.8-3
- make the package noarch, as suggested by Joe Orton
- pick the docs for the arch we're built on

* Fri Jun 22 2007 Bojan Smojver <bojan@rexursive.com> 1.2.8-2
- fixes for issues noted in package review

* Fri Jun  8 2007 Bojan Smojver <bojan@rexursive.com> 1.2.8-1
- initial package
