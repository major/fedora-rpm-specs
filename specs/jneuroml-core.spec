%global pretty_name NeuroML2

# Upstream used this as the release tag:
# https://github.com/NeuroML/jNeuroML/tags
%global gittag NMLv2.0

%global _description %{expand:
This repository contains the NeuroML 2 Schema, the ComponentType definitions in
LEMS and a number of example files in NeuroML 2 and LEMS files for running
simulations.

For more details on LEMS and NeuroML 2 see:

Robert C. Cannon, Padraig Gleeson, Sharon Crook, Gautham Ganapathy, Boris
Marin, Eugenio Piasini and R. Angus Silver, LEMS: A language for expressing
complex biological models in concise and hierarchical form and its use in
underpinning NeuroML 2, Frontiers in Neuroinformatics 2014,
doi:10.3389/fninf.2014.00079
}

Name:           jneuroml-core
Version:        1.6.1
Release:        17%{?dist}
Summary:        The NeuroML 2 Schema and ComponentType definitions in LEMS

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/NeuroML/%{pretty_name}

Source0:        %{url}/archive/%{gittag}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin

%description %_description

# NO javadocs

%package doc
Summary:        NeuroML2 core documentation, schemas, and examples
# bootstrap.css file is ASL 2.0
License:        LGPL-3.0-only AND Apache-2.0

%description doc %_description

%prep
%autosetup -n %{pretty_name}-%{gittag}

# Remove currently unused omv/omt files
rm -fv LEMSexamples/test/.test*


%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.lesser
%doc README.md CONTRIBUTING.md

%files doc
%license LICENSE.lesser
%doc HISTORY.md
%doc examples docs Schemas LEMSexamples NeuroML2CoreTypes


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.1-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.6.1-14
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.6.1-8
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.6.1-7
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.1-3
- Include core types

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.1-1
- Update as per review comments: #1828079
- Remove unneeded file listing
- Remove unused validation files
- Update license for doc subpackage

* Sun Apr 26 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.1-1
- Initial build
