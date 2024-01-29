%global _hardened_build 1
%global minorversion 1.2

Name:           xfce4-cpufreq-plugin
Version:        1.2.8
Release:        3%{?dist}
Summary:        CPU frequency scaling plugin for the Xfce4 panel 

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/xfce4-cpufreq-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel
BuildRequires:  xfce4-panel-devel
BuildRequires:  intltool 

Requires:       xfce4-panel

%description
The CpuFreq Plugin shows in the Xfce Panel the following information:
    current CPU frequency
    current used governor

In a separate dialog it provides you following information:
    all available CPU frequencies
    all available governors
    used driver for the CPU

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

find %{buildroot} -name \*.la -exec rm {} \;


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%license COPYING
%{_libdir}/xfce4/panel/plugins/libcpufreq.so
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/xfce4/panel/plugins/cpufreq.desktop

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Kevin Fenzi <kevin@scrye.com> - 1.2.8-1
- Update to 1.2.8.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 02 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7

* Wed Feb 02 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.6-1
- Update to 1.2.6

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5

* Tue Feb 02 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Tue Nov 10 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Jonathan Wakely <jwakely@redhat.com> - 1.2.1-6
- Correct fix for GCC -fno-common behaviour (#1830261)

* Wed Feb 05 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.1-5
- Fix GCC-10 FTBFS

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 22 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.0-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (GTK-3 port)

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.3-6
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 25 2016 Kevin Fenzi <kevin@scrye.com> - 1.1.3-1
- Update to 1.1.3. Translation fixes.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Kevin Fenzi <kevin@scrye.com> 1.1.2-1
- Update to 1.1.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com>         1.1.1 -2
- Rebuild for Xfce 4.12

* Tue Dec 23 2014 Kevin Fenzi <kevin@scrye.com>         1.1.1 -1
- Update to 1.1.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.0-5
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.0-4
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.0-2
- Rebuild for new libpng

* Wed Mar 16 2011 Hicham HAOUARI <hicham.haouari@gmail.com> - 1.0.0-1
- Initial Fedora package
