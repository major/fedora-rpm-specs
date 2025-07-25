Name:           asm6809
Version:        2.16
Release:        2%{?dist}
Summary:        Multiple pass 6809 & 6309 cross assembler

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.6809.org.uk/asm6809/
Source0:        http://www.6809.org.uk/asm6809/dl/asm6809-%{version}.tar.gz

# https://fedorahosted.org/fpc/ticket/174
Provides:       bundled(gnulib)

BuildRequires:  gcc
BuildRequires: make

%description
asm6809 is a multiple pass 6809 & 6309 cross assembler. Text is read
in and parsed, then as many passes are made over the parsed source as
necessary (up to a limit), until symbols are resolved and addresses
are stable.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/*
%{_mandir}/man1/%{name}.1*
%license COPYING.GPL


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Apr 25 2025 John W. Linville <linville@tuxdriver.com> 2.16-1
- Update for version 2.16 from upstream

* Tue Feb 25 2025 John W. Linville <linville@tuxdriver.com> 2.15-1
- Update for version 2.15 from upstream

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.13-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 John W. Linville <linville@tuxdriver.com> 2.13-1
- Update for version 2.13 from upstream

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 John W. Linville <linville@tuxdriver.com> 2.12-1
- Update for version 2.12 from upstream

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 31 2018 John W. Linville <linville@tuxdriver.com> 2.11-1
- Update for version 2.11 from upstream

* Thu Jul 19 2018 John W. Linville <linville@redhat.com> - 2.10-5
- Add previously unnecessary BuildRequires for gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.10-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 John W. Linville <linville@tuxdriver.com> 2.10-1
- Update for version 2.10 from upstream

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 John W. Linville <linville@tuxdriver.com> 2.9.1-1
- Update for version 2.9.1 from upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 John W. Linville <linville@tuxdriver.com> 2.8-1
- Update for version 2.8 from upstream

* Tue Jan  3 2017 John W. Linville <linville@tuxdriver.com> 2.7-1
- Update for version 2.7 from upstream

* Fri Jun 03 2016 John W. Linville <linville@tuxdriver.com> 2.6-1
- Update for version 2.6 from upstream
- Correct bogus day for Aug 31 2015 changelog entry

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 John W. Linville <linville@tuxdriver.com> 2.5-3
- Update for version 2.5 from upstream
- Bump release number

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 John W. Linville <linville@tuxdriver.com> 2.4-1
- Update for version 2.4 from upstream
- Update URLs for project and source

* Wed Feb  4 2015 John W. Linville <linville@tuxdriver.com> 2.3.1-2
- Use %%license instead of %%doc for file containing license information
- Correct bogus date for 2.3.1-1 changelog entry

* Mon Aug 25 2014 John W. Linville <linville@tuxdriver.com> 2.3.1-1
- Update for version 2.3.1

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2

- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Thu Aug 14 2014 John W. Linville <linville@tuxdriver.com> 2.3-1
- Update for version 2.3

* Thu Aug  7 2014 John W. Linville <linville@tuxdriver.com> 2.2-1
- Update for version 2.2

* Mon Jun 16 2014 John W. Linville <linville@tuxdriver.com> 2.1-1
- Update for version 2.1

* Fri Jun 13 2014 John W. Linville <linville@tuxdriver.com> 2.0-1
- Initial import
