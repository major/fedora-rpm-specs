%bcond bootstrap 0

Name:           plexus-cipher
Version:        2.0
Release:        %autorelease
Summary:        Plexus encryption/decryption component
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-cipher
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.0-28

BuildSystem:    maven
BuildOption:    usesJavapackagesBootstrap
BuildOption:    xmvnToolchain "openjdk21"
BuildOption:    mavenOption "-DjavaVersion=8"
BuildOption:    artifact ":plexus-cipher" {
BuildOption:        file "plexus/plexus-cipher"
BuildOption:        alias "org.sonatype.plexus:"
BuildOption:    }

%description
Plexus Cipher is a Java-based library from the Plexus project,
primarily used by Apache Maven to encrypt and decrypt sensitive data
in configuration files, such as passwords stored in settings.xml.
It enables developers to securely store encrypted credentials instead
of plain-text secrets when accessing Maven repositories or other
protected services.

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%changelog
%autochangelog
