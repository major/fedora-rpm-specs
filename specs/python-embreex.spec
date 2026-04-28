Name:           python-embreex
Version:        4.4.0
Release:        %autorelease
Summary:        Python binding for Intel’s Embree ray engine

License:        BSD-2-Clause
URL:            https://github.com/trimesh/embreex
Source:         %{url}/archive/%{version}/embreex-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l embreex

# embree only supports x86_64, aarch64
# https://bugzilla.redhat.com/show_bug.cgi?id=2461412
ExclusiveArch:  %{x86_64} %{arm64}

BuildRequires:  gcc-c++
BuildRequires:  embree-devel

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
A fork of https://github.com/scopatz/pyembree configured to build wheels on
various platforms and Python interpreters. The name change is to avoid
confusion with the other forks and install methods available.

The goal is to meet the upstream trimesh[easy] preferences for dependencies.}

%description %{common_description}


%package -n python3-embreex
Summary:        %{summary}

%description -n python3-embreex %{common_description}


%check -a
%pytest -v


%files -n python3-embreex -f %{pyproject_files}
%doc README.md
%doc examples/


%changelog
%autochangelog
