%global forgeurl https://github.com/inducer/pycparserext
Version:        2026.1
%forgemeta

Name:           python-pycparserext
Release:        %autorelease
Summary:        Extensions for pycparser

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%global _description %{expand:
Extended functionality for Eli Bendersky's pycparser, in particular support
for parsing GNU extensions and OpenCL.}

%description %_description

%package -n     python%{python3_pkgversion}-pycparserext
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pycparserext %_description


%prep
%autosetup -p1 -n pycparserext-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pycparserext


%check
%pyproject_check_import
%pytest


%files -n python%{python3_pkgversion}-pycparserext -f %{pyproject_files}


%changelog
%autochangelog
