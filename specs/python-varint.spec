%global pypi_name varint

Name:          python-%{pypi_name}
Version:       1.0.2
Release:       %autorelease
BuildArch:     noarch
Summary:       A basic varint implementation in python
License:       MIT
URL:           https://github.com/fmoo/%{name}
# No license file in PyPi tarball.
# Upstream bug - https://github.com/fmoo/python-varint/issues/7
Source:        %{url}/archive/%{version}/varint-%{version}.tar.gz
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%files -n python3-%{pypi_name} -f %{pyproject_files}

%changelog
%autochangelog
