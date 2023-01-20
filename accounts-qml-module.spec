
Name:    accounts-qml-module
Summary: QML bindings for libaccounts-qt + libsignon-qt
Version: 0.7
Release: 9%{?dist}

License: LGPLv2 
URL:     https://gitlab.com/accounts-sso/accounts-qml-module
Source:  https://gitlab.com/accounts-sso/%{name}/-/archive/VERSION_%{version}/%{name}-VERSION_%{version}.tar.bz2

## upstream patches
# PATCH-FIX-UPSTREAM
Patch1:  Fix-compilation-with-Qt-5.13.patch
# PATCH-FIX-UPSTREAM
Patch2:  Build-add-qmltypes-file-to-repository.patch

## upstreamable patches
# disable -Werror, only makes sense for developer builds, not release builds
Patch100: accounts-qml-module-Werror.patch

BuildRequires: qt5-doctools
BuildRequires: cmake(AccountsQt5)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(SignOnQt5)
BuildRequires: make

%description
This QML module provides an API to manage the user's online accounts and get
their authentication data. It's a tiny wrapper around the Qt-based APIs of
libaccounts-qt and libsignon-qt.

%package doc
Summary: Documentation for %{name} 
BuildArch: noarch
%description doc
This package contains the developer documentation for accounts-qml-module.


%prep
%autosetup -n %{name}-VERSION_%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} \
  CONFIG+=release \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  ..
popd

%make_build -C %{_target_platform}


%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

## unpackaged files
# remove tests
rm %{buildroot}%{_bindir}/tst_plugin
# avoid rpmlint warning
rm -fv %{buildroot}/%{_datadir}/%{name}/doc/html/.gitignore


%files
%license COPYING
%doc README.md
%{_qt5_archdatadir}/qml/Ubuntu/

%files doc
%doc %{_datadir}/%{name}/


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 0.7-5
- build without -Werror

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.7-1 
- first try, inspiration from opensuse packaging

