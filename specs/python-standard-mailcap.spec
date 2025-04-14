Name:           python-standard-mailcap
Version:        3.13.0
Release:        %autorelease
Summary:        Standard library mailcap redistribution, "dead battery"

License:        PSF-2.0
URL:            https://github.com/youknowone/python-deadlib
Source:         https://github.com/youknowone/python-deadlib/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-test


%global _description %{expand:
Python is moving forward! Python finally started to remove dead batteries. For
more information, see PEP 594.

If your project depends on a module that has been removed from the standard,
here is the redistribution of the dead batteries.}

%description %_description

%package -n     python3-standard-mailcap
Summary:        %{summary}

%description -n python3-standard-mailcap %_description


%prep
tar -x -f %{SOURCE0} --strip-components=2 python-deadlib-%{version}/mailcap/
sed -i -e "s/setuptools>=75.0/setuptools>=69.0/" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mailcap


%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-standard-mailcap -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
