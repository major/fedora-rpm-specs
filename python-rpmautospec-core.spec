%global srcname rpmautospec_core
%global canonicalname %{py_dist_name %{srcname}}

Name: python-%{canonicalname}
Version: 0.1.1
Release: %autorelease
Summary: Minimum functionality for rpmautospec

License: MIT
URL: https://github.com/fedora-infra/%{canonicalname}
Source0: %{pypi_source %{srcname}}
BuildArch: noarch
BuildRequires: python3-devel >= 3.6.0
# The dependencies needed for testing don’t get auto-generated.
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-cov)
BuildRequires: sed

%generate_buildrequires
%pyproject_buildrequires

%global _description %{expand:
This package contains minimum functionality to determine if an RPM spec file
uses rpmautospec features.}

%description %_description

%package -n python3-%{canonicalname}
Summary: %{summary}

%description -n python3-%{canonicalname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}
# Work around poetry not listing license files as such in package metadata.
sed -i -e 's|^\(.*/LICENSE\)|%%license \1|g' %{pyproject_files}

%check
%pytest

%files -n python3-%{canonicalname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
