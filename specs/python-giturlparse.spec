Name:           python-giturlparse
Version:        0.14.0
Release:        %autorelease
Summary:        Parse & rewrite git urls

License:        Apache-2.0
URL:            https://github.com/nephila/giturlparse
Source:         %{url}/archive/%{version}/giturlparse-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Parse & rewrite git urls (supports GitHub, Bitbucket, FriendCode, Assembla,
Gitlab ...) }

%description %_description

%package -n python3-giturlparse
Summary:        %{summary}

%description -n python3-giturlparse %_description


%prep
%autosetup -n giturlparse-%{version}

# for local development---editable installs
rm -f requirements*txt


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l giturlparse


%check
%pyproject_check_import
%pytest


%files -n python3-giturlparse -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
