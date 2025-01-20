%global         srcname         extruct
%global         forgeurl        https://github.com/scrapinghub/extruct
Version:        0.18.0
%global         tag             %{version}
%forgemeta

Name:           python-%{srcname}
Release:        2%{?dist}
Summary:        Extract embedded metadata from HTML markup

License:        BSD-3-Clause
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

BuildArch: noarch

%global _description %{expand:
extruct is a library for extracting embedded metadata from HTML markup.

Currently, extruct supports:

- W3C's HTML Microdata
- embedded JSON-LD
- Microformat via mf2py
- Facebook's Open Graph
- (experimental) RDFa via rdflib
- Dublin Core Metadata (DC-HTML-2003)
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname} -L

%check 
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%doc AUTHORS
%doc HISTORY.rst
%license LICENSE
%{_bindir}/extruct

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 10 2024 Benson Muite <benson_muite@emailplus.org> - 0.18.0-1
- Update to 0.18.0

* Fri Oct 18 2024 Benson Muite <benson_muite@emailplus.org> - 0.17.0-1
- Initial packaging
