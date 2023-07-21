%global		addon luminosity-masks

Name:		gimp-%{addon}
Version:	0
Release:	15%{?dist}
Summary:	Luminosity mask channels plug-in for Gimp
License:	GPLv2+
URL:		http://registry.gimp.org/node/28644
Source0:	http://registry.gimp.org/files/sg-%{addon}.scm
Source1:	%{name}.metainfo.xml
Source2:	gpl-2.0.txt
%if 0%{?fedora}
BuildRequires:	libappstream-glib
%endif
Requires:	gimp
BuildArch:	noarch

%description
Script-Fu script generating a full set of Light, Dark, and 
Midtone masks as channels for your image.

%prep
# Copy license
cp -p %{SOURCE2} .

%build
## Nothing to build.

%install
%if 0%{?epel}
mkdir -p %{buildroot}%{_datadir}/gimp/2.0/scripts/
%endif

install -Dpm 0644 %{SOURCE0} -t %{buildroot}%{_datadir}/gimp/2.0/scripts/

%if 0%{?fedora}
# Add AppStream metadata
install -Dpm 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/metainfo/

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml
%endif

%files
%license gpl-2.0.txt
%{_datadir}/gimp/2.0/scripts/*.scm
%if 0%{?fedora}
%{_datadir}/metainfo/%{name}.metainfo.xml
%endif

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jul 29 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 0-3
- Renames licensing file
- Adds conditional for EPEL7 build

* Sat Jul 29 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 0-2
- Fixes licensing
- Uses newer upstream appstream guideline

* Fri Jul 28 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 0-1
- Initial package
