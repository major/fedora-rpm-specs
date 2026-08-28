Name:          buildstream-plugins
Summary:       A collection of plugins for the BuildStream project
License:       Apache-2.0
URL:           https://buildstream.build/

BuildArch:     noarch
# Match buildstream: the test suite imports buildstream._testing, and the
# binary already Requires buildstream. Core is unavailable on these arches.
ExcludeArch:   %{ix86} s390x

Version:       2.8.0
Release:       %autorelease
Source0:       https://github.com/apache/buildstream-plugins/archive/%{version}/buildstream-plugins-%{version}.tar.gz

BuildRequires: buildstream >= %{version}
BuildRequires: python3-devel >= 3.10
BuildRequires: git

Requires:      buildstream >= %{version}

Requires:      git
Requires:      lzip
Requires:      patch


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

%ifarch x86_64 aarch64
%check
%pytest -m "not integration" \
  --deselect tests/sources/docker.py::test_docker_fetch \
  --deselect tests/sources/docker.py::test_docker_source_checkout \
  --deselect tests/sources/docker.py::test_fetch_duplicate_layers \
  --deselect tests/sources/cargo.py::test_cargo_track_fetch_build
%endif

%files -n %{name} -f %{pyproject_files}
%doc NEWS README.rst

%changelog
%autochangelog
