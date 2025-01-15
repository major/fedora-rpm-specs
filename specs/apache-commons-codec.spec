%bcond_with bootstrap

Name:           apache-commons-codec
Version:        1.17.1
Release:        %autorelease
Summary:        Implementations of common encoders and decoders
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-codec/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/commons/codec/source/commons-codec-%{version}-src.tar.gz
# Data in DoubleMetaphoneTest.java originally has an inadmissible license.
# The author gives MIT in e-mail communication.
Source1:        aspell-mail.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
%endif

%description
Commons Codec is an attempt to provide definitive implementations of
commonly used encoders and decoders. Examples include Base64, Hex,
Phonetic and URLs.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C
cp %{SOURCE1} aspell-mail.txt
sed -i 's/\r//' RELEASE-NOTES*.txt LICENSE.txt NOTICE.txt

%mvn_file : commons-codec %{name}
%mvn_alias : commons-codec:commons-codec

%build
%mvn_build -- -Dcommons.osgi.symbolicName=org.apache.commons.codec

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt aspell-mail.txt
%doc RELEASE-NOTES*

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
