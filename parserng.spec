Summary: %{nice_name} is a powerful open-source tool that parses and evaluates algebraic and mathematical expressions
%global nice_name ParserNG
Name: parserng
Version: 0.1.8
Release: 2%{?dist}
License: ASL 2.0
URL: https://github.com/gbenroscience/ParserNG
# tarred cloned repo without hidden files and without idea iml
# usptream do not tag, but uses maven versionining
# so this is 1c0ecd8088b18111e44e1291b41606b46c7d8aa5
# which set pom to 0.1.8 and moved it to maven repos
Source0: %{name}-%{version}.tar.xz
Source1: parserng

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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Jiri Vanek <jvanek@redhat.com> - 0.1.8-1
- bumped sources to upstream rc candidate

