%undefine __cmake_in_source_build

%if 0%{?fedora} < 34
%global botan 1
%endif

Name:    qca-qt4
Summary: Qt4 Cryptographic Architecture
Version: 2.2.1
Release: 26%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://userbase.kde.org/QCA
Source0: http://download.kde.org/stable/qca/%{version}/qca-%{version}.tar.xz
%if 0%{?fedora} > 36
Patch0:  qca-2.2.1-openssl3.patch
%endif

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgcrypt-devel
BuildRequires: pkgconfig(libcrypto) pkgconfig(libssl)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(libpkcs11-helper-1)
BuildRequires: pkgconfig(libsasl2)
BuildRequires: pkgconfig(QtCore)

# qca2 renamed qca
Obsoletes: qca2 < 2.1.0
Provides:  qca2 = %{version}-%{release}
Provides:  qca2%{?_isa} = %{version}-%{release}

%if ! 0%{?botan}
Obsoletes: qca-qt4-botan < %{version}-%{release}
%endif

# most runtime consumers seem to assume the ossl plugin be present
Recommends: %{name}-ossl%{?_isa}

%description
Taking a hint from the similarly-named Java Cryptography Architecture,
QCA aims to provide a straightforward and cross-platform crypto API,
using Qt4 datatypes and conventions. QCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

%package -n qca
Summary: %{summary}
# qca2 renamed qca
Obsoletes: qca2 < 2.1.0
Provides:  qca2 = %{version}-%{release}
Provides:  qca2%{?_isa} = %{version}-%{release}
Recommends: qca-ossl%{?_isa}
%description -n qca
%description.

%package -n qca-devel
Summary: Qt4 Cryptographic Architecture development files
# qca2 renamed qca
Obsoletes: qca2-devel < 2.1.0
Provides:  qca2-devel = %{version}-%{release}
Provides:  qca2-devel%{?_isa} = %{version}-%{release}
Requires:  qca%{?_isa} = %{version}-%{release}
%description -n qca-devel
This packages contains the development files for QCA.

%if 0%{?botan}
%package -n qca-botan
Summary: Botan plugin for the Qt4 Cryptographic Architecture
BuildRequires: pkgconfig(botan-2)
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-botan
%{summary}.
%endif

%package -n qca-cyrus-sasl
Summary: Cyrus-SASL plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-cyrus-sasl
%{summary}.

%package -n qca-gcrypt
Summary: Gcrypt plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-gcrypt
%{summary}.

%package -n qca-gnupg
Summary: Gnupg plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-gnupg
%{summary}.

%package -n qca-logger
Summary: Logger plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-logger
%{summary}.

%package -n qca-nss
Summary: Nss plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-nss
%{summary}.

%package -n qca-ossl
Summary: Openssl plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-ossl
%{summary}.

%package -n qca-pkcs11
Summary: Pkcs11 plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-pkcs11
%{summary}.

%package -n qca-softstore
Summary: Softstore plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-softstore
%{summary}.


%prep
%autosetup -p1 -n qca-%{version}


%build
%global optflags %{optflags} -fpermissive

%cmake \
  -DQCA_DOC_INSTALL_DIR:PATH=%{_docdir}/qca \
  -DQCA_BINARY_INSTALL_DIR:STRING=%{_bindir} \
  -DQCA_FEATURE_INSTALL_DIR:PATH=%{_qt4_prefix}/mkspecs/features \
  -DQCA_INCLUDE_INSTALL_DIR:PATH=%{_qt4_headerdir} \
  -DQCA_LIBRARY_INSTALL_DIR:PATH=%{_qt4_libdir} \
  -DQCA_PLUGINS_INSTALL_DIR:PATH=%{_qt4_plugindir} \
  -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{_qt4_headerdir} \
  -DQT4_BUILD:BOOL=ON \
  -DWITH_botan_PLUGIN:BOOL=%{?botan:ON}%{?!botan:OFF}

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets -n qca

%files -n qca
%doc README TODO
%license COPYING
%{_qt4_libdir}/libqca.so.2*
%{_bindir}/mozcerts
%{_bindir}/qcatool
%{_mandir}/man1/qcatool.1*
%dir %{_qt4_plugindir}/crypto/
## HACK alert, quirk of recycling default %%_docdir below in -doc subpkg -- rex
%exclude %{_docdir}/qca/html/

%files -n qca-devel
%{_qt4_headerdir}/QtCrypto/
%{_qt4_libdir}/libqca.so
%{_libdir}/pkgconfig/qca2.pc
%{_libdir}/cmake/Qca/
%{_qt4_prefix}/mkspecs/features/crypto.prf

%if 0%{?botan}
%files -n qca-botan
%doc plugins/qca-botan/README
%{_qt4_plugindir}/crypto/libqca-botan.so
%endif

%files -n qca-cyrus-sasl
%doc plugins/qca-gcrypt/README
%{_qt4_plugindir}/crypto/libqca-cyrus-sasl.so

%files -n qca-gcrypt
%{_qt4_plugindir}/crypto/libqca-gcrypt.so

%files -n qca-gnupg
%doc plugins/qca-cyrus-sasl/README
%{_qt4_plugindir}/crypto/libqca-gnupg.so

%files -n qca-logger
%doc plugins/qca-logger/README
%{_qt4_plugindir}/crypto/libqca-logger.so

%files -n qca-nss
%doc plugins/qca-nss/README
%{_qt4_plugindir}/crypto/libqca-nss.so

%files -n qca-ossl
%doc plugins/qca-ossl/README
%{_qt4_plugindir}/crypto/libqca-ossl.so

%files -n qca-pkcs11
%doc plugins/qca-pkcs11/README
%{_qt4_plugindir}/crypto/libqca-pkcs11.so

%files -n qca-softstore
%doc plugins/qca-softstore/README
%{_qt4_plugindir}/crypto/libqca-softstore.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.1-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 02 2022 Than Ngo <than@redhat.com> - 2.2.1-18
- bz#2021934, fix FTBFS

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.2.1-16
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-13
- drop botan plugin for f34+ (#1892894)

* Fri Sep 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-12
- rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-10
- first try qca-qt4 compat pkg, keep "qca" basename to keep ugprade path
  as simple as possible.

