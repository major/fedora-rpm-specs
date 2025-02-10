%global forgeurl https://github.com/squidfunk/mkdocs-material

Name:           mkdocs-material
Version:        9.5.48
Release:        %autorelease
Summary:        Material design theme for MkDocs

License:        MIT
URL:            https://squidfunk.github.io/mkdocs-material
Source:         %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
# Drop mkdocs-material-extensions from requirements
Patch:          %{forgeurl}/pull/7486.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

# These pull in additional dependencies that enable optional features
Recommends:     python3dist(mkdocs-material[git]) = %{version}
Recommends:     python3dist(mkdocs-material[imaging]) = %{version}
Recommends:     python3dist(mkdocs-material[recommended]) = %{version}

%description
This package provides a powerful documentation framework on top of MkDocs.

%pyproject_extras_subpkg -n %{name} git,imaging,recommended

%prep
%autosetup -p1

# Relax version pins
sed -i 's/~=/>=/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x git,imaging,recommended

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files material

%check
export PYTHONPATH="%{buildroot}/%{python3_sitelib}"
mkdocs new testing
pushd testing
mkdocs build --theme material
popd

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
