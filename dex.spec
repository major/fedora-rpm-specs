%global     commit b1f65ce480b4a797ee624ac2638ca1d6dfbd99f4
%global     shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       dex
Version:    1.0
Release:    17%{?dist}
Summary:    Dextrous text editor
License:    GPLv2
URL:        https://github.com/tihirvon/dex
Source0:    %{url}/archive/%{commit}/dex-v%{version}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires: ncurses-devel
BuildRequires: make

%description
dex is a small and easy to use text editor. Colors and bindings can be
fully customized to your liking. It has some features useful to
programmers, like ctags support and it can parse compiler errors, but
it does not aim to become an IDE.


%prep
%setup -qn dex-%{commit}


%build
cat > Config.mk << END
    CC      = gcc
    CFLAGS  = %{optflags}
    INSTALL = install -p
    prefix  = %{_prefix}
    bindir  = %{_bindir}
    datadir = %{_datadir}
    mandir  = %{_mandir}
END
make %{?_smp_mflags} V=1


%install
%make_install


%files
%doc README.md FAQ COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/dex.1*
%{_mandir}/man7/dex-syntax.7*


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild


* Wed May 06 2015 Craig Barnes <cr@igbarn.es> - 1.0-1
- Update to stable version

* Mon Feb 02 2015 Craig Barnes <cr@igbarn.es> - 0-0.8.20150202gitdbe12c5
- Update snapshot to latest upstream commit
- Add ncurses-devel as a build dependency

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20140609gitece2668
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Craig Barnes <cr@igbarn.es> - 0-0.6.20140609gitece2668
- Fix %%files section

* Mon Jun 09 2014 Craig Barnes <cr@igbarn.es> - 0-0.5.20140609gitece2668
- Update snapshot to latest upstream commit

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20140510git3c0f697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Craig Barnes <cr@igbarn.es> - 0-0.3.20140510git3c0f697
- Update

* Thu Apr 10 2014 Craig Barnes <cr@igbarn.es> - 0-0.2.20140410gitad89dc2
- Enable verbose build, so that flags are fully visible during compilation
- Simplify %%files section

* Thu Apr 10 2014 Craig Barnes <cr@igbarn.es> - 0-0.1.20140410gitad89dc2
- Initial package
