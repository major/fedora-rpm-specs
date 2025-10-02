Name:           python-assertpy
Version:        1.1
Release:        %autorelease
Summary:        Simple assertion library for unit testing in Python with a fluent API

License:        BSD-3-Clause
URL:            https://github.com/assertpy/assertpy
Source:         %{url}/archive/%{version}/assertpy-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l assertpy

BuildArch:      noarch

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
Simple assertions library for unit testing in Python with a nice fluent API.}

%description %{common_description}


%package -n     python3-assertpy
Summary:        %{summary}

%description -n python3-assertpy %{common_description}


%check -a
%pytest


%files -n python3-assertpy -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
