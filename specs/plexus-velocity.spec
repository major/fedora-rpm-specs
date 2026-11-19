Name:           plexus-velocity
Version:        2.4.0
Release:        %autorelease
Summary:        Plexus Velocity Component
License:        Apache-2.0
URL:            https://codehaus-plexus.github.io/plexus-velocity/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/codehaus/plexus/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        https://repo1.maven.org/maven2/org/codehaus/plexus/%{name}/%{version}/%{name}-%{version}-source-release.zip.asc
# Apache Maven public key
Source2:        https://downloads.apache.org/maven/KEYS
Source3:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         0001-pin-deps-to-maven-local-versions.patch

%if 0%{?rhel} && 0%{?rhel} <= 10
BuildRequires:  maven-local-openjdk21
%else
BuildRequires:  maven-local-openjdk25
%endif
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.velocity:velocity-engine-core)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  openpgpverify

%description
This package provides Plexus Velocity component - a wrapper for
Apache Velocity template engine, which allows easy use of Velocity
by applications built on top of Plexus container.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%{openpgpverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%setup -q
%patch -p1 -P0

find -name '*.jar' -delete

cp -p %{SOURCE3} LICENSE

%build
%mvn_build -- -DskipTests

%check
# Upstream test uses @PlexusTest (plexus-testing) rather than sisu InjectedTest,
# so the suite runs cleanly in both maven-local-openjdk21 (EPEL 10) and
# maven-local-openjdk25 (Fedora).
%mvn_build test

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
%autochangelog
