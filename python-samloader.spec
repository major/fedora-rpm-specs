%global date 20221223
%global commit 95d2ac8fb9027b7908d201e4ce807a5b338f923a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global pypi_name samloader

Name:           python-%{pypi_name}
Version:        0.4~%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Download Samsung firmware from official servers

License:        GPL-3.0-or-later
URL:            https://github.com/nlscc/samloader
Source:         %{url}/archive/%{commit}/%{pypi_name}-%{commit}.tar.gz

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
