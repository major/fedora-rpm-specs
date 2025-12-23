# NOTE: We do not build documentation, since this package sits underneath
# several documentation packages, leading to circular dependencies.

%global giturl  https://github.com/pradyunsg/diagnostic

Name:           python-diagnostic
Version:        3.0.0
Release:        %autorelease
Summary:        Build command line tools with great error reporting

License:        MIT
URL:            https://diagnostic.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/diagnostic-%{version}.tar.gz
# Work around a spurious test failure due to ordering issues
# https://github.com/pradyunsg/diagnostic/issues/46
Patch:          %{name}-test.patch

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(generate_buildrequires): tests/requirements.txt
BuildOption(install): -l diagnostic

%description
The diagnostic package makes it easier to build command line tools with great
error reporting.

%package     -n python3-diagnostic
Summary:        Build command line tools with great error reporting

%description -n python3-diagnostic
The diagnostic package makes it easier to build command line tools with great
error reporting.

%prep
%autosetup -n diagnostic-%{version} -p1

# Do not run coverage tools in an RPM build
sed -i '/pytest-cov/d' tests/requirements.txt

%check
%pytest -v

%files -n python3-diagnostic -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
