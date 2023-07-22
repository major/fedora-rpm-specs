Name:           kwalletcli
Version:        3.03
Release:        6%{?dist}
Summary:        CLI for the KDE Wallet

License:        MirOS
URL:            https://www.mirbsd.org/kwalletcli.htm
Source0:        https://www.mirbsd.org/MirOS/dist/hosted/kwalletcli/kwalletcli-%{version}.tar.gz

BuildRequires: make
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwallet-devel
%else
BuildRequires:  kdelibs-devel
%endif

%description
A command-line interface to the KDE Wallet, for KDE 4 and KF5 (so shell
scripts, Python, etc. do not need to use DCOP or D-Bus directly to access it
to store passwords, instead being able to call this convenient wrapper). KF5
does come with a kwallet-query utility, however, it requires the caller to
know the name of the default wallet, which most scripts won’t know, and lacks
kwalletcli’s extra utilities.

%prep
%setup -q -n %{name}
# Fix shell
%if 0%{?rhel} && 0%{?rhel} <= 7
sed -i -e 's,/usr/bin/env ,/bin/,' *kwallet*
%else
sed -i -e 's,/bin/env ,/bin/,' *kwallet*
%endif


%build
%if 0%{?fedora} || 0%{?rhel} > 7
make %{?_smp_mflags} KDE_VER=5 CFLAGS="%{optflags} -fPIC"  LDFLAGS="%{?__global_ldflags}"
%else
make %{?_smp_mflags} KDE_VER=4 KDE_INCS="-I%{_includedir}/Qt -I%{_includedir}/kde4" CFLAGS="%{optflags} -fPIC"  LDFLAGS="-L%{_libdir}/kde4/devel %{?__global_ldflags}"
%endif


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
make install DESTDIR=%{buildroot} INSTALL_STRIP=


%files
%license LICENCE
%{_bindir}/%{name}
%{_bindir}/kwalletaskpass
%{_bindir}/kwalletcli_getpin
%{_bindir}/pinentry-kwallet
%{_mandir}/man1/*.1*


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Orion Poplawski <orion@cora.nwra.com> - 3.03-1
- Update to 3.03

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 7 2017 Orion Poplawski <orion@cora.nwra.com> - 3.00-2
- Fix shell in scripts

* Wed Dec 28 2016 Orion Poplawski <orion@cora.nwra.com> - 3.00-1
- Initial package
