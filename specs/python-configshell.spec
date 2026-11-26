# Copyright 2011, Red Hat
%global oname configshell-fb

Name:           python-configshell
License:        Apache-2.0
Summary:        A framework to implement simple but nice CLIs
Epoch:          1
Version:        2.0.2
Release:        %autorelease
URL:            https://github.com/open-iscsi/configshell-fb
Source:         %{url}/archive/v%{version}/%{oname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description\
A framework to implement simple but nice configuration-oriented\
command-line interfaces.

%description %_description

%package -n python3-configshell
Summary:        A framework to implement simple but nice CLIs

%description -n python3-configshell %_description

%prep
%autosetup -n %{oname}-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l 'configshell*'

%check
%pyproject_check_import

%files -n python3-configshell -f %{pyproject_files}
%doc COPYING README.md

%changelog
%autochangelog
