%if (%{defined fedora} && 0%{?fedora} <= 42) || (%{defined rhel} && 0%{?rhel} <= 10)
# setuptools < 77, can't use new license metadata
%bcond old_setuptools 1
%else
%bcond old_setuptools 0
%endif

Name:           python-merge3
Version:        0.0.16
Release:        %autorelease
Summary:        Python implementation of 3-way merge
License:        GPL-2.0-or-later
URL:            https://www.breezy-vcs.org
# PyPI source does not contain tests
# Source:         %%{pypi_source merge3}
Source:         https://github.com/breezy-team/merge3/archive/v%{version}/merge3-%{version}.tar.gz
# pass -v in tox.ini to unittest invocation
Patch:          merge3-verbose-testlog.diff
# conditional patches (1000+)
Patch1000:      merge3-revert-setuptools-bump.diff

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%global _description %{expand:
A Python implementation of 3-way merge of texts.

Given BASE, OTHER, THIS, tries to produce a combined text
incorporating the changes from both BASE->OTHER and BASE->THIS.
All three will typically be sequences of lines.}

%description %{_description}


%package -n python3-merge3
Summary:        %{summary}

%description -n python3-merge3 %{_description}


%prep
%autosetup -n merge3-%{version} -N
%autopatch -p1 -M 999
%if %{with old_setuptools}
%autopatch -p1 1000
%endif

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files merge3


%check
%tox


%files -n python3-merge3 -f %{pyproject_files}
# license already auto-detected, verified with rpm -qpL
%doc README.rst
%{_bindir}/merge3


%changelog
%autochangelog
