# All tests require Internet access
# to test in mock use:  --enable-network --with check
# to test in a privileged environment use:
#   --with check --with privileged_tests
%bcond_with     check
%bcond_with     privileged_tests

Name:           ansible-bender
Version:        0.10.1
Release:        %autorelease
Summary:        Build container images using Ansible playbooks

License:        MIT
URL:            https://github.com/ansible-community/ansible-bender
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
%if %{with check}
# These are required for tests:
BuildRequires:  python%{python3_pkgversion}-pyyaml
BuildRequires:  python%{python3_pkgversion}-tabulate
BuildRequires:  python%{python3_pkgversion}-jsonschema
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-flexmock
BuildRequires:  python%{python3_pkgversion}-pytest-xdist
BuildRequires:  python%{python3_pkgversion}-libselinux
BuildRequires:  ansible-core
BuildRequires:  podman
BuildRequires:  buildah
BuildRequires:  git
%endif
Requires:       (ansible-core or ansible)
Suggests:       ansible-core
Requires:       buildah

%description
This is a tool which bends containers using Ansible playbooks and
turns them into container images. It has a pluggable builder selection
- it is up to you to pick the tool which will be used to construct
your container image. Right now the only supported builder is
buildah. More to come in the future. Ansible-bender (ab) relies on
Ansible connection plugins for performing builds.

tl;dr Ansible is the frontend, buildah is the backend.

%prep
%autosetup


%build
%pyproject_wheel


%install
%pyproject_install


%if %{with check}
%check
%pytest \
  -v \
  --disable-pytest-warnings \
  --numprocesses=auto \
%if %{with privileged_tests}
  tests
%else
  tests/unit
%endif
%endif


%files
%{python3_sitelib}/ansible_bender-*.dist-info/
%{python3_sitelib}/ansible_bender/
%{_bindir}/ansible-bender
%license LICENSE
%doc docs/* README.md



%changelog
%autochangelog
