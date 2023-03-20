%global srcname sphinx_mdinclude
%global distname sphinx-mdinclude

%global _description %{expand:
sphinx-mdinclude is a simple Sphinx extension that enables including Markdown
documents from within reStructuredText. It provides the `.. mdinclude::`
directive, and automatically converts the content of Markdown documents to
reStructuredText format.}

Name:           python-%{distname}
Version:        0.5.3
Release:        %autorelease
Summary:        Markdown extension for Sphinx

License:        MIT
URL:            https://github.com/omnilib/sphinx-mdinclude
Source:         %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description %{_description}


%package -n     python3-%{distname}
Summary:        %{summary}
Requires:       python3dist(sphinx)

%description -n python3-%{distname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}
# this is only for mistune 0.8.4, and won't import if 2.x is installed
rm %{srcname}/legacy.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import
%pytest -v


%files -n python3-%{distname} -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
