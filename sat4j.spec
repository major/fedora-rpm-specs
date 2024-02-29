# should be consistent across one release
%global build_date 20130405

Name:           sat4j
Version:        2.3.5
Release:        30%{?dist}
Summary:        A library of SAT solvers written in Java

License:        EPL-1.0 or LGPLv2
URL:            http://www.sat4j.org/
# Created by sh sat4j-fetch.sh
Source0:        sat4j-%{version}.tar.xz
Source1:        sat4j-fetch.sh

Patch0:         0001-Fix-runtime-classpath-and-minimum-BREE.patch

BuildRequires:  ant
BuildRequires:  javapackages-local

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
The aim of the SAT4J library is to provide an efficient library of SAT
solvers in Java. The SAT4J library targets first users of SAT "black
boxes", those willing to embed SAT technologies into their application
without worrying about the details.

%prep
%setup -q -n sat4j-%{version}
%patch0 -p1

%build
export ANT_OPTS="-Dfile.encoding=iso-8859-1"
ant -Dbuild.compiler=modern -Drelease=%{version} \
 -Dtarget=1.8 -Dsource=1.8 -DBUILD_DATE=%{build_date} p2

%mvn_artifact "org.ow2.sat4j:org.ow2.sat4j.core::%{version}" dist/%{version}/org.sat4j.core.jar
%mvn_artifact "org.ow2.sat4j:org.ow2.sat4j.pb::%{version}" dist/%{version}/org.sat4j.pb.jar
%mvn_file ":org.ow2.sat4j.core" org.sat4j.core
%mvn_file ":org.ow2.sat4j.pb" org.sat4j.pb

%install
%mvn_install

%files -f .mfiles
# No %%doc files as the about.html is in the jar

%changelog
* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.3.5-30
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.3.5-25
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.3.5-24
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 2.3.5-19
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 18 2020 Mat Booth <mat.booth@redhat.com> - 2.3.5-18
- Allow building on Java 11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Mat Booth <mat.booth@redhat.com> - 2.3.5-15
- Fix license tag

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Mat Booth <mat.booth@redhat.com> - 2.3.5-10
- Install with xmvn

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.5-7
- Add build-requires on javapackages-local

* Mon Jun 22 2015 Mat Booth <mat.booth@redhat.com> - 2.3.5-6
- Remove SCL macros and tidy spec

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Alexander Kurtakov <akurtako@redhat.com> 2.3.5-3
- Remove useless parts.
- Require java-headless.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.3.5-1
- Update to latest upstream.

* Fri May 10 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.3.4-1
- Update to latest upstream.

* Wed Apr 17 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.3.3-7
- Remove jars from source.

* Fri Apr 5 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.3.0-6
- Update to 2.3.3
- Initial sclization.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 25 2011 Andrew Overholt <overholt@redhat.com> 2.3.0-2
- Make 1.5-level bytecode.  This enables bootstrapping of Eclipse
  with OpenJDK 7.

* Mon Apr 04 2011 Chris Aniszczyk <zx@redhat.com> 2.3.0-1
- Update to 2.3.0.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 8 2010 Alexander Kurtakov <akurtako@redhat.com> 2.2.0-1
- Update to 2.2.0.

* Tue Mar 30 2010 Andrew Overholt <overholt@redhat.com> 2.1.1-3
- Fix license tag

* Fri Mar 26 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-2
- Switch to lzma tarball.
- Remove classpath in manifest.

* Sun Mar 7 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-1
- Update to 2.1.1.

* Tue Aug 4 2009 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-1
- Update to 2.1.0 final.

* Wed Apr 8 2009 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-0.1.rc2
- Update to 2.1.0.RC2.

* Thu Feb 26 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.3-1
- Update to 2.0.3.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-7
- eclipse_base is now libdir/eclipse

* Tue Jul 15 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-6
- Build with OpenJDK (java.util.Scanner)

* Tue Jul 15 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-5
- Use sed instead of dos2unix

* Mon Jul 14 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-4
- Remove jmock JARs
- Don't run tests as part of build

* Mon Jul 14 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-3
- Remove Class-Path from pb MANIFEST.MF

* Mon Jul 14 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-2
- Add eclipse-pde BR for pdebuild script

* Fri Jun 27 2008 Andrew Overholt <overholt@redhat.com> 2.0.0-1
- 2.0.0
- Run tests

* Thu Mar 13 2008 Andrew Overholt <overholt@redhat.com> 2.0-0.1.RC5
- Initial version
