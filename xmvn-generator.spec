%global debug_package %{nil}
%bcond_with bootstrap

Name:           xmvn-generator
Version:        1.2.1
Release:        2%{?dist}
Summary:        RPM dependency generator for Java
License:        Apache-2.0
URL:            https://github.com/fedora-java/xmvn-generator
ExclusiveArch:  %{java_arches}

Source0:        https://github.com/fedora-java/xmvn-generator/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  rpm-devel
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif

Requires:       rpm-build
Requires:       lujavrite
Requires:       java-17-openjdk-headless

%description
XMvn Generator is a dependency generator for RPM Package Manager
written in Java and Lua, that uses LuJavRite library to call Java code
from Lua.

%{?javadoc_package}

%prep
%setup -q
%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install
install -D -p -m 644 src/main/lua/xmvn-generator.lua %{buildroot}%{_rpmluadir}/xmvn-generator.lua
install -D -p -m 644 src/main/rpm/macros.xmvngen %{buildroot}%{_rpmmacrodir}/macros.xmvngen
install -D -p -m 644 src/main/rpm/macros.xmvngenhook %{buildroot}%{_sysconfdir}/rpm/macros.xmvngenhook
install -D -p -m 644 src/main/rpm/xmvngen.attr %{buildroot}%{_fileattrsdir}/xmvngen.attr

%files -f .mfiles
%{_rpmluadir}/*
%{_rpmmacrodir}/*
%{_fileattrsdir}/*
%{_sysconfdir}/rpm/*
%license LICENSE NOTICE
%doc README.md

%changelog
* Fri Mar 17 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-2
- Enable javadoc package

* Mon Mar 13 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-1
- Update to upstream version 1.2.1

* Fri Mar 10 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-1
- Update to upstream version 1.2.0

* Mon Mar 06 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.0-1
- Update to upstream version 1.1.0

* Mon Mar 06 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-1
- Initial packaging
