%global pypi_name podman
%global desc %{pypi_name} is a library of bindings to use the RESTful API for Podman.

%global pypi_dist 4
%global built_tag v4.2.0
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

Name: python-%{pypi_name}
Epoch: 3
Version: %{gen_version}
License: ASL 2.0
Release: %autorelease
Summary: RESTful API for Podman
URL: https://github.com/containers/%{pypi_name}-py
# Tarball fetched from upstream
Source0: %{url}/releases/download/%{built_tag}/%{pypi_name}-%{version}.tar.gz
BuildArch: noarch

%description
%desc

%package -n python%{python3_pkgversion}-%{pypi_name}
BuildRequires: git-core
BuildRequires: python%{python3_pkgversion}-devel
%if ! 0%{?fedora} && 0%{?rhel} <= 8
BuildRequires: python%{python3_pkgversion}-pytoml
BuildRequires: python%{python3_pkgversion}-requests
BuildRequires: python%{python3_pkgversion}-setuptools
Requires: python%{python3_pkgversion}-pytoml
Requires: python%{python3_pkgversion}-requests
%else
BuildRequires: pyproject-rpm-macros
%endif
%if 0%{?centos} <= 8
BuildRequires: python%{python3_pkgversion}-pyxdg
Requires: python%{python3_pkgversion}-pyxdg
%endif
BuildRequires: python%{python3_pkgversion}-requests
BuildRequires: python%{python3_pkgversion}-toml
Requires: python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-toml
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
%if 0%{?rhel} <= 8
%py3_build
%else
%pyproject_wheel
%endif

%install
export PBR_VERSION="0.0.0"
%if 0%{?rhel} <= 8
%py3_install
%else
%pyproject_install
%pyproject_save_files %{pypi_name}
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
%autochangelog
