Name:           python-tinydb
Version:        4.8.0
Release:        %autorelease
Summary:        TinyDB is a tiny, document oriented database

License:        MIT
URL:            https://github.com/msiemens/tinydb
Source:         https://github.com/msiemens/tinydb/archive/refs/tags/v%{version}.tar.gz#/tinydb-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
TinyDB is a lightweight document oriented database optimized for your happiness}

%description %_description

%package -n     python3-tinydb
Summary:        %{summary}

%description -n python3-tinydb %_description


%prep
%autosetup -p1 -n tinydb-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tinydb


%check
# fails on mypy-plugin
#%%pyproject_check_import
%tox


%files -n python3-tinydb -f %{pyproject_files}


%changelog
%autochangelog
