Name:           java-jd-decompiler
Version:        1.1.3
Release:        12%{?dist}
Summary:        JAVA library having JAVA decompiler of "Java Decompiler project"

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/java-decompiler/jd-core
Source0:        https://github.com/java-decompiler/jd-core/archive/refs/tags/v%{version}.tar.gz
Source1:        pom.xml
Source2:        Main.java
Source3:        java-jd-decompiler
Source4:        java-jd-decompiler.1

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  java-devel
BuildRequires:  maven-local
BuildRequires:  maven-jar-plugin

Requires:       %{name}-core = %{version}-%{release}

# Explicit requires for javapackages-tools since java-jd-decompiler
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description
This is a launcher for using %{name}-core library from CLI

%package        javadoc    
Summary:        Javadoc for %{name} 
    
%description javadoc    
This package contains the API documentation for %{name}.

%package        core    
Summary:        Main library with decompiler
    
%description    core
This standalone JAVA library has JAVA decompiler of "Java Decompiler project".
It support Java 1.8.0 to Java 12.0.It has support for the Lambda expressions,
method references and default methods.JD-Core is the engine of JD-GUI.


%global debug_package %{nil}

%prep
%setup -q -n jd-core-%{version}
cp %{SOURCE1} pom.xml

%build
%mvn_build -f
javac -d $PWD -cp target/jd-core-%{version}.jar %{SOURCE2}
jar -cvf launcher.jar *.class  
rm -v *.class

%install
%mvn_install
mkdir -p  $RPM_BUILD_ROOT/%{_mandir}/man1

install -d -m 755 $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT/%{_bindir}
cp -v launcher.jar $RPM_BUILD_ROOT/%{_javadir}/java-jd-decompiler
cp -v %{SOURCE4} $RPM_BUILD_ROOT/%{_mandir}/man1

%files
%license LICENSE    
%doc README.md
%{_bindir}/java-jd-decompiler
%{_javadir}/java-jd-decompiler/launcher.jar
%{_mandir}/man1/java-jd-decompiler.1*

%files core -f .mfiles
%license LICENSE    
%doc README.md


%files javadoc -f .mfiles-javadoc
%license LICENSE    
%doc README.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.3-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 22 2024 Marian Koncek <mkoncek@redhat.com> - 1.1.3-9
- Add Requires on javapackages-tools

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.1.3-8
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.1.3-2
- Rebuilt for Drop i686 JDKs

* Mon Dec 13 2021 Jayashree Huttanagoudar <jhuttana@redhat.com> - 1.1.3-1
- Initial java-decompiler package for fedora
