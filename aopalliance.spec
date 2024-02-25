%bcond_with bootstrap

Name:           aopalliance
Epoch:          0
Version:        1.0
Release:        38%{?dist}
Summary:        Java/J2EE AOP standards
License:        LicenseRef-Fedora-Public-Domain
URL:            http://aopalliance.sourceforge.net/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# cvs -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance login
# password empty
# cvs -z3 -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance export -r HEAD aopalliance
Source0:        aopalliance-src.tar.gz
Source1:        http://repo1.maven.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.pom
Source2:        %{name}-MANIFEST.MF

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  ant
BuildRequires:  javapackages-local
%endif

%description
Aspect-Oriented Programming (AOP) offers a better solution to many
problems than do existing technologies, such as EJB.  AOP Alliance
intends to facilitate and standardize the use of AOP to enhance
existing middleware environments (such as J2EE), or development
environements (e.g. Eclipse).  The AOP Alliance also aims to ensure
interoperability between Java/J2EE AOP implementations to build a
larger AOP community.

%{?javadoc_package}

%prep
%setup -q -n %{name}

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} -Dbuild.sysclasspath=only jar javadoc -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8

# Inject OSGi manifest required by Eclipse.
jar umf %{SOURCE2} build/%{name}.jar

%install
%mvn_file : %{name}
%mvn_artifact %{SOURCE1} build/%{name}.jar

%mvn_install -J build/javadoc

%files -f .mfiles

%changelog
* Fri Feb 23 2024 Jiri Vanek <jvanek@redhat.com> - 0:1.0-38
- bump of release for for java-21-openjdk as system jdk

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-35
- Rebuild to regenerate auto-Requires on java

* Fri Sep 01 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-34
- Convert License tag to SPDX format

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 29 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-31
- Implement bootstrap mode

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0:1.0-29
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0:1.0-28
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Mat Booth <mat.booth@redhat.com> - 0:1.0-23
- Generate 1.8 level bytecode to avoid breaking dependent packages that require
  Java 8

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0:1.0-22
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-16
- Switch to automatically-generated javadoc package

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Michael Simacek <msimacek@redhat.com> - 0:1.0-14
- Install with XMvn

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-11
- Add build-requires on javapackages-local

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-8
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-6
- Drop BR on zip, use jar instead
- Add more verbose description
- Update to current packaging guidelines

* Mon Feb 25 2013 Gerard Ryan <galileo.fedoraproject.org> 0:1.0-5
- Add OSGI manifest

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Tomas Radej <tradej@redhat.com> - 0:1.0-3
- Fixed tarball generation guide

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 6 2012 Andy Grimm <agrimm@gmail.com> 0:1.0-1
- build for Fedora
