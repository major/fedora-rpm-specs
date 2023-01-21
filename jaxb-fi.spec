Name:           jaxb-fi
Version:        2.1.0
Release:        2%{?dist}
Summary:        Implementation of the Fast Infoset Standard for Binary XML
# jaxb-fi is licensed ASL 2.0 and EDL-1.0 (BSD)
# bundled org.apache.xerces.util.XMLChar.java is licensed ASL 1.1
License:        ASL 2.0 and BSD and ASL 1.1
URL:            https://github.com/eclipse-ee4j/jaxb-fi
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch1:         0001-Port-to-jaxb-xsom-4.0.1.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.xml.stream.buffer:streambuffer)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.jaxb:xsom)

%description
Fast Infoset Project, an Open Source implementation of the Fast Infoset
Standard for Binary XML.

The Fast Infoset specification (ITU-T Rec. X.891 | ISO/IEC 24824-1)
describes an open, standards-based "binary XML" format that is based on
the XML Information Set.

%package -n FastInfoset
Summary:        FastInfoset
%description -n FastInfoset
%{summary}.

%package -n FastInfosetRoundTripTests
Summary:        FastInfoset Roundtrip Tests
%description -n FastInfosetRoundTripTests
%{summary}.

%package -n FastInfosetSamples
Summary:        FastInfoset Samples
%description -n FastInfosetSamples
%{summary}.

%package -n FastInfosetUtilities
Summary:        FastInfoset Utilities
%description -n FastInfosetUtilities
%{summary}.

%prep
%setup -q
%patch1 -p1

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%mvn_package :fastinfoset-project __noinstall

%build
# Javadoc fails: error: too many module declarations found
%mvn_build -s -j

%install
%mvn_install

%files -n FastInfoset -f .mfiles-FastInfoset
%license LICENSE NOTICE.md
%doc README.md

%files -n FastInfosetRoundTripTests -f .mfiles-FastInfosetRoundTripTests
%license LICENSE NOTICE.md

%files -n FastInfosetSamples -f .mfiles-FastInfosetSamples
%license LICENSE NOTICE.md

%files -n FastInfosetUtilities -f .mfiles-FastInfosetUtilities
%license LICENSE NOTICE.md

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Marian Koncek <mkoncek@redhat.com> - 2.1.0-1
- Update to upstream version 2.1.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.2.18-8
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.2.18-7
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 29 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.2.18-5
- Enable roundtrip-tests and samples module
- Enable singleton package
- Enable javadoc package

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Dogtag PKI Team <pki-devel@redhat.com> - 1.2.18-3
- Disable tests

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.18-1
- Initial package renamed from glassfish-fastinfoset.
