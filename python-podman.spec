%if "%{_vendor}" == "debbuild"
%global python3_pkgversion 3
%endif

%global pypi_name podman
%global desc %{pypi_name} is a library of bindings to use the RESTful API for Podman.

%global pypi_dist 4
%global built_tag_strip 4.2.0

Name: python-%{pypi_name}
Epoch: 3
Version: 4.2.0
%if "%{_vendor}" == "debbuild"
Packager: Podman Debbuild Maintainers <https://github.com/orgs/containers/teams/podman-debbuild-maintainers>
License: ASL-2.0
Release: 0%{?dist}
%else
License: ASL 2.0
Release: %autorelease
%endif
Summary: RESTful API for Podman
URL: https://github.com/containers/%{pypi_name}-py
Source0: %{url}/releases/download/v%{built_tag_strip}/%{pypi_name}-%{version}.tar.gz
BuildArch: noarch

%description 
%desc

%package -n python%{python3_pkgversion}-%{pypi_name}
%if "%{_vendor}" == "debbuild"
BuildRequires: git
BuildRequires: python%{python3_pkgversion}-dev
%else
BuildRequires: git-core
BuildRequires: python%{python3_pkgversion}-devel
%endif
%if ("%{_vendor}" == "debbuild") || (! 0%{?fedora} && 0%{?rhel} <= 8)
BuildRequires: python%{python3_pkgversion}-pytoml
BuildRequires: python%{python3_pkgversion}-requests
BuildRequires: python%{python3_pkgversion}-setuptools
Requires: python%{python3_pkgversion}-pytoml
Requires: python%{python3_pkgversion}-requests
%else
BuildRequires: pyproject-rpm-macros
%endif
%if "%{_vendor}" == "debbuild"
BuildRequires: python%{python3_pkgversion}-xdg
Requires: python%{python3_pkgversion}-xdg
%else
%if 0%{?centos} <= 8
BuildRequires: python%{python3_pkgversion}-pyxdg
Requires: python%{python3_pkgversion}-pyxdg
%endif
%if 0%{?fedora} == 35
BuildRequires: python%{python3_pkgversion}-toml
Requires: python%{python3_pkgversion}-toml
%endif
%endif
Provides: %{pypi_name}-py = %{version}-%{release}
Provides: python%{python3_pkgversion}dist(%{pypi_name}) = %{pypi_dist}
Provides: python%{python3_version}dist(%{pypi_name}) = %{pypi_dist}
Obsoletes: python%{python3_pkgversion}-%{pypi_name}-api <= 0.0.0-1
Provides: python%{python3_pkgversion}-%{pypi_name}-api = %{epoch}:%{version}-%{release}
Summary: %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%desc

%prep
%autosetup -Sgit -n %{pypi_name}-%{built_tag_strip}

%if 0%{?fedora} || 0%{?rhel} >= 9
%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}
%endif

%build
export PBR_VERSION="0.0.0"
%if "%{_vendor}" == "debbuild"
python3 setup.py sdist bdist
%else
%if 0%{?rhel} <= 8
%py3_build
%else
%pyproject_wheel
%endif
%endif

%install
export PBR_VERSION="0.0.0"
%if "%{_vendor}" == "debbuild"
python3 setup.py install --root %{buildroot}
%else
%if 0%{?rhel} <= 8
%py3_install
%else
%pyproject_install
%pyproject_save_files %{pypi_name}
%endif
%endif

%if 0%{?rhel} <= 8
%files -n python3-podman
%license LICENSE
%doc README.md
%{python3_sitelib}/podman/*
%{python3_sitelib}/podman-*/*
%else
%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%endif

%changelog
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
