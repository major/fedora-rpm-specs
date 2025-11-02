Name:           python-docs-theme
Version:        2025.10
Release:        %autorelease
Summary:        The Sphinx theme for the CPython docs and related projects

License:        PSF-2.0
URL:            https://github.com/python/python-docs-theme/
Source:         %{url}archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description Python Docs Sphinx Theme is the theme for the Python documentation.

%description
%_description

%package -n     python3-docs-theme
Summary:        %{summary}

%description -n python3-docs-theme
%_description

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files python_docs_theme

%files -n python3-docs-theme -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
