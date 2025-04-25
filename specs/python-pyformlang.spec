Name:           python-pyformlang
Version:        1.0.11
Release:        %autorelease
Summary:        A python framework for formal grammars

License:        MIT
URL:            https://github.com/Aunsiels/pyformlang
Source:         %{pypi_source pyformlang}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)


%global _description %{expand:
A python framework for formal grammars.}

%description %_description

%package -n     python3-pyformlang
Summary:        %{summary}

%description -n python3-pyformlang %_description


%prep
%autosetup -p1 -n pyformlang-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pyformlang


%check
%pyproject_check_import
%pytest


%files -n python3-pyformlang -f %{pyproject_files}


%changelog
%autochangelog
