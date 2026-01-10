%global srcname uv-dynamic-versioning

Name:           python-uv-dynamic-versioning
Version:        0.12.0
Release:        %autorelease
Summary:        Dynamic versioning based on VCS tags

License:        MIT
URL:            https://github.com/ninoseki/uv-dynamic-versioning
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
# For autosetup -S git:
BuildRequires:  git-core
BuildRequires:  %{py3_dist gitpython}
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Dynamic versioning based on VCS tags for uv/hatch project.}

%description %_description

%package -n python3-uv-dynamic-versioning
Summary:        %{summary}

%description -n python3-uv-dynamic-versioning %_description


%prep
# -S git: tests need to run in a git repository:
%autosetup -p1 -n %{srcname}-%{version} -S git


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l uv_dynamic_versioning


%check
%pyproject_check_import
%pytest


%files -n python3-uv-dynamic-versioning -f %{pyproject_files}
%doc README.md
%{_bindir}/uv-dynamic-versioning


%changelog
%autochangelog
