# This specfile is licensed under:
#
# Copyright (C) 2022 Maxwell G <gotmax@e.email>
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT.html

%bcond libdnf5 %[0%{?fedora} >= 38]

Name:           fedrq
Version:        1.4.0
Release:        2%{?dist}
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

BuildRequires:  python3-devel
# Test deps
BuildRequires:  createrepo_c
BuildRequires:  distribution-gpg-keys
BuildRequires:  python3-argcomplete
BuildRequires:  python3-dnf
%if %{with libdnf5}
BuildRequires:  python3-libdnf5
%endif
# Manpage
BuildRequires:  scdoc

Requires:       (python3-dnf or python3-libdnf5)
Suggests:       (python3-libdnf5 if dnf5)
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
bash -x ./tests/test_data/build.sh

# Use python3 -m to ensure the current directory is part of sys.path so the
# tests can import from its own package.

FEDRQ_BACKEND=dnf %{py3_test_envvars} \
    %{python3} -m pytest -v -m "not no_rpm_mock"

%if %{with libdnf5}
# Some tests are failing only in mock and only with Python 3.12
#   RuntimeError: Failed to download metadata
%if v"0%{?python3_version}" >= v"3.12"
%global skips %{shrink:
    not test_smartcache_not_used
    and not test_smartcache_config
    and not test_baseurl_repog
}
%endif
FEDRQ_BACKEND=libdnf5 %{py3_test_envvars} \
    %{python3} -m pytest -v -m "not no_rpm_mock" %{?skips:-k '%{skips}'}
%endif


%files -f %{pyproject_files}
# Licenses are included in the wheel
%license %{_licensedir}/fedrq/
%doc README.md CONTRIBUTING.md NEWS.md contrib/api_examples
%{_bindir}/fedrq*
%{bash_completions_dir}/fedrq
%{fish_completions_dir}/fedrq.fish
%{_mandir}/man1/fedrq.1*
%{_mandir}/man5/fedrq.5*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 01 2024 Maxwell G <maxwell@gtmx.me> - 1.4.0-1
- Update to 1.4.0.

* Tue Aug 27 2024 Maxwell G <maxwell@gtmx.me> - 1.3.0-1
- Update to 1.3.0.

* Sat Aug 03 2024 Maxwell G <maxwell@gtmx.me> - 1.2.0-1
- Update to 1.2.0.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 29 2024 Python Maint <python-maint@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.13

* Thu May 30 2024 Maxwell G <maxwell@gtmx.me> - 1.1.0-2
- Add patch to fix rpm 4.20 test failures

* Wed May 01 2024 Maxwell G <maxwell@gtmx.me> - 1.1.0-1
- Update to 1.1.0.

* Mon Apr 01 2024 Maxwell G <maxwell@gtmx.me> - 1.0.0-1
- Update to 1.0.0.

* Wed Feb 14 2024 Maxwell G <maxwell@gtmx.me> - 0.15.0-1
- Update to 0.15.0.

* Wed Feb 07 2024 Maxwell G <maxwell@gtmx.me> - 0.14.0-1
- Update to 0.14.0.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Maxwell G <maxwell@gtmx.me> - 0.13.0-2
- Reenable libdnf5 tests

* Mon Dec 18 2023 Maxwell G <maxwell@gtmx.me> - 0.13.0-1
- Update to 0.13.0.

* Mon Sep 11 2023 Maxwell G <maxwell@gtmx.me> - 0.12.0-1
- Update to 0.12.0.

* Thu Aug 31 2023 Maxwell G <maxwell@gtmx.me> - 0.11.0-1
- Update to 0.11.0.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Maxwell G <maxwell@gtmx.me> - 0.10.0-1
- Update to 0.10.0.

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.9.0-2
- Rebuilt for Python 3.12
- Fixes: rhbz#2219993

* Thu Jun 29 2023 Maxwell G <maxwell@gtmx.me> - 0.9.0-1
- Update to 0.9.0.

* Wed Jun 21 2023 Maxwell G <maxwell@gtmx.me> - 0.8.0-1
- Update to 0.8.0.

* Wed May 31 2023 Maxwell G <maxwell@gtmx.me> - 0.7.1-1
- Update to 0.7.1.

* Mon May 29 2023 Maxwell G <maxwell@gtmx.me> - 0.7.0-1
- Update to 0.7.0.

* Sat Apr 8 2023 Maxwell G <maxwell@gtmx.me> - 0.6.0-1
- Update to 0.6.0.

* Wed Mar 22 2023 Maxwell G <maxwell@gtmx.me> - 0.5.0-1
- Initial import (rhbz#2179593)
