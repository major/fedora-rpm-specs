# Since pydicom contains code to download files from the GitHub repository, we
# really need to package a snapshot no older than the packaged pydicom release.
%global commit 8da482f208401d63cd63f3f4efc41b6856ef36c7
%global snapdate 20240919

Name:           python-pydicom-data
Version:        1.0.0^%{snapdate}git%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        Most of the test files used with pydicom, downloaded to cache when needed

# SPDX
License:        MIT
URL:            https://github.com/pydicom/pydicom-data
Source:         %{url}/archive/%{commit}/pydicom-data-%{commit}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l data_store

BuildArch:      noarch

# Test dependencies
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-pydicom-data
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
#
# Note that this would conflict with https://pypi.org/project/data.store/, but
# that project has been inactive for nine years, and it is unlikely that it
# would ever be packaged.
%py_provides python3-data-store

%description -n python3-pydicom-data %{common_description}


%check -a
%pytest -v


%files -n python3-pydicom-data -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
