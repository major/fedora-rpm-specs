Summary: Name-indexed data processing tool
Name: miller
Version: 5.10.2
Release: 6%{?dist}
License: BSD
Source: https://github.com/johnkerl/miller/releases/download/v%{version}/mlr-%{version}.tar.gz
URL: http://johnkerl.org/miller/doc
BuildRequires: make
BuildRequires: gcc
BuildRequires: flex >= 2.5.35

%description
Miller (mlr) allows name-indexed data such as CSV and JSON files to be
processed with functions equivalent to sed, awk, cut, join, sort etc. It can
convert between formats, preserves headers when sorting or reversing, and
streams data where possible so its memory requirements stay small. It works
well with pipes and can feed "tail -f".

%prep
%setup -q -n mlr-%{version}

%build
%configure
%make_build

%check
make check

%install
%make_install

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/mlr
%{_mandir}/man1/mlr.1*

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 Stephen Kitt <skitt@fedoraproject.org> - 5.10.2-1
- 5.10.2 release, restoring the manpage
  Resolves rhbz#1747752 - miller-5.10.2 is available

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 19 2021 Stephen Kitt <skitt@fedoraproject.org> - 5.10.0-1
- 5.10.0 release
  Resolves: #1747752

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Stephen Kitt <skitt@fedoraproject.org> - 5.9.1-1
- 5.9.1 release (CVE-2020-15167)

* Thu Aug 27 2020 Stephen Kitt <skitt@fedoraproject.org> - 5.9.0-1
- 5.9.0 release

* Wed Aug 12 2020 Stephen Kitt <skitt@fedoraproject.org> - 5.8.0-1
- 5.8.0 release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 03 2020 Stephen Kitt <skitt@fedoraproject.org> - 5.6.2-1
- 5.6.2 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Stephen Kitt <skitt@fedoraproject.org> - 5.6.0-1
- 5.6.0 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Stephen Kitt <steve@sk2.org> - 5.4.0-1
- Fix up for Fedora

* Sun Oct 14 2018 John Kerl <kerl.john.r@gmail.com> - 5.4.0-1
- 5.4.0 release

* Sat Jan 06 2018 John Kerl <kerl.john.r@gmail.com> - 5.3.0-1
- 5.3.0 release

* Thu Jul 20 2017 John Kerl <kerl.john.r@gmail.com> - 5.2.2-1
- 5.2.2 release

* Mon Jun 19 2017 John Kerl <kerl.john.r@gmail.com> - 5.2.1-1
- 5.2.1 release

* Sun Jun 11 2017 John Kerl <kerl.john.r@gmail.com> - 5.2.0-1
- 5.2.0 release

* Thu Apr 13 2017 John Kerl <kerl.john.r@gmail.com> - 5.1.0-1
- 5.1.0 release

* Sat Mar 11 2017 John Kerl <kerl.john.r@gmail.com> - 5.0.1-1
- 5.0.1 release

* Mon Feb 27 2017 John Kerl <kerl.john.r@gmail.com> - 5.0.0-1
- 5.0.0 release

* Sun Aug 21 2016 John Kerl <kerl.john.r@gmail.com> - 4.5.0-1
- 4.5.0 release

* Mon Apr 04 2016 John Kerl <kerl.john.r@gmail.com> - 3.5.0-1
- 3.5.0 release

* Sun Feb 14 2016 John Kerl <kerl.john.r@gmail.com> - 3.4.0-1
- 3.4.0 release

* Sun Feb 07 2016 John Kerl <kerl.john.r@gmail.com> - 3.3.2-1
- Initial spec-file submission for Miller
