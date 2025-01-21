Name:    sugar-turtleart
Version: 220
Release: 12%{?dist}
Summary: Turtle Art activity for sugar
License: MIT
URL:     http://sugarlabs.org/go/Activities/Turtle_Art

BuildArch: noarch
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/TurtleArt/TurtleBlocks-%{version}.tar.bz2

BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext

Requires: sugar
Requires: sugar-toolkit-gtk3

%description
The Turtle Art activity is an Logo-inspired graphical "turtle" that 
draws colorful  art based on Scratch-like snap-together visual 
programming elements. 

%prep
%setup -q -n TurtleBlocks-%{version}

sed -i 's/python/python3/' setup.py
sed -i 's#/usr/bin/python#/usr/bin/python3#' *.py
sed -i 's#/usr/bin/python#/usr/bin/python3#' collaboration/*py
sed -i 's#env python#env python3#' TurtleArt/*py
sed -i 's#env python#env python3#' turtleblocks

%build
python3 ./setup.py build

%install
mkdir -p %{buildroot}%{sugaractivitydir}
python3 ./setup.py install --prefix=%{buildroot}%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/TurtleBlocks.activity/

%find_lang org.laptop.TurtleArtActivity

%files -f org.laptop.TurtleArtActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/TurtleBlocks.activity/
%{_datadir}/metainfo/org.laptop.TurtleArtActivity.appdata.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 220-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 220-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 220-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 220-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 220-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 220-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 220-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 220-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 220-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 220-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 220-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 5 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 220-1
- v220
- Update Python3 dependecy declarations
- Add file for package data

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 218-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 218-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 218-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 218-1
- Release 218

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 216-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 216-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 216-1
- Release 216
- Port to GTK3/GST 1.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 210-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 210-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 210-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 210-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  8 2015 Peter Robinson <pbrobinson@fedoraproject.org> 210-1
- release 210

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 209-2
- Add Requires sugar-toolkit

* Sun Nov 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 209-1
- release 209

* Mon Jul 14 2014 Peter Robinson <pbrobinson@fedoraproject.org> 207-1
- release 207

* Sat Jun 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 206-1
- release 206

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 205-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 205-1
- release 205

* Sun May 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 204-1
- release 204

* Mon May  5 2014 Peter Robinson <pbrobinson@fedoraproject.org> 203-1
- release 203

* Mon May  5 2014 Peter Robinson <pbrobinson@fedoraproject.org> 202-1
- release 202

* Sun Mar 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 200-1
- release 200
