## START: Set by rpmautospec
## (rpmautospec version 0.2.6)
%define autorelease(e:s:pb:) %{?-p:0.}%{lua:
    release_number = 4;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{?dist}
## END: Set by rpmautospec

%global srcname azure-storage-blob

Name:           python-%{srcname}
Version:        12.14.1
%global         pypi_version    12.14.1
Release:        %autorelease
Summary:        Azure Storage Blobs client library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{pypi_version} zip}


BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp) >= 3.0


%global _description %{expand:
Azure Storage Blobs client library for Python}

%description %{_description}



%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{pypi_version}
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure


%check
%pyproject_check_import

# pytest unittest are not run as the test depends on the vcrpy that is pinned https://github.com/Azure/azure-sdk-for-python/tree/main/tools/vcrpy
# Furthermore the pypi_source file are missing some test files used to run the test e.g recording rules

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Thu Jul 06 2023 Roman Inflianskas <rominf@aiven.io> - 12.14.1-4
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Rommel Layco <rj.layco@gmail.com> 12.14.1-3
- Update to 12.14.1

* Wed Sep 21 2022 Rommel Layco <rj.layco@gmail.com> 12.13.1-2
- Initial import (fedora#2109341)
- Fix changelog

* Thu Aug 18 2022 John Doe <packager@example.com> 12.13.1-1
- Uncommitted changes
