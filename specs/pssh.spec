Summary:       Parallel SSH tools
Name:          pssh
Version:       2.3.5
Release:       9%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
Url:           https://github.com/lilydjwg/pssh
Source0:       https://github.com/lilydjwg/pssh/archive/refs/tags/v%{version}.tar.gz
Requires:      openssh-clients
BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package provides various parallel tools based on ssh and scp.
Parallell version includes:
 o ssh : pssh
 o scp : pscp
 o nuke : pnuke
 o rsync : prsync
 o slurp : pslurp

%prep
%autosetup
sed -i -e '1 d' psshlib/askpass_{client,server}.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

install -D -m 0755 %{buildroot}%{_bindir}/pssh-askpass \
    %{buildroot}%{_libexecdir}/pssh/pssh-askpass
rm -f %{buildroot}%{_bindir}/pssh-askpass
mv %{buildroot}%{_bindir}/pscp %{buildroot}%{_bindir}/pscp.pssh
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 man/man1/*.1  %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_mandir}/man1/pscp.1 %{buildroot}%{_mandir}/man1/pscp.pssh.1

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/pnuke
%{_bindir}/prsync
%{_bindir}/pscp.pssh
%{_bindir}/pslurp
%{_bindir}/pssh
%{_mandir}/man1/pnuke.1*
%{_mandir}/man1/prsync.1*
%{_mandir}/man1/pscp.pssh.1*
%{_mandir}/man1/pslurp.1*
%{_mandir}/man1/pssh.1*
%{_libexecdir}/pssh
%{python3_sitelib}/pssh-%{version}*
%{python3_sitelib}/psshlib

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.5-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.5-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.3.5-2
- Rebuilt for Python 3.12

* Sun Mar 26 2023 Terje Rosten <terje.rosten@ntnu.no> - 2.3.5-1
- 2.3.5

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.4-2
- Rebuilt for Python 3.11

* Tue Mar 1 2022 Pat Riehecky <riehecky@fnal.gov> - 2.3.4-1
- Sync up with upstream

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.1-32
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-29
- Rebuilt for Python 3.9

* Mon Apr 13 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-28
- Add patch to fix Python 3.8 issue bz#1822306

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-26
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-25
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-21
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-18
- Switch upstream bz#1441779

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-16
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-15
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 25 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-14
- Add patch to fix Python 3.5 issue bz#1330231

* Sat Apr 02 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-13
- Add patch to fix issue when prompting for password

* Thu Feb 04 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-12
- Add patch to fix bz#1294454

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-10
- Use license macro

* Mon Nov 16 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-9
- Use Python 3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 2.3.1-7
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 19 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-2
- Fix bz #794567

* Thu Feb 02 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-1
- 2.3.1
- Add man all pages

* Tue Jan 31 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.3-1
- 2.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Terje Rosten <terje.rosten@ntnu.no> - 2.2.2-1
- 2.2.2

* Thu Jan 27 2011 Terje Rosten <terje.rosten@ntnu.no> - 2.2.1-1
- 2.2.1

* Sat Jan 22 2011 Terje Rosten <terje.rosten@ntnu.no> - 2.2-1
- 2.2

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Mar 26 2010 Terje Rosten <terje.rosten@ntnu.no> - 2.1.1-1
- 2.1.1

* Mon Mar 01 2010 Terje Rosten <terje.rosten@ntnu.no> - 2.1-1
- 2.1

* Sun Nov 01 2009 Terje Rosten <terje.rosten@ntnu.no> - 2.0-1
- 2.0
- Switch to new upstream
- Move pscp to pscp.pssh

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan  5 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.4.3-1
- 1.4.3

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.4.0-2
- Rebuild for Python 2.6

* Mon Aug 25 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.4.0-1
- initial build
