Name:           jfreechart
Version:        1.5.4
Release:        8%{?dist}
Summary:        A 2D chart library for Java applications (JavaFX, Swing or server-side)
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://www.jfree.org/jfreechart
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jfree/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:servlet-api)
# need apiguardian-api until Fedora releases junit >= 5.8.0 (1)
# link:
# https://junit.org/junit5/docs/5.8.0/release-notes/index.html#deprecations-and-breaking-changes
# https://junit.org/junit5/docs/5.8.0/release-notes/index.html#new-features-and-improvements
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)

%description
JFreeChart is a comprehensive free chart library for the Java platform that can
be used on the client-side (JavaFX and Swing) or the server side (with export to
multiple formats including SVG, PNG and PDF).

%{?javadoc_package}

%prep
%autosetup

# (1)
%pom_add_dep org.apiguardian:apiguardian-api:1.1.1

%build
%mvn_build -f -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%license licence-LGPL.txt
%doc README.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.4-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.5.4-5
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.5.4-1
- Update to version 1.5.4
- Skip tests

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.5.3-4
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.5.3-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Didik Supriadi <didiksupriadi41@gmail.com> - 1.5.3-1
- Update to version 1.5.3
- Rewrite spec

* Thu Aug 05 2021 Severin Gehwolf <sgehwolf@redhat.com> - 1.0.19-19
- Add junit BR for running tests. Fixes FTBFS.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.19-17
- Remove unnecessary dependency on parent POM.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1.0.19-15
- Disable -swt sub-package by default.
- Remove -javadoc sub-package since it would fail anyway with JDK 11.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.19-14
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jul 28 2017 Severin Gehwolf <sgehwolf@redhat.com> - 1.0.19-8
- Fix FTBFS, by changing servlet API BRs so as to pull in
  glassfish-servlet-api which provides correct maven artifacts.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.0.19-5
- Add missing BuildRequires to fix FTBFS (BZ#1406128).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 04 2014 Severin Gehwolf <sgehwolf@redhat.com> 1.0.19-2
- Don't Import-Package javax.servlet*

* Tue Sep 02 2014 Severin Gehwolf <sgehwolf@redhat.com> 1.0.19-1
- Update to upstream 1.0.19 release.
- Switch to building with xmvn where possible (swt sub-package
  still uses ant).

* Tue Jun 10 2014 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-12
- Fix FTBFS. Resolves RHBZ#1106941

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-9
- Fix FTBFS due to build-classpath not finding swt.jar any
  longer. See RHBZ#912664.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-7
- Remove itext dependency in pom.

* Fri Nov 16 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-6
- Conditionally build jfreechart-swt.

* Mon Sep 17 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-4
- Set proper Bundle-{Version,SymbolicName,Name} in manifest.

* Tue Jul 24 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-3
- Add aqute bnd instructions so as to produce OSGi metadata.
- Based on kdaniel's suggestion, use build-classpath script to find swt

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Alexander Kurtakov <akurtako@redhat.com> 1.0.14-1
- Update to new upstream version 1.0.14.
- Use pom.xml file from the tarball.

* Wed Feb 15 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.13-5
- Added Maven POM: BZ#789586

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0.13-3
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 19 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.0.13-1
- Update to a later release
- Cosmetic fixes

* Mon Apr 19 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.0.10-4
- Enable SWT support (ELMORABITY Mohamed, #583339)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jul 19 2008 Lubomir Rintel (Fedora Astronomy) <lkundrak@fedoraproject.org> - 1.0.10-1
- Initial packaging
