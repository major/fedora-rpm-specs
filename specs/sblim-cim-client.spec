# sblim-cim-client macros
%global archive_folder_name cim-client
%global cim_client_jar_file sblimCIMClient
%global slp_name sblim-slp-client
%global slp_client_jar_file sblimSLPClient

Summary:        Java CIM Client library
Name:           sblim-cim-client
Version:        1.3.9.3
Release:        36%{?dist}
License:        EPL-1.0
URL:            http://sourceforge.net/projects/sblim/
Source0:        http://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-%{version}-src.zip
Source1:        http://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-samples-%{version}-src.zip
Patch0:         sblim-cim-client-1.3.9.3-fix-for-java-11-openjdk.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  java-devel >= 1.4
BuildRequires:  jpackage-utils
BuildRequires:  xerces-j2 >= 2.7.1
BuildRequires:  ant >= 0:1.6
BuildRequires:  dos2unix

Requires:       java-headless >= 1.4
Requires:       jpackage-utils
Requires:       xerces-j2 >= 2.7.1
Requires:       tog-pegasus >= 2:2.5.1

%description
The purpose of this package is to provide a CIM Client Class Library for Java
applications. It complies to the DMTF standard CIM Operations over HTTP and
intends to be compatible with JCP JSR48 once it becomes available. To learn
more about DMTF visit http://www.dmtf.org.
More info about the Java Community Process and JSR48 can be found at
http://www.jcp.org and http://www.jcp.org/en/jsr/detail?id=48.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for sblim-cim-client.

%package manual
Summary:        Manual and sample code for %{name}
Requires:       sblim-cim-client = %{version}-%{release}

%description manual
Manual and sample code for sblim-cim-client.

%prep
%setup -q -n %{archive_folder_name}
rm version.txt
%setup -q -T -D -b 1 -n %{archive_folder_name}
%autopatch -p1

%build
export ANT_OPTS="-Xmx256m"
ant \
        -Dbuild.compiler=modern \
        -DManifest.version=%{version} \
        build-release

%install
# documentation
dos2unix COPYING README ChangeLog NEWS
# samples (also into _docdir)
pushd samples
  dos2unix README.samples
  pushd org/sblim/slp/example
    dos2unix *
  popd
  pushd org/sblim/wbem/cimclient/sample
    dos2unix *
  popd
popd
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -pm 644 samples/README.samples $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr  samples/org $RPM_BUILD_ROOT%{_datadir}/%{name}
# default cim.defaults
dos2unix cim.defaults slp.conf
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/java
install -pm 644 cim.defaults $RPM_BUILD_ROOT%{_sysconfdir}/java/%{name}.properties
install -pm 644 slp.conf $RPM_BUILD_ROOT%{_sysconfdir}/java/%{slp_name}.properties
# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 %{archive_folder_name}/%{cim_client_jar_file}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
(
  cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{name}.jar %{cim_client_jar_file}.jar;
)
install -pm 644 %{archive_folder_name}/%{slp_client_jar_file}.jar $RPM_BUILD_ROOT%{_javadir}/%{slp_name}.jar
(
  cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{slp_name}.jar %{slp_client_jar_file}.jar;
)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr %{archive_folder_name}/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc COPYING README ChangeLog NEWS
%config(noreplace) %{_sysconfdir}/java/%{name}.properties
%config(noreplace) %{_sysconfdir}/java/%{slp_name}.properties
%{_javadir}/%{name}.jar
%{_javadir}/%{cim_client_jar_file}.jar
%{_javadir}/%{slp_name}.jar
%{_javadir}/%{slp_client_jar_file}.jar

%files javadoc
%doc COPYING
%{_javadocdir}/%{name}

%files manual
%{_datadir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 01 2024 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.3.9.3-34
- Fix patch application
- Fix to build with java-21-openjdk
  Resolves: #2266687

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.3.9.3-33
- Rebuilt for java-21-openjdk as system jdk

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 25 2023 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.3.9.3-29
- SPDX migration

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.3.9.3-26
- Rebuilt for Drop i686 JDKs

* Tue Feb 08 2022 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.3.9.3-25
- Fix for java-17-openjdk as system jdk
  Resolves: #2051209

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.3.9.3-24
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.3.9.3-20
- Fix for java-11-openjdk as sytem JDK
  Resolves: #1858088

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.3.9.3-19
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.3.9.3-10
- Replace 'define' with 'global'

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.3.9.3-7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 31 2013 Mat Booth <fedora@matbooth.co.uk> - 1.3.9.3-6
- Update for newer guidelines
- Fix docdir conflicts rhbz #994071
- Actually package javadocs

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 02 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.3.9.3-1
- Update to sblim-cim-client-1.3.9.3

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.3.9.2-1
- Update to sblim-cim-client-1.3.9.2

* Mon Oct  5 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.3.9.1-1
- Initial support
