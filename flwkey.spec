Name:           flwkey
Version:        1.2.3
Release:        15%{?dist}
Summary:        Modem program for the K1EL Winkeyer series

License:        GPLv3+ and MIT
URL:            http://www.w1hkj.com/
Source0:        http://www.w1hkj.com/files/flwkey/%{name}-%{version}.tar.gz
Source99:       flwkey.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  fltk-devel >= 1.3.4
BuildRequires:  flxmlrpc-devel >= 0.1.0
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires: make

# xdg-open is used in src/flwkey.cxx
Requires:       xdg-utils


%description
Flwkey is a Winkeyer (or clone) control program for Amateur Radio use.  It
may be used concurrently with fldigi, fllog and flrig.


%prep
%autosetup

rm -rf src/xmlrpcpp


%build
# Work around fltk-devel bug in RHEL 7.
# https://bugzilla.redhat.com/show_bug.cgi?id=1510482
export LIBS="-lfltk"
%configure
%make_build


%install
%make_install

%if 0%{?fedora}
#install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 0644 %{SOURCE99} %{buildroot}%{_datadir}/metainfo/
%endif


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%if 0%{?fedora}
    appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif


%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{?fedora:%{_datadir}/metainfo/%{name}.appdata.xml}
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Richard Shaw <hobbes1069@gmail.com> - 1.2.3-2
- Add appdata file.

* Thu Mar 24 2016 Richard Shaw <hobbes1069@gmail.com> - 1.2.3-1
- Initial packaging.
