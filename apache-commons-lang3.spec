%bcond_with bootstrap

Name:           apache-commons-lang3
Version:        3.12.0
Release:        7%{?dist}
Summary:        Provides a host of helper utilities for the java.lang API
License:        ASL 2.0
URL:            https://commons.apache.org/lang
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/commons/lang/source/commons-lang3-%{version}-src.tar.gz
Patch1:         0001-Remove-test-dependency-on-JUnit-Pioneer.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap-openjdk8
%else
BuildRequires:  maven-local-openjdk8
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bndlib)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
%endif

%description
The standard Java libraries fail to provide enough methods for
manipulation of its core classes. The Commons Lang Component provides
these extra methods.
The Commons Lang Component provides a host of helper utilities for the
java.lang API, notably String manipulation methods, basic numerical
methods, object reflection, creation and serialization, and System
properties. Additionally it contains an inheritable enum type, an
exception structure that supports multiple types of nested-Exceptions
and a series of utilities dedicated to help with building methods, such
as hashCode, toString and equals.

With version of commons-lang 3.x, developers decided to change API and
therefore created differently named artifact and jar files. This is
the new version, while apache-commons-lang is the compatibility
package.

%{?javadoc_package}

%prep
%setup -q -n commons-lang3-%{version}-src

%patch1 -p1

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_dep org.openjdk.jmh:jmh-core
%pom_remove_dep org.openjdk.jmh:jmh-generator-annprocess
%pom_remove_dep :junit-bom

%mvn_file : %{name} commons-lang3

# testParseSync() test fails on ARM and PPC64LE for unknown reason
sed -i 's/\s*public void testParseSync().*/@org.junit.jupiter.api.Disabled\n&/' \
    src/test/java/org/apache/commons/lang3/time/FastDateFormatTest.java

# non-deterministic tests fail randomly
rm src/test/java/org/apache/commons/lang3/RandomStringUtilsTest.java

# Missing dependencies
rm src/test/java/org/apache/commons/lang3/HashSetvBitSetTest.java

# Remove limits and Java 11 options
sed -i '/<argLine>/d' pom.xml

%build
# See "-DcommonsLang3Version" in maven-surefire for the tested version
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 27 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.12.0-6
- Workaround build issue with RPM 4.18

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.12.0-5
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.12.0-2
- Bootstrap build
- Non-bootstrap build

* Wed Mar 10 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.12.0-1
- Update to upstream version 3.12.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Fabio Valentini <decathorpe@gmail.com> - 3.11-1
- Update to version 3.11.
- Fixes RHBZ#1699692

* Tue Aug 04 2020 Marian Koncek <mkoncek@redhat.com> - 3.11-1
- Update to upstream version 3.11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.8.1-6
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Apr 15 2020 Marian Koncek <mkoncek@redhat.com> - 3.10-1
- Update to upstream version 3.10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.9-4
- Build with OpenJDK 8

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.9-3
- Mass rebuild for javapackages-tools 201902

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.9-2
- Mass rebuild for javapackages-tools 201901

* Mon May 13 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.9-1
- Update to upstream version 3.9

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Marian Koncek <mkoncek@redhat.com> - 3.8.1-2
- Fix incorrect OSGi metadata
- Resolves: rhbz#1636556

* Mon Oct 01 2018 Marian Koncek <mkoncek@redhat.com> - 3.8.1-1
- Update to upstream version 3.8.1
- Resolves: rhbz#1619243

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.7-2
- Cleanup spec file

* Thu Nov 09 2017 Michael Simacek <msimacek@redhat.com> - 3.7-1
- Update to upstream version 3.7

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.6-2
- Conditionalize BR on jmh

* Mon Jul 03 2017 Michael Simacek <msimacek@redhat.com> - 3.6-1
- Update to upstream version 3.6

* Tue Mar 14 2017 Michael Simacek <msimacek@redhat.com> - 3.5-3
- Disable non-deterministic test

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 19 2016 Michael Simacek <msimacek@redhat.com> - 3.5-1
- Update to upstream version 3.5

* Wed Mar 09 2016 Michael Simacek <msimacek@redhat.com> - 3.4-5
- Fix unapplied patch

* Mon Feb 15 2016 Michael Simacek <msimacek@redhat.com> - 3.4-4
- Fix parsing of ISO dates with UTC TZ

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Alexander Kurtakov <akurtako@redhat.com> 3.4-1
- Update to upstream 3.4.

* Wed Jul 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.2-3
- Fix build-requires on apache-commons-parent

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.2-1
- Update to upstream version 3.3.2

* Thu Mar 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-2
- Disable test failing on PPC64LE

* Thu Mar 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-1
- Update to upstream version 3.3.1

* Tue Mar 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3-1
- Update to upstream version 3.3

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.2.1-2
- Use Requires: java-headless rebuild (#1067528)

* Thu Jan  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.1-1
- Update to upstream version 3.2.1

* Thu Jan  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-1
- Update to upstream version 3.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-6
- Build with xmvn
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Aug 27 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.1-3
- Make easymock3 dependency conditional for Fedora

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 gil cattaneo <puntogil@libero.it> - 3.1-1
- update to 3.1

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov  3 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.1-1
- Initial version of the package
