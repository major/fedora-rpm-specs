Name:		gimp-save-for-web
Version:	0.29.3
Release:	17%{?dist}
Summary:	Save for web plug-in for GIMP
License:	GPLv2+ and MIT
URL:		http://registry.gimp.org/node/33
Source0:	http://registry.gimp.org/files/%{name}-%{version}.tar.bz2
Source1:	%{name}.metainfo.xml
BuildRequires:	gimp-devel
BuildRequires:	intltool
BuildRequires:	libtool
%if 0%{?fedora} >= 21  
BuildRequires:	libappstream-glib
%endif
BuildRequires: make
Requires:	gimp >= 2.6.0

%description
Save for Web allows to find compromise between minimal file size
and acceptable quality of image quickly. While adjusting various
settings, you may explore how image quality and file size change.
Options to reduce file size of an image include setting compression
quality, number or colors, resizing, cropping, Exif information
removal, etc.

%prep
%autosetup -n  %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang gimp20-save-for-web

%if 0%{?fedora} >= 21  
# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.metainfo.xml
%endif

%files -f gimp20-save-for-web.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/gimp/2.0/plug-ins/webexport
%{_datadir}/gimp-save-for-web
%if 0%{?fedora} >= 21  
#AppStream metadata
%{_datadir}/appdata/%{name}.metainfo.xml
%endif

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Apr 17 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0.29.3-1
- Initial build based on Russian Fedora spec

