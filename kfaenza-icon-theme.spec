Name:           kfaenza-icon-theme
Version:        0.8.9
Release:        21%{?dist}
Summary:        Faenza-Cupertino Icon Theme for KDE

License:        GPLv3
URL:            http://kde-look.org/content/show.php?content=143890
# Original source found here:
# Source0:      http://ompldr.org/vYjR0NQ/kfaenza-icon-theme-0.8.9.tar.gz
# It was cleaned of trademarks via the script in Source1.
Source0:        kfaenza-icon-theme-0.8.9-clean.tar.gz
Source1:        kfaenza-icon-theme-generate-tarball.sh
BuildArch:      noarch

%description
Contains icons for Faenza-Cupertino theme for KDE.

%prep
%setup -qn KFaenza

%install
rm INSTALL
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/icons/KFaenza
rm $(find . -name ".directory" |xargs)
cp -r . ${RPM_BUILD_ROOT}%{_datadir}/icons/KFaenza

%post
touch --no-create %{_datadir}/icons/KFaenza &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/KFaenza &>/dev/null
  gtk-update-icon-cache %{_datadir}/icons/KFaenza &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/KFaenza &>/dev/null || :

%files
%{_datadir}/icons/KFaenza

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Tom Callaway <spot@fedoraproject.org> - 0.8.9-12
- clean out troublesome icons

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Minh Ngo <minh@fedoraproject.org> - 0.8.9-4
- upd scriptnets
- removing uneeded dependencies

* Wed Sep 26 2012 Minh Ngo <minh@fedoraproject.org> - 0.8.9-3
- Removing hidden files.

* Sun Jul 01 2012 Minh Ngo <ignotusp@fedoraproject.org> - 0.8.9-2
- Fixing inherited icon theme
- Updating icon cache

* Sat Jun 16 2012 Minh Ngo <nlminhtl@gmail.com> - 0.8.9-1
- Intial RPM release
