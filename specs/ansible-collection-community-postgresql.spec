%bcond tests %{undefined rhel}

Name:           ansible-collection-community-postgresql
Version:        3.0.0
Release:        6%{?dist}
Summary:        Manage PostgreSQL with Ansible

# See the license files in the repo root and file headers
License:        GPL-3.0-or-later AND BSD-2-Clause AND PSF-2.0
URL:            %{ansible_collection_url community postgresql}
Source:         https://github.com/ansible-collections/community.postgresql/archive/%{version}/community.postgresql-%{version}.tar.gz
# build_ignore development files, tests, and docs
Patch:          build_ignore.patch

BuildArch:      noarch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
BuildRequires:  %{py3_dist psycopg}
%endif

%description
%{summary}.


%prep
%autosetup -p1 -n community.postgresql-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +


%build
%ansible_collection_build


%install
%ansible_collection_install


%check
%if %{with tests}
%ansible_test_unit
%endif


%files -f %{ansible_collection_filelist}
%license COPYING PSF-license.txt simplified_bsd.txt
%doc README.md CHANGELOG.rst


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Maxwell G <maxwell@gtmx.me> - 3.0.0-1
- Initial package. Fixes rhbz#2222130.
