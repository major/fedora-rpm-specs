Name:           sugar-xoirc
Version:        14
Release:        11%{?dist}
Summary:        IRC client for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/sugarlabs/irc-activity/
Source0:        http://download.sugarlabs.org/sources/honey/IRC/IRC-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gobject-introspection-devel
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3-devel
Requires:       sugar >= 0.116
Requires:       sugar-toolkit-gtk3


%description
This activity allows you to contact other OLPC users and enthusiasts
on the internet, and chat with them. 


%prep
%setup -q -n IRC-%{version}

sed -i 's/python/python3/' *.py

%build
python3 ./setup.py build


%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/IRC.activity/

%files
%license COPYING
%doc README TODO
%{sugaractivitydir}/IRC.activity/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 14-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 14-1
- Release version 14
- Change to py_byte_compile as stated in phase 3
  (See https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3)

* Wed Aug 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 13-1
- Update to IRC 13

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 12-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 12-5
- Fix FTBFS issue 

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 12-1
- New upstream 12 release

* Tue Jan 20 2015 Peter Robinson <pbrobinson@fedoraproject.org> 11-1
- New upstream 11 release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 14 2011 Peter Robinson <pbrobinson@gmail.com> - 10-1
- New upstream 10 release

* Tue Mar  8 2011 Peter Robinson <pbrobinson@gmail.com> - 9-1
- New upstream 9 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@gmail.com> - 8-3
- Bump build

* Tue Nov 23 2010 Peter Robinson <pbrobinson@gmail.com> - 8-2
- Correct changelog

* Tue Nov 23 2010 Peter Robinson <pbrobinson@gmail.com> - 8-1
- New upstream 8 release

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 6-5
- recompiling .py files against Python 2.7 (rhbz#623393)

* Thu Mar 25 2010 Sebastian Dziallas <sebastian@when.com> - 6-4
- Fix class name to make activity start again

* Thu Mar 25 2010 Sebastian Dziallas <sebastian@when.com> - 6-3
- Try again to rename base file to fit new naming scheme

* Fri Mar 19 2010 Sebastian Dziallas <sebastian@when.com> - 6-2
- Rename base file to fit new naming scheme

* Sat Feb 27 2010 Sebastian Dziallas <sebastian@when.com> - 6-1
- New upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20090129
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20090129
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Fabian Affolter <fabian@bernewireless.net> - 0-0.1.20090129
- Initial package for Fedora
