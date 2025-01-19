%global github_version 1.0-1
%global fedora_version %(echo -n %{github_version} | sed 's/-/./')

Name:           jcip-annotations
Version:        %{fedora_version}
Release:        2%{?dist}
Summary:        A clean room implementation of the JCIP Annotations

License:        Apache-2.0
URL:            https://github.com/stephenc/jcip-annotations
Source0:        https://github.com/stephenc/jcip-annotations/archive/refs/tags/jcip-annotations-%{github_version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local

%description
A clean room implementation of the JCIP Annotations based entirely on the
specification provided by the javadocs.

%package javadoc
Summary:        Javadoc for jcip-annotations

%description javadoc
Javadoc documentation for the jcip-annotations package.

%prep
%setup -q -n %{name}-%{name}-%{github_version}

# Remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove unnecessary dependency on JUnit
%pom_remove_dep junit:junit

# Compile for Java 8
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/*" 1.8

# Install JAR directly in /usr/share/java
%mvn_file :jcip-annotations %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 30 2024 Richard Fearn <richardfearn@gmail.com> - 1.0_1-1
- Switch to clean room implementation, as original implementation uses
  CC-BY-2.5 licence, which is not allowed for code in Fedora

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-44.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1-43.20060626
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-42.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-41.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-40.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-39.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 Richard Fearn <richardfearn@gmail.com> - 1-38.20060626
- Use SPDX license identifier

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-37.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1-36.20060626
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1-35.20060626
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-34.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-33.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 15 2021 Richard Fearn <richardfearn@gmail.com> - 1-32.20060626
- Migrate away from %%add_maven_depmap

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-31.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-30.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1-29.20060626
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 23 2020 Richard Fearn <richardfearn@gmail.com> - 1-28.20060626
- Enable building with JDK 11: use source/target 1.8

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-27.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-26.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-25.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-24.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-23.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> - 1-22.20060626
- Remove unnecessary Group: tags

* Fri Jul 28 2017 Richard Fearn <richardfearn@gmail.com> - 1-21.20060626
- Add temporary dependency on javapackages-local, for %%add_maven_depmap macro

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-20.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-19.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1-18.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 25 2015 Richard Fearn <richardfearn@gmail.com> - 1-17.20060626
- jcip-annotations-javadoc no longer depends on jcip-annotations

* Wed Jul 01 2015 Richard Fearn <richardfearn@gmail.com> - 1-16.20060626
- Disable doclint when building Javadoc

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-15.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-14.20060626
- Add alias for com.github.stephenc.jcip:jcip-annotations

* Tue Jun 10 2014 Richard Fearn <richardfearn@gmail.com> - 1-13.20060626
- Switch to .mfiles

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-12.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 16 2014 Richard Fearn <richardfearn@gmail.com> - 1-11.20060626
- Change java dependency to java-headless (bug #1068255)

* Sun Feb 23 2014 Richard Fearn <richardfearn@gmail.com> - 1-10.20060626
- Remove jpackage-utils dependency from jcip-annotations-javadoc

* Sun Feb 23 2014 Richard Fearn <richardfearn@gmail.com> - 1-9.20060626
- Update source URL

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-8.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-7.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-6.20060626
- Update to current packaging guidelines
- Resolves: rhbz#880283

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-5.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-4.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-3.20060626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec  3 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-2.20060626
- Fix maven metadata and pom filename (Resolves rhbz#655807)
- Use versionless jars and javadoc
- Few other packaging fixes

* Wed Jan  6 2010 Jerry James <loganjerry@gmail.com> - 1-1.20060626
- Add maven depmap
- Upstream uploaded a new source jar with a trivial difference
- Fix the version-release number

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-20060628.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-20060627.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May  5 2008 Jerry James <loganjerry@gmail.com> - 0-20060626.4
- Don't package source or HTML files in the jar

* Fri Apr 18 2008 Jerry James <loganjerry@gmail.com> - 0-20060626.3
- Changes required by new Java packaging guidelines

* Wed Nov 14 2007 Jerry James <loganjerry@gmail.com> - 0-20060626.2
- Don't make the javadocs appear in a docs subdirectory

* Tue Sep 18 2007 Jerry James <loganjerry@gmail.com> - 0-20060626.1
- Initial RPM
