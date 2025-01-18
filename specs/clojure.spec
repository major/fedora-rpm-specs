%global project     clojure
%global groupId     org.clojure
%global artifactId  clojure
%global archivename %{project}-%{artifactId}

Name:           clojure
Epoch:          1
Version:        1.12.0
Release:        2%{?dist}
Summary:        A dynamic programming language that targets the Java Virtual Machine

License:        EPL-1.0
URL:            http://clojure.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{name}-%{version}.zip

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.clojure:core.specs.alpha)
BuildRequires:  mvn(org.clojure:spec.alpha)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
Requires:       javapackages-tools

%description 
Clojure is a dynamic programming language that targets the Java
Virtual Machine. It is designed to be a general-purpose language,
combining the approachability and interactive development of a
scripting language with an efficient and robust infrastructure for
multithreaded programming. Clojure is a compiled language - it
compiles directly to JVM bytecode, yet remains completely
dynamic. Every feature supported by Clojure is supported at
runtime. Clojure provides easy access to the Java frameworks, with
optional type hints and type inference, to ensure that calls to Java
can avoid reflection.

%prep
%setup -q -n %{archivename}-%{version}

%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :nexus-staging-maven-plugin

%build
%mvn_build -f -j

%install

%mvn_install

# startup script
%jpackage_script clojure.main "" "" clojure:clojure-spec-alpha:clojure-core-specs-alpha clojure false

%files -f .mfiles
%license epl-v10.html 
%doc changes.md readme.txt 
%{_bindir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 11 2024 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.12.0-1
- Update to upstream release 1.12.0, closes rhbz#2186974

* Tue Oct 8 2024 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.11.3-1
- Update to upstream release 1.11.3

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 15 2024 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.11.2-1
- Update to upstream release 1.11.2

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1:1.11.1-2
- Rebuilt for Drop i686 JDKs

* Sun Apr 10 2022 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.11.1-1
- Update to upstream release 1.11.1

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1:1.10.3-4
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 06 2021 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.10.3-1
- Update to upstream release 1.10.3

* Sat Jan 30 2021 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.10.2-1
- Update to upstream release 1.10.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.10.1-6
- Add javapackages-tools dependency to fix wrapper script.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1:1.10.1-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 02 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.10.1-3
- Use jpackage_script to generate clojure application shell script.

* Fri May 01 2020 Fabio Valentini <decathorpe@gmail.com> - 1:1.10.1-2
- Remove unnecessary maven-release-plugin and drop redundant Requires.

* Wed Apr 15 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.10.1-1
- Update to upstream release 1.10.1
- Update clojure-spec-alpha and clojure-core-specs-alpha dependency
- Remove jsr166y pom_remove_dep

* Tue Apr 14 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.9.0-1
- Update to upstream release 1.9.0, update clojure-spec-alpha dependency

* Sat Apr 11 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.9.0-0.beta3.1
- Update to upstream release 1.9.0-beta3
- Switch to use maven building
- Remove plugin org.sonatype.plugins:nexus-staging-maven-plugin
- Remove jsr166 dependency from pom 

* Sat Apr 04 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.9.0-0.alpha15.1
- Update to upstream release 1.9.0-alpha15
- Update to require JDK 1.8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Markku Korkeala <markku.korkeala@iki.fi> - 1:1.8.0-1
- Update to upstream release 1.8.0
- Add sonatype-oss-parent as a build requirement
- Add license macro and fix license short name

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.0-0.beta1.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.0-0.beta1.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.0-0.beta1.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.0-0.beta1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.0-0.beta1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.0-0.beta1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.0-0.beta1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 15 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.8.0-0.beta1
- New prerelease of Clojure 1.8.0

* Wed Jun 17 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.7.0-0.5
- New upstream release (clojure-1.7.0-RC2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.7.0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun  5 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.7.0-0.3
- New upstream release

* Fri May  1 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.7.0-0.2
- New upstream release

* Tue Apr 14 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.7.0-0.1
- New upstream release

* Thu Jul 24 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.6.0-3
- Migrating to the new JAVA packaging guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 25 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.6.0-1
- New upstream release

* Mon Mar 24 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.6.0-0.5
- New release candidate of clujure 1.6.0

* Tue Mar 18 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.6.0-0.3
- Relöease candidate of clojure 1.6.0

* Wed Mar  5 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.6.0-0.2
- New upstream pre-release
- Add support for headless java (#1068005)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.5.1-1
- New upstream release.

* Sat Mar  2 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.5.0-1
- New upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.5.0-0.RC1.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:1.5.0-0.RC1.1.1
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Dec 24 2012 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.5.0-0.RC1.1
- Use -Dmaven.test.skip=1 to sip test run

* Sun Dec 23 2012 Jochen Schmitt <Jochen herr-schmitt de> - 1:1.5.0-0.RC1
- New upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun  6 2012 Michel Salim <salimma@fedoraproject.org> - 1:1.4.0-2
- Update to better follow packaging guidelines

* Tue Apr 17 2012 Jochen Schmitt <Jochen herr-schmitt de> 1:1.4.0-1
- New upstream release

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 25 2011 Jochen Schmitt <Jochen herr-schmitt de> 1:1.3.0-1
- New upstream release
- Remove temp. patch to resolve JDK-1.7 issue

* Wed Sep 21 2011 Jochen Schmitt <Jochen herr-schmitt de> 1:1.3.0-0.1
- New upstrem release
- Remove no-classpath patch (#684060)
- Add patch to resolve JDK-1.7 related issues with test suite

* Tue Jul 12 2011 Jochen Schmitt <Jochen herr-schmitt de> 1:1.2.1-1
- New minor bug fixing release from upstream

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 20 2010 Jochen Schmitt <Jochen herr-schmitt de> 1:1.2.0-1
- New upstream release

* Wed Jan 20 2010 Jochen Schmitt <Jochen herr-schmitt de> 1:1.1.0-1
- New upstream release

* Wed Dec  2 2009 Jochen Schmitt <Jochen herr-schmitt de> 1:1.0.0-5
- Installing maven pom file

* Wed Dec  2 2009 Jochen Schmitt <Jochen herr-schmitt de> 1:1.0.0-3
- Add Epoch to get proper EVR path

* Tue Dec  1 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.0.0-2
- Forgot uploading soruces

* Tue Dec  1 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.0.0-1
- New upstream release
- change license tag to EPL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090320-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 20 2009 Colin Walters <walters@verbum.org> - 20090320
- New upstream

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081217-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Colin Walters <walters@verbum.org> - 20081217-1
- New upstream

* Fri Oct 24 2008 Colin Walters <walters@verbum.org> - 20080916-2
- BR OpenJDK, we need 1.6

* Tue Sep 30 2008 Colin Walters <walters@verbum.org> - 20080916-1
- initial version

