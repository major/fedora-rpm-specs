%global pypi_name readme_renderer
%global pkg_name readme-renderer

Name:           python-%{pkg_name}
Version:        44.0
Release:        %autorelease
Summary:        Library for rendering "readme" descriptions for Warehouse

License:        Apache-2.0
URL:            https://github.com/pypa/readme_renderer
Source:         %{pypi_source %{pypi_name}}

# Fix tests with pygments >= 2.19.0
# Backport of https://github.com/pypa/readme_renderer/pull/325
Patch:          fix-tests-pygments-2.19.0.patch
# Support docutils 0.22+
Patch:          https://github.com/pypa/readme_renderer/pull/332.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%global _description %{expand:
Readme Renderer Readme Renderer is a library that will safely render arbitrary
README files into HTML. It is designed to be used in Warehouse_ to render the
long_description for packages. It can handle Markdown, reStructuredText (.rst),
and plain text.}

%description %{_description}

%package -n     python%{python3_pkgversion}-%{pkg_name}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{pkg_name} %{_description}

%pyproject_extras_subpkg -n python%{python3_pkgversion}-%{pkg_name} md

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# pytest-icdiff not packaged and not essential
sed -i "/pytest-icdiff/d" tox.ini

%generate_buildrequires
%pyproject_buildrequires -t -x md

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
%pytest -v tests

%files -n python%{python3_pkgversion}-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
