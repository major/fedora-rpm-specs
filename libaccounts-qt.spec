
%global commit0 525ec684cfa8d234f797d7e49e21c476eea04d8e
%global tag0 VERSION_%{version}

Name:           libaccounts-qt
Summary:        Accounts framework Qt bindings
Version:        1.16
Release:        6%{?dist}

License:        LGPLv2
URL:            https://gitlab.com/accounts-sso/libaccounts-qt

Source0:        https://gitlab.com/accounts-sso/libaccounts-qt/repository/archive.tar.gz?ref=%{tag0}#/libaccounts-qt-%{version}.tar.gz

BuildRequires:  pkgconfig(libaccounts-glib) >= 1.23
BuildRequires:  doxygen
BuildRequires:  graphviz

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%package        -n libaccounts-qt5
Summary:        Accounts framework Qt5 bindings
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires: make
Obsoletes:      libaccounts-qt-qt5 < 1.13-11
%description    -n libaccounts-qt5
%{summary}.

%package        -n libaccounts-qt5-devel
Summary:        Development files for %{name}
Obsoletes:      libaccounts-qt-qt5-devel < 1.13-11
Requires:       libaccounts-qt5%{?_isa} = %{version}-%{release}
%description    -n libaccounts-qt5-devel
%{summary}.

%package        doc
Summary:        User and developer documentation for %{name}
Obsoletes:      libaccounts-qt5-doc < 1.13-10
Provides:       libaccounts-qt5-doc = %{version}-%{release}
BuildArch:      noarch
%description    doc
%{summary}.


%prep
%setup -q -n libaccounts-qt-%{tag0}-%{commit0}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} \
    QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    LIBDIR=%{_libdir} \
    ../accounts-qt.pro
popd

%make_build -C %{_target_platform}


%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

# create/own dirs
mkdir -p %{buildroot}%{_datadir}/accounts/{providers,services}

## unpackaged files
rm -fv %{buildroot}%{_datadir}/doc/accounts-qt/html/installdox

#remove tests for now
rm -rfv %{buildroot}%{_datadir}/libaccounts-qt-tests
rm -fv %{buildroot}%{_bindir}/accountstest


%ldconfig_scriptlets -n libaccounts-qt5

%files -n libaccounts-qt5
%license COPYING
%{_libdir}/libaccounts-qt5.so.*
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/

%files -n libaccounts-qt5-devel
%{_libdir}/libaccounts-qt5.so
%{_includedir}/accounts-qt5/
%{_libdir}/pkgconfig/accounts-qt5.pc
%{_libdir}/cmake/AccountsQt5

%files doc
%{_docdir}/accounts-qt/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.16-1
- 1.16
- use %%make_build

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.15-1
- libaccounts-qt-1.15, drop qt4 support (FTBFS)
- enable proper out-of-tree build

* Fri Aug 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.13-13
- more robust libdir handling (#1366692)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13-11
- name qt5 subpkgs properly (libaccounts-qt-qt5 => libaccounts-qt5)

* Thu Oct 29 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.13-10
- hack around cannot build out of src-tree
- provide -qt5, -doc here
- own %%_datadir/accounts/{providers,services}

* Mon Sep 28 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13-1
- libaccounts-qt-1.13, merge improvements from libaccounts-qt5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.11-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.11-4
- Update 64 bits arch patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 08 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.11-2
- Rebuild against fixed qt to fix -debuginfo (#1074041)

* Wed Feb 26 2014 Daniel Vrátil <dvratil@redhat.com> - 1.11-1
- Update to 1.11

* Sat Dec 14 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.6-4
- Fix duplicate documentation (#1001255)
- Add %%?_isa to -devel base package dep
- Remove %%defattr

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Karsten Hopp <karsten@redhat.com> 1.6-2
- add s390x and ppc64 to 64bit archs using lib64

* Mon Mar 04 2013 Jaroslav Reznik <jreznik@redhat.com> - 1.6-1
- Update to 1.6
- Fix rebuild issues with GCC 4.8
- Remove accounts-tool
- Cleanup
