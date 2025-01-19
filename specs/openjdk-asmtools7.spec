#Definig major and minor because Version allows only '-'
%global major 7.0
%global minor b10
#Using pre-release snapshot versioning
%global commit f40a2c014cfd32eb6cc1e1c6c4264a0411fe0415
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20210610

%global project_name openjdk-asmtools

Name:           %{project_name}7
Version:        %{major}.%{minor}
Release:        0.15.%{commitdate}.git%{shortcommit}%{?dist}
Summary:        Set of tools used to assemble / disassemble proper and improper Java .class files for JDK version 11 and lesser

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/openjdk/asmtools
#If we use regular versioning then Source0 looks as below
#Source0:        https://github.com/openjdk/%%{name}/archive/%%{major}-%%{minor}.tar.gz
#As we are using pre-release snapshot versioning, Source0 looks as below
#To download source: spectool -g openjdk-asmtools.spec
Source0:        https://github.com/openjdk/asmtools/archive/%{commit}/%{project_name}-%{shortcommit}.tar.xz
Source1:        openjdk-asmtools7.in
Source2:        openjdk-asmtools7.1

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  java-devel
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-jar-plugin

# Explicit requires for javapackages-tools since scripts
# use /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description
AsmTools helps develop tools to create proper and improper Java .class files.
Aids various Java .class based testing and OpenJDK development applications.
Asmtools supports latest class file formats, in lock-step with JDK development.
AsmTools consist of a set of (Java class file) assembler/dis-assemblers:
* Jasm/Jdis:
An assembler language to provide Java-like declaration of member signatures,
providing Java VM specification compliant mnemonics for byte-code instructions.
* JCod/JDec:
An assembler language to provide byte-code containers of class-file constructs.

This version works with JDK version 11 and lesser.

%package        javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
#This is commented till the version on the master branch is released
#%%setup -q -n asmtools-%%{version}
#Added to handle pre-release version
%autosetup -n asmtools-%{commit}
cd maven
sed -i "s|ln -sv|cp -r|g" mvngen.sh
sh mvngen.sh
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-gpg-plugin
sed "s/<addClasspath.*//" -i pom.xml
sed "s/<<mainClass.*//" -i pom.xml

%build
cd maven
%mvn_build --xmvn-javadoc

%install
rm -rf $RPM_BUILD_ROOT
pushd maven
%mvn_install
popd

mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
#!/bin/sh
for launcher in "" "-jasm" "-jdis" "-jcoder" "-jdec" "-jcdec"; do
  switch=`echo $launcher |sed "s/-//"`
  cat %{SOURCE1} | sed "s/@SCD@/$switch/"  > $RPM_BUILD_ROOT%{_bindir}/%{name}$launcher
done
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/

%files -f maven/.mfiles
%license LICENSE
%doc README.md
%attr(755, root, -) %{_bindir}/*
%{_mandir}/man1/openjdk-asmtools7.1*

%files javadoc -f maven/.mfiles-javadoc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.b10-0.15.20210610.gitf40a2c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 7.0.b10-0.14.20210610.gitf40a2c0
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.b10-0.13.20210610.gitf40a2c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 23 2024 Marian Koncek <mkoncek@redhat.com> - 7.0.b10-0.12.20210610.gitf40a2c0
- Require javapackages-tools at runtime

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 7.0.b10-0.11.20210610.gitf40a2c0
- Rebuilt for java-21-openjdk as system jdk

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.b10-0.10.20210610.gitf40a2c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.b10-0.9.20210610.gitf40a2c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.b10-0.8.20210610.gitf40a2c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 09 2023 Marian Koncek <mkoncek@redhat.com> - 7.0.b10-0.7.20210610.gitf40a2c0
- Improve summary and description

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.b10-0.6.20210610.gitf40a2c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 08 2021 Jayashree Huttanagoudar <jhuttana@redhat.com> - 7.0.b10-0.4.20210610.gitf40a2c0
- Use XMvn javadoc so as to work-around maven-javadoc-plugin issue.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.b10-0.3.20210610.gitf40a2c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Jiri Vanek <jvanek@redhat.com> - 7.0.b10-0.2.20210610.gitf40a2c0
- updated to latest sources
- moved mvngen to prep

* Wed Jan 27 2021 Jayashree Huttanagoudar <jhuttana@redhat.com> - 7.0.b10-0.1.20210122.git7eadbbf
- Initial openjdk-asmtools package for fedora
