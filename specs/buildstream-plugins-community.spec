%global srcname buildstream_plugins_community

Name:          buildstream-plugins-community
Summary:       A collection of community-maintained plugins for BuildStream
License:       LGPL-2.0-or-later AND MIT AND Apache-2.0
URL:           https://gitlab.com/BuildStream/buildstream-plugins-community

BuildArch:     noarch
# Tests import buildstream._testing._sourcetests, which only has
# Alpine images for x86-64 and aarch64:
# https://github.com/apache/buildstream/blob/master/src/buildstream/_testing/_sourcetests/project/project.conf
# https://github.com/apache/buildstream/blob/master/src/buildstream/_testing/_sourcetests/project/elements/base/base-alpine.bst
ExclusiveArch: x86_64 aarch64

Version:       2.3.3
Release:       %autorelease
Source0:       %{pypi_source}
# https://gitlab.com/BuildStream/buildstream-plugins-community/-/merge_requests/487
Patch:         no_click.patch

BuildRequires: buildstream >= %{version}
BuildRequires: python3-devel >= 3.10
BuildRequires: git

Requires:      buildstream >= %{version}

Requires:      quilt
# Plugin extras: +extra metapackages so the extras generator
# supplies Python deps from upstream METADATA. Recommend them
# from the base package. See:
# - https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_extras
# - https://fedoraproject.org/wiki/Changes/PythonExtras
Recommends:    %{name}+pypi
Recommends:    %{name}+deb
Recommends:    %{name}+httpfetcher
Recommends:    %{name}+git
Recommends:    %{name}+cargo2


%description
A collection of community-maintained plugins for BuildStream

%pyproject_extras_subpkg -n %{name} cargo2 deb git httpfetcher pypi

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -g test -x httpfetcher,pypi,deb,git,cargo2

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
# Ignore test that require network access
%pytest \
    --ignore=tests/sources/bazel.py \
    --ignore=tests/sources/bazel_file.py \
    --deselect=tests/sources/git_tag.py::test_gitlfs_off \
    --deselect=tests/sources/git_tag.py::test_gitlfs_notset

%files -n %{name} -f %{pyproject_files}
%doc NEWS README.rst
%license LICENSE

%changelog
%autochangelog
