Name:           python-deepl
Version:        1.27.0
Release:        %autorelease
Summary:        Python library for the DeepL API

License:        MIT
URL:            https://github.com/DeepLcom/deepl-python
Source:         %{pypi_source deepl}

BuildSystem:    pyproject
BuildOption(install):  -l deepl
BuildOption(generate_buildrequires): -x keyring

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  crudini

%global _description %{expand:
The DeepL Python library offers a convenient way for applications
written in Python to interact with the DeepL API. We intend to support all API
functions with the library, though support for new features may be added to the
library after they’re added to the API.}

%description %_description

%package -n     python3-deepl
Summary:        %{summary}

%description -n python3-deepl %_description

%prep -a
# relax the deps
crudini --set pyproject.toml tool.poetry.dependencies keyring '{version = ">=25.7.0", optional = true}'

%pyproject_extras_subpkg -n python3-deepl keyring

%check
%pyproject_check_import

%files -n python3-deepl -f %{pyproject_files}
%{_bindir}/deepl
%license LICENSE

%changelog
%autochangelog
