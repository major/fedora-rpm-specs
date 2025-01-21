Name:		sugar-deducto
Version:	11
Release:	12%{?dist}
Summary:	A learning activity aimed towards improving children’s skills to deducing logic

# sprites.py is in MIT and all other files in GPLv3+
# Automatically converted from old format: GPLv3+ and MIT - review is highly recommended.
License:	GPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL:		http://activities.sugarlabs.org/en-US/sugar/addon/4220
Source0:	http://download.sugarlabs.org/sources/honey/Deducto/Deducto-%{version}.tar.bz2

BuildRequires:	gettext
BuildRequires:	python3-devel
BuildRequires:	sugar-toolkit-gtk3
Requires:	sugar
Requires:	sugar-toolkit-gtk3
BuildArch:	noarch

%description
A learning activity aimed towards improving children's skills 
to deducing logic through pattern recognition.

%prep
%setup -q -n Deducto-%{version}
#sed -i "s|python|python2|g" setup.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Deducto.activity/

%find_lang  in.seeta.Deducto


%files -f in.seeta.Deducto.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Deducto.activity/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 11-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 11-1
- Update to 11, migrate to python3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 9-15
- Fix build without python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 9-7
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Danishka Navin  <snavin@lists.fedoraproject.org> - 9-5
- Fixed %%BuildRequires 

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 06 2013 Danishka Navin <danishka@gmail.com> - 9-3
- Updated the license tag with GPLv3+ and MIT

* Thu Jun 06 2013 Danishka Navin <danishka@gmail.com> - 9-2
- add a comment above the license tag
- removed backslash between %%{buildroot} and %%{_prefix}

* Thu Jun 06 2013 Danishka Navin <danishka@gmail.com> - 9-1
- initial packaging
