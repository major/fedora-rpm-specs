%global pypi_name readme_renderer
%global pkg_name readme-renderer

Name:           python-%{pkg_name}
Version:        37.2
Release:        %autorelease
Summary:        Library for rendering "readme" descriptions for Warehouse

License:        ASL 2.0
URL:            https://github.com/pypa/readme_renderer
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description %{expand:
Readme Renderer Readme Renderer is a library that will safely render arbitrary
README files into HTML. It is designed to be used in Warehouse_ to render the
long_description for packages. It can handle Markdown, reStructuredText (.rst),
and plain text.}

%description %{_description}

%package -n     python%{python3_pkgversion}-%{pkg_name}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{pkg_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} 
%generate_buildrequires
%pyproject_buildrequires -t
 
%build
%pyproject_wheel
 
%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v tests -k "not test_md_fixtures"
 
%files -n python%{python3_pkgversion}-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog

