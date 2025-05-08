Name:           python-re-assert
Version:        1.1.0
Release:        %autorelease
Summary:        Show where your regex match assertion failed

# SPDX
License:        MIT
URL:            https://github.com/asottile/re-assert
Source:         %{url}/archive/v%{version}/re-assert-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l re_assert

BuildArch:      noarch

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
%{summary}!}

%description %{common_description}


%package -n python3-re-assert
Summary: %{summary}

%description -n python3-re-assert %{common_description}


%check -a
%pytest


%files -n python3-re-assert -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
