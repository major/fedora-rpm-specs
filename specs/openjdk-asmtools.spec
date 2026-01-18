#Definig major and minor because Version allows only '-'
%global major 9.0
%global minor b12.ea.eb1979669

Name:           openjdk-asmtools
Version:        %{major}.0.%{minor}
Release:        1%{?dist}
Summary:        Set of tools used to assemble / disassemble proper and improper Java .class files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/openjdk/asmtools
#If we use regular versioning then Source0 looks as below
Source0:        %{major}-%{minor}.tar.gz
#As we are using pre-release snapshot versioning, Source0 looks as below
#To download source: spectool -g openjdk-asmtools.spec
#Source0:        https://github.com/openjdk/asmtools/archive/%%{commit}/%%{name}-%%{shortcommit}.tar.xz
Source1:        openjdk-asmtools.in
Source2:        openjdk-asmtools.1

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  (java-21-openjdk-devel or java-25-devel or java-latest-openjdk-devel)
BuildRequires:  maven-local-openjdk25
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  junit5
Requires:       java-headless
Requires:       javapackages-tools

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

%package        javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
#This is commented till the version on the master branch is released
%autosetup -n asmtools-upstream
cd maven
sed -i "s|ln -sv|cp -r|g" mvngen.sh
sh mvngen.sh
#%%pom_remove_plugin :maven-javadoc-plugin
#%%pom_remove_plugin :maven-source-plugin
#%%pom_remove_plugin :maven-gpg-plugin
sed "s/<addClasspath.*//" -i pom.xml
sed "s/<<mainClass.*//" -i pom.xml

%build
cd maven
xmvn -version
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
%{_mandir}/man1/openjdk-asmtools.1*

%files javadoc -f maven/.mfiles-javadoc
%doc README.md
%license LICENSE


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0.b12.ea.eb1979669-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

%autochangelog
