Name:           jaxb-fi
Version:        1.2.18
Release:        9%{?dist}
Summary:        Implementation of the Fast Infoset Standard for Binary XML
# jaxb-fi is licensed ASL 2.0 and EDL-1.0 (BSD)
# bundled org.apache.xerces.util.XMLChar.java is licensed ASL 1.1
License:        ASL 2.0 and BSD and ASL 1.1
URL:            https://github.com/eclipse-ee4j/jaxb-fi
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.xml.stream.buffer:streambuffer)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.jaxb:xsom)

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-fastinfoset = %{version}-%{release}
Obsoletes:      glassfish-fastinfoset < 1.2.15-5

# javadoc subpackage is currently not built
Obsoletes:      glassfish-fastinfoset-javadoc < 1.2.15-5

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
%autosetup

pushd code
# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and not required
%pom_remove_parent

# disable unnecessary plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin

# disable parent
%mvn_package :fastinfoset-project __noinstall
popd

%build
pushd code
%mvn_build -s -f -j -- -DbuildNumber=unknown -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
popd

%install
pushd code
%mvn_install
popd

%files -n FastInfoset -f code/.mfiles-FastInfoset
%license LICENSE NOTICE.md
%doc README.md

%files -n FastInfosetRoundTripTests -f code/.mfiles-FastInfosetRoundTripTests
%license LICENSE NOTICE.md

%files -n FastInfosetSamples -f code/.mfiles-FastInfosetSamples
%license LICENSE NOTICE.md

%files -n FastInfosetUtilities -f code/.mfiles-FastInfosetUtilities
%license LICENSE NOTICE.md

%changelog
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

