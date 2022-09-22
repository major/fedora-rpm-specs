%global cli_tool cplc

Name:           classpathless-compiler
Version:        2.1.1
Release:        5%{?dist}
Summary:        Tool for recompiling java sources with customizable class providers
License:        ASL 2.0
URL:            https://github.com/mkoncek/classpathless-compiler
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/mkoncek/classpathless-compiler/archive/refs/tags/%{version}.tar.gz

BuildRequires:  javapackages-extra
BuildRequires:  maven-local
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.ow2.asm:asm-tree)

Requires:       java-headless
Requires:       beust-jcommander
Requires:       javapackages-tools

%description
Classpathless compiler (CPLC) is a compiler wrapper used for compiling java
sources with customizable class providers. This tool works differently from the
traditional java compiler in that it doesn't use provided classpath but instead
pulls dependencies using an API.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n classpathless-compiler-%{version}

%java_remove_annotations -n SuppressFBWarnings

%pom_remove_dep :spotbugs-annotations

%pom_remove_plugin :maven-assembly-plugin impl
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin

%build
%mvn_build

%install
%mvn_install

%jpackage_script io.github.mkoncek.classpathless.Tool "" "" classpathless-compiler/classpathless-compiler:classpathless-compiler/classpathless-compiler-api:classpathless-compiler/classpathless-compiler-util:beust-jcommander %{cli_tool}

%files -f .mfiles
%{_bindir}/%{cli_tool}

%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Marian Koncek <mkoncek@redhat.com> - 2.1.1-4
- Add ExclusiveArch field

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.1.1-3
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Marian Koncek <mkoncek@redhat.com> - 2.1.1-1
- Update to upstream version 2.1.1

* Tue Dec 14 2021 Marian Koncek <mkoncek@redhat.com> - 2.1-1
- Update to upstream version 2.1

* Sun Nov 28 2021 Marian Koncek <mkoncek@redhat.com> - 2.0-1
- Update to upstream version 2.0

* Thu Jul 22 2021 Marian Koncek <mkoncek@redhat.com> - 1.4-1
- Update to upstream version 1.4

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Marian Koncek <mkoncek@redhat.com> - 1.3-1
- Initial release
