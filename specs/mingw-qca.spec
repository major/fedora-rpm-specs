%{?mingw_package_header}

%global pkgname qca

Name:           mingw-%{pkgname}
Version:        2.3.8
Release:        3%{?dist}
Summary:        MinGW Windows Qt Cryptographic Architecture
BuildArch:      noarch

License:        LGPL-2.0-or-later
URL:            https://userbase.kde.org/QCA
Source0:        http://download.kde.org/stable/%{pkgname}/%{version}/%{pkgname}-%{version}.tar.xz
# Install pkgconfig file
Patch0:         qca_pkgconfig.patch

BuildRequires:  make
BuildRequires:  cmake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw32-qt5-qtbase
# TODO
# BuildRequires:  mingw32-botan2
# BuildRequires:  mingw32-pkcs11-helper
# BuildRequires:  mingw32-nss
# BuildRequires:  mingw32-cyrus-sasl


BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw64-qt5-qtbase
# TODO
# BuildRequires:  mingw64-botan2
# BuildRequires:  mingw64-pkcs11-helper
# BuildRequires:  mingw64-nss
# BuildRequires:  mingw64-cyrus-sasl



%description
MinGW Windows Qt Cryptographic Architecture.


%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows Qt Cryptographic Architecture

%description -n mingw32-%{pkgname}-qt5
MinGW Windows Qt Cryptographic Architecture.


%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows Qt Cryptographic Architecture

%description -n mingw64-%{pkgname}-qt5
MinGW Windows Qt Cryptographic Architecture.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
export MINGW32_CMAKE_ARGS="
    -DQCA_FEATURE_INSTALL_DIR:PATH=%{mingw32_libdir}/qt5/mkspecs/features
    -DQCA_INCLUDE_INSTALL_DIR:PATH=%{mingw32_includedir}/qt5
    -DQCA_LIBRARY_INSTALL_DIR:PATH=%{mingw32_libdir}
    -DQCA_PLUGINS_INSTALL_DIR:PATH=%{mingw32_libdir}/qt5/plugins
    -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{mingw32_includedir}/qt5
"
export MINGW64_CMAKE_ARGS="
    -DQCA_FEATURE_INSTALL_DIR:PATH=%{mingw64_libdir}/qt5/mkspecs/features
    -DQCA_INCLUDE_INSTALL_DIR:PATH=%{mingw64_includedir}/qt5
    -DQCA_LIBRARY_INSTALL_DIR:PATH=%{mingw64_libdir}
    -DQCA_PLUGINS_INSTALL_DIR:PATH=%{mingw64_libdir}/qt5/plugins
    -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{mingw64_includedir}/qt5
"
%mingw_cmake \
    -DUSE_RELATIVE_PATHS=ON \
    -DQT4_BUILD:BOOL=OFF
%mingw_make_build


%install
%mingw_make_install

# Drop man pages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}



%files -n mingw32-%{pkgname}-qt5
%license COPYING
%{mingw32_bindir}/libqca-qt5.dll
%{mingw32_bindir}/mozcerts-qt5.exe
%{mingw32_bindir}/qcatool-qt5.exe
%{mingw32_prefix}/certs/
%{mingw32_includedir}/qt5/QtCrypto
%{mingw32_libdir}/libqca-qt5.dll.a
%dir %{mingw32_libdir}/qt5/plugins/crypto/
%{mingw32_libdir}/qt5/plugins/crypto/libqca-gcrypt.dll
%{mingw32_libdir}/qt5/plugins/crypto/libqca-gnupg.dll
%{mingw32_libdir}/qt5/plugins/crypto/libqca-logger.dll
%{mingw32_libdir}/qt5/plugins/crypto/libqca-ossl.dll
%{mingw32_libdir}/qt5/plugins/crypto/libqca-softstore.dll
%{mingw32_libdir}/cmake/Qca-qt5
%{mingw32_libdir}/pkgconfig/qca2-qt5.pc
%{mingw32_libdir}/qt5/mkspecs/features/crypto.prf


%files -n mingw64-%{pkgname}-qt5
%license COPYING
%{mingw64_bindir}/libqca-qt5.dll
%{mingw64_bindir}/mozcerts-qt5.exe
%{mingw64_bindir}/qcatool-qt5.exe
%{mingw64_prefix}/certs/
%{mingw64_includedir}/qt5/QtCrypto
%{mingw64_libdir}/libqca-qt5.dll.a
%dir %{mingw64_libdir}/qt5/plugins/crypto/
%{mingw64_libdir}/qt5/plugins/crypto/libqca-gcrypt.dll
%{mingw64_libdir}/qt5/plugins/crypto/libqca-gnupg.dll
%{mingw64_libdir}/qt5/plugins/crypto/libqca-logger.dll
%{mingw64_libdir}/qt5/plugins/crypto/libqca-ossl.dll
%{mingw64_libdir}/qt5/plugins/crypto/libqca-softstore.dll
%{mingw64_libdir}/cmake/Qca-qt5
%{mingw64_libdir}/pkgconfig/qca2-qt5.pc
%{mingw64_libdir}/qt5/mkspecs/features/crypto.prf


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 03 2024 Sandro Mani <manisandro@gmail.com> - 2.3.8-1
- Update to 2.3.8

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Sandro Mani <manisandro@gmail.com> - 2.3.7-1
- Update to 2.3.7

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 19 2023 Sandro Mani <manisandro@gmail.com> - 2.3.6-1
- Update to 2.3.6

* Fri Mar 03 2023 Sandro Mani <manisandro@gmail.com> - 2.3.5-1
- Update to 2.3.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 20 2022 Sandro Mani <manisandro@gmail.com> - 2.3.4-6
- Install pkgconfig file

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.3.4-4
- Rebuild with mingw-gcc-12

* Thu Feb 17 2022 Sandro Mani <manisandro@gmail.com> - 2.3.4-3
- Rebuild (openssl)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 29 2021 Sandro Mani <manisandro@gmail.com> - 2.3.4-1
- Update to 2.3.4

* Mon Aug 02 2021 Sandro Mani <manisandro@gmail.com> - 2.3.3-1
- Update to 2.3.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Sandro Mani <manisandro@gmail.com> - 2.3.1-1
- Update to 2.3.1

* Tue Jun 30 2020 Sandro Mani <manisandro@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.2.1-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Thu Apr 25 2019 Sandro Mani <manisandro@gmail.com> - 2.2.0-1
- Initial package
