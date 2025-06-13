Name:           dola
Version:        1.0.0
Release:        %autorelease
Summary:        Declarative system for Java RPM packaging
License:        Apache-2.0
URL:            https://github.com/mizdebsk/dola
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source:         https://github.com/mizdebsk/dola/releases/download/%{version}/dola-%{version}.tar.zst

BuildRequires:  lujavrite
BuildRequires:  maven-local
BuildRequires:  mvn(io.kojan:kojan-parent:pom:)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.maven:maven-model:4.0.0-rc-3)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-api:5.0.0)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-core:5.0.0)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.ow2.asm:asm)

Requires:       java-21-openjdk-headless
Requires:       lujavrite
Requires:       rpm-build
Requires:       xmvn5-minimal
Requires:       xmvn5-toolchain-openjdk21
Requires:       xmvn5-tools
Requires:       xmvn5-mojo
Requires:       dola-gleaner
Requires:       dola-transformer

%description
Dola is a modern, declarative system for RPM packaging of Maven-based
Java projects.  It enables package maintainers to entirely avoid
writing `%%prep`, `%%build`, or `%%install` scriptlets in RPM spec files.
Instead, all build configuration is expressed using BuildOption tags
(introduced in RPM 4.20), resulting in cleaner, more maintainable spec
files.

%prep
%autosetup -p1 -C

%build
%mvn_build -j -- -P\!quality

%install
%mvn_install
install -D -p -m 644 dola-bsx/src/main/lua/dola-bsx.lua %{buildroot}%{_rpmluadir}/dola-bsx.lua
install -D -p -m 644 dola-dbs/src/main/lua/dola-dbs.lua %{buildroot}%{_rpmluadir}/dola-dbs.lua
install -D -p -m 644 dola-generator/src/main/lua/dola-generator.lua %{buildroot}%{_rpmluadir}/dola-generator.lua
install -D -p -m 644 dola-bsx/src/main/rpm/macros.dola-bsx %{buildroot}%{_rpmmacrodir}/macros.dola-bsx
install -D -p -m 644 dola-dbs/src/main/rpm/macros.dola-dbs %{buildroot}%{_rpmmacrodir}/macros.zzz-dola-dbs
install -D -p -m 644 dola-generator/src/main/rpm/macros.dola-generator %{buildroot}%{_rpmmacrodir}/macros.dola-generator
install -D -p -m 644 dola-generator/src/main/rpm/macros.dola-generator-etc %{buildroot}%{_sysconfdir}/rpm/macros.dola-generator-etc
install -D -p -m 644 dola-generator/src/main/rpm/dolagen.attr %{buildroot}%{_fileattrsdir}/dolagen.attr
install -D -p -m 644 dola-bsx/src/main/conf/dola-bsx.conf %{buildroot}%{_javaconfdir}/dola/classworlds/00-dola-bsx.conf
install -D -p -m 644 dola-dbs/src/main/conf/dola-dbs.conf %{buildroot}%{_javaconfdir}/dola/classworlds/04-dola-dbs.conf
install -D -p -m 644 dola-generator/src/main/conf/dola-generator.conf %{buildroot}%{_javaconfdir}/dola/classworlds/03-dola-generator.conf
install -D -p -m 644 dola-rpm-api/src/main/conf/dola-rpm-api.conf %{buildroot}%{_javaconfdir}/dola/classworlds/02-dola-rpm-api.conf

%files -f .mfiles
%{_rpmluadir}/*
%{_rpmmacrodir}/*
%{_fileattrsdir}/*
%{_sysconfdir}/rpm/*
%{_javaconfdir}/*
%license LICENSE NOTICE
%doc README.md

%changelog
%autochangelog
