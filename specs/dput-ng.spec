Name:    dput-ng
Version: 1.21
Release: 23%{?dist}

Summary: Next generation Debian package upload tool
# Automatically converted from old format: GPLv2+ and MIT - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:     https://debian.pages.debian.net/dput-ng/
Source0: http://deb.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz

BuildArch: noarch

BuildRequires: asciidoc
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-debian
BuildRequires: python3-paramiko
#BuildRequires: python3-sphinx

Requires: python3
Requires: python3-dput = %{version}-%{release}

%description
dput-ng is a Debian package upload tool which provides an easy to use
interface to Debian (like) package archive hosting facilities. It allows
anyone who works with Debian packages to upload their work to a remote
service, including Debian's ftp-master, mentors.debian.net, Launchpad or other
package hosting facilities for Debian package maintainers.

dput-ng features many enhancements over dput, such as more comprehensive
checks, an easy to use plugin system, and code designed to handle the numerous
archives that any Debian package hacker will interact with.

dput-ng aims to be backwards compatible with dput in command-line flags,
configuration files, and expected behavior.

%package -n python3-dput
Summary: Python 3 library for dput-ng

Requires: python3
Requires: python3-debian
Requires: python3-distro-info
#Requires: python-validictory
Requires: python3-paramiko

%{?python_provide:%python_provide python3-dput}

%description -n python3-dput
Python 3 library for dput-ng.

%prep
%autosetup

%build
#make -C docs man
for man in docs/man/*.man
do
  a2x --doctype manpage --format manpage -D docs/man ${man}
done

python3 setup.py build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5

cp -p bin/* %{buildroot}%{_bindir}
cp -pr skel/metas %{buildroot}%{_datadir}/%{name}
cp -pr skel/profiles %{buildroot}%{_datadir}/%{name}
cp -pr skel/hooks %{buildroot}%{_datadir}/%{name}
cp -pr skel/commands %{buildroot}%{_datadir}/%{name}
cp -pr skel/interfaces %{buildroot}%{_datadir}/%{name}
cp -pr skel/uploaders %{buildroot}%{_datadir}/%{name}
cp -pr skel/schemas %{buildroot}%{_datadir}/%{name}
cp -pr skel/codenames %{buildroot}%{_datadir}/%{name}
cp -p skel/README %{buildroot}%{_datadir}/%{name}
cp -p docs/man/*.1 %{buildroot}%{_mandir}/man1
cp -p docs/man/*.5 %{buildroot}%{_mandir}/man5

python3 setup.py install --root=%{buildroot}

%files
%doc FAQ README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/*/*

%files -n python3-dput
%{python3_sitelib}/dput
%{python3_sitelib}/dput*.egg-info

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.21-22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.21-20
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.21-16
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.21-13
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.21-10
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.21-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.21-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.21-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Michael Kuhn <suraia@fedoraproject.org> - 1.21-1
- Update to 1.21

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.11-6
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.11-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Michael Kuhn <suraia@fedoraproject.org> - 1.11-1
- Update to 1.11.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Michael Kuhn <suraia@fedoraproject.org> - 1.10-3
- Explicitly require python2.
- Rename python-* packages to python2-*.
- Provide python-dput.

* Tue Dec 29 2015 Michael Kuhn <suraia@fedoraproject.org> - 1.10-2
- Install metas and profiles to /use/share.
- Use %%license for license text.

* Tue Sep 15 2015 Michael Kuhn <suraia@fedoraproject.org> - 1.10-1
- Initial package.
