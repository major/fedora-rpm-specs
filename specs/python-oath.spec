Name:           python-oath
Version:        1.4.5
Release:        %autorelease
Summary:        Python implementation of HOTP, TOTP and OCRA

License:        BSD-3-Clause
URL:            https://github.com/bdauvergne/python-oath
Source:         %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
%{summary}.}

%description %_description

%package -n     python3-oath
Summary:        %{summary}

%description -n python3-oath %_description


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files oath -L


%check
%{py3_test_envvars} %{python3} -m unittest


%files -n python3-oath -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
