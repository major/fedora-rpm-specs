Name:			gimp-paint-studio
Version:		2.0
Release:		28%{?dist}
Summary:		A collection of tool option presets and brushes for GIMP
License:		CC-BY-SA and GPLv2
URL:			http://code.google.com/p/gps-%{name}/
Source0:		https://gps-%{name}.googlecode.com/files/GPS_2_0.tar.gz
Source1:		%{name}.metainfo.xml

Patch0:         gps-2.0-rateRange.patch
Patch1:         gps-2.0-replaceBlends.patch

BuildArch:		noarch

Requires:		gimp >= 2.10

%description
GIMP Paint Studio(GPS) is a collection of brushes and accompanying tool
presets. Tool presets are a simply saved tool options, highly useful feature of
the GIMP. The goal of GPS is to provide an adequate working environment for
graphic designers and artists to begin to paint and feel comfortable with GIMP
from their first use.

%prep
%setup -qc %{name}-%{version}

%patch0 -p1
%patch1 -p1

%install
mkdir -p %{buildroot}%{_datadir}/gimp/2.0
# Remove xcf files from patterns directory
rm -rf %{_builddir}/%{name}-%{version}/patterns/GPS-Pat/*.xcf
cp -pr %{_builddir}/%{name}-%{version}/brushes \
		%{_builddir}/%{name}-%{version}/dynamics \
		%{_builddir}/%{name}-%{version}/gradients \
		%{_builddir}/%{name}-%{version}/splashes\
		%{_builddir}/%{name}-%{version}/palettes \
		%{_builddir}/%{name}-%{version}/patterns \
		%{_builddir}/%{name}-%{version}/tool-presets \
		%{buildroot}%{_datadir}/gimp/2.0

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%files
#CC-BY-SA
%{_datadir}/gimp/2.0/brushes/GPS-Brushes/
%{_datadir}/gimp/2.0/dynamics/GPS-Eraser/
%{_datadir}/gimp/2.0/dynamics/GPS-Fx/
%{_datadir}/gimp/2.0/dynamics/GPS-Set1/
%{_datadir}/gimp/2.0/dynamics/GPS-Set2/
%{_datadir}/gimp/2.0/dynamics/GPS-Sketch/
%{_datadir}/gimp/2.0/dynamics/GPS-Smudge/
%{_datadir}/gimp/2.0/gradients/GPS-Grad/
%{_datadir}/gimp/2.0/splashes/GPS-2_0--splash-techno-dark.jpg
%{_datadir}/gimp/2.0/palettes/GPS-Pal/
%{_datadir}/gimp/2.0/patterns/GPS-Pat/
#GPLv2
%{_datadir}/gimp/2.0/tool-presets/GPS-Eraser/
%{_datadir}/gimp/2.0/tool-presets/GPS-Fx/
%{_datadir}/gimp/2.0/tool-presets/GPS-Ink/
%{_datadir}/gimp/2.0/tool-presets/GPS-Set1/
%{_datadir}/gimp/2.0/tool-presets/GPS-Set2/
%{_datadir}/gimp/2.0/tool-presets/GPS-Sketch/
%{_datadir}/gimp/2.0/tool-presets/GPS-Smudge/
#AppStream metadata
%{_datadir}/appdata/%{name}.metainfo.xml

# Conditional for RHEL6 and less
%if 0%{?rhel} <= 6
	%doc License?for?Contents License_gpl-2.0.txt Readme.txt
%else
	%doc "License for Contents" License_gpl-2.0.txt Readme.txt
%endif

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan  3 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.0-22
- Patch some tool presets for compatibility with newer GIMP releases

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 25 2015 Luya Tshimbalanga <luya@fedoraproject.org> - 2.0-9
- Add metainfo files for software center 

* Sun Nov 09 2014 Luya Tshimbalanga <luya@fedoraproject.org> - 2.0-8
- Removal of xcf files within patterns directory (rhbz#1054967)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 2.0-6
- Add conditional for documentation due to rpm < 4.10 bug

* Wed Aug 14 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 2.0-5
- Rebuilt with new upstream file including licenses

* Mon Aug 12 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 2.0-4
- Fixes spec according to review (rhbz#989359)

* Sat Jul 27 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 2.0-1
- Initial release for Fedora

