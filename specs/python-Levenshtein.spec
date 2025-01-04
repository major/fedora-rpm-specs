%global srcname Levenshtein

%global forgeurl https://github.com/maxbachmann/%{srcname}
Version:        0.26.1
%forgemeta

Name:         python-%{srcname}
Summary:      Python extension computing string distances and similarities
Release:      %{autorelease}

License:      GPL-2.0-or-later

# Levenshtein is the latest name of the package, though the python-Levenshtein repo
# is still being kept up-to-date in lock-step to this official upstream.
URL:          %{forgeurl}

Source0:      %{forgesource}

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: rapidfuzz-cpp-static

%global _description %{expand:
Levenshtein computes Levenshtein distances, similarity ratios, generalized
medians and set medians of Strings and Unicodes.}

%description %_description

%package -n python3-%{srcname}

Summary:  %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
# Levenshtein can build under older Cython successfully
sed 's/Cython>=3.0.0[ab0-9]\+/Cython>=0.29.26/' -i pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
# To avoid empty debugsourcefiles.list, we need to build the package
# with RelWithDebInfo
# Upstream issue: https://github.com/scikit-build/scikit-build-core/issues/915
export SKBUILD_CMAKE_BUILD_TYPE=RelWithDebInfo
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license COPYING


%changelog
%{autochangelog}
