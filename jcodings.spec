# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           jcodings
Version:        1.0.55
Release:        2%{?dist}
Summary:        Java-based codings helper classes for Joni and JRuby

License:        MIT
URL:            https://github.com/jruby/%{name}
Source0:        https://github.com/jruby/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

%description
Java-based codings helper classes for Joni and JRuby.

%package javadoc
Summary: API documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find -name '*.class' -delete
find -name '*.jar' -delete

%mvn_file : %{name}

# Remove pointless parent pom
%pom_remove_parent

# Remove wagon extension
%pom_xpath_remove "pom:build/pom:extensions"

# Remove plugins not relevant for downstream RPM builds
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

# Generate OSGi metadata by using bundle packaging
%pom_xpath_inject pom:project "<packaging>bundle</packaging>"
%pom_add_plugin org.apache.felix:maven-bundle-plugin "<extensions>true</extensions>"

%build
# the pom is already on 1.7, I had not found what builds by 6 deep in sources 
%mvn_build  -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.55-1
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.55-0
- Rebuilt for java-17-openjdk as system jdk
- bumped build to 1.0.55
- bumped src/target

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 02 2020 Mat Booth <mat.booth@redhat.com> - 1.0.36-2
- Add OSGi metadata

* Wed Sep 02 2020 Mat Booth <mat.booth@redhat.com> - 1.0.36-1
- Update to a version that properly supports JDK 9+
- Modernise specfile

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.9-19
- Remove unnecessary dependency on maven-javadoc-plugin.
- Fixes build and javadoc generation with both Java 8 and 11.
- Remove maven-compiler-plugin configuration that's broken with Java 11.
- Override javac source and target version with 1.8.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.9-18
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.0.9-10
- Add missing BuildRequires to fix FTBFS (BZ#1406099).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.9-6
- Use Requires: java-headless rebuild (#1067528)

* Thu Aug 29 2013 Mat Booth <fedora@matbooth.co.uk> - 1.0.9-5
- Fix unowned dir.

* Thu Aug 29 2013 Mat Booth <fedora@matbooth.co.uk> - 1.0.9-4
- Update for latest guidelines, rhbz #992612

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.9-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan 25 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.9-1
- Updated to version 1.0.9.
- Switch to maven builds, as it seems to be preffered upstream way.

* Tue Oct 09 2012 gil cattaneo <puntogil@libero.it> - 1.0.5-4
- add maven pom
- adapt to current guideline

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 01 2011 Mo Morsi <mmorsi@redhat.com> - 1.0.5-1
- update to latest upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 09 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> - 1.0.2-2
- Fix the clean up code in the prep section
- Fix typo
- Save changelog

* Thu Jan 28 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> - 1.0.2-1
- 1.0.2
- Remove gcj bits
- New URL
- Update summary and description
- Use macros in all sections of the spec
- Add README.txt generated on the fly

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Conrad Meyer <konrad@tylerc.org> - 1.0.1-1
- Bump to 1.0.1 for jruby 1.1.6.

* Wed Dec 17 2008 Conrad Meyer <konrad@tylerc.org> - 1.0-2
- Add gcj bits.

* Fri Nov 28 2008 Conrad Meyer <konrad@tylerc.org> - 1.0-1
- Initial package (needed for jruby 1.1.5 and joni 1.1.1).
