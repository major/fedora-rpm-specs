Name:     jnr-ffi
Version:  2.2.12
Release:  1%{?dist}
Summary:  Java Abstracted Foreign Function Layer
License:  ASL 2.0
URL:      http://github.com/jnr/%{name}/
Source0:  https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz

# Arm assembler is not packaged
Patch0:   0001-Remove-Arm-stub-compiler.patch

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jffi)
BuildRequires:  mvn(com.github.jnr:jffi::native:)
BuildRequires:  mvn(com.github.jnr:jnr-x86asm)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)


BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

%description
An abstracted interface to invoking native functions from java

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
rm src/main/java/jnr/ffi/provider/jffi/ARM_64StubCompiler.java
rm src/main/java/jnr/ffi/provider/jffi/AbstractA64StubCompiler.java

# remove all builtin jars
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

# Unnecessary for RPM builds
%pom_remove_parent
%pom_remove_plugin ":maven-javadoc-plugin"

# Port to maven-antrun-plugin 3.0.0
sed -i s/tasks/target/ pom.xml

# don't fail on unused parameters... (TODO: send patch upstream)
sed -i 's|-Werror||' libtest/GNUmakefile

%build
# Sometimes get test failures on non-intel arches
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Tue Oct 25 2022 Mat Booth <mat.booth.wg@bp.renesas.com> - 2.2.12-1
- Update to latest upstream release

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.1.8-15
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.1.8-14
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 05 2021 Mat Booth <mat.booth@redhat.com> - 2.1.8-11
- Allow building with antrun 3.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Mat Booth <mat.booth@redhat.com> - 2.1.8-9
- Fix fallback logic on non-intel architectures

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.1.8-6
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Mat Booth <mat.booth@redhat.com> - 2.1.8-2
- Set the required version of ASM

* Sat Dec 08 2018 Mat Booth <mat.booth@redhat.com> - 2.1.8-1
- Update to latest upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.6-3
- Rebuild to regenerate OSGi manifest after ASM6 upgrade

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Mat Booth <mat.booth@redhat.com> - 2.1.6-1
- Update to latest release, fix FTBFS, re-enable tests

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 2.1.2-3
- Regenerate BRs

* Wed Feb  1 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.2-2
- Add missing build-requires on GCC

* Mon Dec 19 2016 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-1
- Update to upstream 2.1.2.

* Fri Dec 16 2016 Merlin Mathesius <mmathesi@redhat.com> - 2.0.9-2
- Add missing BuildRequires to fix FTBFS (BZ#1405595).

* Mon Apr 18 2016 Alexander Kurtakov <akurtako@redhat.com> 2.0.9-1
- Update to upstream 2.0.9 release.

* Fri Feb 5 2016 Alexander Kurtakov <akurtako@redhat.com> 2.0.6-1
- Update to upstream 2.0.6 release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.4-1
- Update to upstream 2.0.4 and drop unneeded osgification patch/source.

* Tue Jun 23 2015 Roland Grunberg <rgrunber@redhat.com> - 2.0.3-4
- Add missing Import-Package statements to manifest.

* Wed Jun 17 2015 Jeff Johnston <jjohnstn@redhat.com> - 2.0.3-3
- Add proper MANIFEST.MF.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 5 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.3-1
- Update to upstream 2.0.3.
- Skip tests.

* Thu Apr 30 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.2-1
- Update to upstream 2.0.2.

* Thu Feb 19 2015 Michal Srb <msrb@redhat.com> - 2.0.1-3
- Skip tests on arm

* Wed Feb 18 2015 Michal Srb <msrb@redhat.com> - 2.0.1-2
- Build with jffi-native

* Mon Jan 05 2015 Mo Morsi <mmorsi@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 25 2013 Michal Srb <msrb@redhat.com> - 0.7.10-4
- Adapt to current guidelines
- Remove unneeded patch
- Enable tests
- Fix BR

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 06 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.10-2
- Depend on objectweb-asm4, not objectweb-asm.

* Tue Feb 05 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.10-1
- Update to version 0.7.10.
- Switch from ant to maven.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 23 2011 Mo Morsi <mmorsi@redhat.com> - 0.5.10-3
- more updates to conform to fedora guidelines

* Wed Aug 10 2011 Mo Morsi <mmorsi@redhat.com> - 0.5.10-2
- updated to conform to fedora guidelines

* Tue Aug 02 2011 Mo Morsi <mmorsi@redhat.com> - 0.5.10-1
- initial package
