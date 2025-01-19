Summary: %{nice_name} is a powerful open-source tool that parses and evaluates algebraic and mathematical expressions
%global nice_name ParserNG
Name: parserng
Version: 0.1.9
Release: 9%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/gbenroscience/ParserNG
# tarred cloned repo without hidden files and without idea iml
# usptream do not tag, but uses maven versionining
# so this is f619fad1fefa21116bab4a0abba2dd0ebe719e45
# which set pom to 0.1.9 and moved it to maven repos
# git clone https://github.com/gbenroscience/ParserNG &&  cd ParserNG  && git checkout f619fad1fefa21116bab4a0abba2dd0ebe719e45 && tar -cJf parserng-0.1.9.tar.xz *
Source0: %{name}-%{version}.tar.xz
Source1: parserng
Patch1: jdk21rounding.patch

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires: maven-local
BuildRequires: junit5
BuildRequires: ant-junit5
BuildRequires: junit
BuildRequires: ant-junit
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-junit5
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
BuildRequires: maven-clean-plugin
BuildRequires: java-devel
Requires: java-headless
Provides: ParserNG
Provides: parser-ng

%description
Rich and Performant, Cross Platform Java Library(100% Java)...
Now allows the differentiation function to be differentiated with
respect to any variable(not just x).  Next to math.Main main cmdline entry point 
also parser.MathExpression and parser.cmd.ParserCmd  are here for cmdline service

%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -c %{name}-%{version}
%patch -P1 -p1
for x in `find | grep pom.xml` ; do
    sed "s;<maven.compiler.source>.*7.*;<maven.compiler.source>8</maven.compiler.source>;g" -i $x;
    sed "s;<maven.compiler.target>.*7.*;<maven.compiler.target>8</maven.compiler.target>;g" -i $x;
done

%build
%pom_remove_plugin :maven-jar-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%mvn_build

%install
%mvn_install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/
chmod 755 $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

%files -f .mfiles
%license LICENSE
%{_bindir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.9-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0.1.9-6
- Rebuilt for java-21-openjdk as system jdk
- fixed source/target
- added patch to cover slightly different rounding on jdk21

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Jiri Vanek <jvanek@redhat.com> - 0.1.8-1
- bumped sources to upstream rc candidate

