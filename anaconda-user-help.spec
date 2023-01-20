Summary: Content for the Anaconda built-in help system
Name: anaconda-user-help
URL: https://pagure.io/install-guide
Version: 26.2
Release: 4%{?dist}
BuildArch: noarch

# The tarball is created from the Fedora Installation Guide
# git repository with git archive from the corresponding
# anaconda-user-help-x.x git tag.
# The blivet-gui documentation tarball is made from the user help files
# for blivet-gui:
# https://github.com/rhinstaller/blivet-gui

Source0: %{name}-%{version}.tar.gz
Source1: %{name}-blivet-gui.tar.gz

License: CC-BY-SA
BuildRequires: python3-devel
BuildRequires: python3-lxml
BuildRequires: xmlto
# lynx is required by xmlto for successful xml to plain text conversion
BuildRequires: lynx

%description
This package provides content for the Anaconda built-in help system.

%prep
%setup -q -a 1

%build
%{__python3} prepare_anaconda_help_content.py

%install
mkdir -p %{buildroot}%{_datadir}/anaconda/help/fedora
cp anaconda-*.json %{buildroot}%{_datadir}/anaconda/help/fedora
cp -r anaconda_help_content/* %{buildroot}%{_datadir}/anaconda/help/fedora
cp -r blivetgui_help_content/* %{buildroot}%{_datadir}/anaconda/help/fedora

%files
%{_datadir}/anaconda/help/fedora/*

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 26.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 26.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Vendula Poncova <vponcova@redhat.com> - 26.2-1
- Add mapping files for the unified help support (vponcova)
- Install help files to the fedora directory (vponcova)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 26.1-7
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Martin Kolman <mkolman@redhat.com> - 26.1-4
- Add help for blivet-gui spoke (#1439565) (vtrefny)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Martin Kolman <mkolman@redhat.com> - 26.1-2
- Add lynx dependency to fix xml to plain text conversion (mkolman)

* Thu Oct 27 2016 Martin Kolman <mkolman@redhat.com> - 26.1-1
- Generate plain text variants of the help content files (mkolman)
- Add a plain text version of of the placeholder (mkolman)
- Fix some typos (mkolman)
- Use /usr/bin/python3 in conversion script header (mkolman)
- Update help content (mkolman)
- Fix link to the installation guide git repository (mkolman)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 22.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Martin Kolman <mkolman@redhat.com> - 22.4-1
- Add help content for the Kdump spoke (mkolman)

* Wed Dec 10 2014 Martin Kolman <mkolman@redhat.com> - 22.1-1
- Initial release (mkolman)
