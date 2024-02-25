# Break dependency loops in a bootstrap situation
%bcond_with bootstrap

# Disable Maven reporting in bootstrap mode and in RHEL
%if %{with bootstrap} || 0%{?rhel}
%bcond_with maven_reporting
%else
%bcond_without maven_reporting
%endif

Name:           javacc-maven-plugin
Version:        3.0.1
Release:        7%{?dist}
Summary:        JavaCC Maven Plugin

License:        Apache-2.0
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
URL:            https://github.com/mojohaus/javacc-maven-plugin
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.javacc:javacc)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%endif

%if %{with maven_reporting}
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
%endif

%description
Maven Plugin for processing JavaCC grammar files.

%javadoc_package

%prep
%autosetup -n %{name}-%{name}-%{version}
cp -p %{SOURCE1} .

# Do not use jtb, which is unmaintained.  It is accessed only via reflection to
# avoid depending on Java 1.5 for compilation.
%pom_remove_dep edu.ucla.cs.compilers:jtb

# Disable integration tests
%pom_remove_plugin org.apache.maven.plugins:maven-invoker-plugin
rm -fr src/it

# Disable building the web site
rm -fr src/site

# In bootstrap mode, disable documentation and reporting
# Add in a formerly transitive dependency that is still needed
%if %{without maven_reporting}
%pom_remove_dep org.apache.maven.doxia:
%pom_remove_dep org.apache.maven.reporting:
rm src/main/java/org/codehaus/mojo/javacc/JJDocMojo.java
%pom_add_dep org.apache.maven:maven-core:3.8.6
%endif

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt src/main/resources/NOTICE

%changelog
* Fri Feb 23 2024 Jiri Vanek <jvanek@redhat.com> - 3.0.1-7
- bump of release for for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 01 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.1-4
- Rebuild

* Sat Aug 26 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.1-3
- Bootstrap using javapackages-bootstrap

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 19 2023 Jerry James <loganjerry@gmail.com> - 3.0.1-1
- Add bootstrap mode to break a dependency loop

* Wed Mar 29 2023 Jerry James <loganjerry@gmail.com> - 3.0.1-1
- Version 3.0.1
- Convert License tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.6-36
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.6-35
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.6-30
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-22
- Add missing build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-19
- Mavenize requires and build-requires

* Mon Jun  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-18
- Update to current packaging guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-16
- Use .mfiles generated during build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 08 2013 Michal Srb <msrb@redhat.com> - 2.6-14
- Migrate from maven-doxia to doxia subpackages (Resolves: #909835)

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.6-13
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Nov 26 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-12
- Copy LICENSE-2.0.txt to builddir

* Fri Nov 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-11
- Install license files
- Resolves: rhbz#880189

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Alexander Kurtakov <akurtako@redhat.com> 2.6-8
- Build with maven 3.
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 6 2010 Orion Poplawski <orion@cora.nwra.com> 2.6-6
- Require mojo-parent.

* Thu Sep 16 2010 Alexander Kurtakov <akurtako@redhat.com> 2.6-5
- BR mojo-parent.

* Wed Mar 24 2010 Alexander Kurtakov <akurtako@redhat.com> 2.6-4
- Fix BRs.

* Wed Mar 24 2010 Alexander Kurtakov <akurtako@redhat.com> 2.6-3
- Fix plugin metadata build.

* Wed Mar 17 2010 Alexander Kurtakov <akurtako@redhat.com> 2.6-2
- Fix Requires.

* Mon Mar 15 2010 Alexander Kurtakov <akurtako@redhat.com> 2.6-1
- Initial package.
