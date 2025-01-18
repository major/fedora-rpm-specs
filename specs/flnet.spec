# For test builds, should be set to 0 for release builds.
%global alpha 0

Name:           flnet
Version:        7.5.0
Release:        9%{?dist}
Summary:        Amateur Radio Net Control Station

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.w1hkj.com/Net-help/index.html
%if %{alpha}
Source0:        http://www.w1hkj.com/alpha/%{name}/%{name}-%{version}.tar.gz
%else
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
%endif
Source99:       flnet.appdata.xml

BuildRequires:  gcc-c++ make
BuildRequires:  fltk-devel >= 1.3.4
%if %{?fedora}
BuildRequires:  flxmlrpc-devel >= 0.1.0
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


%description
Net provides the Amateur Radio Net Control Station operator with a real time
tool to assist him or her in managing the net activities.  A single screen with
multiple windows is used to allow rapid entry, search, pick and display of all
stations calling in to the net.  All operations on the main screen are
accomplished with keyboard entries only.  No mouse action is required to
perform the net control functions.  Experience has shown that most net control
operators prefer this method of operation to improve the speed of entry and
selection.


%prep
%autosetup

%if 0%{?fedora}
# Remove bundled xmlrpc library
rm -rf src/xmlrpcpp
%endif


%build
# Work around fltk-devel bug in RHEL 7.
# https://bugzilla.redhat.com/show_bug.cgi?id=1510482
export LIBS="-lfltk"
%configure
%make_build


%install
%make_install

%if 0%{?fedora}
# Install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 0644 %{SOURCE99} %{buildroot}%{_datadir}/metainfo/
%endif


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/flnet.desktop
%if 0%{?fedora}
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif


%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/flnet
%{_datadir}/applications/flnet.desktop
%{?fedora:%{_datadir}/metainfo/%{name}.appdata.xml}
%{_datadir}/pixmaps/flnet.xpm


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 7.5.0-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 04 2022 Richard Shaw <hobbes1069@gmail.com> - 7.5.0-1
- Update to 7.5.0.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Richard Shaw <hobbes1069@gmail.com> - 7.4.0-1
- Update to 7.4.0.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Richard Shaw <hobbes1069@gmail.com> - 7.3.3-1
- Update to 7.3.3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Richard Shaw <hobbes1069@gmail.com> - 7.3.2-1
- Update to latest upstream release.
- Add appdata file.

* Fri Oct 28 2016 Richard Shaw <hobbes1069@gmail.com> - 7.3.1-1
- Update to latest upstream release.

* Tue Oct 25 2016 Richard Shaw <hobbes1069@gmail.com> - 7.2.6-1
- Update to latest upstream release.

* Wed Dec  2 2015 Richard Shaw <hobbes1069@gmail.com> - 7.2.5-1
- Update to latest upstream release.

* Tue Nov  3 2015 Richard Shaw <hobbes1069@gmail.com> - 7.2.4-1
- Update to latest upstream release.

* Tue May  5 2015 Richard Shaw <hobbes1069@gmail.com> - 7.2.3-1
- Update to latest upstream release.
- Build with external xmlrpc library.
- Update package to use %%license where appropriate.

* Wed Mar 11 2015 Richard Shaw <hobbes1069@gmail.com> - 7.2.2-1
- Update to latest upstream release.

* Tue Jan 13 2015 Richard Shaw <hobbes1069@gmail.com> - 7.2.1-1
- Update to latest upstream release.

* Mon Feb  3 2014 Richard Shaw <hobbes1069@gmail.com> - 7.0.1-1
- Initial packaging.
