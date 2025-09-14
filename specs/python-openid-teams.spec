Name:           python-openid-teams
Version:        1.1
Release:        %autorelease
Summary:        Teams extension for python-openid

License:        BSD-3-Clause
URL:            https://github.com/puiterwijk/python-openid-teams
Source:         https://github.com/puiterwijk/python-openid-teams/releases/download/v%{version}/python-openid-teams-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description\
Teams extension implementation for python-openid\


%description %_description

%package -n python3-openid-teams
Summary:        OpenID support for Flask
Requires:       python3-openid

%description -n python3-openid-teams
Teams extension implementation for python-openid

This package includes the python 3 version of the module.


%prep
%autosetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L openid_teams

 
%files -n python3-openid-teams -f %{pyproject_files}
# TODO: Upstream error: no COPYING in latest release
# %%license COPYING


%changelog
%autochangelog
