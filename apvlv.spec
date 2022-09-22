%global debug_package %{nil}

Name:           apvlv
Version:        0.4.0
Release:        1%{?dist}
Summary:        PDF viewer which behaves like Vim

License:        GPLv2+
URL:            https://github.com/naihe2010/apvlv
Source0:        https://github.com/downloads/naihe2010/apvlv/apvlv-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  djvulibre-devel
BuildRequires:  ebook-tools-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  gtk3-devel
BuildRequires:  man-db
BuildRequires:  poppler-glib-devel
BuildRequires:  webkit2gtk3-devel

%description
apvlv is a GTK2 PDF and DjVu viewer with a vim look-and-feel.
It can also browse through directories of such documents.

%prep
%autosetup -p 1

%build
# umd.h is missing to enable the following:
# -DAPVLV_WITH_UMD:BOOL=ON 
# Does not compile with the following option:
# -DAPVLV_WITH_HTML:BOOL=ON

export LDFLAGS="-fPIE"
%cmake . -DDOCDIR=%{_pkgdocdir} -DAPVLV_WITH_DJVU:BOOL=ON -DAPVLV_WITH_TXT:BOOL=ON
%cmake_build

%install
%cmake_install
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{SOURCE1}

%files
%doc TODO NEWS
%doc AUTHORS THANKS
%doc %{_pkgdocdir}/*
%{_bindir}/apvlv
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/apvlv.1*
%config(noreplace)%{_sysconfdir}/apvlvrc

%changelog
* Fri Aug 26 2022 Filipe Rosset <rosset.filipe@gmail.com> - 0.4.0-1
- Update to 0.4.0 fixes rhbz#1983340

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.2.0-1
- Update to 0.2.0 fixes rhbz#1778828

* Tue Aug 04 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.1.5-10
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.1.5-6
- Rebuild for poppler-0.84.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.1.5-4
- Fix FTBFS rhbz #1674653

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.1.5-1
- update to latest upstream version 0.1.5
- spec cleanup and modernization

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 16 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 0.1.4-11
- Fix FTBFS with GCC 6 (#1307321)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.4-8
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Till Maas <opensource@till.name> - 0.1.4-5
- Use %%{_pkgdocdir}

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 28 2012 Till Maas <opensource@till.name> - 0.1.4-2
- Build with rpm_opt_flags (fix RH #861445)
- cleanup %%prep

* Wed Sep 26 2012 Till Maas <opensource@till.name> - 0.1.4-1
- Update to new release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 0.0.9.8-11
- Rebuild (poppler-0.20.0)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9.8-10
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.0.9.8-8
- rebuild(poppler)

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 0.0.9.8-7
- Rebuild (poppler-0.18.0)

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 0.0.9.8-6
- Rebuild (poppler-0.17.3)

* Tue Aug 02 2011 Pierre Carrier <pierre@spotify.com> 0.0.9.8-5
- Patch for poppler 0.17+

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 0.0.9.8-4
- Rebuild (poppler-0.16.3)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.0.9.8-2
- rebuild (poppler)

* Fri Oct 29 2010 Pierre Carrier <prc@redhat.com> 0.0.9.8-1
- Initial packaging
