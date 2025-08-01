%global shortname looks

Name:           jgoodies-looks
Version:        2.7.0
Release:        16%{?dist}
Summary:        Free high-fidelity Windows and multi-platform appearance

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.jgoodies.com/freeware/libraries/looks/
# Upstream no longer distributes the library under an Open Source license. Latest
# Open Source release is taken from Maven Central
Source0:        https://repo1.maven.org/maven2/com/jgoodies/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/com/jgoodies/%{name}/%{version}/%{name}-%{version}.pom
# Fix build with JDK 11
Patch0:         %{name}-2.7.0-jdk11.patch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.jgoodies:jgoodies-common)
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
The JGoodies look&feels make your Swing applications and applets look better.
They have been optimized for readability, precise micro-design and usability.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.


%prep
%autosetup -c -p0
mkdir -p src/main/java/
mv com/ src/main/java/

cp %{SOURCE1} pom.xml

# Remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove useless dependency on JUnit (no test available)
%pom_remove_dep junit:junit

%mvn_file :%{name} %{name} %{name}

# Drop Windows L&F support files (unsupported on JDK 11)
rm -r src/main/java/com/jgoodies/looks/windows/

# Fix source/target version for JDK 17
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8"
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8"


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles


%files javadoc -f .mfiles-javadoc


%changelog
* Tue Jul 29 2025 jiri vanek <jvanek@redhat.com> - 2.7.0-16
- Rebuilt for java-25-openjdk as preffered jdk

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7.0-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.7.0-11
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.7.0-5
- Rebuilt for Drop i686 JDKs

* Fri Feb 18 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.7.0-4
- Fix build with JDK 17

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.7.0-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 2.6.0-15
- Remove unnecessary dependency on parent POM.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.6.0-13
- Fix build with JDK11

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.6.0-12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.6.0-5
- Add missing BR on mvn(org.sonatype.oss:oss-parent:pom:)
- Spec cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 13 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5.3-3
- Update for newer guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.5.2-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 01 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2
- Drop patch jgoodies-looks-2.5.1-build.patch

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5.1-2
- Include missing resources in JAR file (reported and fixed by Mary Ellen
  Foster)

* Fri May 04 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1

* Thu Feb 16 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0
- Add missing look jars

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.4.2-2
- Add necessary Provides/Obsoletes since there is no more jgoodies-looks-demo
  subpackage

* Fri Dec 16 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2
- Spec cleanup

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May 19 2008 Mary Ellen Foster <mefoster at gmail.com> 1.2.0-1
- Update to 1.2.0

* Tue Oct 16 2007 Mary Ellen Foster <mefoster at gmail.com> 1.1.0-2
- Fix encoding on HTML files
- Use empty CLASSPATH when building
- Fix indentation in spec file

* Wed Sep  5 2007 Mary Ellen Foster <mefoster at gmail.com> 1.1.0-1
- Initial version for Fedora, based on JPackage spec by Eric Lavarde
