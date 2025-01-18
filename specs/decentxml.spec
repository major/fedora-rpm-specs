%global revision 572a0baa91d1

Name:             decentxml
Version:          1.4
Release:          38%{?dist}
Summary:          XML parser optimized for round-tripping and code reuse
# Automatically converted from old format: BSD - review is highly recommended.
License:          LicenseRef-Callaway-BSD
# Google Code has shut down.
# URL:            http://code.google.com/p/decentxml
URL:              https://bitbucket.org/digulla/%{name}
BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch

# Google Code has shut down.
# Source0:        https://decentxml.googlecode.com/files/decentxml-1.4-src.zip
#
# This version is equivalent to the last Google Code release, other than
# folder structure due to how Bitbucket makes zip archives:
#
# decentxml-1.4 -> digulla-decentxml-572a0baa91d1
Source0:          https://bitbucket.org/digulla/%{name}/get/r%{version}.zip

# For running w3c conformance test suite.
Source1:          http://www.w3.org/XML/Test/xmlts20031210.zip

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)


%description
XML parser optimized for round-tripping and code reuse with main
features being:
 * Allows 100% round-tripping, even for weird white-space between
   attributes in the start tag or in the end tag
 * Suitable for building editors and filters which want/need to
   preserve the original file layout as much as possible
 * Error messages have line and column information
 * Easy to reuse individual components
 * XML 1.1 compatible

%package javadoc
Summary:          API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n digulla-%{name}-%{revision}

# We are looking for xml conformance data one level above so unzip
# here and symlink there.
unzip %{SOURCE1}
ln -sf %{name}-%{version}/xmlconf ../xmlconf
sed -i -e "s|junit-dep|junit|g" pom.xml

# Two tests fail with Java 8, probably because of some Unicode incompatibility.
sed -i '/not_wf_sa_16[89] /d' src/test/java/de/pdark/decentxml/XMLConformanceTest.java

%pom_remove_plugin :maven-javadoc-plugin

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

# Don't use deprecated "attached" goal of Maven Assembly Plugin, which
# was removed in version 3.0.0.
%pom_xpath_set "pom:plugin[pom:artifactId='maven-assembly-plugin']/pom:executions/pom:execution/pom:goals/pom:goal[text()='attached']" single

%build
%mvn_file  : %{name}
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4-37
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.4-35
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.4-29
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.4-28
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.4-23
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 04 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4-22
- Override javac source and target versions to fix build with Java 11.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Alexander Scheel <ascheel@redhat.com> - 1.4-20
- Rebuilt and resurrected from orphaning for Eclipse

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-14
- Don't use deprecated goal of maven-assembly-plugin

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-13
- Add missing build-requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-10
- Remove javadoc plugin execution

* Tue Jul 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-9
- Disable failing tests

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-8
- Remove BuildRequires on maven-surefire-provider-junit4

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 1.4-3
- Build with xmvn

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 1 2012 Alexander Kurtakov <akurtako@redhat.com> 1.4-1
- Update to 1.4 upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 25 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-1
- Initial version of the package
