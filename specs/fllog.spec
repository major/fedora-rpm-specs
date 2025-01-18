Name:           fllog
Version:        1.2.8
Release:        6%{?dist}
Summary:        Amateur Radio Log Program

# Automatically converted from old format: GPLv3+ and GPLv2+ - review is highly recommended.
License:        GPL-3.0-or-later AND GPL-2.0-or-later
URL:            http://w1hkj.com/fllog-help/index.html
Source0:        http://downloads.sourceforge.net/fldigi/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  fltk-devel >= 1.3.0
BuildRequires:  flxmlrpc-devel >= 1.0
BuildRequires:  libX11-devel
BuildRequires:  make


%description
Fllog is a transceiver control program for Amateur Radio use.  It does
not use any 3rd party transceiver control libraries.  It is a c++ pro-
gram that encapsulates each transceiver in its own class.  Where ever
possible the transceiver class(s) use polymorphism to reuse code that
is portable across a series of transceivers.


%prep
%autosetup

rm -rf src/xmlrpcpp
rm -f src/include/XmlRpc*.h


%build
# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1510482
%{?rhel:export LDFLAGS="%{optflags}"}
%configure
%make_build


%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license COPYING
%doc AUTHORS README
%{_bindir}/fllog
%{_datadir}/applications/fllog.desktop
%{_datadir}/pixmaps/fllog.xpm


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.8-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Richard Shaw <hobbes1069@gmail.com> - 1.2.8-1
- Update to 1.2.8.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Richard Shaw <hobbes1069@gmail.com> - 1.2.7-1
- Update to 1.2.7.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 14 2019 Richard Shaw <hobbes1069@gmail.com> - 1.2.6-1
- Update to 1.2.6.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Richard Shaw <hobbes1069@gmail.com> - 1.2.5-1
- Update to latest upstream release.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Richard Shaw <hobbes1069@gmail.com> - 1.2.4-1
- Update to latest upstream release.

* Sun May 08 2016 Richard Shaw <hobbes1069@gmail.com> - 1.2.3-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Richard Shaw <hobbes1069@gmail.com> - 1.2.0-1
- Update to latest upstream release.
- Build with external xmlrpc library.
- Minor spec tweaks per review request feedback.

* Tue Feb  4 2014 Richard Shaw <hobbes1069@gmail.com> - 1.1.8-1
- Bugfix release.

* Mon Feb  3 2014 Richard Shaw <hobbes1069@gmail.com> - 1.1.7-1
- Initial packaging.
