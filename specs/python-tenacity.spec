%global pypi_name tenacity
%global _description %{expand:
Tenacity is a general-purpose retrying library to simplify the task of adding
retry behavior to just about anything.}

Name:           python-%{pypi_name}
Version:        8.2.3
Release:        6%{?dist}
Summary:        Retry code until it succeeds
License:        Apache-2.0
URL:            https://github.com/jd/%{pypi_name}
Source:         %{pypi_source}
BuildArch:      noarch

%description %{_description}

%package -n python3-%{pypi_name}
Summary:          %{summary}
BuildRequires:    python3-devel
# for tests
BuildRequires:    python3-pytest
BuildRequires:    python3-tornado


%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p 1
# Avoid type checking dependency
sed -e '/typeguard/d' -i setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -k "not test_retry_type_annotations"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 8.2.3-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 15 2023 Jonathan Wright <jonathan@almalinux.org> - 8.2.3-1
- Update to 8.2.3 rhbz#2231911

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 22 2023 Python Maint <python-maint@redhat.com> - 8.2.2-2
- Rebuilt for Python 3.12

* Sat Mar 25 2023 Jonathan Wright <jonathan@almalinux.org - 8.2.2-1
- Update to 8.2.2 rhbz#2129009

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Carl George <carl@george.computer> - 8.0.1-5
- Convert to pyproject macros

* Sat Jul 02 2022 Orion Poplawski <orion@nwra.com> - 8.0.1-4
- Skip typeguard tests

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 8.0.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 09 2021 Matthias Runge <mrunge@redhat.com> - 8.0.1-1
- update to 8.0.1 (rhbz#1980599)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.0.0-2
- Rebuilt for Python 3.10

* Thu Mar 4 2021 Christopher Brown <chris.brown@redhat.com> - 7.0.0-1
- Update to 7.0.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Christopher Brown <chris.brown@redhat.com> - 6.3.1-1
- Update to 6.3.1

* Fri Sep 04 2020 Yatin Karel <ykarel@redhat.com> - 6.2.0-1
- Update to 6.2.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-2
- Rebuilt for Python 3.9

* Tue Feb 4 2020 Christopher Brown <chris.brown@redhat.com> - 6.0.0-1
- Bump to 6.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-2
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Christopher Brown <chris.brown@redhat.com> - 5.1.1-1
- Bump to 5.1.1
- Add setuptools_scm BR

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Christopher Brown <chris.brown@redhat.com> - 5.0.4-1
- Bump to 5.0.4

* Wed Jan 30 2019 Christopher Brown <chris.brown@redhat.com> - 5.0.3-1
- Bump to 5.0.3

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.2-2
- Enable python dependency generator

* Tue Dec 4 2018 Christopher Brown <chris.brown@redhat.com> - 5.0.2-1
- Bump to 5.0.2
  Add conditionals for F30 and CentOS
  Add description macro

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.12.0-2
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Thu Jul 19 2018 Matthias Runge <mrunge@redhat.com> - 4.12.0-1
- rebase to 4.12.0 (rhbz#1551561)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 13 2018 Pradeep Kilambi <pkilambi@redhat.com> - 4.9.0-1
- rebase to 4.9.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.8.0-3
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.8.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 16 2018 Pradeep Kilambi <pkilambi@redhat.com> - 4.8.0-1
- rebase to 4.8.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug  5 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 4.4.0-1
- Upstream 4.4.0
- Run unit tests

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-2
- Rebuild for Python 3.6

* Thu Oct 06 2016 Pradeep Kilambi <pkilambi@redhat.com> - 3.2.1-1
- rebase to 3.2.1

* Wed Sep 07 2016 Pradeep Kilambi <pkilambi@redhat.com> - 3.0.0-1
- initial package release
