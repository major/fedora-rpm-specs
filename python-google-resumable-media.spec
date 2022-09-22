# tests are enabled by default
%bcond_without tests

%global         srcname     google-resumable-media
%global         forgeurl    https://github.com/googleapis/google-resumable-media-python
Version:        2.3.3
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Utilities for Google media downloads and resumable uploads

License:        ASL 2.0
URL:            %forgeurl
Source0:        %forgesource
# Opened upstream PR to fix mock import:
# https://github.com/googleapis/google-resumable-media-python/pull/329
Patch0:         https://github.com/googleapis/google-resumable-media-python/pull/329.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(google-auth)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(urllib3)
%endif

%global _description %{expand:
Utilities for Google media downloads and resumable uploads}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%if %{with tests}
%check
# Work around an usual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest --disable-warnings tests/unit
mv google{_,}
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%{python3_sitelib}/google_resumable_media-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
