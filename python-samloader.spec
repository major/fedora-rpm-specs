%global forgeurl https://github.com/nlscc/samloader
%global commit 820375214f1b7b26109e5c3aea8d005fcc56eebf
%forgemeta

%global pypi_name samloader

Name:           python-%{pypi_name}
Version:        0
Release:        %autorelease
Summary:        Download Samsung firmware from official servers

License:        GPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         %{url}/pull/59.patch#/Use-tqdm-for-progress-bar.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
samloader is a tool to download firmware for Samsung devices from the official
servers.}

%description %_description

%package -n %{pypi_name}
Summary:        %{summary}

%description -n %{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{commit}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import %{pypi_name}


%files -n %{pypi_name} -f %{pyproject_files}
%license COPYING
%doc README.md
%{_bindir}/%{pypi_name}

%changelog
%autochangelog
