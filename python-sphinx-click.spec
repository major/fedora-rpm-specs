%global pypi_name sphinx-click

Name:           python-%{pypi_name}
Version:        4.3.0
Release:        %autorelease
Summary:        Sphinx extension that automatically documents Click applications

License:        MIT
URL:            https://github.com/click-contrib/sphinx-click
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# pytest is not an upstream dependency, we use it here out of convenience
BuildRequires:  python3dist(pytest)
BuildRequires:  pyproject-rpm-macros

%global package_desc \
sphinx-click is a Sphinx plugin that allows you to automatically extract\
documentation from a click-based application and include it in your docs.

%description
%{package_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

# The doc subpackage was removed, obsolete it to have clean upgrade path
# This was added in Fedora 35 and can be removed in Fedora 37
Obsoletes:      python-%{pypi_name}-doc < 2.7.1-1

%description -n python3-%{pypi_name}
%{package_desc}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_click

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst ChangeLog

%changelog
%autochangelog
