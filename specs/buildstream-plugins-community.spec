Name:          buildstream-plugins-community
Summary:       A collection of community-maintained plugins for BuildStream
License:       LGPL-2.0-or-later AND MIT AND Apache-2.0
URL:           https://gitlab.com/BuildStream/buildstream-plugins-community

BuildArch:     noarch
# Match buildstream: the test suite imports buildstream._testing, and the
# binary already Requires buildstream. Core is unavailable on these arches.
ExcludeArch:   %{ix86} s390x

Version:       2.3.3
Release:       %autorelease
Source0:       https://files.pythonhosted.org/packages/source/b/buildstream-plugins-community/buildstream_plugins_community-%{version}.tar.gz
# https://gitlab.com/BuildStream/buildstream-plugins-community/-/merge_requests/487
Patch:         no_click.patch

BuildRequires: buildstream >= %{version}
BuildRequires: python3-devel >= 3.10
BuildRequires: git

Requires:      buildstream >= %{version}

Requires:      quilt


%description
A collection of community-maintained plugins for BuildStream


%prep
%autosetup -n %{name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -g test -x httpfetcher,pypi,deb,git,cargo2

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l buildstream_plugins_community

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
