Name:           tomcat-native
Epoch:          1
Version:        1.3.0
Release:        %autorelease
Summary:        Tomcat native library

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://tomcat.apache.org/tomcat-9.0-doc/apr.html
Source0:        http://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/%{name}-%{version}-src.tar.gz
ExclusiveArch: %{java_arches}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  apr-devel >= 1.6.3
BuildRequires:  openssl-devel >= 1.1.1
# Upstream compatibility:
Provides:       tcnative = %{version}-%{release}

%description
Tomcat can use the Apache Portable Runtime to provide superior
scalability, performance, and better integration with native server
technologies.  The Apache Portable Runtime is a highly portable library
that is at the heart of Apache HTTP Server 2.x.  APR has many uses,
including access to advanced IO functionality (such as sendfile, epoll
and OpenSSL), OS level functionality (random number generation, system
status, etc), and native process handling (shared memory, NT pipes and
Unix sockets).  This package contains the Tomcat native library which
provides support for using APR in Tomcat.


%prep
%setup -q -n %{name}-%{version}-src
f=CHANGELOG.txt ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f


%build
cd native
export CFLAGS="${CFLAGS} -DOPENSSL_NO_ENGINE"
%configure \
    --with-apr=%{_bindir}/apr-1-config \
    --with-java-home=%{_jvmdir}/java
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make -C native install DESTDIR=$RPM_BUILD_ROOT
# Perhaps a devel package sometime?  Not for now; no headers are installed.
rm -f $RPM_BUILD_ROOT%{_libdir}/libtcnative*.*a
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig
rm -rf ${RPM_BUILD_ROOT}%{_includedir}/*.h


%ldconfig_scriptlets


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE NOTICE
%doc CHANGELOG.txt README.txt
# Note: unversioned *.so needed here due to how Tomcat loads the lib :(
%{_libdir}/libtcnative*.so*


%changelog
* Thu Jan 30 2025 Dimitris Soumis <dsoumis@redhat.com> - 1:1.3.0-9
- Resolves: rhbz#2341450 - Fix non-existing java-home

* Tue Jul 30 2024 Dimitris Soumis <dsoumis@redhat.com> - 1:1.3.0-3
- Resolves: rhbz#2301332

* Tue Jul 30 2024 Coty Sutherland <csutherl@redhat.com> - 1:1.3.0-3
- Add buildrequires for openssl-devel-engine

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1:1.3.0-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Dimitris Soumis <dsoumis@redhat.com> - 1:1.3.0-1
- Update to 1.3.0

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1:1.2.36-4
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Hui Wang <huwang@redhat.com> - 1:1.2.36-1
- Downgrade to 1.2.36 (#2124703)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Hui Wang <huwang@redhat.com> - 2.0.2-1
- Update to 2.0.2 (#2141021)

* Thu Aug 25 2022 Hui Wang <huwang@redhat.com> - 2.0.1-1
- Update to 2.0.1 (#1829298)

* Fri Aug 19 2022 Coty Sutherland <csutherl@redhat.com> - 1.2.35-1
- Update to 1.2.35 (#2119331)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.2.23-8
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.2.23-6
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.2.23-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat Feb 01 2020 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.23-1
- Update to 1.2.23 (#1590816)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Coty Sutherland <csutherl@redhat.com> - 1.2.21-1
- Update to 1.2.21 (#1671548)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.17-1
- Update to 1.2.17 (#1590816)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.16-1
- Update to 1.2.16, fixes CVE-2017-15698 (#1540826)

* Tue Nov 07 2017 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.14-1
- Update to 1.2.14 (#1488142)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 1.2.12-1
- Update to 1.2.12 (#1425783)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Coty Sutherland <csutherl@redhat.com> - 1.2.10-1
- Update to 1.2.10

* Tue Aug 16 2016 Coty Sutherland <csutherl@redhat.com> - 1.2.8-1
- Update to 1.2.8

* Tue May 10 2016 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.7-1
- Update to 1.2.7

* Thu Apr 28 2016 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.6-1
- Update to 1.2.6

* Tue Mar 08 2016 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.5-2
- Update to 1.2.5 (#1315533)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.4-1
- Update to 1.2.4

* Sun Dec 27 2015 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.1.34-1
- Update to 1.1.34

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.1.33-1
- Update to 1.1.33

* Mon Oct 27 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.1.32-1
- Update to 1.1.32
- Mark LICENSE and NOTICE as %%license where available

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  8 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.1.31-1
- Update to 1.1.31

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.1.30-1
- Update to 1.1.30

* Tue Oct 15 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.1.29-1
- Update to 1.1.29.

* Mon Sep 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.1.28-1
- Update to 1.1.28.
- Make buildable on EL5 again; min supported APR version lowered back to 1.2.1.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.1.27-1
- Update to 1.1.27.
- Clean up specfile constructs no longer needed in Fedora or EL6+.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.1.24-1
- Update to 1.1.24.

* Wed Mar  7 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.1.23-1
- Update to 1.1.23.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug  9 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.1.22-1
- Update to 1.1.22.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 17 2010 Ville Skyttä <ville.skytta@iki.fi> - 1.1.20-1
- Update to 1.1.20 (#566131).

* Mon Jan 11 2010 Ville Skyttä <ville.skytta@iki.fi> - 1.1.19-1
- Update to 1.1.19 (#554315), OpenSSL 1.0 patch applied upstream.

* Tue Nov 24 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.1.18-1
- Update to 1.1.18 (security; CVE-2009-3555).

* Wed Nov  4 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.1.17-1
- Update to 1.1.17 (#532931).

* Wed Aug 26 2009 Tomas Mraz <tmraz@redhat.com> - 1.1.16-5
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 1.1.16-2
- rebuild with new openssl

* Thu Nov 20 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.1.16-1
- 1.1.16.

* Thu Sep 11 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.1.15-1
- 1.1.15.

* Sat Jul  5 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.1.14-1
- 1.1.14.

* Sat Feb 16 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.1.13-1
- 1.1.13.

* Tue Feb 12 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.1.12-2
- Apply upstream fix to silence (seemingly harmless?) configure error spewage.

* Sat Dec 22 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.1.12-1
- 1.1.12.

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.1.10-3
- Rebuild for deps

* Wed Dec  5 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.1.10-2
- Rebuild.

* Thu Sep  6 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.1.10-1
- First Fedora build.

* Mon Aug 20 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.1.10-0.2
- License: ASL 2.0.

* Mon Apr 16 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.1.10-0.1
- 1.1.10.

* Tue Apr  3 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.1.9-0.1
- 1.1.9.

* Sat Jan  6 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.1.8-0.1
- 1.1.8.

* Tue Dec 12 2006 Ville Skyttä <ville.skytta@iki.fi> - 1.1.7-0.1
- 1.1.7.

* Mon Nov 13 2006 Ville Skyttä <ville.skytta@iki.fi> - 1.1.6-0.1
- 1.1.6.

* Sat Sep 30 2006 Ville Skyttä <ville.skytta@iki.fi> - 1.1.4-0.1
- 1.1.4, specfile cleanup.

* Wed Jun 14 2006 Ville Skyttä <ville.skytta@iki.fi> - 1.1.3-0.1
- First build.
