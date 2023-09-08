%global pypi_name sphinx-typlog-theme
%global srcname sphinx_typlog_theme

%global _description %{expand:
A sphinx theme sponsored by Typlog, created by Hsiaoming Yang.}

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        %autorelease
Summary:        A Sphinx theme sponsored by Typlog

License:        BSD-3-Clause
URL:            https://github.com/typlog/sphinx-typlog-theme
Source:         %{pypi_source}

# Contributed upstream: https://github.com/typlog/sphinx-typlog-theme/pull/26
Patch:          Ensure-compatibility-with-Sphinx-7.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%description %{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(sphinx)

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
