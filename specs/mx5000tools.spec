%global commit c575ea33f92495b4b0ccdb1ce09099f9c011e43f
%global commitdate 20190613
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mx5000tools
Version:        0.1.2
Release:        18.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Tools for the MX5000 series keyboard
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/jwrdegoede/mx5000tools
Source0:        https://github.com/jwrdegoede/mx5000tools/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        90-mx5000tools.rules
BuildRequires: make
BuildRequires:  gcc netpbm-devel libtool systemd-rpm-macros
Provides:       %{name}-libs = %{version}-%{release}
Obsoletes:      %{name}-libs < %{version}-%{release}
# for _udevrulesdir ownership
Requires:       systemd-udev

%description
mx5000tools are tools to control the extra features on the Logitech MX
5000 Bluetooth cordless keyboard. 


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit}
autoreconf -ivf


%build
%configure --disable-static
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mkdir -p $RPM_BUILD_ROOT%{_udevrulesdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_udevrulesdir}


%files
%license COPYING
%doc README
%{_udevrulesdir}/90-mx5000tools.rules
%{_bindir}/mx5000-tool
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-18.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.2-17.20190613gitc575ea3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-16.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-15.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-14.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-13.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct  3 2019 Hans de Goede <hdegoede@redhat.com> - 0.1.2-5.20190613gitc575ea3
- Drop requires kernel-core >= 5.2
- We have a new enough kernel everywhere now and this breaks the build of
  lcdproc on i686 since we no longer build i686 kernels

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4.20190613gitc575ea3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul  1 2019 Hans de Goede <hdegoede@redhat.com> - 0.1.2-3.20190613gitc575ea3
- New upstream git snapshot with various improvements
- Merge -lib subpackage into the main package
- Add udev rules for automatically setting the keyboard time when a supported
  keyboard is detected

* Thu Apr 18 2019 Hans de Goede <hdegoede@redhat.com> - 0.1.2-2.20190418git59d929d
- Add BuildRequires: gcc
- Drop obsolete Group tag from -devel subpackage
- New upstream git snapshot which drops the inclusion of the (unused)
  revoLUTIONconTROL sources, as those are under a dubious license
- The new git snapshot also fixes various rpmlint warnings and errors

* Sun Apr  7 2019 Hans de Goede <hdegoede@redhat.com> - 0.1.2-1.20190407git4967881
- Initial mx5000tools Fedora package
