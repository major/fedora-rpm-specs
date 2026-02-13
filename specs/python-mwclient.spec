%global github_owner    mwclient
%global github_name     mwclient

Name:           python-mwclient
Version:        0.11.0
Release:        %autorelease
Summary:        Mwclient is a client to the MediaWiki API

License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/v%{version}.tar.gz
# Maintainers, please upstream
Patch0:         python-mwclient-rm-python-mock-usage.diff
BuildArch:      noarch

%description
mwclient is a lightweight Python client library to the MediaWiki API which
provides access to most API functionality.

%package -n python3-%{github_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{github_name}}
Obsoletes:      python2-%{github_name} < %{version}-%{release}

BuildRequires:  python3-devel

%description -n python3-%{github_name}
%{github_name} is a lightweight Python client library to the MediaWiki API which
provides access to most API functionality. This is the Python 3 build of
%{github_name}.

%prep
%autosetup -p1 -n %{github_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{github_name}

%check
%tox

%files -n python3-%{github_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
