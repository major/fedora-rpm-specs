Name:           xmlgraphics-commons
Version:        2.10
Release:        2%{?dist}
Epoch:          0
Summary:        XML Graphics Commons

License:        Apache-2.0 
URL:            http://xmlgraphics.apache.org/
Source0:        http://archive.apache.org/dist/xmlgraphics/commons/source/xmlgraphics-commons-%{version}-src.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(xml-resolver:xml-resolver)

%description
Apache XML Graphics Commons is a library that consists of
several reusable components used by Apache Batik and
Apache FOP. Many of these components can easily be used
separately outside the domains of SVG and XSL-FO. You will
find components such as a PDF library, an RTF library,
Graphics2D implementations that let you generate PDF &
PostScript files, and much more.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q %{name}-%{version}

find -name "*.jar" -delete

# Disable plugins not needed for RPM build
%pom_remove_plugin :maven-checkstyle-plugin

# Make into OSGi bundle
%pom_xpath_inject pom:project '<packaging>bundle</packaging>'
%pom_add_plugin org.apache.felix:maven-bundle-plugin . \
" <extensions>true</extensions>
  <configuration>
    <instructions>
      <Bundle-SymbolicName>org.apache.xmlgraphics</Bundle-SymbolicName>
    </instructions>
  </configuration>"

%build
%mvn_file : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%doc README

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 0:2.10-1
- 2.10

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0:2.9-3
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Gwyn Ciesla <gwync@protonmail.com> - 0:2.9-1
- 2.9

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 0:2.8-3
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 09 2022 Gwyn Ciesla <gwync@protonmail.com> - 0:2.8-1
- 2.8

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0:2.7-3
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0:2.7-2
- Rebuilt for java-17-openjdk as system jdk

* Mon Jan 24 2022 Gwyn Ciesla <gwync@protonmail.com> - 0:2.7-1
- 2.7

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 01 2021 Jie Kang <jkang@redhat.com> - 0:2.6-1
- Update to latest upstream release

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 01 2020 Mat Booth <mat.booth@redhat.com> - 0:2.4-1
- Update to latest upstream release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0:2.3-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Mat Booth <mat.booth@redhat.com> - 0:2.3-1
- Update to latest upstream release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Mat Booth <mat.booth@redhat.com> - 0:2.2-1
- Update to latest release
- Switch to maven-based build
- Add OSGi metadata

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Michael Simacek <msimacek@redhat.com> - 0:2.0.1-5
- Install with XMvn

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Michael Simacek <msimacek@redhat.com> - 0:2.0.1-1
- Update to upstream version 2.0.1

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 30 2015 Rüdiger Landmann <rlandmann@redhat.com> - 0:2.0-1
- Rebase on new upstream

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.5-4
- Update to current packaging guidelines
- Resolves: rhbz#1107290

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 19 2013 Mat Booth <fedora@matbooth.co.uk> - 0:1.5-1
- Update to 1.5, rhbz #895934
- Drop unneeded patch

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 06 2012 Deepak Bhole <dbhole@redhat.com> 1.4-5
- Added dist to the release tag

* Thu Mar 01 2012 Jiri Vanek <jvanek@redhat.com> - 0:1.4-5
- Resolves: rhbz#796341
- Added xmlgraphics-commons-java-7-fix.patch to fix build with Java 7

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May  3 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.4-3
- Install maven metadata
- Versionless jars & javadocs
- Fixes according to new guidelines

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 1 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.4-1
- Updte to 1.4.

* Sat Jan 9 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.3.1-1
- Update to 1.3.1.
- Fix Source0 url.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr 02 2008 Lillian Angel <langel at redhat.com> - 0:1.3-1
- Added java-1.6.0-openjdk-devel as build requirement.

* Mon Mar 31 2008 Lillian Angel <langel at redhat.com> - 0:1.3-1
- Updated sources to 1.3.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Added epoch.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Added missing BuildRoot line.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Fixed install section.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Fixed rpmlint errors.

* Tue Sep 18 2007 Joshua Sumali <jsumali at redhat.com> - 0:1.2-1jpp
- Update to 1.2

* Tue May 23 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.0-1jpp
- First JPP-1.7 release
