%global owner wting

Name:           autojump
Version:        22.5.3
Release:        19%{?dist}

Summary:        A fast way to navigate your filesystem from the command line

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/%{owner}/%{name}
Source:         https://github.com/%{owner}/%{name}/archive/release-v%{version}/%{name}-%{version}.tar.gz
Patch0:         remove-homebrew-check.patch
Patch1:         install-add-distribution-arg.patch

BuildArch:      noarch

BuildRequires:  pandoc
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires: make

%description
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.


%package zsh
Requires:       %{name} = %{version}-%{release}
Summary:        Autojump for zsh

%description zsh
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.
autojump-zsh is designed to work with zsh.


%package fish
Requires:       %{name} = %{version}-%{release}
Summary:        Autojump for fish shell

%description fish
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.
autojump-fish is designed to work with fish shell.


%prep
%autosetup -p1 -n %{name}-release-v%{version}

# Use system argparse
sed -i 's|autojump_argparse|argparse|' bin/%{name}
# Fix shebangs, non .py files need to be specified manually, so we provide bin/* as well as .
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -pn . ./bin/*
sed -i '1{/^#!/d}' bin/%{name}_*.py

%build
make docs

%install
./install.py --destdir %{buildroot} --prefix usr --zshshare %{buildroot}%{_datadir}/zsh/site-functions --distribution
# Do not need bundled modules
rm %{buildroot}%{_bindir}/%{name}_argparse.py
# Move modules to proper directory
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}%{_bindir}/%{name}_*.py %{buildroot}%{python3_sitelib}/

%check
%{__python3} -m pytest tests -vv

%files
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{python3_sitelib}/%{name}_data.py
%{python3_sitelib}/%{name}_match.py
%{python3_sitelib}/%{name}_utils.py
%{python3_sitelib}/__pycache__/%{name}*.pyc
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icon.png
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%config(noreplace) %{_datadir}/%{name}/%{name}.bash

%files zsh
%config(noreplace) %{_datadir}/%{name}/%{name}.zsh
%{_datadir}/zsh/site-functions/_j

%files fish
%config(noreplace) %{_datadir}/%{name}/%{name}.fish

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 22.5.3-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 22.5.3-16
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 22.5.3-12
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 22.5.3-9
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 22.5.3-6
- Rebuilt for Python 3.10

* Thu Mar  4 2021 Tim Landscheidt <tim@tim-landscheidt.de> - 22.5.3-5
- Fix broken URL

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 22.5.3-2
- Rebuilt for Python 3.9

* Sun Mar 01 2020 Sérgio Basto <sergio@serjux.com> - 22.5.3-1
- Update to 22.5.3 (#1732680)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 22.5.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 22.5.1-7
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 22.5.1-3
- Rebuilt for Python 3.7

* Thu May 03 2018 Miro Hrončok <mhroncok@redhat.com> - 22.5.1-2
- Fix all the shebangs properly

* Mon Apr 02 2018 Miro Hrončok <mhroncok@redhat.com> - 22.5.1-1
- Update to 22.5.1
- Build docs again
- Switch to Python 3
- Run tests
- Remove obsoleted %%pre (added in F25)

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 22.3.2-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22.3.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 24 2016 Tomas Tomecek <ttomecek@redhat.com> - 22.3.2-1
- update to 22.3.2

* Wed May 4 2016 Orion Poplawski <orion@cora.nwra.com> - 22.3.0-3
- Cleanup old .pyc files in /usr/bin

* Mon May 2 2016 Orion Poplawski <orion@cora.nwra.com> - 22.3.0-2
- Use system argparse
- Install python modules to python module directory
- Fix duplicate file ownership
- Drop %%defattr()
- Use %%license

* Tue Mar 22 2016 Tomas Tomecek <ttomecek@redhat.com> - 22.3.0-1
- update to 22.3.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 22.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Tomas Tomecek <ttomecek@redhat.com> - 22.2.4-2
- patch: don't check for homebrew

* Tue Sep 08 2015 Tomas Tomecek <ttomecek@redhat.com> - 22.2.4-1
- update to 22.2.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 01 2014 Dan Horák <dan[at]danny.cz> - 21.7.1-4
- drop ExclusiveArch workaround

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Tomas Tomecek <ttomecek@redhat.com> - 21.7.1-2
- Python 3.4 rebuild

* Wed Apr 23 2014 Tomas Tomecek <ttomecek@redhat.com> - 21.7.1-1
- Update to 21.7.1

* Thu Mar 20 2014 Tomas Tomecek <ttomecek@redhat.com> - 21.6.9-1
- Update to 21.6.9

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 12 2012 Thibault North <tnorth@fedoraproject.org> - 21.1.2-2
- Fix builrequires section

* Wed Dec 12 2012 Thibault North <tnorth@fedoraproject.org> - 21.1.2-1
- Update to 21.1.2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Thibault North <tnorth@fedoraproject.org> - 20-1
- Update to version 20

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 11 2011 Thibault North <tnorth@fedoraproject.org> - 19-2
- Add symlink for jumpapplet

* Sun Dec 11 2011 Thibault North <tnorth@fedoraproject.org> - 19-1
- Update to version 19

* Sun Apr 10 2011 Thibault North <tnorth@fedoraproject.org> - 15-1
- New upstream release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Thibault North <tnorth@fedoraproject.org> - 14-2
- Fixes for review

* Sat Dec 18 2010 Thibault North <tnorth@fedoraproject.org> - 14-1
- Initial package

