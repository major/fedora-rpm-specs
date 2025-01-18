# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (C) Fedora Project Authors
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT

%bcond tests 1

Name:           bindep
Version:        2.11.0
Release:        6%{?dist}
Summary:        Binary dependency utility

License:        Apache-2.0
URL:            https://docs.opendev.org/opendev/bindep
Source:         %{pypi_source bindep}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description
Bindep is a tool for checking the presence of binary packages needed to use an
application / library.


%prep
%autosetup -p1
# Remove dependencies unwanted in Fedora
sed -i -E '/(coverage|pytest-cov|mock)/d' test-requirements.txt
find -type f -name '*.py' | xargs -d'\n' sed -i \
    -e 's/^\( *\)import mock/\1from unittest import mock/' \
    -e 's/^\( *\)from mock import /\1from unittest.mock import /'


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:test-requirements.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files bindep


%check
%if %{with tests}
%pytest \
    -s \
    -k 'not test_arch_implies_pacman and not test_manjaro_implies_pacman'
%endif


%files -f %{pyproject_files}
# Note(gotmax23): Yes, pyproject_save_files and setuptools already handle
# this automatically, but I don't rely on it, as it makes it too easy to
# miss licenses when upstream changes their build system or something else.
%license LICENSE
%doc README.rst doc/source/*.rst
%{_bindir}/bindep


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.11.0-4
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 15 2023 Maxwell G <maxwell@gtmx.me> - 2.11.0-1
- Initial package. Closes rhbz#2232708.
