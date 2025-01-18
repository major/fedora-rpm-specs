Name:      brazil
Version:   2.3
Release:   39%{?dist}
Summary:   Extremely small footprint Java HTTP stack
License:   SPL-1.0
URL:       https://github.com/mbooth101/brazil

Source0:   https://github.com/mbooth101/brazil/archive/%{name}-%{version}.tar.gz

# upsteam's build script doesn't build javadocs, so use our own, better script - it is not better, pls fix upstream pom.xm!
Source2:   brazil-build.xml

# https://github.com/mbooth101/brazil/pull/1
Patch0:   jdk17.patch

BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:    java-devel
BuildRequires:    jpackage-utils
BuildRequires:    ant
Requires:         java-headless
Requires:         jpackage-utils

%description
Brazil is as an extremely small footprint HTTP stack and flexible architecture 
for adding URL-based interfaces to arbitrary applications and devices from Sun 
Labs. This package contains the core set of classes that are not dependent on 
any other external Java libraries.

%package javadoc
Summary:   Java-docs for %{name}

%description javadoc
API documentation for %{name}.

%package demo
Summary:   Demos for %{name}
Requires:  %{name} = %{version}-%{release}
Requires:  tcl

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%patch -P0 -p1
 
# fix permissions and interpreter in sample scripts
grep -lR -e ^\#\!/usr/sfw/bin/tclsh8.3 samples | xargs sed --in-place "s|/usr/sfw/bin/tclsh8.3|/usr/bin/tclsh|"
grep -lR -e ^\#\!/usr/bin/tclsh        samples | xargs chmod 755
grep -lR -e ^\#\!/bin/sh               samples | xargs chmod 755

%build
cp -p %{SOURCE2} build.xml
ant all

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# samples
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr samples %{buildroot}%{_datadir}/%{name}

%files
%doc README.md srcs/license.terms
%{_javadir}/%{name}.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%files demo
%doc %{_datadir}/%{name}/samples/README
%{_datadir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 15 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3-37
- convert license to SPDX

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.3-36
- Rebuilt for java-21-openjdk as system jdk

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.3-30
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.3-29
- Rebuilt for java-17-openjdk as system jdk
- commented about "our own, better script - it is not better, pls fix upstream pom.xm"
- added patch jdk17.patch
- preffixed keyword yeald and bumped source/target
- https://github.com/mbooth101/brazil/pull/1

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3-24
- Set javac source and target to 1.8 to fix Java 11 builds.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.3-23
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Mat Booth <fedora@matbooth.co.uk> - 2.3-12
- Tidy up spec for latest guidelines
- Drop versioned jars, rhbz #1022086
- Require java-headless, rhbz #1067988
- New upstream, drop no longer needed patches

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Mat Booth <fedora@matbooth.co.uk> 2.3-5
- Drop support for GCJ ahead of time compilation.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Apr 18 2008 Mat Booth <fedora@matbooth.co.uk> 2.3-3
- Minor grammatical corrections.

* Sun Apr 13 2008 Mat Booth <fedora@matbooth.co.uk> 2.3-2
- Updated package for new Java guidelines.
- Spec now builds a demo package containing the samples.

* Wed Dec 26 2007 Mat Booth <fedora@matbooth.co.uk> 2.3-1
- Initial release.
