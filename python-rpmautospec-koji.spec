%global srcname rpmautospec_koji
%global canonicalname rpmautospec-koji

Name: python-%{canonicalname}
Version: 0.4.0
Release: %autorelease
Summary: Koji plugin for packages using rpmautospec

License: MIT
URL: https://github.com/fedora-infra/%{canonicalname}
# This …:
Source0: https://github.com/fedora-infra/%{canonicalname}/releases/download/%{version}/%{srcname}-%{version}.tar.gz
# … should be this …:
# Source0: %%{pypi_source %%{srcname}}
# … but rpmautospec is currently blocked on PyPI. See https://github.com/pypi/support/issues/3312
BuildArch: noarch
BuildRequires: python3-devel >= 3.9.0
# The dependencies needed for testing don’t get auto-generated.
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-cov)
BuildRequires: sed

%generate_buildrequires
%pyproject_buildrequires

%global _description %{expand:
A Koji plugin for generating RPM releases and changelogs with rpmautospec.}

%description %_description

%package -n python3-%{canonicalname}
Summary: %{summary}
Obsoletes: koji-builder-plugin-rpmautospec < 0.4
Provides: koji-builder-plugin-rpmautospec = %{version}-%{release}
Requires: koji-builder-plugins
Requires: redhat-rpm-config

%description -n python3-%{canonicalname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}
# Work around poetry not listing license files as such in package metadata.
sed -i -e 's|^\(.*/LICENSE\)|%%license \1|g' %{pyproject_files}

mkdir -p  %{buildroot}%{_prefix}/lib/koji-builder-plugins/
cat << EOF > %{buildroot}%{_prefix}/lib/koji-builder-plugins/rpmautospec_builder.py
from rpmautospec_koji.rpmautospec_builder import process_distgit_cb  # noqa: F401
EOF

%py_byte_compile %{python3} %{buildroot}%{_prefix}/lib/koji-builder-plugins/

%check
%pytest

%files -n python3-%{canonicalname} -f %{pyproject_files}
%{_prefix}/lib/koji-builder-plugins/*

%changelog
%autochangelog
