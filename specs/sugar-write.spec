Name:    sugar-write
Version: 101
Release: 14%{?dist}
Summary: Word processor for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://wiki.sugarlabs.org/go/Activities/Write
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Write/Write-%{version}.tar.bz2

BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: libabiword-devel
BuildRequires: python3-devel
BuildRequires: python3-abiword
BuildRequires: sugar-toolkit-gtk3-devel

Requires: gobject-introspection
Requires: python3-abiword
Requires: sugar

BuildArch: noarch

%description
The Write activity provides a word processor for the Sugar interface.

%prep
%setup -n Write-%{version}

sed -i 's/python/python3/' *.py

%build
python3 ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Write.activity/

%find_lang org.laptop.AbiWordActivity


%files -f  org.laptop.AbiWordActivity.lang
%doc NEWS
%{sugaractivitydir}/Write.activity/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 101-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 101-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 101-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 101-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 101-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 101-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 101-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 101-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 101-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 101-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 101-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Peter Robinson <pbrobinson@fedoraproject.org> 101-1
- Release 101

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Kalpa Welivitigoda <callkalpa@gmail.com> - 100-1
- Release 100

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 09 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 99.1-1
- Release 99.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 98.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 98.4-1
- Release 98.4

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 98.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 98.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 98.3-1
- Release 98.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 22 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 98-1
- Release 98

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 97-1
- Update to v97

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Peter Robinson <pbrobinson@fedoraproject.org> 96-1
- Update to v96

* Sun Jul 27 2014 Peter Robinson <pbrobinson@fedoraproject.org> 95-1
- Update to v95

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 94-1
- Update to v94

* Mon Oct 14 2013 Peter Robinson <pbrobinson@fedoraproject.org> 93-1
- Update to v93

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 79-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 79-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 79-1
- New 79 release

* Mon Mar 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 78-1
- New 78 release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  2 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 77-1
- New 77 release

* Mon Sep  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 76-1
- New 76 release

* Mon Apr  4 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 73-1
- New upstream 73 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 72-2
- Bump build

* Sat Oct 23 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 72-1
- New upstream 72 release

* Thu Sep 30 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 71-1
- New upstream 71 release

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 69-2
- recompiling .py files against Python 2.7 (rhbz#623392)
