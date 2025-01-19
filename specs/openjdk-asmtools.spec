#Definig major and minor because Version allows only '-'
%global major 8.0
%global minor b09
#Using pre-release snapshot versioning from at8 branch
#%%global commit c0e14f4fbe2efdbbb51cd2818880be8fdfdfc634 
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
#%%global commitdate 20230113

Name:           openjdk-asmtools
Version:        %{major}.%{minor}
#Release:        0.6.%%{commitdate}.git%%{shortcommit}%%{?dist}
Release:        9%{?dist}
Summary:        Set of tools used to assemble / disassemble proper and improper Java .class files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/openjdk/asmtools
#If we use regular versioning then Source0 looks as below
Source0:        https://github.com/openjdk/asmtools/archive/%{major}-%{minor}.tar.gz
#As we are using pre-release snapshot versioning, Source0 looks as below
#To download source: spectool -g openjdk-asmtools.spec
#Source0:        https://github.com/openjdk/asmtools/archive/%%{commit}/%%{name}-%%{shortcommit}.tar.xz
Source1:        openjdk-asmtools.in
Source2:        openjdk-asmtools.1

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

#asmtools8 requires jdk16 amd up
BuildRequires:  (java-17-openjdk-devel or java-21-openjdk-devel or java-latest-openjdk-devel)
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  junit5
Requires:  (java-17-headless or java-21-openjdk-headless or java-latest-openjdk-headless)

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
%autosetup -n asmtools-%{major}-%{minor}
#Added to handle pre-release version
#%%autosetup -n asmtools-%{commit}
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
#export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
xmvn -version
# there are two test failures
%mvn_build --xmvn-javadoc --force

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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.b09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 8.0.b09-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.b09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 23 2024 Marian Koncek <mkoncek@redhat.com> - 8.0.b09-6
- Require javapackages-tools at runtime

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.b09-5
- experimental drop of java_home

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.b09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.b09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.b09-1
- bumped to freshly released 8.0.b09
- javadoc reapeared

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.b02.ea-0.6.20230113.gitc0e14f4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 09 2023 Marian Koncek <mkoncek@redhat.com> - 8.0.b02.ea-0.5.20230113.gitc0e14f4
- make br/r more flexible for jdk 17 and up

* Tue May 09 2023 Marian Koncek <mkoncek@redhat.com> - 8.0.b02.ea-0.4.20230113.gitc0e14f4
- Improve summary and description

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.b02.ea-0.3.20230113.gitc0e14f4
- bumped to next RC
- enabled tests
- javadoc disapeared

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.b02.ea-0.2.20221108.git608867a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 10 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.b02.ea-0.1.20221108.git608867a
- bumped to asmtools8

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.b10-0.8.20210610.gitf40a2c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 7.0.b10-0.7.20210610.gitf40a2c0
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 7.0.b10-0.6.20210610.gitf40a2c0
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.b10-0.5.20210610.gitf40a2c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Jayashree Huttanagoudar <jhuttana@redhat.com> - 7.0.b10-0.4.20210610.gitf40a2c0
- Use XMvn javadoc so as to work-around maven-javadoc-plugin issue.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.b10-0.3.20210610.gitf40a2c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Jiri Vanek <jvanek@redhat.com> - 7.0.b10-0.2.20210610.gitf40a2c0
- updated to latest sources
- moved mvngen to prep

* Wed Jan 27 2021 Jayashree Huttanagoudar <jhuttana@redhat.com> - 7.0.b10-0.1.20210122.git7eadbbf
- Initial openjdk-asmtools package for fedora
