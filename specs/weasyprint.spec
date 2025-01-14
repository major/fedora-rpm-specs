%global modname weasyprint
%global srcname weasyprint

Name:           weasyprint
Version:        63.1
Release:        1%{?dist}
Summary:        Utility to render HTML and CSS to PDF

License:        BSD-3-Clause
URL:            https://weasyprint.org
Source0:        %{pypi_source weasyprint}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# used as "build-backend" in pyproject.toml but not detected by Fedora's
# macros to generate build requirements
BuildRequires:  python3dist(flit-core)
# requirements for testing
BuildRequires:  dejavu-fonts-all
BuildRequires:  ghostscript
# https://doc.courtbouillon.org/weasyprint/latest/first_steps.html
BuildRequires:  pango >= 1.44.0
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)

Requires:       python3-weasyprint = %{version}-%{release}


%description
WeasyPrint can render HTML and CSS to PDF. It aims to support web standards
for printing.

%package -n python3-weasyprint
Summary:        Python library to render HTML and CSS to PDF
Requires:       pango >= 1.44.0
# other Python dependencies will be picked up automatically
# Weasyprint will fail if no fonts are installed. There's no way to know
# what fonts the user would actually want, but require a few common ones
# that might be useful:
Requires:       dejavu-sans-fonts
Requires:       dejavu-sans-mono-fonts
Requires:       dejavu-serif-fonts

%description -n python3-weasyprint
The WeasyPrint Python library is a rendering engine for HTML and CSS that
can export to PDF. It aims to support web standards for printing.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest -n auto
# do not ship tests
rm -rf %{buildroot}%{python3_sitelib}/%{modname}/tests

%files
%license LICENSE
%doc README.rst
%{_bindir}/weasyprint

%files -n python3-weasyprint
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}-%{version}.dist-info/
%{python3_sitelib}/%{modname}/

%changelog
* Sat Jan 11 2025 Felix Schwarz <fschwarz@fedoraproject.org> - 63.1-1
- update to 63.1

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 62.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 62.3-1
- update to 62.3

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 62.2-2
- Rebuilt for Python 3.13

* Tue Jun 04 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 62.2-1
- update to 62.2

* Mon May 06 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 62.1-1
- update to 62.1

* Thu May 02 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 62.0-1
- update to 62.0

* Sat Mar 09 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 61.2-1
- update to 61.2

* Mon Feb 26 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 61.1-1
- update to 61.1

* Mon Feb 12 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 61.0-1
- update to 61.0

* Thu Jan 25 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 60.2-2
- use just flit-core as build dependency

* Tue Dec 12 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 60.2-1
- update to 60.2

* Thu Oct 05 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 60.1-1
- update to 60.1

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 59.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 09 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 59.0-2
- add patch so the test suite passes for Python 3.12

* Thu May 11 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 59.0-1
- update to 59.0

* Sat Apr 15 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 58.1-2
- SPDX migration
- make tests pass with pydyf 0.6

* Tue Mar 07 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 58.1-1
- update to 58.1

* Fri Feb 17 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 58.0-1
- update to 58.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 57.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 57.2-1
- update to 57.2

* Sat Nov 05 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 57.1-1
- update to 57.1

* Mon Jul 25 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 56.1-1
- update to 56.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 56.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 56.0-1
- update to 56.0

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 55.0-2
- Rebuilt for Python 3.11

* Thu May 12 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 55.0-1
- update to 55.0

* Mon Apr 04 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 54.3-1
- update to 54.3

* Tue Mar 01 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 54.2-1
- update to 54.2

* Mon Jan 31 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 54.1-1
- update to 54.1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 54.0-1
- update to 54.0

* Sun Nov 14 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 53.4-1
- update to 53.4

* Fri Sep 10 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 53.3-1
- update to 53.3

* Fri Aug 27 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 53.2-1
- update to 53.2

* Sun Aug 22 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 53.1-1
- update to 53.1

* Sun Aug 01 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 53.0-1
- update to 53.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 52.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 52.5-2
- Rebuilt for Python 3.10

* Sun Apr 18 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 52.5-1
- update to 52.5

* Tue Mar 23 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 52.4-2
- add patch for pango 1.48.3

* Fri Mar 12 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 52.4-1
- update to 52.4

* Tue Mar 02 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 52.3-1
- update to 52.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 52.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec  6 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 52.2-1
- update to 52.2

* Sun Nov 08 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 52.1-1
- update to 52.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 51-4
- Rebuilt for Python 3.9

* Wed Mar 04 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 51-3
- drop runtime requirement on "dejavu-fonts-common" (#1810150)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 2019 Felix Schwarz <fschwarz@fedoraproject.org> 51-1
- update to upstream version 51

* Sun Dec 01 2019 Felix Schwarz <fschwarz@fedoraproject.org> 50-1
- update to new upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.39-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.39-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Felix Schwarz <fschwarz@fedoraproject.org> 0.39-2
- avoid dependency on Python 3.3
- require python3-xcffib directly (#1685654)

* Tue Apr 30 2019 Eric Smith <brouhaha@fedoraproject.org> 0.39-1
- Update to newer (but not latest) upstream.

* Tue Apr 30 2019 Eric Smith <brouhaha@fedoraproject.org> 0.22-16
- Update requirements, use license macro, and other minor changes from
  Felix Schwarz <fschwarz@fedoraproject.org>.
- Use better github tarball naming.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.22-14
- Remove python2 subpackage (#1631306)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.22-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.22-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.22-9
- Python 2 binary package renamed to python2-weasyprint
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.22-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 28 2014 Eric Smith <brouhaha@fedoraproject.org> 0.22-1
- Update to latest upstream.
- No Python 3 in EL7.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Mar 20 2014 Eric Smith <brouhaha@fedoraproject.org> 0.21-3
- Add Python 3 support.
- Require python-html5lib 0.999, which has epoch 1 because
  that is newer than upstream 1.0b2.

* Fri Mar 14 2014 Eric Smith <brouhaha@fedoraproject.org> 0.21-2
- Add some missing Requires (#1076734).

* Mon Mar 10 2014 Eric Smith <brouhaha@fedoraproject.org> 0.21-1
- Update to lastest upstream.

* Sun Jul 28 2013 Eric Smith <brouhaha@fedoraproject.org> 0.19.2-3
- Remove /usr/bin/env from Python script shebang lines.

* Sun Jul 21 2013 Eric Smith <brouhaha@fedoraproject.org> 0.19.2-2
- Fixed dependencies.

* Sat Jul 20 2013 Eric Smith <brouhaha@fedoraproject.org> 0.19.2-1
- initial version
