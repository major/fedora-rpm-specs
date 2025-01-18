Name: aha
Summary: Convert terminal output to HTML
License: MPL-1.1 OR LGPL-2.0-or-later

Version: 0.5.1
Release: 13%{?dist}

URL: https://github.com/theZiz/aha
Source0: %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

# Fix a null pointer dereference when interpreting
# invalid 24-bit color code escape sequences.
#
# Submitted upstream: https://github.com/theZiz/aha/pull/97
Patch0: 0000-fix-null-pointer-dereference.patch

BuildRequires: gcc
BuildRequires: make


%description
%{name} parses output from other programs,
recognizes ANSI terminal escape sequences
and produces an HTML rendition of the original text.


%prep
%autosetup -p1
# Extract license header from source code
cat aha.c | awk '1;/\*\//{exit}' > LICENSE


%build
%set_build_flags
%make_build


%install
%make_install PREFIX=%{_prefix}


%files
%license LICENSE
%license LICENSE.MPL1.1 LICENSE.LGPLv2+
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 08 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.1-12
- Convert License tag to SPDX
- Include full license texts in the package

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.1-5
- Add a patch to fix segfault because of null pointer dereference

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.1-1
- Update to latest upstream release

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Artur Iwicki <fedora@svgames.pl> - 0.5-1
- Update to latest upstream release

* Wed Jul 18 2018 Artur Iwicki <fedora@svgames.pl> - 0.4.10.6-2
- Invoke %%set_build_flags before building
- Use %%make_build instead of "make %%{?_smp_flags}"

* Sun Jul 15 2018 Artur Iwicki <fedora@svgames.pl> - 0.4.10.6-1
- Initial packaging
