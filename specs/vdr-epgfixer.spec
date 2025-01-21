%global pname   epgfixer
%global __provides_exclude_from ^%{vdr_plugindir}/
%global commit  354f28b0112ba27f08f6509243b410899f74b6ed
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20180416
# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

Name:           vdr-%{pname}
Version:        0.3.1
Release:        36.%{gitdate}git%{shortcommit}%{?dist}
Summary:        VDR plugin for doing extra fixing of EPG data

License:        GPL-2.0-or-later
URL:            https://github.com/vdr-projects/vdr-plugin-epgfixer
Source0:        https://github.com/vdr-projects/vdr-plugin-epgfixer/archive/%{commit}/%{name}-%{version}-git%{shortcommit}.tar.gz
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  pcre-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
Epgfixer is a VDR plugin for doing extra fixing of EPG data. Features
include modifying EPG data using regular expressions, character set
conversions, blacklists, cloning EPG data, removing HTML tags, and
editing all settings through setup menu.

%prep
%autosetup -p1 -n vdr-plugin-%{pname}-%{commit}

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" \
     LIBDIR=. LOCALEDIR=./locale VDRDIR=%{_libdir}/vdr

%install
%make_install
install -dm 755 %{buildroot}%{vdr_configdir}/plugins/%{pname}
install -pm 644 epgfixer/{blacklist,charset,epgclone,regexp}.conf \
    %{buildroot}%{vdr_configdir}/plugins/%{pname}
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{vdr_plugindir}/libvdr-%{pname}*.so.%{vdr_apiversion}
%defattr(-,%{vdr_user},root,-)
%config(noreplace) %{vdr_configdir}/plugins/%{pname}/
%defattr(-,root,root,-)

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-36.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-35.20180416git354f28b
- Rebuilt for new VDR API version 2.7.2

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.1-34.20180416git354f28b
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-33.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-32.20180416git354f28b
- Rebuilt for new VDR API version 2.6.9

* Thu Jul 11 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-31.20180416git354f28b
- Rebuilt for new VDR API version 2.6.8

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-30.20180416git354f28b
- Rebuilt for new VDR API version

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-29.20180416git354f28b
- Rebuilt for new VDR API version

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-28.20180416git354f28b
- Rebuilt for new VDR API version
- Add BR gettext for rawhide

* Wed Jul 26 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-27.20180416git354f28b
- Rebuilt for rawhide

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-26.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-25.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-24.20180416git354f28b
- Rebuilt for new VDR API version

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-23.20180416git354f28b
- Rebuilt for new VDR API version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-22.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-21.20180416git354f28b
- Rebuilt for new VDR API version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-20.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-19.20180416git354f28b
- Rebuilt for new VDR API version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-18.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-17.20180416git354f28b
- Rebuilt for new VDR API version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-16.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-15.20180416git354f28b
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-14.20180416git354f28b
- Rebuilt for new VDR API version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-12.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-10.20180416git354f28b
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8.20180416git354f28b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-7.20180416git354f28b
- Update to 0.3.1-7.20180416git354f28b
- Rebuilt for vdr-2.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Ville Skyttä <ville.skytta@iki.fi> - 0.3.1-1
- First Fedora build
