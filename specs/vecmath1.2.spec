Name:           vecmath1.2
Version:        1.14
Release:        38%{?dist}
Summary:        Free version of vecmath from the Java3D 1.2 specification
License:        MIT
URL:            http://www.objectclub.jp/download/vecmath_e
Source0:        http://www.objectclub.jp/download/files/vecmath//%{name}-%{version}.tar.gz
Patch0:         vecmath1.2-1.14-javadoc-fixes.patch
Patch1:         vecmath1.2-1.14-javac-1.8.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires: make
BuildRequires:  java-devel >= 1:1.6.0
Requires:       java-headless >= 1:1.6.0
Requires:       javapackages-filesystem
# Necessary due to architecture change to noarch
Obsoletes:      %{name} < %{version}-%{release}

%description
This is an unofficial implementation (java source code) of the javax.vecmath
package specified in the Java(TM) 3D API 1.2 . The package includes classes
for 3-space vector/point, 4-space vector, 4x4, 3x3 matrix, quaternion,
axis-angle combination and etc. which are often utilized for computer graphics
mathematics. Most of the classes have single and double precision versions.
Generic matrices' LU and SV decomposition are also there.


%package javadoc
Summary:        Javadoc for %{name}
# Necessary due to architecture change to noarch
Obsoletes:      %{name}-javadoc < %{version}-%{release}

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
find -name *.jar -delete
find -name *.class -delete


%build
make -f Makefile.unix all docs
pushd classes
jar cf ../%{name}.jar .
popd


%install
# jar
install -D -m 644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/
cp -r docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/


%files
%doc README CHANGES
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.14-36
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.14-31
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.14-30
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Fabio Valentini <decathorpe@gmail.com> - 1.14-25
- Set javac source / target version to 1.8 to fix issues on Java 11.

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.14-24
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Hans de Goede <hdegoede@redhat.com> - 1.14-22
- Drop obsolete [Build]Requires: jpackage-utils
- Drop -javadoc sub-package Requires on the main package

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Hans de Goede <hdegoede@redhat.com> - 1.14-14
- Fix FTBFS due to javadoc errors

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.14-11
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 28 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.14-5
- Modernized spec file to conform to Java guidelines.
- Removed clash with vecmath package.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.14-2
- Autorebuild for GCC 4.3

* Sat Sep  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.14-1
- Initial Fedora package
