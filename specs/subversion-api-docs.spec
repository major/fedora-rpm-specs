Name:           subversion-api-docs
Version:        1.14.5
Release:        1%{?dist}
Summary:        Subversion API documentation

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://subversion.tigris.org/
Source0:        http://svn.collab.net/repos/svn/tags/%{version}/doc/doxygen.conf
Source1:        http://svn.collab.net/repos/svn/tags/%{version}/COPYING
BuildRequires:  subversion-devel = %{version}, doxygen
BuildArch:      noarch

%description
Subversion is a concurrent version control system which enables one or more
users to collaborate in developing and maintaining a hierarchy of files and
directories while keeping a history of all changes. This package provides
Subversion API documentation for developers.

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
cd %{name}-%{version}
cp %{SOURCE0} doxygen.conf

%build
cd %{name}-%{version}
sed -e 'N;N;s,^\(INPUT *= *\).*$,\1%{_includedir}/subversion-1\n,' \
doxygen.conf | 
sed -e 's,^\(OUTPUT_DIRECTORY *= *\).*$,\1docs,' \
    -e 's,^\(GENERATE_TAGFILE *= *\).*$,\1docs/svn.tag,' | \
doxygen -

%install
cd %{name}-%{version}
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/subversion/api-docs/search
install -m 644 docs/svn.tag $RPM_BUILD_ROOT%{_docdir}/subversion/api-docs
install -m 644 docs/html/search/* $RPM_BUILD_ROOT%{_docdir}/subversion/api-docs/search
install -m 644 `find docs/html -type f -maxdepth 1` $RPM_BUILD_ROOT%{_docdir}/subversion/api-docs
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/subversion/api-docs

%files
%doc %dir %{_docdir}/subversion
%doc %dir %{_docdir}/subversion/api-docs
%doc %{_docdir}/subversion/api-docs/*

%changelog
* Wed Jan 22 2025 Bojan Smojver <bojan@rexursive.com> 1.14.5-1
- bump up to 1.14.5

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 1.14.3-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Bojan Smojver <bojan@rexursive.com> 1.14.3-1
- bump up to 1.14.3

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug  2 2022 Bojan Smojver <bojan@rexursive.com> 1.14.2-1
- bump up to 1.14.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 30 2021 Bojan Smojver <bojan@rexursive.com> 1.14.1-1
- bump up to 1.14.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Bojan Smojver <bojan@rexursive.com> 1.14.0-1
- bump up to 1.14.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug  2 2019 Bojan Smojver <bojan@rexursive.com> 1.12.2-1
- bump up to 1.12.2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Bojan Smojver <bojan@rexursive.com> 1.12.0-1
- bump up to 1.12.0

* Thu Feb 14 2019 Bojan Smojver <bojan@rexursive.com> 1.11.1-1
- bump up to 1.11.1

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov  7 2018 Bojan Smojver <bojan@rexursive.com> 1.11.0-1
- bump up to 1.11.0

* Sat Jul 21 2018 Bojan Smojver <bojan@rexursive.com> 1.10.2-1
- bump up to 1.10.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Bojan Smojver <bojan@rexursive.com> 1.9.7-1
- bump up to 1.9.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug  1 2017 Bojan Smojver <bojan@rexursive.com> 1.9.6-1
- bump up to 1.9.6

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Bojan Smojver <bojan@rexursive.com> 1.9.5-1
- bump up to 1.9.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb  9 2016 Bojan Smojver <bojan@rexursive.com> 1.9.3-1
- bump up to 1.9.3

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul  6 2015 Bojan Smojver <bojan@rexursive.com> 1.8.13-1
- bump up to 1.8.13

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 29 2014 Bojan Smojver <bojan@rexursive.com> 1.8.10-1
- bump up to 1.8.10

* Mon Jun  9 2014 Bojan Smojver <bojan@rexursive.com> 1.8.9-1
- bump up to 1.8.9

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Bojan Smojver <bojan@rexursive.com> 1.8.8-1
- bump up to 1.8.8

* Wed Dec 11 2013 Bojan Smojver <bojan@rexursive.com> 1.8.5-1
- bump up to 1.8.5

* Mon Sep  9 2013 Bojan Smojver <bojan@rexursive.com> 1.8.3-1
- bump up to 1.8.3

* Thu Aug  8 2013 Bojan Smojver <bojan@rexursive.com> 1.8.1-1
- bump up to 1.8.1
- switch to unversioned documentation directory

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Bojan Smojver <bojan@rexursive.com> 1.8.0-1
- bump up to 1.8.0

* Thu Jun  6 2013 Bojan Smojver <bojan@rexursive.com> 1.7.10-1
- bump up to 1.7.10

* Mon Jun  3 2013 Bojan Smojver <bojan@rexursive.com> 1.7.9-1
- bump up to 1.7.9

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 24 2013 Bojan Smojver <bojan@rexursive.com> 1.7.8-1
- bump up to 1.7.8

* Thu Oct 25 2012 Bojan Smojver <bojan@rexursive.com> 1.7.7-1
- bump up to 1.7.7

* Mon Aug 20 2012 Bojan Smojver <bojan@rexursive.com> 1.7.6-1
- bump up to 1.7.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Bojan Smojver <bojan@rexursive.com> 1.7.5-1
- bump up to 1.7.5

* Fri Mar 23 2012 Bojan Smojver <bojan@rexursive.com> 1.7.4-1
- bump up to 1.7.4

* Tue Feb 14 2012 Bojan Smojver <bojan@rexursive.com> 1.7.3-1
- bump up to 1.7.3

* Fri Feb 10 2012 Bojan Smojver <bojan@rexursive.com> 1.7.2-1
- bump up to 1.7.2

* Sun Jan 15 2012 Bojan Smojver <bojan@rexursive.com> 1.7.1-1
- bump up to 1.7.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Bojan Smojver <bojan@rexursive.com> 1.6.17-1
- bump up to 1.6.17

* Mon Mar  7 2011 Bojan Smojver <bojan@rexursive.com> 1.6.16-1
- bump up to 1.6.16

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Bojan Smojver <bojan@rexursive.com> 1.6.15-1
- bump up to 1.6.15

* Thu Oct  7 2010 Bojan Smojver <bojan@rexursive.com> 1.6.13-1
- bump up to 1.6.13

* Mon Jul 19 2010 Bojan Smojver <bojan@rexursive.com> 1.6.12-1
- bump up to 1.6.12

* Mon May 10 2010 Bojan Smojver <bojan@rexursive.com> 1.6.11-1
- bump up to 1.6.11

* Mon Feb 15 2010 Bojan Smojver <bojan@rexursive.com> 1.6.9-1
- bump up to 1.6.9

* Thu Nov 19 2009 Bojan Smojver <bojan@rexursive.com> 1.6.6-1
- bump up to 1.6.6

* Thu Sep  3 2009 Bojan Smojver <bojan@rexursive.com> 1.6.5-3
- fix search

* Sat Aug 29 2009 Bojan Smojver <bojan@rexursive.com> 1.6.5-2
- attempt to fix docs install

* Sat Aug 29 2009 Bojan Smojver <bojan@rexursive.com> 1.6.5-1
- bump up to 1.6.5

* Tue Aug 11 2009 Bojan Smojver <bojan@rexursive.com> 1.6.4-1
- bump up to 1.6.4

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Bojan Smojver <bojan@rexursive.com> 1.6.3-1
- bump up to 1.6.3

* Fri May 29 2009 Bojan Smojver <bojan@rexursive.com> 1.6.2-1
- bump up to 1.6.2

* Thu Apr 16 2009 Bojan Smojver <bojan@rexursive.com> 1.6.1-1
- bump up to 1.6.1

* Sat Apr  4 2009 Bojan Smojver <bojan@rexursive.com> 1.6.0-1
- bump up to 1.6.0

* Sun Mar 22 2009 Bojan Smojver <bojan@rexursive.com> 1.5.6-1
- bump up to 1.5.6

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb  3 2009 Bojan Smojver <bojan@rexursive.com> 1.5.5-1
- bump up to 1.5.5

* Mon Nov  3 2008 Bojan Smojver <bojan@rexursive.com> 1.5.4-1
- bump up to 1.5.4

* Fri Oct 24 2008 Bojan Smojver <bojan@rexursive.com> 1.5.3-1
- bump up to 1.5.3

* Tue Aug  5 2008 Bojan Smojver <bojan@rexursive.com> 1.5.1-1
- bump up to 1.5.1

* Tue Jul  8 2008 Bojan Smojver <bojan@rexursive.com> 1.5.0-1
- bump up to 1.5.0

* Thu Feb 14 2008 Bojan Smojver <bojan@rexursive.com> 1.4.6-1
- bump up to 1.4.6

* Fri Aug 24 2007 Bojan Smojver <bojan@rexursive.com> 1.4.4-2
- bump up to 1.4.4

* Sat Mar 31 2007 Bojan Smojver <bojan@rexursive.com> 1.4.3-1
- bump up to 1.4.3

* Wed Nov 01 2006 Bojan Smojver <bojan@rexursive.com> 1.4.2-2
- re-tag for rebuild

* Wed Nov 01 2006 Bojan Smojver <bojan@rexursive.com> 1.4.2-1
- bump up to 1.4.2

* Sat Sep 16 2006 Bojan Smojver <bojan@rexursive.com> 1.3.2-2.1
- mass rebuild

* Tue Jul 25 2006 Bojan Smojver <bojan@rexursive.com> 1.3.2-2
- remove subversion-devel dependency (hopefully make mock happy)

* Sat Jun 10 2006 Bojan Smojver <bojan@rexursive.com> 1.3.2-1
- bump up to 1.3.2

* Sun Apr 09 2006 Bojan Smojver <bojan@rexursive.com> 1.3.1-1
- bump up to 1.3.1

* Wed Jan 11 2006 Bojan Smojver <bojan@rexursive.com> 1.3.0-1
- initial package
