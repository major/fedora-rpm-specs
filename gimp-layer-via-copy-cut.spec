%global	addon layer-via-copy-cut

Name:		gimp-%{addon}
Version:	1.6
Release:	25%{?dist}
Summary:	Layer via copy/cut plug-in for GIMP
License:	GPLv3+
URL:		http://some-gimp-plugins.com/contents/en/
Source0:	http://some-gimp-plugins.com/contents/en/extensions/002/%{addon}.zip
Source1:	%{name}.metainfo.xml
Source2:	LICENSE.txt
BuildRequires:	python2-devel
# for %%py2_shebang_fix
BuildRequires:	python3
BuildRequires:	libappstream-glib
Requires:	gimp

%description
Copy and move the selected area to a new layer in the same position.

# Upstream changed plugins path and this package is no longer noarch
%global debug_package %{nil}
%prep
%autosetup -c  %{name}
cp -p %{SOURCE2} .

# Fix Python shebangs for lessen Fedora release
%py2_shebang_fix %{addon}.py

%build

%install
install -Dpm 0755 %{addon}.py -t %{buildroot}%{_libdir}/gimp/2.0/plug-ins/

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.metainfo.xml


%files 
%license LICENSE.txt
#%%doc info.txt changelog.txt
%{_libdir}/gimp/2.0/plug-ins/%{addon}.py*
#AppStream metadata
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.6-14
- Apply sheband fix for Fedora 30 and up

* Tue Mar 19 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.6-13
- Revert to Python 2 dependency 

* Thu Feb 14 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Switch to Python 3 as dependency

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 13 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 1.6-4
- Fix plug-ins path due to upstream change
- Silence complain about empty debugging file

* Sun May 29 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 1.6-2
- Include license file

* Thu Apr 21 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 1.6-1
- Initial build 
