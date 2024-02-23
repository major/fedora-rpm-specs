# The pytest-xdist package is not available when bootstrapping or for EL builds
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

Name: python-%{srcname}
Version: 0.6.3
Release: %autorelease
Summary: Package and CLI tool to generate release fields and changelogs
License: MIT
URL: https://github.com/fedora-infra/%{srcname}
Source0: https://github.com/fedora-infra/%{srcname}/releases/download/%{version}/%{srcname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: git
# the langpacks are needed for tests
BuildRequires: glibc-langpack-de
BuildRequires: glibc-langpack-en
BuildRequires: python3-devel >= 3.9.0
# The dependencies needed for testing don’t get auto-generated.
BuildRequires: python3dist(pytest)
%if %{with xdist}
BuildRequires: python3dist(pytest-xdist)
%endif
BuildRequires: python3dist(pyyaml)
BuildRequires: sed

%global _description %{expand:
A package and CLI tool to generate RPM release fields and changelogs.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%package -n %{srcname}
Summary:  CLI tool for generating RPM releases and changelogs
Requires: python3-%{srcname} = %{version}-%{release}

%description -n %{srcname}
CLI tool for generating RPM releases and changelogs

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
%autosetup -n %{srcname}-%{version}
%if %{with oldpoetry}
sed -i \
    -e 's/\[tool\.poetry\.group\.dev\.dependencies\]/[tool.poetry.dev-dependencies]/g' \
    pyproject.toml
%endif

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -i -e '/pytest-cov/d; /addopts.*--cov/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}
# Work around poetry not listing license files as such in package metadata.
sed -i -e 's|^\(.*/LICENSE\)|%%license \1|g' %{pyproject_files}

%if %{with rpmmacropkg}
mkdir -p %{buildroot}%{rpmmacrodir}
install -m 644  rpm/macros.d/macros.rpmautospec %{buildroot}%{rpmmacrodir}/
%endif

%check
%pytest -v \
%if %{with xdist}
--numprocesses=auto
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%files -n %{srcname}
%{_bindir}/rpmautospec

%if %{with rpmmacropkg}
%files -n rpmautospec-rpm-macros
%{rpmmacrodir}/macros.rpmautospec
%endif

%changelog
%autochangelog
