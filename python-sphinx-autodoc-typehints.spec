%global srcname sphinx-autodoc-typehints
%global altname sphinx_autodoc_typehints

%global common_description %{expand:
This extension allows you to use Python 3 annotations for documenting
acceptable argument types and return value types of functions.}

Name:           python-%{srcname}
Version:        1.18.3
Release:        %autorelease
Summary:        Type hints support for the Sphinx autodoc extension

License:        MIT
URL:            https://github.com/agronholm/sphinx-autodoc-typehints
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(nptyping)
BuildRequires:  python3dist(sphobjinv)
BuildRequires:  python3dist(typish)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Requires:       python3-sphinx

%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files %{altname}

# %%check
# %%pytest

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
%autochangelog
