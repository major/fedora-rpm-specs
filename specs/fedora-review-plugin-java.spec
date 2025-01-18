Name:           fedora-review-plugin-java
Version:        4.6.1
Release:        19%{?dist}
Summary:        Java plugin for FedoraReview
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-java/fedora-review-plugin-java
BuildArch:      noarch

Source0:        https://github.com/fedora-java/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:         0001-Pep-8-whitespace-fixes.patch
Patch1:         0002-Add-pylint-pep8-configs-and-script-to-run-them.patch
Patch2:         0003-Fix-pylint-pep8-warnings.patch
Patch3:         0004-Search-for-both-jpackage-utils-and-javapackages-tool.patch

Requires:       fedora-review

%description
This package provides a plugin for FedoraReview tool that allows
checking packages for conformance with Java packaging guidelines.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/fedora-review/plugins/
install -pm644 fedora-review/java_guidelines.py %{buildroot}%{_datadir}/fedora-review/plugins/

%files
%license LICENSE
%{_datadir}/fedora-review/plugins/java_guidelines.py*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.6.1-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 Sérgio Basto <sergio@serjux.com> - 4.6.1-10
- Add the last 4 commits from upstream

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.6.1-3
- Improve package description

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Michael Simacek <msimacek@redhat.com> - 4.6.1-1
- Initial packaging after split
