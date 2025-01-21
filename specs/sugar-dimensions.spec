Name:           sugar-dimensions
Version:        60
Release:        11%{?dist}
Summary:        A pattern matching game

# namingalert.py is licensed as LGPLv2+
# sprites.py is licensed under the MIT license
# other files are licensed as GPLv3+
# Automatically converted from old format: GPLv3+ and LGPLv2+ and MIT - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
URL:            https://github.com/sugarlabs/dimensions
Source0:        http://download.sugarlabs.org/sources/honey/Dimensions/Dimensions-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3-devel
BuildArch:      noarch
Requires:       sugar >= 0.116

%description
The object is to find sets of three cards where each attribute—color,
shape, number of elements, and shading—either match on all three cards
or are different on all three cards. The current version doesn't yet
support sharing with multiple players or saving to the Journal, but it
can be played by a single player.


%prep
%autosetup -n Dimensions-%{version}

for lib in $(find . -name "*.py" -type f); do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done

%build
python3 ./setup.py build


%install
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
chmod 0644 %{buildroot}/%{sugaractivitydir}/Dimensions.activity/gencards.py
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{__python3} %{buildroot}/%{sugaractivitydir}/Dimensions.activity/

%find_lang org.sugarlabs.VisualMatchActivity


%files -f org.sugarlabs.VisualMatchActivity.lang
%license COPYING COPYING.MIT
%doc NEWS
%{sugaractivitydir}/Dimensions.activity/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 60-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 60-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 60-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 60-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 60-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 60-2
- Change package name

* Fri Feb 26 2021 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 60-1
- New 60 release
- Fix py byte compile 

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 49-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 49-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 49-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 49-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 49-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 49-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 49-9
- Fix FTBFS (#1556475)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 49-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 49-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 49-1
- Release 49

* Sat Jan 26 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 47-1
- New 47 release

* Sun Oct 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> 45-1
- New 45 release

* Sat Oct 13 2012 Peter Robinson <pbrobinson@fedoraproject.org> 43-1
- New 43 release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 30 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 38-1
- New 38 release

* Sat Apr 21 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 37-1
- New 37 release

* Fri Apr 20 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 36-1
- New 36 release

* Wed Feb 29 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 35-1
- New 35 release

* Sun Jan 08 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 34-1
- New 34 release

* Tue Dec 20 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 33-1
- New 33 release

* Fri Nov 18 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 32-1
- New 32 release

* Sun Oct  2 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 30-1
- New 30 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 27-1
- New 27 release

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 23-2
- recompiling .py files against Python 2.7 (rhbz#623391)

* Thu Jul 08 2010 Sebastian Dziallas <sebastian@when.com> - 23-1
- new upstream release

* Sat Feb 27 2010 Sebastian Dziallas <sebastian@when.com> - 21-1
- new upstream release

* Mon Feb 15 2010 Sebastian Dziallas <sebastian@when.com> - 20-3
- make sure to grab locale files now

* Mon Feb 15 2010 Sebastian Dziallas <sebastian@when.com> - 20-2
- add gettext build requirement

* Mon Feb 15 2010 Sebastian Dziallas <sebastian@when.com> - 20-1
- new upstream release

* Tue Jan 12 2010 Sebastian Dziallas <sebastian@when.com> - 17-1
- new upstream release
- switch to GPLv3+

* Tue Dec 29 2009 Sebastian Dziallas <sebastian@when.com> - 13-1
- new upstream release
- fix license tag

* Sun Dec 06 2009 Sebastian Dziallas <sebastian@when.com> - 8-1
- initial packaging
