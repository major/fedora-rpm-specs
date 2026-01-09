%global srcname academic-file-converter

Name:           academic-admin
Version:        0.11.2
Release:        %autorelease
Summary:        Admin tool for the Academic website builder

License:        MIT
URL:            https://github.com/BuildLore/%{srcname}
Source:         https://github.com/BuildLore/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         academic-admin-0.11.2-dependencies.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
An admin tool for the Academic website builder.}

%description %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n academic-admin
%doc README.md
%license LICENSE.md
%{python3_sitelib}/academic/
%{python3_sitelib}/academic-%{version}.dist-info/
%{_bindir}/*

%changelog
%autochangelog
