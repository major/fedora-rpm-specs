%global srcname sphinx-gallery

Name:           python-%{srcname}
Version:        0.19.0
Release:        %autorelease
Summary:        Sphinx extension to automatically generate an examples gallery

License:        BSD-3-Clause
URL:            https://sphinx-gallery.github.io/stable/index.html
Source0:        https://github.com/sphinx-gallery/sphinx-gallery/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
A Sphinx extension that builds an HTML version of any Python script and puts
it into an examples gallery.


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-absl-py
BuildRequires:  python%{python3_pkgversion}-lxml
BuildRequires:  python%{python3_pkgversion}-matplotlib

%description -n python%{python3_pkgversion}-%{srcname}
A Sphinx extension that builds an HTML version of any Python script and puts
it into an examples gallery.


%pyproject_extras_subpkg -n python%{python3_pkgversion}-%{srcname} recommender
%pyproject_extras_subpkg -n python%{python3_pkgversion}-%{srcname} show_api_usage


%prep
%autosetup -n %{srcname}-%{version}

# No coverage report
sed -i -e 's/"--cov[^ ]*//g' pyproject.toml


%generate_buildrequires
# extras with missing deps:
#  "show_memory": ["memory_profiler"],
#  "jupyterlite": ["jupyterlite_sphinx"],
%pyproject_buildrequires -x recommender -x show_api_usage


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sphinx_gallery


%check
# test_dummy_image requires jupyterlite_sphinx optional dep
# test_embed_code_links_get_data requires network
%pytest -v -k 'not test_dummy_image and not test_embed_code_links_get_data'


%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%doc README.rst CHANGES.rst
%{_bindir}/sphinx_gallery_py2jupyter


%changelog
%autochangelog
