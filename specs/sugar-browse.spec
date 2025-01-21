Name:    sugar-browse
Version: 208
Release: 4%{?dist}
Summary: Browse activity for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://wiki.laptop.org/go/Browse
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Browse/Browse-%{version}.tar.bz2

BuildRequires: gobject-introspection-devel
BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: webkitgtk4-devel
BuildRequires: gettext
Requires: sugar-toolkit-gtk3
Requires: webkit2gtk4.1

BuildArch: noarch

%description
A browser for the Sugar platform based on the WebKit web browser
engine. 

%prep
%autosetup -n Browse-%{version}

%build
python3 ./setup.py build

%install
mkdir -p %{buildroot}/%{sugaractivitydir}
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{sugaractivitydir}/Browse.activity/

%find_lang org.laptop.WebActivity

%files -f org.laptop.WebActivity.lang
%license COPYING
%doc AUTHORS
%{sugaractivitydir}/Browse.activity/
/usr/share/metainfo/org.laptop.WebActivity.appdata.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 208-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 208-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 208-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 07 2024 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 208-1
- Update to 208

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 207-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 207-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 207-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 207-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 207-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 01 2021 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 207-3
* Use %{sugaractivitydir} macro

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 207-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 14 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 207-1
- Update to 207

* Sun Feb  7 2021 Alex Perez <aperez@sugarlabs.org> 206-1
- New 206 release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 204-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 204-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 204-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  1 2020 Peter Robinson <pbrobinson@fedoraproject.org> 204-1
- New 204 release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 203.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 203.1-1
- Update to 203.1 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 203-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Kalpa Welivitigoda <callkalpa@gmail.com> - 203-1
- New 203 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct  6 2018 Peter Robinson <pbrobinson@fedoraproject.org> 202-1
- New 202 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 201.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 201.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 201.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 201.2-1
- New 201.2 release, fix Browse crash on startup

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 201.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 201.1-1
- New 201.1 release

* Tue May 30 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 201-1
- New 201 release

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 200-3
- Fix FTBFS issue

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 200-1
- New 200 release
- Use webkitgtk4

* Fri Apr  1 2016 Peter Robinson <pbrobinson@fedoraproject.org> 157.3-1
- New 157.3 release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 157.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 157.2-1
- New 157.2 release

* Wed Jun 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 157.1-1
- New 157.1 release

* Fri Oct  3 2014 Peter Robinson <pbrobinson@fedoraproject.org> 157-1
- New 157 release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 156-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 12 2013 Peter Robinson <pbrobinson@fedoraproject.org> 156-1
- New 156 release

* Mon Oct 7  2013 Peter Robinson <pbrobinson@fedoraproject.org> 155-1
- New 155 release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 153-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 153-1
- New 153 release

* Mon May 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 149.3-1
- New 149.3 release

* Thu Apr 11 2013 Peter Robinson <pbrobinson@fedoraproject.org> 149.2-1
- New 149.2 release

* Thu Mar 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 149.1-1
- New 149.1 release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 149-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 149-1
- New 149 release

* Thu Nov 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 148-1
- New 148 release

* Wed Nov 21 2012 Manuel Quiñones <manuq@laptop.org> - 147-1
- New 147 release

* Wed Nov  7 2012 Manuel Quiñones <manuq@laptop.org> - 146-1
- New 146 release

* Thu Oct 25 2012 Manuel Quiñones <manuq@laptop.org> - 145-1
- New 145 release

* Tue Oct 16 2012 Manuel Quiñones <manuq@laptop.org> - 144-1
- New 144 release

* Fri Oct 12 2012 Manuel Quiñones <manuq@laptop.org> - 143-1
- New 143 release

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 142-1
- New 142 release

* Fri Sep 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 141-1
- New 141 release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 140-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Manuel Quiñones <manuq@laptop.org> - 140-1
- New 140 release

* Fri Jun 15 2012 Manuel Quiñones <manuq@laptop.org> - 139-1
- New 139 release

* Fri Jun  1 2012 Manuel Quiñones <manuq@laptop.org> - 138-1
- New 138 release

* Fri May  4 2012 Manuel Quiñones <manuq@laptop.org> - 137-1
- New 137 release

* Mon Apr 30 2012 Manuel Quiñones <manuq@laptop.org> - 136-1
- New 136 release

* Tue Apr 17 2012 Manuel Quiñones <manuq@laptop.org> - 135-1
- New 135 release

* Fri Apr  6 2012 Manuel Quiñones <manuq@laptop.org> - 134-1
- New 134 release

* Fri Mar 23 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 133-1
- New 133 release

* Fri Mar  2 2012 Manuel Quiñones <manuq@laptop.org> - 132-1
- New 132 release

* Tue Feb  7 2012 Manuel Quiñones <manuq@laptop.org> - 131-1
- New 131 release

* Sun Jan 22 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 130-3
- Obsolete sugar-surf

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 130-1
- Release 130 using gtk3, gobject-introspection, webkitgtk3 and more
