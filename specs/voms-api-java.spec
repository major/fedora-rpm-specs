Name:		voms-api-java
Version:	3.3.3
Release:	3%{?dist}
Summary:	Virtual Organization Membership Service Java API

License:	Apache-2.0
URL:		https://wiki.italiangrid.it/VOMS
Source0:	https://github.com/italiangrid/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

#		Disable failing tests
#		IllegalState object explicit - implicit expected.
#		https://github.com/italiangrid/voms-api-java/issues/29
Patch0:		%{name}-disable-some-tests.patch
#		Disable tests that fail due to expired certificates
#		https://github.com/italiangrid/voms-api-java/issues/30
#		2022-09-24 (test0.cert.pem, wilco_cnaf_infn_it.cert.pem)
Patch1:		%{name}-expired-2022-09-24.patch
#		2022-10-08 (test_host_cnaf_infn_it.cert.pem)
Patch2:		%{name}-expired-2022-10-08.patch
#		2022-12-12 (test_host_2_cnaf_infn_it.cert.pem)
Patch3:		%{name}-expired-2022-12-12.patch
#		Adjust to removed deprecaded API in Mockito
Patch4:		%{name}-mockito4.patch

BuildArch:	noarch
ExclusiveArch:	%{java_arches} noarch

BuildRequires:	maven-local
%if %{?rhel}%{!?rhel:0} == 8
BuildRequires:	mvn(com.google.guava:guava:20.0)
%else
BuildRequires:	mvn(com.google.guava:guava)
%endif
BuildRequires:	mvn(eu.eu-emi.security:canl) >= 2.6
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.hamcrest:hamcrest-library)
BuildRequires:	mvn(org.mockito:mockito-core)
Requires:	mvn(eu.eu-emi.security:canl) >= 2.6

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides a java client API for VOMS.

%package javadoc
Summary:	Virtual Organization Membership Service Java API Documentation

%description javadoc
Virtual Organization Membership Service (VOMS) Java API Documentation.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 9
%patch -P 4 -p1
%endif

# Remove unused dependency
%pom_remove_dep net.jcip:jcip-annotations

# Use default location for javadoc output
%pom_xpath_remove "//pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:outputDirectory"
%pom_xpath_remove "//pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:reportOutputDirectory"

# F33+ and EPEL8+ doesn't use the maven-javadoc-plugin to generate javadoc
# Remove maven-javadoc-plugin configuration to avoid build failure
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

# Do not create source jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Cobertura no longer in Fedora due to licensing issues
%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin

# Remove license plugin
%pom_remove_plugin com.mycila.maven-license-plugin:maven-license-plugin

%if %{?fedora}%{!?fedora:0} >= 40 || %{?rhel}%{!?rhel:0} >= 10
# Update bouncycastle dependencies
%pom_change_dep org.bouncycastle:bcprov-jdk15on org.bouncycastle:bcprov-jdk18on
%pom_change_dep org.bouncycastle:bcpkix-jdk15on org.bouncycastle:bcpkix-jdk18on
%endif

%if %{?rhel}%{!?rhel:0} == 8
# Adapt guava dependency for EPEL 8
%pom_change_dep com.google.guava:guava:* com.google.guava:guava:20.0
%endif

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc AUTHORS README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 28 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.3-2
- Update bouncycastle dependencies for EPEL 10

* Sat Aug 03 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.3-1
- Update to version 3.3.3

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 14 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.2-17
- Update bouncycastle dependencies

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 3.3.2-16
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 16 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.2-14
- Adjust to removed deprecaded API in Mockito

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.2-11
- Disable tests that fail due to more expired certificates

* Mon Oct 17 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.2-10
- Disable tests that fail due to expired certificates

* Wed Sep 28 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.2-9
- Disable failing multi-thread test
- Disable tests using obsolete hashes (md5/sha1)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.3.2-7
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.3.2-6
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.2-4
- Disable failing tests due to changes in bouncycastle

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.2-1
- Update to version 3.3.2 - matches canl-java 2.6.x
- Drop patches voms-api-java-javadoc-source.patch and -no-local.patch

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.0-10
- Fedora 33 builds javadoc the same way EPEL 8 does

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 3.3.0-9
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue May 05 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.0-8
- Only remove the maven-javadoc-plugin configuration on EPEL 8
- Add source version to javadoc configuration (backported from git)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.0-6
- Remove maven-javadoc-plugin configuration
- Remove unused dependency net.jcip:jcip-annotations

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.0-3
- Add BuildRequires on hamcrest-library (no longer pulled in by mockito)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.0-1
- Update to version 3.3.0 - matches canl-java 2.5.x
- Drop patch voms-api-java-canl-2.5.patch

* Fri Jan 05 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.0-5
- Adapt to canl-java 2.5
- Use jcip-annotations for EPEL 7 build

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.0-3
- Remove maven source plugin

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.2.0-1
- Update to version 3.2.0 - matches canl-java 2.2.x
- Drop patches: voms-api-java-bc147.patch, -javadoc.patch and -testfix.patch

* Sun Feb 14 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1.0-1
- Update to version 3.1.0 - matches canl-java 2.1.x
- Drop patches: voms-api-java-bc147.patch and -javadoc.patch

* Thu Feb 11 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.5-5
- Backport fix for failing test due to new canl-java version

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 11 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.5-3
- Remove build-dependency on cobertura-maven-plugin
  (cobertura was removed from Fedora due to licensing issues)
- Enable tests in EPEL 7
- Implement new license packaging guidelines

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 16 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.5-1
- Update to version 3.0.5
- Rebase patches (and fix some deprecation warnings)

* Mon Nov 17 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.4-1
- Update to version 3.0.4
- Drop patch voms-api-java-timezone-dep-test.patch (fixed upstream)

* Thu Jun 26 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.3-1
- Update to version 3.0.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.2-2
- Disable tests that fail outside the Central European time zone

* Sun Mar 09 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.2-1
- Update to version 3
- Apply patch for bouncycastle 1.47+ on Fedora 21+ and EPEL 7+
- Convert to using xmvn

* Mon Oct 14 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.10-4
- Disable CRL tests (the CRL in the sources has expired)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.10-2
- Add BR on maven-surefire-provider-junit

* Mon Feb 11 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.10-1
- Update to version 2.0.10

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.0.9-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sun Dec 02 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.9-2
- Correct runtime requires and URL tag

* Thu Nov 29 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.9-1
- Update to version 2.0.9

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.8-1
- Update to version 2.0.8 (EMI 2 version)

* Mon Apr 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.7-2
- Fix compatibility maven fragment

* Tue Mar 20 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.7-1
- The Java API is now a separate source tree from the rest of voms
