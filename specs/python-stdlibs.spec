Name:           python-stdlibs
Version:        2024.12.3
Release:        %autorelease
Summary:        List of packages in the stdlib

License:        MIT
URL:            https://stdlibs.omnilib.dev
Source:         %{pypi_source stdlibs}
# use tomllib instead of the deprecated toml
Patch:          stdlibs-use-tomllib.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(moreorless)


%global _description %{expand:
This package provides a static listing of all known modules in the Python
standard library, with separate lists available for each major release dating
back to Python 2.3. It also includes combined lists of all module names that
were ever available in any 3.x release, any 2.x release, or both.

Note: On Python versions 3.10 or newer, a list of module names for the active
runtime is available sys.stdlib_module_names. This package exists to provide an
historical record for use with static analysis and other tooling.

This package only includes listings for CPython releases. If other runtimes
would be useful, open an issue and start a discussion on how best that can be
accomodated.}


%description %_description

%package -n     python3-stdlibs
Summary:        %{summary}

%description -n python3-stdlibs %_description


%prep
%autosetup -p1 -n stdlibs-%{version}
# not intended for use by consumers of the library
# see https://github.com/omnilib/stdlibs/pull/105
rm stdlibs/fetch.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files stdlibs


%check
%pyproject_check_import
%py3_test_envvars %python3 -m unittest -v


%files -n python3-stdlibs -f %{pyproject_files}
# license file not tagged correctly
%license %{python3_sitelib}/stdlibs-%{version}.dist-info/LICENSE
%doc README.md


%changelog
%autochangelog
