%bcond_with bootstrap

Name:           xz-java
Version:        1.9
Release:        %autorelease
Summary:        Java implementation of XZ data compression
License:        LicenseRef-Fedora-Public-Domain
URL:            https://tukaani.org/xz/java.html
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://tukaani.org/xz/xz-java-%{version}.zip

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  javapackages-local
BuildRequires:  ant
%endif

%description
A complete implementation of XZ data compression in Java.

It features full support for the .xz file format specification version 1.0.4,
single-threaded streamed compression and decompression, single-threaded
decompression with limited random access support, raw streams (no .xz headers)
for advanced users, including LZMA2 with preset dictionary.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -p1 -C

%mvn_file : %{name} xz

%build
# During documentation generation the upstream build.xml tries to download
# package-list from oracle.com. Create a dummy package-list to prevent that.
mkdir -p extdoc && touch extdoc/package-list

%ant -Dsourcever=8 maven

%install
%mvn_artifact build/maven/xz-%{version}.pom build/jar/xz.jar

%mvn_install -J build/doc

%files -f .mfiles
%doc README THANKS
%license COPYING

%files javadoc -f .mfiles-javadoc
%license COPYING

%changelog
%autochangelog
