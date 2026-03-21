# Default: when bootstrapping -> disable tests
%bcond bootstrap 0
%bcond tests %{without bootstrap}

Name:           python-wheel
Version:        0.46.3
Release:        %autorelease
Epoch:          1
Summary:        Command line tool for manipulating wheel files

License:        MIT
URL:            https://github.com/pypa/wheel
Source:         %{url}/archive/%{version}/wheel-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:    pyproject
BuildOption(install): -l wheel

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
%if %{defined fedora}
# optional test dependencies (flit is unwanted in RHEL, a test is skipped without both of those)
BuildRequires:  python3-build
BuildRequires:  python3-flit
%endif
%endif

%global _description %{expand:
This is a command line tool for manipulating Python wheel files,
as defined in PEP 427. It contains the following functionality:

- Convert .egg archives into .whl.
- Unpack wheel archives.
- Repack wheel archives.
- Add or remove tags in existing wheel archives.}

%description %{_description}


%package -n     python3-wheel
Summary:        %{summary}

%description -n python3-wheel %{_description}


%install -a
# for backwards compatibility only
mv %{buildroot}%{_bindir}/wheel{,-%{python3_version}}
ln -s wheel-%{python3_version} %{buildroot}%{_bindir}/wheel-3
ln -s wheel-3 %{buildroot}%{_bindir}/wheel


%check -a
# Smoke test
%{py3_test_envvars} wheel version

%if %{with tests}
%pytest -v
%endif


%files -n python3-wheel -f %{pyproject_files}
%doc README.rst
%{_bindir}/wheel-%{python3_version}
%{_bindir}/wheel-3
%{_bindir}/wheel


%changelog
%autochangelog
