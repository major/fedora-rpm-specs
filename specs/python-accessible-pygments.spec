%global giturl  https://github.com/Quansight-Labs/accessible-pygments

Name:           python-accessible-pygments
Version:        0.0.5
Release:        %autorelease
Summary:        Accessible pygments themes

BuildArch:      noarch
License:        BSD-3-Clause
URL:            https://quansight-labs.github.io/accessible-pygments/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/accessible-pygments-%{version}.tar.gz

BuildRequires:  python3-devel

%description
This package includes a collection of accessible themes for pygments
based on different sources.

%package     -n python3-accessible-pygments
Summary:        %{summary}

%py_provides python3-a11y-pygments

%description -n python3-accessible-pygments
This package includes a collection of accessible themes for pygments
based on different sources.

%prep
%autosetup -n accessible-pygments-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -x tests

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l a11y_pygments

%check
%pytest -v

%files -n python3-accessible-pygments -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog
