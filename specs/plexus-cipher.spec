%bcond_with bootstrap

Name:           plexus-cipher
Version:        2.0
Release:        %autorelease
Summary:        Plexus Cipher: encryption/decryption Component
License:        Apache-2.0
# project moved to GitHub and it looks like there is no official website anymore
URL:            https://github.com/codehaus-plexus/plexus-cipher
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
%endif

%description
Plexus Cipher: encryption/decryption Component

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C
%mvn_file : plexus/%{name}
%mvn_alias org.codehaus.plexus: org.sonatype.plexus:

%build
%mvn_build -- -DjavaVersion=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
