
%global modname svg.path

Name:               python-svg-path
Version:            6.3
Release:            %autorelease
Summary:            SVG path objects and parser

License:            MIT
URL:                http://pypi.python.org/pypi/svg.path
Source0:            https://github.com/regebro/svg.path/archive/%{version}.tar.gz
# Patch to fix tests with newer pillow versions
# Already proposed upstream by debian maintainer
Patch0:             https://patch-diff.githubusercontent.com/raw/regebro/svg.path/pull/105.patch

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-pytest
BuildRequires:      python3-pillow

%global _description\
svg.path is a collection of objects that implement the different path\
commands in SVG, and a parser for SVG path definitions.

%description %_description

%package -n python3-svg-path
Summary:            SVG path objects and parser

Requires:           python3-setuptools

%description -n python3-svg-path
svg.path is a collection of objects that implement the different path
commands in SVG, and a parser for SVG path definitions.

%prep
%autosetup -p1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l svg

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-svg-path -f %{pyproject_files}
%doc README.rst CHANGES.txt CONTRIBUTORS.txt

%changelog
%autochangelog
