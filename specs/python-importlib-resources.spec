Name:           python-importlib-resources
Version:        6.5.2
Release:        %autorelease
Summary:        Backport of the importlib.resources module

License:        Apache-2.0
URL:            https://github.com/python/importlib_resources
Source:         %{pypi_source importlib_resources}

BuildArch:      noarch
BuildRequires:  python3-devel
%if 0%{?epel} == 9
# Change the build backend in EPEL9 because `setuptools>=61.2` is needed for PEP621
BuildRequires:  tomcli
%endif

%global _description %{expand:
importlib_resources is a backport of Python standard library importlib.resources
module for older Pythons.

The key goal of this module is to replace parts of pkg_resources with a solution in
Python's stdlib that relies on well-defined APIs. This makes reading resources
included in packages easier, with more stable and consistent semantics.}

%description %_description

%package -n python3-importlib-resources
Summary:        %{summary}
%description -n python3-importlib-resources %_description


%prep
%autosetup -n importlib_resources-%{version}
%if 0%{?epel} == 9
tomcli set pyproject.toml lists str "build-system.requires" "hatchling" "hatch-vcs"
tomcli set pyproject.toml str "build-system.build-backend" "hatchling.build"
tomcli set pyproject.toml str "tool.hatch.version.source" "vcs"
%endif


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files importlib_resources


%check
%pytest %{?el9:--import-mode prepend}


%files -n python3-importlib-resources -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
