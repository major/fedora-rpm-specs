%global         srcname         recipe-scrapers
%global         forgeurl        https://github.com/hhursev/%{srcname}
Version:        15.11.0
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Package for scraping recipe data

License:        MIT
URL:            %{forgeurl}
# Test data does not have license information, so
# remove it
Source:         %{srcname}-%{version}-clean.tar.gz
# Script to download source files and rmeove test data
Source:         prepare.sh

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

BuildArch: noarch

%global _description %{expand:
A simple scraping tool for recipe webpages.
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}
# restore removed test data directory as it is used
# for tests
mkdir -p tests/test_data

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files recipe_scrapers -l

%check
%pyproject_check_import
# Tests that do not use test data
%pytest -k 'not (TestMainMethods and test_online_mode_html_retrieval)'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%doc docs/

%changelog
%autochangelog
