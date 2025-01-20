# Some tests fail. Pass --with all_tests to retry
%bcond_with all_tests

# Created by pyp2rpm-3.3.4
%global pypi_name authheaders

Name:           python-%{pypi_name}
Version:        0.16.3
Release:        2%{?dist}
Summary:        A library wrapping email authentication header verification and generation

# Licensing described in LICENSE file
License:        MIT and ZPL-2.1
URL:            https://github.com/ValiMail/authentication-headers
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  help2man

%description
%{summary}.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       publicsuffix-list

%description -n python3-%{pypi_name}
%{summary}.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled publicsuffix data
rm -f %{pypi_name}/public_suffix_list.txt
# Use public suffix data from installed RPM
ln -s %{_datadir}/publicsuffix/public_suffix_list.dat %{pypi_name}/public_suffix_list.txt
# fix shebang
sed -i '/^#!\/usr\/bin\/python3/,+2 d' %{pypi_name}/dmarcpolicyfind.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} help2man --no-info \
  --name="Find DMARC policy for a domain" \
  --version-string=%{version} \
  %{buildroot}%{_bindir}/dmarc-policy-find \
  -o %{buildroot}%{_mandir}/man1/dmarc-policy-find.1

%check
%pyproject_check_import %{pypi_name}
# test_authenticate_dmarc_psdsub: test fixture not shipped
%pytest -v \
%if %{without all_tests}
  -k "not test_authenticate_dmarc_psdsub" \
%endif
;

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGES
%license COPYING
%{_bindir}/dmarc-policy-find
%{_mandir}/man1/dmarc-policy-find.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Michel Lind <salimma@fedoraproject.org> - 0.16.3-1
- Update to version 0.16.3; Fixes: RHBZ#2258214
- Fix rpmlint issues

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.15.3-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 25 2023 Michel Lind <salimma@fedoraproject.org> - 0.15.3-1
- Update to 0.15.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.15.2-2
- Rebuilt for Python 3.12

* Mon Mar 27 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.15.2-1
- Update to 0.15.2
- Convert to SPDX
- Convert to new Python guidelines
- Run tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.13.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.13.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Neal Gompa <ngompa13@gmail.com> - 0.13.0-1
- Initial package.
