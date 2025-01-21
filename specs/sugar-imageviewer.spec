Name:          sugar-imageviewer
Version:       65
Release:       13%{?dist}
Summary:       Simple Image viewer for Sugar

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://wiki.laptop.org/go/Image_Viewer
Source0:       http://download.sugarlabs.org/sources/sucrose/fructose/ImageViewer/ImageViewer-%{version}.tar.bz2
BuildArch:     noarch

BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext
Requires: sugar

%description
The Image Viewer activity is a simple and fast image viewer tool for Sugar.
It has features one would expect of a standard image viewer, like zoom,
rotate, etc. 

%prep
%autosetup -n ImageViewer-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/ImageViewer.activity/

%find_lang org.laptop.ImageViewerActivity


%files -f org.laptop.ImageViewerActivity.lang
%license COPYING
%doc AUTHORS NEWS
%{sugaractivitydir}/ImageViewer.activity/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 65-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 65-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 65-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 65-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 65-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 65-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 65-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 65-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 65-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 65-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> 65-1
- Release 65

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 64-1
- Release 64

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 63-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 63-1
- Release 63

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 62-4
- Fix FTBFS issue 

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 62-1
- Release 62

* Mon Jan 12 2015 Peter Robinson <pbrobinson@fedoraproject.org> 61-1
- Release 61

* Wed Dec 24 2014 Peter Robinson <pbrobinson@fedoraproject.org> 60-1
- Release 60

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 8  2013 Peter Robinson <pbrobinson@fedoraproject.org> 59-1
- Release 59

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Peter Robinson <pbrobinson@fedoraproject.org> 57-1
- Release 57

* Mon Jun  3 2013 Peter Robinson <pbrobinson@fedoraproject.org> 56-1
- Release 56

* Mon May 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 55-1
- Release 55

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
