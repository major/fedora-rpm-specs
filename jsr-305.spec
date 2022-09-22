%bcond_with bootstrap

Name:           jsr-305
Version:        3.0.2
Release:        6%{?dist}
Summary:        Correctness annotations for Java code

# The majority of code is BSD-licensed, but some Java sources
# are licensed under CC-BY license, see: $ grep -r Creative .
License:        BSD and CC-BY
URL:            https://code.google.com/p/jsr-305
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
# File containing URL to CC-BY license text
Source1:        NOTICE-CC-BY.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap-openjdk8
%else
BuildRequires:  maven-local-openjdk8
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif

%description
This package contains reference implementations, test cases, and other
documents for Java Specification Request 305: Annotations for Software Defect
Detection.

%{?javadoc_package}

%prep
%setup -q
cp %{SOURCE1} NOTICE-CC-BY

%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/*" 1.6

sed -i 's|<groupId>com\.google\.code\.findbugs</groupId>|<groupId>org.jsr-305</groupId>|' ri/pom.xml
sed -i 's|<artifactId>jsr305</artifactId>|<artifactId>ri</artifactId>|' ri/pom.xml

%mvn_file :ri %{name}
%mvn_alias :ri com.google.code.findbugs:jsr305
%mvn_package ":{proposedAnnotations,tcl}" __noinstall

# do not build sampleUses module - it causes Javadoc generation to fail
%pom_disable_module sampleUses

%pom_remove_parent ri
%pom_add_parent org.jsr-305:jsr-305:0.1-SNAPSHOT ri

%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin ri

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license ri/LICENSE NOTICE-CC-BY
%doc sampleUses

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.0.2-5
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.2-2
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 11 2020 Marian Koncek <mkoncek@redhat.com> - 3.0.2-1
- Rebuild a properly versioned package

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0-0.29.20130910svn
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 23 2020 Richard Fearn <richardfearn@gmail.com> - 0-0.28.20130910svn
- Enable building with JDK 11: use source/target 1.8

* Sun Feb 02 2020 Richard Fearn <richardfearn@gmail.com> - 0-0.27.20130910svn
- Use %%license

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.25.20130910svn
- Build with OpenJDK 8

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.24.20130910svn
- Mass rebuild for javapackages-tools 201902

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.23.20130910svn
- Mass rebuild for javapackages-tools 201901

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.18.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.17.20130910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Richard Fearn <richardfearn@gmail.com> - 0-0.16.20130910svn
- Update to r51

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.15.20090319svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.14.20090319svn
- Update to current packaging guidelines

* Tue Jun 18 2013 Michal Srb <msrb@redhat.com> - 0-0.14.20090319svn
- Install license file with javadoc subpackage (Resolves: rhbz#975411)
- Add file containing link to CC-BY license text

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.13.20090319svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0-0.12.20090319svn
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.11.20090319svn
- Add CC-BY to license tag
- Resolves: rhbz#876648

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20090319svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Richard Fearn <richardfearn@gmail.com> - 0-0.9.20090319svn
- Do not build sampleUses module as it causes Javadoc generation to fail

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20090319svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0-0.7.20090319svn
- Use maven3 to build
- Fix depmap
- Fix Jave BRs

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20090319svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 26 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0-0.5.20090319svn
- Fix pom filename (Resolves rhbz#655811)
- Remove tomcat5 BR (not needed anymore)
- Use new maven plugin names
- Remove gcj support
- Few tweaks according to new guidelines
- Make jars and javadocs versionless

* Thu Jan 14 2010 Jerry James <loganjerry@gmail.com> - 0-0.4.20090319svn
- Update to 19 Mar 2009 snapshot
- Compress with xz instead of bzip2
- BR tomcat5, a horrible workaround to solve bz 538868

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20090203svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar  4 2009 Jerry James <loganjerry@gmail.com> - 0-0.3.20090203svn
- Explicitly require OpenJDK to build

* Sat Feb 28 2009 Jerry James <loganjerry@gmail.com> - 0-0.2.20090203svn
- Update to 03 Feb 2009 snapshot

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20080824svn.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20080824svn.1
- Cleaned up summary

* Mon Sep  8 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20080824svn
- Update to 24 Aug 2008 snapshot

* Mon Aug  4 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20080721svn
- Update to 21 Jul 2008 snapshot

* Mon Jun 30 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20080613svn
- Update to 13 Jun 2008 snapshot
- Fix broken URLs
- Include instructions on regenerating the tarball
- Conditionalize the gcj bits

* Mon Jun  2 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20080527svn
- Update to 27 May 2008 snapshot

* Mon May 12 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20071105svn
- Initial RPM
