Name:           python-acres
Version:        0.5.0
Release:        %{autorelease}
Summary:        Access resources on your terms

License:        Apache-2.0
URL:            https://github.com/nipreps/acres
Source:         %{url}/archive/%{version}/acres-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L acres

BuildArch:      noarch

# See the test dependency group, but we do not want coverage dependencies.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
This module aims to provide a simple way to access package resources
that will fit most use cases.}

%description %{common_description}


%package -n python3-acres
Summary:        %{summary}

%description -n python3-acres %{common_description}


%generate_buildrequires -p
export PDM_BUILD_SCM_VERSION='%{version}'


%build -p
export PDM_BUILD_SCM_VERSION='%{version}'


%check -a
%pytest -v


%files -n python3-acres -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
