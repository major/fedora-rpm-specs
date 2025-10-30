%global modname mwparserfromhell

Name:           python-mwparserfromhell
Version:        0.7.2
Release:        %autorelease
Summary:        A Python parser for MediaWiki wikicode

License:        MIT
URL:            https://github.com/earwig/mwparserfromhell
Source:         %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  tomcli

%global _description %{expand:
mwparserfromhell (the MediaWiki Parser from Hell) is a Python package that
provides an easy-to-use and outrageously powerful parser for MediaWiki
wikicode.}

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}

%package -n python3-%{modname}-devel
Summary:        Source and header files for the mwparserfromhell C extension
Requires:       python3-%{modname}%{?_isa} = %{version}-%{release}

%description -n python3-%{modname} %_description
%description -n python3-%{modname}-devel %_description

%prep
%autosetup -p1 -n %{modname}-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem dependency-groups.dev 'pytest-cov\b.*'
# Only needed for building documentation:
tomcli set pyproject.toml lists delitem dependency-groups.dev 'sphinx\b.*'


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -g dev


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname} -l


%check
%pyproject_check_import
%pytest


%files -n python3-%{modname} -f %{pyproject_files}
%doc README.*
%exclude %{python3_sitearch}/mwparserfromhell/parser/ctokenizer/


%files -n python3-%{modname}-devel
%{python3_sitearch}/mwparserfromhell/parser/ctokenizer/

%changelog
%autochangelog
