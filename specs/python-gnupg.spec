Name:           python-gnupg
Version:        0.5.0
Release:        10%{?dist}
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://gnupg.readthedocs.io/
Source0:        https://pypi.io/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Source1:        https://pypi.io/packages/source/p/%{name}/%{name}-%{version}.tar.gz.asc
# from keys.openpgp.net based on fingerprinted listed on pypi page
Source2:	CA749061914EAC138E66EADB9147B477339A9B86.gpg
Source3:	tox.ini
Source4:	pyproject.toml
BuildArch:      noarch

%description
GnuPG bindings for python. This uses the gpg command.

%package -n     python3-gnupg
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gnupg2
Requires:       gnupg
%{?python_provide:%python_provide python3-gnupg}

%description -n python3-gnupg
GnuPG bindings for python. This uses the gpg command.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}
# add missing pyproject.toml and tox.ini (taken from github.com/vsajip/python-gnupg
cp %{SOURCE3} %{SOURCE4} .

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gnupg

%check
%tox

%files -n python3-gnupg -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.0-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 31 2022 Paul Wouters <paul.wouters@aiven.io - 0.5.0-1
- update to 0.5.0
- Use newer pyproject python macros

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.8-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Ken Dreyer <kdreyer@redhat.com> - 0.4.8-1
- Update to 0.4.8
- Add gpg verification with upstream key

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.6-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.4.6-1
- Update to 0.4.6

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-4
- Subpackage python2-gnupg has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Paul Wouters <pwouters@redhat.com> - 0.4.4-1
- Resolves rhbz#1670364 Fixes CVE-2019-6690

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Paul Wouters <pwouters@redhat.com> - 0.4.3-1
- Updated to 0.4.3, updated URL and Source fields
- Resolves: rhbz#1547638 New version is available

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.8-10
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.8-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.8-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.3.8-3
- Put the gnupg dependence for both py2 and py3 packages

* Wed May 04 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.3.8-2
- Fix provides and obsoletes

* Sun Feb 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.3.8-1
- Enable python3 compilation
- Move to current python standard
- Update 0.3.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 06 2015 Paul Wouters <pwouters@redhat.com> - 0.3.7-1
- Updated to 0.3.7 Merged in export-minimal and armor options, many encoding fixes

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Paul Wouters <pwouters@redhat.com> - 0.3.6-3
- Removed patch as gpg.decode_errors=ignore works well

* Thu Apr 17 2014 Paul Wouters <pwouters@redhat.com> - 0.3.6-2
- Re-instate part of export patch that fixed encoding bug

* Thu Feb 06 2014 Paul Wouters <pwouters@redhat.com> - 0.3.6-1
- Updated to 0.3.6 which includes Security fix (CVE-2014-XXXX)
- Upstream including our export patch and converted README file
- Upstream switched to new download site

* Mon Jan 06 2014 Paul Wouters <pwouters@redhat.com> - 0.3.5-4
- Require gnupg (duh)
- Remove cleaning in install target
- Fix license to BSD
- Link to upstream bug tracker for included patch

* Sat Jan 04 2014 Paul Wouters <pwouters@redhat.com> - 0.3.5-3
- Remove unused global, fix python macro, buildroot macro
- Converted README from DOS to unix (and reported upstream)

* Tue Dec 31 2013 Paul Wouters <pwouters@redhat.com> - 0.3.5-2
- Added minimal= and armor= options to export_keys()

* Sun Dec 22 2013 Paul Wouters <pwouters@redhat.com> - 0.3.5-1
- Initial package
