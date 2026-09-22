# Check "min-version" at https://github.com/apache/buildstream-plugins/blob/master/project.conf
%global bst_minver 2.5.0

Name:          buildstream-plugins
Summary:       A collection of plugins for the BuildStream project
License:       Apache-2.0
URL:           https://buildstream.build/

BuildArch:     noarch
# Tests import buildstream._testing._sourcetests, which only has
# Alpine images for x86-64 and aarch64:
# https://github.com/apache/buildstream/blob/master/src/buildstream/_testing/_sourcetests/project/project.conf
# https://github.com/apache/buildstream/blob/master/src/buildstream/_testing/_sourcetests/project/elements/base/base-alpine.bst
ExclusiveArch: x86_64 aarch64

Version:       2.8.0
Release:       %autorelease
Source0:       https://github.com/apache/buildstream-plugins/archive/%{version}/buildstream-plugins-%{version}.tar.gz

BuildRequires: buildstream >= %{bst_minver}
BuildRequires: python3-devel >= 3.10
BuildRequires: git

Requires:      buildstream >= %{bst_minver}

# docker plugin
Recommends:    %{py3_dist requests}
# git plugin
Recommends:    git
# patch plugin
Recommends:    patch

%description
A collection of plugins for the BuildStream project


%prep
%autosetup -n %{name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires requirements/test-requirements.txt requirements/plugin-requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l buildstream_plugins

%check
%pytest -m "not integration" \
  --deselect tests/sources/docker.py::test_docker_fetch \
  --deselect tests/sources/docker.py::test_docker_source_checkout \
  --deselect tests/sources/docker.py::test_fetch_duplicate_layers \
  --deselect tests/sources/cargo.py::test_cargo_track_fetch_build

%files -n %{name} -f %{pyproject_files}
%doc NEWS README.rst

%changelog
%autochangelog
