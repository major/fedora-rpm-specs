# when bootstrapping Python, pytest-xdist is not yet available
%bcond xdist %{undefined rhel}

# Package the placeholder rpm-macros (moved to redhat-rpm-config in F40)
%if ! (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
%bcond rpmmacropkg 1
%else
%bcond rpmmacropkg 0
%endif

# Appease old Poetry versions (<1.2.0a2)
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 38 || 0%{?rhel} >= 10
%bcond oldpoetry 0
%else
%bcond oldpoetry 1
%endif

%global srcname rpmautospec
%global canonicalname %{py_dist_name %{srcname}}

Name: python-%{canonicalname}
Version: 0.3.8
Release: %autorelease
Summary: Package and CLI tool to generate release fields and changelogs
License: MIT
URL: https://github.com/fedora-infra/%{canonicalname}
Source0: https://github.com/fedora-infra/%{canonicalname}/releases/download/%{version}/%{canonicalname}-%{version}.tar.gz
Patch100: rpmautospec-0.3.7-old-poetry.patch

BuildArch: noarch
BuildRequires: git
# the langpacks are needed for tests
BuildRequires: glibc-langpack-de
BuildRequires: glibc-langpack-en
BuildRequires: koji
BuildRequires: python3-devel >= 3.9.0
# The dependencies needed for testing don’t get auto-generated.
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-cov)
%if %{with xdist}
BuildRequires: python3dist(pytest-xdist)
%endif
BuildRequires: python3dist(pyyaml)
BuildRequires: sed

%global _description %{expand:
A package and CLI tool to generate RPM release fields and changelogs.}

%description %_description

%package -n python3-%{canonicalname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires: koji
Requires: rpm
# for "rpm --specfile"
Requires: rpm-build >= 4.9

%description -n python3-%{canonicalname} %_description

%package -n %{canonicalname}
Summary:  CLI tool for generating RPM releases and changelogs
Requires: python3-%{canonicalname} = %{version}-%{release}

%description -n %{canonicalname}
CLI tool for generating RPM releases and changelogs

%package -n koji-builder-plugin-rpmautospec
Summary: Koji plugin for generating RPM releases and changelogs
Requires: python3-%{canonicalname} = %{version}-%{release}
Requires: koji-builder-plugins

%description -n koji-builder-plugin-rpmautospec
A Koji plugin for generating RPM releases and changelogs.

%if %{with rpmmacropkg}
%package -n rpmautospec-rpm-macros
Summary: Rpmautospec RPM macros for local rpmbuild
Requires: rpm

%description -n rpmautospec-rpm-macros
This package contains RPM macros with placeholders for building rpmautospec
enabled packages locally.
%endif

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{srcname}-%{version} -N
%autopatch -M 99
%if %{with oldpoetry}
%autopatch 100
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}
# Work around poetry not listing license files as such in package metadata.
sed -i -e 's|^\(.*/LICENSE\)|%%license \1|g' %{pyproject_files}

mkdir -p  %{buildroot}%{_prefix}/lib/koji-builder-plugins/
install -m 0644 koji_plugins/rpmautospec_builder.py \
    %{buildroot}%{_prefix}/lib/koji-builder-plugins/

%py_byte_compile %{python3} %{buildroot}%{_prefix}/lib/koji-builder-plugins/

%if %{with rpmmacropkg}
mkdir -p %{buildroot}%{rpmmacrodir}
install -m 644  rpm/macros.d/macros.rpmautospec %{buildroot}%{rpmmacrodir}/
%endif

%check
%pytest -v \
%if %{with xdist}
--numprocesses=auto
%endif

%files -n python3-%{canonicalname} -f %{pyproject_files}
%doc README.rst

%files -n %{canonicalname}
%{_bindir}/rpmautospec

%files -n koji-builder-plugin-rpmautospec
%{_prefix}/lib/koji-builder-plugins/*

%if %{with rpmmacropkg}
%files -n rpmautospec-rpm-macros
%{rpmmacrodir}/macros.rpmautospec
%endif

%changelog
%autochangelog
