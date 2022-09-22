Name:           humanity-icon-theme
Version:        0.6.15
Release:        9%{?dist}
Summary:        Humanity icon theme

License:        GPLv2
URL:            https://launchpad.net/humanity/
Source0:        %{name}-%{version}-without-logos.tar.xz
# Humanity icon theme contains copyrighted Ubuntu logo icons. Therefore we use
# this script to delete these files and remove any reference to the Ubuntu
# trademark before shipping it
Source1:        %{name}-generate-tarball.sh

BuildRequires:  icon-naming-utils
BuildRequires:  python3-scour
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description
Humanity and Humanity Dark are nice and well polished icon themes for the GNOME
desktop.


%prep
%autosetup


%build
for i in $(find . -type f -name "*.svg"); do
    scour -i $i -o $i.tmp --disable-style-to-xml && mv $i.tmp $i
done

for d in Humanity/*/ Humanity-Dark/*/; do
    pushd "$d"
    for i in */; do
        icon-name-mapping -c $i
    done
    popd
done


%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a Humanity/ $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a Humanity-Dark/ $RPM_BUILD_ROOT%{_datadir}/icons/

# Remove documentation and license files in theme folders
rm $RPM_BUILD_ROOT%{_datadir}/icons/Humanity/{AUTHORS,CONTRIBUTORS,COPYING}
rm $RPM_BUILD_ROOT%{_datadir}/icons/Humanity-Dark/{AUTHORS,COPYING}


%files
%doc Humanity/{AUTHORS,CONTRIBUTORS}
%license Humanity/COPYING
%{_datadir}/icons/Humanity/
%ghost %{_datadir}/icons/Humanity/icon-theme.cache
%{_datadir}/icons/Humanity-Dark/
%ghost %{_datadir}/icons/Humanity-Dark/icon-theme.cache


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.15-1
- Update to 0.6.15
- Spec cleanup

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.13-1
- Update to 0.6.13
- Spec cleanup

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.10-1
- Update to 0.6.10

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.8-1
- Update to 0.6.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.5-1
- Update to 0.6.5

* Sat Nov 02 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Thu Aug 29 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 07 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 06 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Fri Sep 21 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6-1
- Update to 0.6

* Sat Aug 11 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.3.12-1
- Update to 0.5.3.12

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.3.11-2
- Repack source to remove copyrighted Ubuntu logos
- Remove dependency on fedora-logos

* Sun Oct 09 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.3.11-1
- Initial RPM release
