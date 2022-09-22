%bcond_with bootstrap

Name:           atinject
Version:        1.0.5
Release:        4%{?dist}
Summary:        Dependency injection specification for Java (JSR-330)
License:        ASL 2.0
URL:            https://github.com/eclipse-ee4j/injection-api
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/eclipse-ee4j/injection-api/archive/%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif

%description
This package specifies a means for obtaining objects in such a way as
to maximize reusability, testability and maintainability compared to
traditional approaches such as constructors, factories, and service
locators (e.g., JNDI). This process, known as dependency injection, is
beneficial to most nontrivial applications.

%{?javadoc_package}

%prep
%setup -q -n injection-api-%{version}

%pom_remove_parent
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :moditect-maven-plugin

%mvn_alias : javax.inject:javax.inject
%mvn_file : atinject

%build
%mvn_build

%install
%mvn_install

%files -n %{?module_prefix}%{name} -f .mfiles
%license LICENSE.txt NOTICE.md

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.5-3
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.5-1
- Update to upstream version 1.0.5

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.3-2
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-36.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.3-1
- Update to upstream version 1.0.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-35.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1-34.20100611svn86
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat Jun 20 2020 Mat Booth <mat.booth@redhat.com> - 1-33.20100611svn86
- Allow building against Java 11

* Sat May 16 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-1
- Update to upstream version 1.0.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-32.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-31.20100611svn86
- Build with OpenJDK 8

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-30.20100611svn86
- Mass rebuild for javapackages-tools 201902

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-31.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-29.20100611svn86
- Mass rebuild for javapackages-tools 201901

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-30.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-29.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-28.20100611svn86
- Remove javax.inject Provides

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-27.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-26.20100611svn86
- Cleanup spec file

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-25.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-24.20100611svn86
- Use build-classpath to symlink junit JAR

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-23.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1-22.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-21.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-20.20100611svn86
- Disable javadoc doclint

* Thu Mar 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-19.20100611svn86
- Add javapackages Maven coordinates to manifests

* Wed Feb 18 2015 Mat Booth <mat.booth@redhat.com> - 1-18.20100611svn86
- Add OSGi manifest to tck jar
- Install with mvn_install

* Mon Jun 09 2014 Michal Srb <msrb@redhat.com> - 1-17.20100611svn86
- Apply the "source/target 1.5" patch

* Mon Jun  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-16.20100611svn86
- Compile with source/target 1.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-15.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-14.20100611svn86
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-13.20100611svn86
- Add javax.inject provides and directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-12.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-11.20100611svn86
- Remove unneeded BRs
- Install missing LICENSE file
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-10.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1-9.20100611svn86
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Jul 23 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-8.20100611svn86
- Add zip BR

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-7.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 24 2012 Krzysztof Daniel <kdaniel@redhat.com> - 1-6.20100611svn86
- Added OSGi manifest.

* Mon Feb 13 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-5.20100611svn86
- Add tck subpackage
- Use upstream build method

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-4.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 10 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-3.20100611svn86
- Use maven3 to build
- Versionless jars & javadocs

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-2.20100611svn86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 21 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-1.20100611svn86
- Initial version of the package
