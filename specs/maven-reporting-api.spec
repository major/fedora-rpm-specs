Name:           maven-reporting-api
Version:        4.1.0
Release:        %autorelease
Epoch:          1
Summary:        API to manage report generation
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-reporting-api
VCS:            git:https://github.com/apache/maven-reporting-api.git

Source0:        https://archive.apache.org/dist/maven/reporting/%{name}-%{version}-source-release.zip
# Source file signature
Source1:        https://archive.apache.org/dist/maven/reporting/%{name}-%{version}-source-release.zip.asc
# Apache Maven public key
Source2:        https://downloads.apache.org/maven/KEYS

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%if 0%{?rhel} && 0%{?rhel} <= 10
BuildRequires:  maven-local-openjdk21
%else
BuildRequires:  maven-local-openjdk25
%endif
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  openpgpverify

%{?javadoc_package}

# Enable the upstream test suite (disabled by default in %%mvn_build)
%global mvn_test_opts -DskipTests=false

%description
API to manage report generation.  Maven-reporting-api is included in the Maven
2.x core distribution, but was moved to shared components to achieve report
decoupling from the Maven 3 core.

%prep
%{openpgpverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup

# Fix end of line encoding
sed -i.orig 's/\r//' README.md
touch -r README.md.orig README.md
rm README.md.orig

%build
%mvn_build

%install
%mvn_install

%check
%mvn_build

%files -f .mfiles
%doc README.md
%license LICENSE NOTICE

%changelog
%autochangelog
