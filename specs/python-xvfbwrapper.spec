
%global pypi_name xvfbwrapper

Name:           python-%{pypi_name}
Version:        0.2.12
Release:        %autorelease
Summary:        run headless display inside X virtual framebuffer (Xvfb)

License:        MIT
URL:            https://github.com/cgoldberg/xvfbwrapper
Source0:        https://files.pythonhosted.org/packages/source/x/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%global _description\
Python wrapper for running a display inside X virtual framebuffer (Xvfb)

%description %_description


%package -n python3-%{pypi_name}
Summary:        run headless display inside X virtual framebuffer (Xvfb)

BuildRequires: python3-devel
BuildRequires: xorg-x11-server-Xvfb

%description -n python3-%{pypi_name}
Python wrapper for running a display inside X virtual framebuffer (Xvfb)

%prep
%autosetup -n %{pypi_name}-%{version}

# remove shebang
sed -i '1{\@^#!/usr/bin/env python@d}' xvfbwrapper.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
export DISPLAY=:0.0
%pytest

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/*

%changelog
%autochangelog
