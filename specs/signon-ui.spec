%global gitdate 20240205
%global commit0 eef943f0edf3beee8ecb85d4a9dae3656002fc24
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           signon-ui
Version:        0.15^%{gitdate}.%{shortcommit0}
Release:        3%{?dist}
Summary:        Online Accounts Sign-on Ui

License:        GPL-3.0-only
URL:            https://launchpad.net/signon-ui

# Source0:      https://launchpad.net/signon-ui/trunk/%{version}/+download/signon-ui-%{version}.tar.bz2
Source0:        https://gitlab.com/accounts-sso/%{name}/-/archive/%{commit0}/%{name}-%{commit0}.tar.bz2

%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  libaccounts-qt6-devel
BuildRequires:  signon-qt6-devel
BuildRequires:  signon-devel
BuildRequires:  libproxy-devel
BuildRequires:  libnotify-devel

Requires:       dbus

%description
Sign-on UI is the component responsible for handling the user interactions which
can happen during the login process of an online account.
It can show password dialogs and dialogs with embedded web pages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit0}


%build
export PATH=%{_qt6_bindir}:$PATH
%{qmake_qt6} QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release signon-ui.pro

make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}

# Own directory where others can install provider-specific configuration
mkdir -p %{buildroot}/%{_sysconfdir}/signon-ui/webkit-options.d

%files
%doc README TODO NOTES
%license COPYING
%{_bindir}/signon-ui
%{_datadir}/dbus-1/services/*.service
%{_datadir}/applications/signon-ui.desktop
%{_sysconfdir}/signon-ui

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15^20240205.eef943f-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15^20240205.eef943f-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Alessandro Astone <ales.astone@gmail.com> - 0.15^20240205.eef943f-1
- Update to git snapshot for qt6
- Restrict to qt6_qtwebengine_arches

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.15-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar 25 2015 Daniel Vrátil <dvratil@redhat.com> - 0.15-2
- fix license
- fix typo in mkdir arguments
- use %%license

* Tue Mar 17 2015 Daniel Vrátil <dvratil@redhat.com> - 0.15-1
- Initial version
