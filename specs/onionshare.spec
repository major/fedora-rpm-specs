%global _hardened_build 1

Name:           onionshare
Version:        2.5
Release:        11%{?dist}
Summary:        Securely and anonymously share files of any size

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://onionshare.org/
Source0:        https://github.com/micahflee/%{name}/archive/v%{version}.tar.gz

#Patch0:        % {name}-appdata.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       python3-flask
Requires:       python3-stem
Requires:       python3-qt5
Requires:       nautilus-python
Requires:       tor


%description
OnionShare lets you securely and anonymously share files of any size. It works
by starting a web server, making it accessible as a Tor hidden service, and
generating an unguessable URL to access and download files. It doesn't require
setting up a server on the internet somewhere or using a third party
file sharing service. You host files on your own computer and use a Tor
hidden service to make it temporarily accessible over the internet. The other
user just needs to use Tor Browser to download a file from you.


%prep
%setup -qn %{name}-%{version}

#%patch0 -p1 -b .orig


%build
(cd cli; %{__python3} setup.py build)
(cd desktop; %{__python3} setup.py build)

%install
(cd cli; %{__python3} setup.py install --skip-build --root %{buildroot})
(cd desktop; %{__python3} setup.py install --skip-build --root %{buildroot})

#desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
#mkdir -p %{buildroot}%{_datadir}/appdata/
#install -m 644 %{_builddir}/%{name}-%{version}/install/%{name}.appdata.xml \
#    %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
#chmod +x %{buildroot}/%{_datadir}/nautilus-python/extensions/%{name}-nautilus*

%check
#appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc LICENSE README.md
%{_bindir}/*
%{python3_sitelib}/%{name}*

#% {_datadir}/doc/onionshare/*
#% aappdata/% {name}.*
#% {_datadir}/pixmaps/*
#% {_datadir}/% {name}/*
#% {_datadir}/applications/*
#% {_datadir}/nautilus-python/extensions/% {name}-nautilus*
#% {_bindir}/% {name}-gui


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.5-8
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.5-4
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 pjp <pjp@fedoraproject.org> - 2.5-1
- Latest releae

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3-15
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3-12
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-9
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-2
- Rebuilt for Python 3.7

* Thu Apr 05 2018 Nikos Roussos <comzeradd@fedoraproject.org> - 1.3-1
- Update to 1.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Kushal Das <kushal@fedoraproject.org> - 1.2-1
- Update to 1.2

* Mon Nov 27 2017 Kushal Das <kushal@fedoraproject.org> - 1.1-1
- Update to 1.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 25 2017 pjp <comzeradd@fedoraproject.org> - 1.0-1
- Update to 1.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 pjp <comzeradd@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 0.8.1-3
- Requires: pyqt4-webkit

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 robyduck <robyduck@fedoraproject.org> - 0.8.1-1
- Fixed crash in Windows 7
- Fixed crash related to non-ephemeral hidden services in Linux
- Fixed minor bugs

* Mon Aug 31 2015 pjp <robyduck@fedoraproject.org> - 0.7.1-1
- Upstream release v0.7.1-1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 pjp <pjp@fedoraproject.org> - 0.6-5
- Fixed spec file as per review BZ#1151747#c8,9.

* Mon Oct 13 2014 pjp <pjp@fedoraproject.org> - 0.6-4
- Fixed this spec file as per review BZ#1151747#c6.

* Sun Oct 12 2014 pjp <pjp@fedoraproject.org> - 0.6-3
- Fixed Source0 definition as per review BZ#1151747#c4.

* Sat Oct 11 2014 pjp <pjp@fedoraproject.org> - 0.6-2
- Fixed oname and Source0 definition as per review BZ#1151747#c2.

* Sat Oct 11 2014 pjp <pjp@fedoraproject.org> - 0.6-1
- Initial release onionshare v0.6.
