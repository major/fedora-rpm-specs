%bcond tests 1
%global forgeurl https://github.com/fralau/mkdocs-macros-plugin

Name:           python-mkdocs-macros-plugin
Version:        1.3.7
Release:        %autorelease
Summary:        Unleash the power of MkDocs with macros and variables

License:        MIT
URL:            https://mkdocs-macros-plugin.readthedocs.io
# PyPI tarball is missing test artifacts
Source:         %{forgeurl}/archive/v%{version}/mkdocs-macros-plugin-%{version}.tar.gz
# Assume D2 is installed instead of shelling out to brew
Patch:          mkdocs-macros-plugin-assume-d2-installed.patch

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  d2
BuildRequires:  python3dist(rich)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
mkdocs-macros-plugin is a plugin that makes it easier for contributors of an
MkDocs website to produce richer and more beautiful pages. It transforms the
markdown pages into jinja2 templates that use variables, calls to macros and
custom filters.}

%description %_description

%package -n     python3-mkdocs-macros-plugin
Summary:        %{summary}

%description -n python3-mkdocs-macros-plugin %_description

%prep
%autosetup -p1 -n mkdocs-macros-plugin-%{version}

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -x test
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_macros

# We don't want to install the test package
rm -r %{buildroot}%{python3_sitelib}/test/

%check
%if %{with tests}
# Disable broken tests that need further investigation
%pytest -v \
  --deselect=test/module/test_site.py::test_pages \
  --deselect=test/opt_in/test_site.py::test_opt_in \
  --deselect=test/register_macros/test_doc.py::test_pages \
  --deselect=test/simple/test_site.py::test_pages \
  %{nil}
%else
%pyproject_check_import
%endif

%files -n python3-mkdocs-macros-plugin -f %{pyproject_files}
%doc README.md CHANGELOG.md logo.png macros_info.png

%changelog
%autochangelog
