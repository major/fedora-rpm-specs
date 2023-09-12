%global _description %{expand:
Tool for analysis of electrophysiology in Python.

This package was originally developed by Mike Vella. This has been updated by
Padraig Gleeson and others (and moved to NeuralEnsemble) to continue
development of pyelectro and Neurotune for use in OpenWorm, Open Source Brain
and other projects.}

Name:           python-pyelectro
Version:        0.2.7
Release:        %autorelease
Summary:        A library for analysis of electrophysiological data

# spdx
License:        BSD-2-Clause
URL:            https://github.com/NeuralEnsemble/pyelectro
Source0:        %{url}/archive/v%{version}/pyelectro-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-pyelectro
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-pyelectro %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n pyelectro-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyelectro

%check
%{pytest}

%files -n python3-pyelectro -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%doc examples

%changelog
%autochangelog
