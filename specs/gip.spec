%undefine _ld_as_needed

Name:       gip
Version:    1.7.0
Release:    18%{?dist}
Summary:    Internet Protocol Calculator for Gnome

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later

Url:        http://code.google.com/p/gip/
Source0:    https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/gip/%{name}-%{version}-1.tar.gz
Patch1:     %{name}-%{version}-ubuntu.patch
Patch2:     %{name}-%{version}-c++11.patch

BuildRequires:  gtkmm24-devel
BuildRequires:  intltool
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Gip is an application for making IP address based calculations.
For example, it can display IP addresses in binary format.
It is also possible to calculate subnets.

%prep
%autosetup -p1 -n %{name}-%{version}-1

sed -i 's|CFLAGS="-std=c++11|CFLAGS="$(echo $CFLAGS) -std=c++11|' build.sh
sed -i 's|LFLAGS=`pkg-config $REQUIRED_LIBS --libs`|LFLAGS="$(echo $LDFLAGS) `pkg-config $REQUIRED_LIBS --libs`"|' build.sh
sed -i "s|INST_LIBDIR=\"\$INST_PREFIX/lib/\$EXECUTABLE\"|INST_LIBDIR=\"\$INST_PREFIX/share/\$EXECUTABLE\"|" build.sh
sed -i "s|INST_PIXMAPDIR=\"\$INST_PREFIX/lib/\$EXECUTABLE\"|INST_PIXMAPDIR=\"\$INST_PREFIX/share/\$EXECUTABLE\"|" build.sh

%build
%set_build_flags
./build.sh --prefix %{_prefix}

%install
mkdir -p %{buildroot}%{_prefix}
./build.sh --install --prefix %{buildroot}%{_prefix}
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/calc.png
%{_datadir}/mime/packages/%{name}.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.0-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 1.7.0-1
- Initial release
