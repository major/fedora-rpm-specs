%global         pypi_name mycli
Summary:        Interactive CLI for MySQL Database with auto-completion and syntax highlighting
Name:           mycli
Version:        1.27.2
Release:        6%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://mycli.net
Source0:        %{pypi_source}
Patch0:         mycli-1.27.1-reqs.patch
Patch1:         mycli-1.26.1-paramiko.patch
Patch2:         mycli-1.26.1-pycryptodomex.patch
Patch3:         mycli-1.27.0-test_auto_escaped_col_names.patch
Patch4:         mycli-1.27.2-py313.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest) >= 2.7.0
BuildRequires:  python3dist(behave) >= 1.2.4
BuildRequires:  python3dist(pexpect) >= 3.3
BuildRequires:  python3dist(paramiko) >= 2.7.2
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(prompt-toolkit) >= 3.0.5
BuildRequires:  python3dist(cli-helpers) >= 2.0.1
BuildRequires:  python3dist(cli-helpers[styles]) >= 2.0.1
BuildRequires:  python3dist(configobj) >= 5.0.5
BuildRequires:  python3dist(pycryptodomex)
BuildRequires:  python3dist(pymysql) >= 0.9.2
BuildRequires:  python3dist(pyperclip)
Suggests:       python3-mycli+ssh
%py_provides    python3-%{pypi_name}

%description
Nice interactive shell for MySQL Database with auto-completion and
syntax highlighting.

%pyproject_extras_subpkg -n python3-%{pypi_name} ssh
%generate_buildrequires
%pyproject_buildrequires -x ssh

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -f %{pyproject_files}
%license LICENSE.txt
%doc mycli/AUTHORS README.md mycli/SPONSORS
%{_bindir}/%{pypi_name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.27.2-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.27.2-3
- Rebuilt for Python 3.13

* Tue May 07 2024 Terje Rosten <terje.rosten@ntnu.no> - 1.27.2-2
- Add patch to build with Python 3.13

* Wed Apr 10 2024 Terje Rosten <terje.rosten@ntnu.no> - 1.27.2-1
- 1.27.2

* Mon Apr 01 2024 Terje Rosten <terje.rosten@ntnu.no> - 1.27.1-1
- 1.27.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 13 2023 Terje Rosten <terje.rosten@ntnu.no> - 1.27.0-1
- 1.27.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.26.1-4
- Rebuilt for Python 3.12

* Sun Apr 16 2023 Terje Rosten <terje.rosten@ntnu.no> - 1.26.1-3
- Switch from pyaes to pycryptodomex

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 05 2022 Terje Rosten <terje.rosten@ntnu.no> - 1.26.1-1
- 1.26.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Terje Rosten <terje.rosten@ntnu.no> - 1.25.0-3
- Some strange 3.11 error in tests

* Mon Jun 27 2022 Python Maint <python-maint@redhat.com> - 1.25.0-2
- Rebuilt for Python 3.11

* Sat Apr 02 2022 Terje Rosten <terje.rosten@ntnu.no> - 1.25.0-1
- 1.25.0

* Sun Jan 23 2022 Terje Rosten <terje.rosten@ntnu.no> - 1.24.3-1
- 1.24.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Terje Rosten <terje.rosten@ntnu.no> - 1.24.2-1
- 1.24.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.24.1-3
- Rebuilt for Python 3.10

* Sat May 8 2021 Dick Marinus <dick@mrns.nl> - 1.24.1-2
- Use pyproject-rpm-macros to eliminate error-prone manual BR’s
- Do not manually duplicate automatic Requires
- Do not use obsolete python_provide macro; use py_provides macro instead
- Add the Python extras metapackage for the keyring extra
- Use the pytest macro
- Switch to HTTPS URL

* Sun Mar 14 2021 Terje Rosten <terje.rosten@ntnu.no> - 1.24.1-1
- 1.24.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Terje Rosten <terje.rosten@ntnu.no> - 1.23.2-1
- 1.23.2

* Thu Jan 14 2021 Terje Rosten <terje.rosten@ntnu.no> - 1.23.0-1
- 1.23.0
- Adjust reqs to more sensible levels

* Sun Oct 11 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.22.2-1
- 1.22.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.22.1-1
- 1.22.1

* Fri Jul 24 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.21.1-6
- Make srpm to be identical on all branches and fix pymysql 0.10 issue

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.21.1-5
- Rebuilt for Python 3.9

* Thu May 07 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.21.1-4
- Use prompt toolkit 3.0.0 on f33+

* Tue May 05 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.21.1-3
- Use sqlparse 0.3.0 on f32+

* Sun May 03 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.21.1-2
- Add patch to find default socket file

* Sun May 03 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.21.1-1
- 1.21.1

* Sun May 03 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.21.0-1
- 1.21.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.20.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.20.1-1
- 1.20.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.20.0-4
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.20.0-3
- Don't mask failures

* Wed Aug 14 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.20.0-2
- Add sqlparse 0.2.4 patch from Dick Marinus, thanks!

* Tue Aug 13 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.20.0-1
- 1.20.0

* Fri Aug 09 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.19.0-4
- Fix build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.19.0-1
- 1.19.0

* Mon Nov 12 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.18.2-2
- Fix prompt_toolkit 1 patch, update by Dick

* Wed Nov 07 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.18.2-1
- 1.18.2
- Add patch for compat with prompt_toolkit 1, thanks to Dick Marinus
- Add patch to work with prompt_toolkit > 2.0.6

* Fri Oct 19 2018 Carl George <carl@george.computer> - 1.18.0-2
- Add patch0 for prompt_toolkit 2 compatibility

* Sun Sep 30 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.18.0-1
- 1.18.0

* Sat Jul 14 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.17.0-4
- Tests started to fail again

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.17.0-1
- 1.17.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.16.0-1
- 1.16.0

* Sun Oct 01 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.13.1-1
- 1.13.1

* Sun Sep 24 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.13.0-2
- Skip tests on older releases

* Sat Sep 23 2017 Dick Marinus <dick@mrns.nl> - 1.13.0-1
- 1.13.0

* Sat Sep 02 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.12.1-2
- Fix date
- Remove sedding

* Thu Aug 31 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.12.1-1
- 1.12.1
- Adjust reqs.
- Remove all patches

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 20 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.10.0-2
- Add patch from Dick Marinus to fix sqlparse issue

* Sat May 06 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.10.0-1
- 1.10.0

* Tue Feb 14 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.8.1-4
- Add patch to work with sqlparse >= 0.2.2 (rhbz#1422211)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-2
- Rebuild for Python 3.6

* Tue Oct 25 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.8.1-1
- 1.8.1

* Sat Sep 17 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.8.0-2
- Add patch from Dick Marinus to fix issue with newer sqlparse

* Tue Aug 09 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.8.0-1
- 1.8.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 13 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.7.0-1
- 1.7.0

* Sun Mar 27 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.6.0-1
- 1.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.5.2-4
- Add patch to enable prompt_toolkit 0.57 support.

* Thu Jan 07 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.5.2-3
- Remove configobj patch
- Use name macro

* Sun Jan 03 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.5.2-2
- remove egginfo
- fix deps and summary

* Sat Jan 02 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.5.2-1
- initial package
