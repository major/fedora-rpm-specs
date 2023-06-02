# This specfile is licensed under:
#
# Copyright (C) 2022 Maxwell G <gotmax@e.email>
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT.html

%bcond libdnf5 %[0%{?fedora} >= 38]

Name:           fedrq
Version:        0.7.1
Release:        1%{?dist}
Summary:        A tool to query the Fedora and EPEL repositories

# - code is GPL-2.0-or-later
# - the data and config files in fedrq/data are UNLICENSEed
# - Embeded repo defs are MIT.
# - PSF-2.0 code copied from Cpython 3.11 for older Python versions
License:        GPL-2.0-or-later AND Unlicense AND MIT AND PSF-2.0
URL:            https://fedrq.gtmx.me
%global furl    https://git.sr.ht/~gotmax23/fedrq
Source0:        %{furl}/refs/download/v%{version}/fedrq-%{version}.tar.gz
Source1:        %{furl}/refs/download/v%{version}/fedrq-%{version}.tar.gz.asc
Source2:        https://meta.sr.ht/~gotmax23.pgp

BuildArch:      noarch

BuildRequires:  tomcli+tomlkit
BuildRequires:  python3-devel
# Test deps
BuildRequires:  createrepo_c
BuildRequires:  distribution-gpg-keys
BuildRequires:  python3-argcomplete
BuildRequires:  python3-dnf
%if %{with libdnf5}
BuildRequires:  python3-libdnf5
BuildRequires:  python3-rpm
%endif
# Manpage
BuildRequires:  scdoc

Requires:       (python3-dnf or (python3-libdnf5 and python3-rpm))
Suggests:       python3-dnf
Requires:       distribution-gpg-keys
Recommends:     fedora-repos-rawhide
Recommends:     python3-argcomplete

# fedrq config --dump
Recommends:     python3-tomli-w


%description
fedrq is a tool to query the Fedora and EPEL repositories.


%prep
%gpgverify -d0 -s1 -k2
%autosetup -p1

# See the comments in pyproject.toml
tomcli-set pyproject.toml del tool.flit.external-data
tomcli-set pyproject.toml list build-system.requires "flit_core >=3.2,<4"

%generate_buildrequires
%pyproject_buildrequires -x test


%build
%py3_shebang_fix contrib/api_examples/*.py

%pyproject_wheel
scdoc <doc/fedrq.1.scd >fedrq.1
scdoc <doc/fedrq.5.scd >fedrq.5
register-python-argcomplete --shell bash fedrq >fedrq.bash
register-python-argcomplete --shell fish fedrq >fedrq.fish


%install
%pyproject_install
%pyproject_save_files fedrq
install -Dpm 0644 fedrq.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 fedrq.5 -t %{buildroot}%{_mandir}/man5/
install -Dpm 0644 fedrq.bash %{buildroot}%{bash_completions_dir}/fedrq
install -Dpm 0644 fedrq.fish %{buildroot}%{fish_completions_dir}/fedrq.fish


%check
FEDRQ_BACKEND=dnf %pytest -v -m "not no_rpm_mock"
%if %{with libdnf5}
FEDRQ_BACKEND=libdnf5 %pytest -v -m "not no_rpm_mock"
%endif


%files -f %{pyproject_files}
# Licenses are included in the wheel
%license LICENSES/*.txt
%doc README.md CONTRIBUTING.md NEWS.md contrib/api_examples
%{_bindir}/fedrq*
%{bash_completions_dir}/fedrq
%{fish_completions_dir}/fedrq.fish
%{_mandir}/man1/fedrq.1*
%{_mandir}/man5/fedrq.5*


%changelog
* Wed May 31 2023 Maxwell G <maxwell@gtmx.me> - 0.7.1-1
- Update to 0.7.1.

* Mon May 29 2023 Maxwell G <maxwell@gtmx.me> - 0.7.0-1
- Update to 0.7.0.

* Sat Apr 8 2023 Maxwell G <maxwell@gtmx.me> - 0.6.0-1
- Update to 0.6.0.

* Wed Mar 22 2023 Maxwell G <maxwell@gtmx.me> - 0.5.0-1
- Initial import (rhbz#2179593)
