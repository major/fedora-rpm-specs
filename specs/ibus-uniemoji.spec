# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3

%global __python %{__python3}


Summary:  Input method for entering unicode symbols and emoji by name
Name: ibus-uniemoji
Version: 0.7.0
Release: 2%{?dist}
# emojione.json is in MIT
# UnicodeData.txt is in Unicode
# uniemoji is in GPLv3+
License: Unicode-DFS-2015 AND MIT AND GPL-3.0-or-later
Source0: https://github.com/salty-horse/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/salty-horse/ibus-uniemoji

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: make
Requires: ibus

%description
This simple input method for ibus allows you to
enter unicode emoji and other symbols by name.

%prep
%autosetup

%install
mkdir -p %{buildroot}/%{_datadir}/ibus/component
make install DESTDIR=%{buildroot}

%py_byte_compile %{python3} %{buildroot}%{_datadir}/ibus-uniemoji

%files
%license COPYING COPYING.*
%doc HISTORY README.md
%{_datadir}/ibus/component/*.xml
%{_datadir}/ibus-uniemoji
%dir %{_sysconfdir}/xdg/uniemoji
%config(noreplace) %{_sysconfdir}/xdg/uniemoji/custom.json

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 23 2024 Peng Wu <pwu@redhat.com> - 0.7.0-1
- Update to 0.7.0
- Resolves: RHBZ#2298797

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May  8 2023 Peng Wu <pwu@redhat.com> - 0.6.0-20
- Rebuild the package

* Mon May  8 2023 Peng Wu <pwu@redhat.com> - 0.6.0-19
- Migrate to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec  3 2021 Peng Wu <pwu@redhat.com> - 0.6.0-15
- Update the spec file

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug  5 2020 Peng Wu <pwu@redhat.com> - 0.6.0-12
- Use py_byte_compile macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Peng Wu <pwu@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Thu Jul 21 2016 Peng Wu <pwu@redhat.com> - 0.5.0-2
- Update spec

* Mon Jun 27 2016 Takao Fujiwara <tfujiwar@redhat.com> - 0.1-1
- Initial release
