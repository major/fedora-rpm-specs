Name:           jol
Version:        0.16
Release:        6%{?dist}
Summary:        Java Object Layout

License:        GPLv2 with exceptions
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

# Uncomment this once javadocs can be generated again
# See https://github.com/fedora-java/xmvn/issues/58
#%%{?javadoc_package}

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

# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1981486
%pom_add_dep org.apache.commons:commons-lang3:3.12.0:test

# Build for JDK 1.8
sed -i 's/1\.7/1.8/' pom.xml

%build
# Skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -s -j

%install
%mvn_install

%files parent -f .mfiles-jol-parent
%license LICENSE

%files core -f .mfiles-jol-core
%doc README.md
%license LICENSE

%files cli -f .mfiles-jol-cli

%changelog
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
