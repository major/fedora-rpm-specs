Name:           lwtools
Version:        4.23
Release:        2%{?dist}
Summary:        Cross-development tool chain for Motorola 6809 and Hitachi 6309

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://www.lwtools.ca/
Source0:        http://www.lwtools.ca/releases/lwtools/lwtools-%{version}.tar.gz


%description
LWTOOLS is a set of cross-development tools for the Motorola 6809 and
Hitachi 6309 microprocessors. It supports assembling to raw binaries,
CoCo LOADM binaries, and a proprietary object file format for later
linking. It also supports macros and file inclusion among other things.

%package doc
Summary:        Documentation for the LWTOOLS cross-development tool chain
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

BuildRequires: make
BuildRequires:  gcc

%description doc
The complete documentation for the LWTOOLS cross-development tool chain.


%prep
%setup -q

%build
export LDFLAGS=${LDFLAGS:-%__global_ldflags}
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
make install PREFIX=%{buildroot}/usr LWCC_LIBBIN_FILES=''

mkdir -p %{buildroot}%{_docdir}/%{name}
mv docs/*.txt %{buildroot}%{_docdir}/%{name}
mv docs/manual %{buildroot}%{_docdir}/%{name}
cp -a 00README.txt %{buildroot}%{_docdir}/%{name}


%files
%{_bindir}/*
%dir %{_docdir}/%{name}
%license COPYING GPL3

%files doc
%{_docdir}/%{name}/*.txt
%{_docdir}/%{name}/manual


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 04 2024 John W. Linville <linville@tuxdriver.com> 4.23-1
- Update for version 4.23 from upstream

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 4.22-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 01 2024 John W. Linville <linville@tuxdriver.com> 4.22-1
- Update for version 4.22 from upstream

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 09 2023 John W. Linville <linville@tuxdriver.com> 4.20-1
- Update for version 4.20 from upstream

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 John W. Linville <linville@tuxdriver.com> 4.19-1
- Update for version 4.19 from upstream

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 02 2021 John W. Linville <linville@tuxdriver.com> 4.18-1
- Update for version 4.18 from upstream

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 John W. Linville <linville@tuxdriver.com> 4.17-4
- Correct FBTFS due to variable defined in a header file

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 John W. Linville <linville@tuxdriver.com> 4.17-1
- Update for version 4.17 from upstream

* Mon Feb 11 2019 John W. Linville <linville@tuxdriver.com> 4.16-1
- Update for version 4.16 from upstream
- Update URLs

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 John W. Linville <linville@redhat.com> - 4.15-4
- Add previously unnecessary BuildRequires for gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 John W. Linville <linville@tuxdriver.com> 4.15-1
- Update for version 4.15 from upstream

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 10 2017 John W. Linville <linville@tuxdriver.com> 4.14-1
- Update for version 4.14 from upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 18 2016 John W. Linville <linville@tuxdriver.com> 4.13-1
- Update for version 4.13 from upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 4.12-1
- Update to 4.12 (#1270624)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 John W. Linville <linville@tuxdriver.com> 4.11-1
- Update for version 4.11 from upstream

* Wed Feb  4 2015 John W. Linville <linville@tuxdriver.com> 4.10-3
- Use license macro for files containing license information

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 John W. Linville <linville@tuxdriver.com> 4.10-1
- Initial import
