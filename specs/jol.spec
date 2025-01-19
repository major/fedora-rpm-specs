Name:           jol
Version:        0.17
Release:        7%{?dist}
Summary:        Java Object Layout

# GPL-2.0-only: the project as a whole
# GPL-2.0-only WITH Classpath-exception-2.0:
#   Every file containing the following text: "Oracle designates this
#   particular file as subject to the "Classpath" exception as provided by
#   Oracle in the LICENSE file that accompanied this code.
# BSD-3-Clause: jol-samples/ (not shipped in any binary RPM)
License:        GPL-2.0-only AND GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://openjdk.java.net/projects/code-tools/jol/
Source0:        https://github.com/openjdk/jol/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sf.jopt-simple:jopt-simple)
BuildRequires:  mvn(org.ow2.asm:asm)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%global _desc %{expand:
JOL (Java Object Layout) is a tiny toolbox to analyze Java object
layouts.  These tools use Unsafe, JVMTI, and Serviceability Agent (SA)
heavily to decode the actual object layout, footprint, and references.
This makes JOL much more accurate than other tools relying on heap dumps,
specification assumptions, etc.}

%description %_desc

%{?javadoc_package}

%package        parent
Summary:        Java Object Layout parent POM

%description    parent %_desc

This package contains the parent POM for JOL.

%package        core
Summary:        Java Object Layout core classes

%description    core %_desc

This package contains the core classes for JOL.

%package        cli
Summary:        Java Object Layout command line interface
Requires:       %{name}-core = %{version}-%{release}

%description    cli %_desc

This package contains a command line interface to JOL.

%prep
%autosetup

# Unnecessary plugins for an RPM build
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-license-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-source-plugin

# We do not need benchmarks or samples
%pom_disable_module jol-benchmarks
%pom_disable_module jol-samples

%build
%mvn_build -s

%install
%mvn_install

%files parent -f .mfiles-jol-parent
%license LICENSE

%files core -f .mfiles-jol-core
%doc README.md
%license LICENSE

%files cli -f .mfiles-jol-cli

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0.17-5
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 28 2023 Jerry James <loganjerry@gmail.com> - 0.17-1
- Version 0.17
- Generate javadocs

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Jerry James <loganjerry@gmail.com> - 0.16-6
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0.16-5
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.16-4
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Jerry James <loganjerry@gmail.com> - 0.16-2
- Add workaround for bz 1981486

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jerry James <loganjerry@gmail.com> - 0.16-1
- Version 0.16

* Wed Mar 31 2021 Jerry James <loganjerry@gmail.com> - 0.15-1
- Version 0.15

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Jerry James <loganjerry@gmail.com> - 0.14-1
- Initial RPM
